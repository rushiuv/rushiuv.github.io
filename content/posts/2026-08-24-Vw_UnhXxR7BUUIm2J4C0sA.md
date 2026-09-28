---
title: "角度报文很干净时间轴却在抖：低速啸叫换了更高分辨率编码器叫得更凶"
date: 2026-08-24T08:29:00+08:00
slug: "Vw_UnhXxR7BUUIm2J4C0sA"
description: "台架上低速段那声啸叫，轴像打摆子。第一反应多半是转矩环刚度不够、带宽不够，于是提速、换更快的主站、把编码器从 17 位换成 19 位——越贵的编码器分辨率越高。结果叫得更凶，钱白花。"
original: "https://mp.weixin.qq.com/s/Vw_UnhXxR7BUUIm2J4C0sA"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUTpdGVzUicJOMeBl07wIjH39eMNcFK8c3RWC9x4OCBPeW4KdHNPSPdgDZzXYzmP5n5FDEqUHtBChefw4eaLwazia7zZB53yibTxw/640?wx_fmt=png&from=appmsg)

## 角度报文很干净时间轴却在抖：低速啸叫换了更高分辨率编码器叫得更凶

台架上低速段那声啸叫，轴像打摆子。第一反应多半是转矩环刚度不够、带宽不够，于是提速、换更快的主站、把编码器从 17 位换成 19 位——越贵的编码器分辨率越高。结果叫得更凶，钱白花。

抓一包总线，角度曲线干干净净：CRC 全绿、数值逐拍递增、没半点跳变。问题不在信号幅值，在**时间轴**——编码器每一拍给出的角度都对，可控制器拿到它时，转子已经往前走了一段。

这里先要把 EtherCAT 摘干净。EtherCAT 的分布时钟（DC）本来就是干这件事的：各从站共享本地高精度时基，采样由本地时钟触发，通信到达时间和物理采样时刻是解耦的，同步抖动可以做到远低于 1 µs。所以「总线被温度、日志、DMA 排队挤得周期乱跳」不是 EtherCAT 该有的样子。真正抖的是**采样 → 从站处理 → PDO 发出 → 主站接收 → 控制任务消费**这一整条链——尤其当采样没锁到 DC、主站任务又不是严格实时的时候，控制任务看到数据的时刻会明显偏离理论周期。本文要打的靶子，是这条链上的时间基准，不是 EtherCAT 总线本身。

把这条链拆成三个时刻，问题才看得清：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6B9TZK0cTAP3b52BYBHL88N0wQ0WE4nBZl1ONp5nRAXPgloDRALTZ9M9XRpW3pHyeIM044Ke17Q1gkRlqjuKSmVR9eDq0sBlJrFgOxkcHocw/640?wx_fmt=svg&from=appmsg)

**第一类，确定性延迟 latency。** 芯片 ADC、数字滤波、CORDIC、接口发送固定要花的时间

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4PRr8BrhzyAGOgicOF3icojqGpPBicoWh4XgaxIHCfk0ydVbKfMlqBELyfyI8L9oSpAqxemRxHfn3NjLZnBO7k8gZzI4qcWxLpk6tia2l1CqXWzQ/640?wx_fmt=svg&from=appmsg)

，比如 25 µs。它稳定，所以可以外推补偿：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7W4LCE6oSkibgIjbDr5aMTFV9ekf3BSsyo5Hrr20yI3BBQ5deG8NSjv87Wwp4UQQ11YI6xKKkFbLbyp7Ys9mfG5BxPu32dkqH4ia4QoRXjxokw/640?wx_fmt=svg&from=appmsg)

。固定群延迟能救，靠的是这个。

**第二类，采样 jitter。** 这才是真靶子：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5dnpFkhIaNtwftwrCXFeb1kcMntFX1wkGiaQWHmoEUCDqQhc2qOkN0OIjpqgMxKRA5kNWu1nqhS3vSQ7HpuA1kX4e52DKbWDtobv5GpdbJbTw/640?wx_fmt=svg&from=appmsg)

每拍的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6erialA0bCAibC67nJ957rtsUnLkPSmL9415WJDSO3iaRhNB1rftYVPkV02zroUDMwyTibEibrhk597v6Ae7WjOYKmX89S18rqohdrhW1cPMf75uw/640?wx_fmt=svg&from=appmsg)

 都不一样，于是

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5ElmsL1o8h9F7aBFVT7s6vrVOhia4UhRaRBChHNEJscvt5GaicgNxQJicWIEV50dErHKeB6o2a1UCr9IjQmjhnqjzmyyHx6ibexTr2icNCfCk2TZg/640?wx_fmt=svg&from=appmsg)

角度值没错，错的是角度**所属的时间**。没有采样时间戳的高分辨率角度，本质上只是一张不知道拍摄时间的高清照片。

**第三类，传输 / 消费 jitter。** 数据可能早已在正确的 Sync0 时点采好，只是

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6FiaRiaaoUZvQrHo8221zajdQNFHKzkl62PJsiaL3iaDALdibEdBbs8O3M8fgdoWN5CBcxKRTiahb9AENIB2PCZXxZJVnotFKMasB9eXn4SFK0Kqtw/640?wx_fmt=svg&from=appmsg)

 晚了一点。这种情况下只要数据带着真正的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7mcJU3kxXJR6AIgXImxp7ibzt30r4jRK9GibqyOXV3D5nZMQ2lEAn1ic4NHWxNexV3ybhB31ARTfncsNY7W6aA0YiaBsdVeZf1Zl00CsIJ8sbIibw/640?wx_fmt=svg&from=appmsg)

，控制器就知道「我现在收到的是 43.2 µs 前的角度」，问题大幅缓解。所以那句「真正坏的旋钮是时间戳」不是修辞——没有

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qjlUAvTu6h0xmGIc4rKN6gd0sHPX8b7j0HLPcJZNg3mia3NvUFYLvNKicRoE6MhO2sfu7aTJGBFDgp3Uwic9emOiciaUSrbRI6QenKClyGaGh9pA/640?wx_fmt=svg&from=appmsg)

 的高分辨率角度，分辨率再高也是假精确。

这同一个采样 jitter，高速段和低速段演成两出不同的故障。

高速段，抖动量折成电气角滞后：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4YyDiaBccP8bBpFu7Aicm0VascB3aHutFQ8CDGhq7rNNM87uPSkYKDfDRhug5zIvwJLAmzHMUSVlNmn5XKqXpWs0vNRFrMkDTxqPgboR3Vr1Sw/640?wx_fmt=svg&from=appmsg)

关键在**电气角**不是机械角——极对数把机械转速抬成电气转速，同样的 Δt，转速越高折出的电气角误差越离谱。举个极端但纯净的假设：高速轴的位置环节本已做到几十微秒级更新，仅仅额外引入 100 µs 的采样时刻不确定性；在 12 对极、3 万 rpm（电气频率 6000 Hz、周期 167 µs）下，这 100 µs 就对应 216° 电气角，电流矢量直接反向，换相彻底乱掉。这里甚至还没讨论总反馈周期，只单算时间误差本身——但正因为 216° 这么大，反过来说明这种极高电气频率的系统**早就不可能拿 1 ms 的反馈周期直接换相**，它从架构上就得把采样锁到微秒级、靠外推补足，抖动一旦没锁住才暴露成换相崩。高速段叫得最凶，锅不在磁钢也不在分辨率，是时间基准在电气角上被极对数放大了。

低速段，电气角速度小，Δt 折出的滞后相位很小，换相不会乱。麻烦在另一处：它污染差分测速。最普通的算法

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5QzUTKYQozFE2TATuA8bnOjvlw8J8sCbicHcopRs9ZpDwRlcaRujX4bj68YZmoibJsTZjrPuIuPKWXTfcW6wt7KIklak8PYs08qsvzWicICQ3KQ/640?wx_fmt=svg&from=appmsg)

默认分母就是固定的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qjlUAvTu6hibHsbewQHiccIOs7HrYHDOnD5D3SrUq3phHtM2ibYDQxXg93QPYorz9eicdOcaXvSuyAkfz5brnDHic22KsECjEZcth7XNRCGFvjrw/640?wx_fmt=svg&from=appmsg)

；可真实间隔是

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6klCb3grBQiaWibJvJoOCJSUn20CAME4wGEiaBc6mm41UyUOegQ7TyQrdMXRoZJN68NstibyKAnc4oSmDNrqlKLicib7blf59KteVKGicVDSAVGic0ew/640?wx_fmt=svg&from=appmsg)

，控制器却还拿

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6OBPpNBN5yrem1qP1B4Ky3yfZdoV25zJL9ia7ljUict7p47maGAKibjkiaaYzhrfKqsVMSV9Feg5fftX0L4ryaIMHSNmkwBh7S2DONiagEaGJzxicQ/640?wx_fmt=svg&from=appmsg)

 去除。小扰动下

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7rxUPpZIJsiag7R1r7EEl7m4yfSkR4PD5MznfRd0alEkhQAicLuWlgkfN0tCzjibmauTiajmaBQ2wllBCBq8ribFS4orvaXuabNB7LzRau2IvTU3w/640?wx_fmt=svg&from=appmsg)

1 ms 周期里若采样时刻在 ±0.4 ms 晃，等效测速增益误差就能到几十个百分点。低速时

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM79ySL8Ys0QMsv8dFot1xAbtiawnqzCJPdvTicG79ibMHbtHSKt76NcG2BUVhw6rsCLyLaLhnvoCPgvPiaPyX6PxsxLNu0FoiaRv2T5IBc7OUyj56g/640?wx_fmt=svg&from=appmsg)

 本就小，再叠加量化、摩擦、死区、速度滤波，速度环增益随时间乱变，很容易激发 hunting 甚至极限环，台架就响。根因和高速那出一样，只是表现从「换相相位崩」换成了「速度估计被时间抖动带歪」。

那为什么换更贵的编码器反而更凶？因为空间分辨率和时间准确度是两回事：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5v9ic2qe33gYhVBISrPLLRoC9PFQFP7ntGqyL0APJJM3Vf41wRtUTQXSNGv3jsUCBRYEFxiczicnZ4GStcrpuKKm392Ob0Ua1D0uSVFtq9eHaAA/640?wx_fmt=svg&from=appmsg)

17 位换 19 位，量化步距从约 0.00275° 降到 0.000687°，漂亮了 4 倍。可若是采样时刻抖了 50 µs，这 50 µs 一纳秒都没因为 19 位消失。19 位只是把一条干净但错位的曲线标得更细，Δt 这个量一个 bit 没变。手边唯一能换的旋钮是「位数」，真正坏的旋钮是「时间戳」。

根子在时间基准没对齐，不是角度不准。开了 DC 不等于真锁了——很多设计里编码器采样还跟着自己的 SPI 读节奏走，Sync0 只准时触发了「发送 PDO」，没触发「采样那一下」。于是你准时发出了一份采样时刻不确定的数据。要锁的是位置被物理采样、锁存的那一下，不是报文进网口那一下。差这一个定义，DC 白开。

确诊别只抓网络包。PDO 可能准时得像钟表，内部采样却一直在抖——所以要看三条时间线对不对得上：传感器真实的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM41d1kW0icLEbiaFT1Tm4Go0utxmbiaZCv4JYymkUQkdyYUGblCZpeBnTnG6icEehAeeiaGFB1ChZOpSa8CUvTsGGajdO8gTqu3Jibz6yYrwwaXW3icA/640?wx_fmt=svg&from=appmsg)

（sample/latch 时间戳）、EtherCAT DC / PDO 的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM536sAhMhgKQ8g6HfvGjUW19O6dibewG98RzuTbn35V15gDbpTwbibEToUQ7iauE6IeAZeSmiaBkcAbv69IsRQbWYZqlU6htFgoibNhA2TfxXpPVWw/640?wx_fmt=svg&from=appmsg)

、控制任务真正消费该角度的

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4tjGHibgxCibRiaiaK2MicVwzxSQZxVqTVm8ZZpuBNEsNTBHrtZgeEAT4wZPvMzabzD6K3AAycFveFM2cPzuSxe1BAfB2e8UsUFKJru8fh2WO8HYQ/640?wx_fmt=svg&from=appmsg)

。三者叠一张图，看 p95 / p99 和连续两帧最大间隔，别看均值——十次里九次差 1 µs、一次差 200 µs，均值还是好看，可那一次在高速段就是上百度电气角滞后。给报文加上递增计数和采样时间戳再抓一次，画出来就能分清是角度在抖还是采样时刻在抖。

花了更贵的编码器叫得更凶，根子常常不是分辨率，是时间轴歪了。编码器交给控制器的本来就不该只是一个角度 θ，而是一对 (θ,t)——只有 θ 没有 t，19 位也可能是假精确。
