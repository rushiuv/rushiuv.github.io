---
title: "角度报文很干净时间轴却在抖：低速啸叫换了更高分辨率编码器叫得更凶"
date: 2026-08-24T08:29:00+08:00
slug: "Vw_UnhXxR7BUUIm2J4C0sA"
description: "台架上低速段那声啸叫，轴像打摆子。第一反应多半是转矩环刚度不够、带宽不够，于是提速、换更快的主站、把编码器从 17 位换成 19 位——越贵的编码器分辨率越高。结果叫得更凶，钱白花。"
original: "https://mp.weixin.qq.com/s/Vw_UnhXxR7BUUIm2J4C0sA"
tags: ["EtherCAT"]
---

![](/images/wx/c85317041a9bfba0c3827b6f471a83de.webp)

台架上低速段那声啸叫，轴像打摆子。第一反应多半是转矩环刚度不够、带宽不够，于是提速、换更快的主站、把编码器从 17 位换成 19 位——越贵的编码器分辨率越高。结果叫得更凶，钱白花。

抓一包总线，角度曲线干干净净：CRC 全绿、数值逐拍递增、没半点跳变。问题不在信号幅值，在<strong>时间轴</strong>——编码器每一拍给出的角度都对，可控制器拿到它时，转子已经往前走了一段。

这里先要把 EtherCAT 摘干净。EtherCAT 的分布时钟（DC）本来就是干这件事的：各从站共享本地高精度时基，采样由本地时钟触发，通信到达时间和物理采样时刻是解耦的，同步抖动可以做到远低于 1 µs。所以「总线被温度、日志、DMA 排队挤得周期乱跳」不是 EtherCAT 该有的样子。真正抖的是<strong>采样 → 从站处理 → PDO 发出 → 主站接收 → 控制任务消费</strong>这一整条链——尤其当采样没锁到 DC、主站任务又不是严格实时的时候，控制任务看到数据的时刻会明显偏离理论周期。本文要打的靶子，是这条链上的时间基准，不是 EtherCAT 总线本身。

把这条链拆成三个时刻，问题才看得清：

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>𝑡</mi><mrow><mi>𝑠</mi><mi>𝑎</mi><mi>𝑚</mi><mi>𝑝</mi><mi>𝑙</mi><mi>𝑒</mi></mrow></msub><mo>→</mo><msub><mi>𝑡</mi><mrow><mi>𝑟</mi><mi>𝑒</mi><mi>𝑎</mi><mi>𝑑</mi><mi>𝑦</mi></mrow></msub><mo>→</mo><msub><mi>𝑡</mi><mrow><mi>𝑐</mi><mi>𝑜</mi><mi>𝑛</mi><mi>𝑠</mi><mi>𝑢</mi><mi>𝑚</mi><mi>𝑒</mi></mrow></msub></math>

<strong>第一类，确定性延迟 latency。</strong> 芯片 ADC、数字滤波、CORDIC、接口发送固定要花的时间<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑇</mi><mi>𝑑</mi></msub></math>，比如 25 µs。它稳定，所以可以外推补偿：

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mrow><mover><mi>𝜃</mi><mo>^</mo></mover></mrow><mo>(</mo><mi>𝑡</mi><mo>)</mo><mo>=</mo><mi>𝜃</mi><mo>(</mo><mi>𝑡</mi><mo>−</mo><msub><mi>𝑇</mi><mi>𝑑</mi></msub><mo>)</mo><mo>+</mo><mrow><mover><mi>𝜔</mi><mo>^</mo></mover></mrow><msub><mi>𝑇</mi><mi>𝑑</mi></msub></math>。固定群延迟能救，靠的是这个。

<strong>第二类，采样 jitter。</strong> 这才是真靶子：

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>𝑡</mi><mrow><mi>𝑠</mi><mi>𝑎</mi><mi>𝑚</mi><mi>𝑝</mi><mi>𝑙</mi><mi>𝑒</mi><mo>,</mo><mi>𝑘</mi></mrow></msub><mo>=</mo><mi>𝑘</mi><msub><mi>𝑇</mi><mi>𝑠</mi></msub><mo>+</mo><mi>𝛿</mi><msub><mi>𝑡</mi><mi>𝑘</mi></msub></math>

每拍的<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mi>𝛿</mi><msub><mi>𝑡</mi><mi>𝑘</mi></msub></math>都不一样，于是

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>𝛿</mi><msub><mi>𝜃</mi><mrow><mi>𝑒</mi><mo>,</mo><mi>𝑘</mi></mrow></msub><mo>≈</mo><msub><mi>𝜔</mi><mi>𝑒</mi></msub><mrow><mspace width="0.22em"/></mrow><mi>𝛿</mi><msub><mi>𝑡</mi><mi>𝑘</mi></msub></math>

角度值没错，错的是角度<strong>所属的时间</strong>。没有采样时间戳的高分辨率角度，本质上只是一张不知道拍摄时间的高清照片。

<strong>第三类，传输 / 消费 jitter。</strong> 数据可能早已在正确的 Sync0 时点采好，只是<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑡</mi><mrow><mi>𝑐</mi><mi>𝑜</mi><mi>𝑛</mi><mi>𝑠</mi><mi>𝑢</mi><mi>𝑚</mi><mi>𝑒</mi><mo>,</mo><mi>𝑘</mi></mrow></msub></math>晚了一点。这种情况下只要数据带着真正的<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑡</mi><mrow><mi>𝑠</mi><mi>𝑎</mi><mi>𝑚</mi><mi>𝑝</mi><mi>𝑙</mi><mi>𝑒</mi></mrow></msub></math>，控制器就知道「我现在收到的是 43.2 µs 前的角度」，问题大幅缓解。所以那句「真正坏的旋钮是时间戳」不是修辞——没有<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑡</mi><mrow><mi>𝑠</mi><mi>𝑎</mi><mi>𝑚</mi><mi>𝑝</mi><mi>𝑙</mi><mi>𝑒</mi></mrow></msub></math>的高分辨率角度，分辨率再高也是假精确。

这同一个采样 jitter，高速段和低速段演成两出不同的故障。

高速段，抖动量折成电气角滞后：

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mi>𝜃</mi><mrow><mi>𝑒</mi><mi>𝑟</mi><mi>𝑟</mi></mrow></msub><mo>=</mo><msub><mi>𝜔</mi><mrow><mi>𝑒</mi><mi>𝑙</mi><mi>𝑒</mi><mi>𝑐</mi></mrow></msub><mo>⋅</mo><mi>Δ</mi><mi>𝑡</mi></math>

关键在<strong>电气角</strong>不是机械角——极对数把机械转速抬成电气转速，同样的 Δt，转速越高折出的电气角误差越离谱。举个极端但纯净的假设：高速轴的位置环节本已做到几十微秒级更新，仅仅额外引入 100 µs 的采样时刻不确定性；在 12 对极、3 万 rpm（电气频率 6000 Hz、周期 167 µs）下，这 100 µs 就对应 216° 电气角，电流矢量直接反向，换相彻底乱掉。这里甚至还没讨论总反馈周期，只单算时间误差本身——但正因为 216° 这么大，反过来说明这种极高电气频率的系统<strong>早就不可能拿 1 ms 的反馈周期直接换相</strong>，它从架构上就得把采样锁到微秒级、靠外推补足，抖动一旦没锁住才暴露成换相崩。高速段叫得最凶，锅不在磁钢也不在分辨率，是时间基准在电气角上被极对数放大了。

低速段，电气角速度小，Δt 折出的滞后相位很小，换相不会乱。麻烦在另一处：它污染差分测速。最普通的算法

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msub><mrow><mover><mi>𝜔</mi><mo>^</mo></mover></mrow><mi>𝑘</mi></msub><mo>=</mo><mfrac><mrow><msub><mi>𝜃</mi><mi>𝑘</mi></msub><mo>−</mo><msub><mi>𝜃</mi><mrow><mi>𝑘</mi><mo>−</mo><mn>1</mn></mrow></msub></mrow><msub><mi>𝑇</mi><mi>𝑠</mi></msub></mfrac></math>

默认分母就是固定的<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑇</mi><mi>𝑠</mi></msub></math>；可真实间隔是<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑇</mi><mi>𝑠</mi></msub><mo>+</mo><mi>𝛿</mi><msub><mi>𝑇</mi><mi>𝑘</mi></msub></math>，控制器却还拿<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑇</mi><mi>𝑠</mi></msub></math>去除。小扰动下

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mfrac><mrow><mi>𝛿</mi><mi>𝜔</mi></mrow><mi>𝜔</mi></mfrac><mo>≈</mo><mfrac><mrow><mi>𝛿</mi><mi>𝑇</mi></mrow><msub><mi>𝑇</mi><mi>𝑠</mi></msub></mfrac></math>

1 ms 周期里若采样时刻在 ±0.4 ms 晃，等效测速增益误差就能到几十个百分点。低速时<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mi>Δ</mi><msub><mi>𝜃</mi><mi>𝑘</mi></msub></math>本就小，再叠加量化、摩擦、死区、速度滤波，速度环增益随时间乱变，很容易激发 hunting 甚至极限环，台架就响。根因和高速那出一样，只是表现从「换相相位崩」换成了「速度估计被时间抖动带歪」。

那为什么换更贵的编码器反而更凶？因为空间分辨率和时间准确度是两回事：

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mtext>spatial resolution</mtext><mo>≠</mo><mtext>temporal accuracy</mtext></math>

17 位换 19 位，量化步距从约 0.00275° 降到 0.000687°，漂亮了 4 倍。可若是采样时刻抖了 50 µs，这 50 µs 一纳秒都没因为 19 位消失。19 位只是把一条干净但错位的曲线标得更细，Δt 这个量一个 bit 没变。手边唯一能换的旋钮是「位数」，真正坏的旋钮是「时间戳」。

根子在时间基准没对齐，不是角度不准。开了 DC 不等于真锁了——很多设计里编码器采样还跟着自己的 SPI 读节奏走，Sync0 只准时触发了「发送 PDO」，没触发「采样那一下」。于是你准时发出了一份采样时刻不确定的数据。要锁的是位置被物理采样、锁存的那一下，不是报文进网口那一下。差这一个定义，DC 白开。

确诊别只抓网络包。PDO 可能准时得像钟表，内部采样却一直在抖——所以要看三条时间线对不对得上：传感器真实的<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑡</mi><mrow><mi>𝑠</mi><mi>𝑎</mi><mi>𝑚</mi><mi>𝑝</mi><mi>𝑙</mi><mi>𝑒</mi></mrow></msub></math>

（sample/latch 时间戳）、EtherCAT DC / PDO 的<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑡</mi><mrow><mi>𝑃</mi><mi>𝐷</mi><mi>𝑂</mi></mrow></msub></math>、控制任务真正消费该角度的<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><msub><mi>𝑡</mi><mrow><mi>𝑡</mi><mi>𝑎</mi><mi>𝑠</mi><mi>𝑘</mi></mrow></msub></math>。三者叠一张图，看 p95 / p99 和连续两帧最大间隔，别看均值——十次里九次差 1 µs、一次差 200 µs，均值还是好看，可那一次在高速段就是上百度电气角滞后。给报文加上递增计数和采样时间戳再抓一次，画出来就能分清是角度在抖还是采样时刻在抖。

花了更贵的编码器叫得更凶，根子常常不是分辨率，是时间轴歪了。编码器交给控制器的本来就不该只是一个角度 θ，而是一对 (θ,t)——只有 θ 没有 t，19 位也可能是假精确。
