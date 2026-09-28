---
title: "芯片设计是一个 大概率会失败的事, 也聊聊编码器芯片 KTM5800 架构"
date: 2026-08-18T08:08:00+08:00
slug: "tKPJ756Y-hhozRbyt-Zvlw"
description: "CHIP DESIGN · ENCODER IC · TAPE-OUT"
original: "https://mp.weixin.qq.com/s/tKPJ756Y-hhozRbyt-Zvlw"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWB9ZibtsqrbPHhOgOFYsJ8kHNbkZZsVAK3U84wRJywoJpdUBVQHCOib3xva4iaz5wkGUia2jOtLxjibg0QwwQvQKmy0J8ojmUSYJck/640?wx_fmt=png&from=appmsg)

CHIP DESIGN · ENCODER IC · TAPE-OUT

## 芯片设计是一个
大概率会失败的事

一个做编码器芯片的人，关于 Tape-out、验证、边界条件和硅片回来的几次深夜。

“没发现问题”和“没有问题”，完全是两回事。

做芯片久了以后，有一个场景我一直觉得很特别。Tape-out 前最后几天，真正让人不安的往往不是还有几个红色 violation，而是全绿了。

STA clean，CDC clean，DRC、LVS clean，Regression 跑完了，coverage 也够了，模拟 corner、Monte Carlo 都扫过了，该签的 sign-off 全签了。然后群里有人问一句：“还有问题吗？”这时候，反而没人敢很快回答。

因为做过几颗芯片的人都知道：**“没发现问题”和“没有问题”，完全是两回事。**

2024 年 Siemens EDA 与 Wilson Research Group 的 IC/ASIC 功能验证调查里，first-silicon success 只有 14%。14% 不能简单理解成剩下 86% 全部报废或者都要 respin，但已经足够说明一件事：第一次把硅拿回来，各项功能和指标就完全达到预期，本来就是一件很难的事。

工具越来越强，服务器越来越多，Verification 越来越规范，工程师也没有突然变笨。真正麻烦的是：**每一个模块都可以是对的，最后系统仍然可以错。**

### 做 KTM5800 这种编码器芯片，这种感觉尤其强

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXmEvCZQiajYEibdPEfZ2CLonXsewiau4meky347WerXw2X6dFKBibiaIP6e9e4EjicNgRmpOGPic21v1PELkqltFlgiaqgRF9k683BNxk/640?wx_fmt=png&from=appmsg)

###

KTM5800 的架构其实特别适合说明这件事。它不是一颗“读两路 sin/cos 然后做个 atan2”这么简单的芯片。外部 AMR、TMR、光栅或者光编送进来的是差分正弦、余弦模拟信号，前面经过可编程增益和双 16bit、2MHz SAR ADC，后面还有数字滤波、线性校准、反正切角度计算、非线性补偿、多极对计数、圈数计算，最后再从 SPI、ABZ、UVW、PWM 等接口送出去。单对极细分最高 18bit，同时支持最多 4096 对极，因此整个绝对位置可以扩展到 30bit。芯片内部还有 256 点非线性误差 LUT、自动线性/非线性校准等模块。

这条链拉开以后，你会发现一个很残酷的事实：**每一块都验证正确，并不能推出最后的 angle 是对的。**

因为真正危险的，往往发生在模块与模块之间。

### 30bit 不是一个寄存器，而是一串脆弱的时间关系

比如 5800 支持最多 4096 对极。对于多极磁环或者光栅，ADC 和 ATAN 算出来的首先只是当前这一小段周期里的 fine angle；要得到整圈绝对机械位置，还必须知道自己现在位于第几个周期。

可以粗略理解成：**绝对位置 = 当前周期编号 + 当前周期内的细分角度。**

真正麻烦的是跨界那一拍。假设 fine angle 正从 359.999° 跳到 0°，同时周期计数应该从 N 变成 N+1。如果数字滤波后的 fine angle 和 cycle counter 在 pipeline 上差一拍，会发生什么？

两个数都可能是合法的。fine angle 没错，counter 也没错。只是它们不是同一个时刻的数据。最后拼出来的绝对位置，就可能瞬间错一个 pole pitch。

4096 对极时，一个 pole pitch 只有约 0.0879°。对一颗目标做到百分之几度级 INL 的高精度编码器，这已经完全不能忽略。更恶心的是，它不是一直错，而是可能只在跨周期那一拍错。静态转台慢慢扫，未必容易看到；高速跑起来，却可能每跨一次边界都留下一个异常点。

这类 bug 最难受的地方就在这里：**ATAN 对，counter 对，filter 对，最后答案错。**

### 两路 ADC 都对，不代表这一对数据是对的

编码器的另一条命门是 sin/cos。理想情况下，两路信号分别代表同一个物理时刻的正弦和余弦，然后送进 atan2。

KTM5800 使用双 16bit、2MHz SAR ADC 去读取两路差分信号。这个架构本身就是为了高速、低延迟地把两路正交模拟量送进后面的数字处理。

但从 verification 角度，真正该问的不是“两个 ADC 都准吗”，而是：**这两个 code 是否代表同一个物理时刻的磁场？**

假设 sin/cos 等效采样时间存在 Δt，转子角速度是 ω，那么两路对应的相位天然就会出现 δ = ωΔt。转速越高，同样的时间误差会直接变成更大的角度误差。

所以静态精度很漂亮，并不能证明高速动态精度也漂亮。ADC 的 ENOB 可以对，offset/gain calibration 可以对，ATAN 也可以 bit-exact，最后仍然可能因为整个链路的时间关系出现动态误差。

做编码器以后，我越来越觉得：**高精度位置芯片，本质上不只是“数值正确”，还是“时间正确”。** 一个 angle，如果不知道它属于哪个时刻，这个 angle 本身就还没有定义完整。

### 我现在反而不太怕 report 里有红色

STA 报 −100 ps，我反而放心。修这 −100 ps 就行。Monte Carlo 某个 corner 尾巴很难看，也没关系，继续拆 mismatch。非线性校准在某个点挂了，就去看 LUT、插值和 wrap。SPI assertion 报 frame 异常，就沿着 waveform 往前追。

至少问题已经站在你面前。

真正让人睡不着的是：STA 全绿，Regression 全 PASS，角度 INL 漂漂亮亮，Monte Carlo 也很好，然后晚上十一点突然有人在群里说：“等一下，多极模式下 fine angle 和 cycle count 跨界那一拍是一起锁的吗？”

群里突然安静了。有人回一句：“正常情况跑过。”然后第二个人问：**“4096 对极、最高速、跨界，同时 SPI 连续读呢？”**

没人回答。接下来就是重新开服务器，补 testcase，重新跑。

这才是 Tape-out 前真正让人怕的东西。

### EDA 最大的边界，是它不会怀疑你没有怀疑过的事

STA 可以检查几百万条 path，前提是 constraint 写对了。CDC 可以帮你检查跨时钟域，前提是你意识到这里的问题不仅仅是 metastability，而可能是 multi-bit coherency。Monte Carlo 可以跑一万次，前提是那个物理失效机制已经在 model 里。Formal 可以证明一个 property 永远成立，前提是你写下来的 property 就是系统真正应该满足的东西。

KTM5800 这种芯片尤其明显。模拟输入、ADC、校准、filter、ATAN、非线性补偿、周期计数、绝对位置、SPI/ABZ 输出，一路上几十个状态和时间关系叠在一起。框图画出来非常清楚，但真正的硅不会按照框图一块一块工作，它们是在同一颗 die 上同时工作的。

EDA 很强。

**但它有一个非常冷酷的边界：你没有告诉它的那个世界，对它来说根本不存在。**

### 总得有一个人说：出吧

所以 Tape-out 前经常会发生一种很有芯片行业特色的事情：一个已经 review 三遍的模块又被打开，一个两个月前 close 的 issue 又被翻出来，晚上十一点群里突然有人发一句：“我刚想到一种情况……”

这句话很烦，但所有人都会点开。

因为真正可怕的从来不是已经找到的 bug，而是那个已经跟着 GDS 一起出去、却还没有人意识到它是 bug 的东西。

文件最终总要发出去。所有 report 都绿了，所有人都签字了，角度仿真不知道已经转了多少亿圈，总得有一个人说：**“出吧。”**

按下去以后，办公室其实什么都没变。屏幕还亮着，服务器还在跑，桌上的咖啡也还没喝完。但做过 Tape-out 的人都知道，从这一秒开始，同一个错误的价格已经变了。

昨天发现 fine angle 和 counter 差一拍，可能只是改几行 RTL；昨天发现 LUT wrap 有问题，也许只是改一个地址；昨天发现输出 snapshot 不对，可能只是加一个寄存器。今天再发现，可能是 ECO。再晚一点，是 mask。再晚一点，是 respin。再晚一点，就是客户把高速电机架起来，然后问你：**“为什么这个编码器偶尔跳一下？”**

Bug 没有变。**只是它活得太久了。**

### 让错误死得早一点

所以我们做 verification、corner、Monte Carlo、formal、FPGA、review、sign-off，从来不是因为这些东西能够证明这颗编码器芯片一定成功。

我们只是想让错误死得早一点。

最好死在 spec。晚一点，死在 Matlab。再晚一点，死在 RTL。再晚一点，死在 simulation。再晚一点，死在 FPGA。

最贵的，是让它一路活着，穿过 GDS，穿过 Tape-out，最后等硅片回来，外面的磁铁真正转起来，它才第一次从角度数据里钻出来。

**芯片设计，本来就是一个大概率会失败的事。**

而编码器芯片更残酷一点。因为最后审判你的，不只是数字逻辑，还有真实的模拟信号、磁场、气隙、偏心、温度、转速、EMI，以及一个从来不会按照 testbench 方式运行的电机。

我们能做的，不过是在每一次 Tape-out 前，把那些失败的可能一个一个提前找出来。直到实在找不到了。然后发送 GDS。

**剩下的，交给硅，和那颗真正转起来的磁铁回答。**

我们能做的，不过是在每一次 Tape-out 前，把失败的可能一个一个提前找出来。

剩下的，交给硅，和那颗真正转起来的磁铁回答。
