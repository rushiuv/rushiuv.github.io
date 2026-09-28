---
title: "为什么两块普通磁编码器，能比一块高价的测得更准？"
date: 2026-03-28T16:52:00+08:00
slug: "-u0jR_oddZix0LA2qTKA7Q"
description: "在很多设备里，系统是否稳定，往往取决于一个很不起眼的东西——角度测量。"
original: "https://mp.weixin.qq.com/s/-u0jR_oddZix0LA2qTKA7Q"
---

在很多设备里，系统是否稳定，往往取决于一个很不起眼的东西——角度测量。

电机转了多少、机械臂停在哪个位置、云台指向哪里，本质上都依赖一个数字：当前角度。

磁编码器就是用来提供这个数字的。它通过感知旋转磁场，把连续变化的磁信号转换成角度值，作为控制系统的“眼睛”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIUMCqmBqkdAh0PznTjia2gC5zoHwWLKlx2Ytw2NZXm5C31TXeiagnia8kTic1yRuXKr9wLGlia24Com8gWza3RpdnE8UAnGbibcrfIeY/640?wx_fmt=jpeg)

问题在于，这只“眼睛”并不完美。

很多人第一次看到编码器数据时会有一种错觉：数值很稳定，看起来误差很小。但只要把数据按角度展开，问题就会变得很明显——角度误差不是随机分布的，而是在固定位置反复出现。

换句话说，它不是“偶尔错一下”，而是“每次转到这个位置都错”。

这种误差对控制系统的影响非常直接。在低速运动时，会表现为速度波动；在位置控制时，会变成末端抖动；在高精度场景下，会直接限制系统上限。

很多人会本能地选择更高精度的芯片来解决问题，但很快会发现一个现实：这些误差中，有相当一部分并不来自芯片本身，而来自信号本身的结构问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIVg1kqBAEOLR2RkAVmhFrfhiaBmBwsibPeIrTLg2fYibbTs6icyT0KPSxyqoz83wntvKvRY8WX6jpTbCkIJQUvVcuMj9jQiaudr7MibE/640?wx_fmt=jpeg)

这时候，引入第二颗编码器，事情就开始发生变化。

两颗磁编码器同时测量同一根轴，并且在安装时引入固定的相位差（例如对置安装）。系统不再依赖单一路径的测量结果，而是将两路数据进行融合。

从结果上看，最直观的变化是：原本周期性的误差明显减弱。

这种改善并不是因为“多了一份平均”，而是因为误差被分解了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIVfz58HSibBtAaH27y4ficytyWTVu3Uc1Wib7ePnBCa2MVr659rmfd1zk5BNwUUyWD8KX1r7Qib5fHcqxDoboNDQQo5rsNy92QuqjE/640?wx_fmt=jpeg)

要理解这一点，需要往信号本身看一层。

磁编码器内部并不是直接测角度，而是获取两路信号（通常称为 X 和 Y），它们理想状态下应该分别是正弦和余弦关系。角度的计算，本质上是通过这两路信号的比值关系得到的。

一旦这两路信号偏离理想状态，就会产生可预测的误差结构。

最常见的几种情况如下：

当信号存在偏置（offset）时，两路信号整体偏离中心点。原本应该围绕零点旋转的信号轨迹被平移，导致角度计算出现一倍角误差。这类误差在一圈中出现一次，通常与磁铁偏心、应力或温漂有关。

当两路信号幅值不一致时，信号轨迹由圆变成椭圆。此时角度误差会表现为二次项，即一圈中出现两次波动。这在霍尔类传感器中非常常见，尤其在温度变化或气隙变化时更明显。

当两路信号不再严格正交时（存在相位误差），信号的几何关系进一步扭曲。一倍项和二次项会发生耦合，误差形态变得更加复杂。这类误差往往来源于通道匹配不一致或前端电路偏差。

这些误差有一个共同特征：它们不是随机的，而是“跟角度绑定”的。

也正因为如此，单个传感器很难摆脱它们。

而两颗传感器一旦形成相位关系，就提供了额外的信息维度。

设真实角度为 θ，两颗传感器分别输出：

θ₁ = θ + ε₁(θ)

θ₂ = θ + ε₂(θ + Δ)

其中 Δ 为安装相位差。

这个 Δ 的存在，使得同一类误差在两路信号中呈现出不同的相位特征。例如，一些由偏心或偏置引起的一倍角误差，在对置结构下会表现出明显差异；而某些幅值类误差，在两路中的响应也不会完全一致。

一旦把两路数据统一到同一角度参考系，再进行建模，就可以把这些误差从“一个整体”拆成“多个可识别的成分”。

工程上常见的做法，并不是简单平均，而是：

先进行角度对齐 → 再进行误差拟合 → 最后做补偿或加权融合

这一步之后，误差就从“不可控”变成“可建模”。

这也是为什么两颗普通编码器，有机会超过一颗高端芯片。

行业中已经有不少类似思路的应用。maxon 在 EPOS4 中采用电机侧与负载侧双编码器反馈，用于提升位置精度与动态性能；Synapticon 和 Ingenia 的驱动系统中也支持双编码器结构，用于提高控制稳定性；学术界在机器人关节控制中，也广泛使用双编码器来抑制减速器带来的误差和振动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIUWfwa1IiaUR9MBpeRUhgfKmR2EIGgH8AAgeeaP6tVtXwg7YQicBxRbdOK94Z7ZA9RdV4lnyYYykybwJF6oGh9nsFa7G6FPBniamU/640?wx_fmt=jpeg)

在磁编码器领域，像昆泰芯微电子这样的厂商，也在单芯片内部加入非线性校准与误差补偿机制，本质上也是在做同一件事：识别误差结构并修正它。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIXxDQ4myIb9qNTDmjmt38NfEMoCkfM5p1t6Z84b5ibOvicibRlGomzXa4picSvEQzIVPMuRLe6NUKiata2RSGphDFVgFuibODibTgBbJE/640?wx_fmt=jpeg)

只是单芯片是在“内部做”，双传感器是在“系统层做”。

当这两条思路结合起来，精度的提升就不再依赖单一器件，而依赖整个系统对误差的理解能力。

到这里再回头看最初那个现象，就不再奇怪了。

两颗便宜芯片叠在一起，并不是简单叠加性能，而是通过结构和算法，把原本混在一起的误差拆开，再逐步压掉。

精度不是被“平均”出来的，而是被“识别”出来的。

如果你在做电机控制、机器人或者编码器相关设计，评论区可以聊聊你遇到过的误差类型，或者你是怎么处理 offset / 幅值 / 相位这些问题的。很多看起来“玄学”的现象，背后其实都有很明确的结构逻辑。

有兴趣加作者朋友聊聊：

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIW3nl7Chw6rHETibswaHO2gmDvvFP9uHvThjmYpMxlA9py8YiarcNw70BSaESwwhPU6HPE8ibIk3Z8s9ucq72MkxM8oQ1f7xzqgJ0/640?wx_fmt=jpeg)
