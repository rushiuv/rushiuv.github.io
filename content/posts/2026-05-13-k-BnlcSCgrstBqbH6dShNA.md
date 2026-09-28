---
title: "TDK TMR角度传感器杂散场补偿深度解析：从结构假设、专利路线到离轴磁编码器的校准边界"
date: 2026-05-13T09:33:00+08:00
slug: "k-BnlcSCgrstBqbH6dShNA"
description: "很多人第一次接触磁编码器，最容易被一个直觉骗住：没有光学码盘，没有镜头，没有读头，磁铁一转，芯片一算，角度自然就出来了。"
original: "https://mp.weixin.qq.com/s/k-BnlcSCgrstBqbH6dShNA"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWThQyqPJu1e2ZpCtYu7vEHPQLsBKQ1wmdP4zJh0HrFL9ljLLKmOwNwbXyO7FnbjB1479Os2StsiaIxb8jRM1JbR2nt8OE2icbXo/640?wx_fmt=png&from=appmsg)

## TDK TMR角度传感器杂散场补偿深度解析：从结构假设、专利路线到离轴磁编码器的校准边界

很多人第一次接触磁编码器，最容易被一个直觉骗住：没有光学码盘，没有镜头，没有读头，磁铁一转，芯片一算，角度自然就出来了。

可真到现场，系统往往不是败在“算不出角度”，而是败在“局部磁场已经不是你以为的那个样子”。正转和反转误差曲线对不上，换向那一下最难看，低速时速度纹波莫名放大，继续单向转一会儿，曲线又像自己恢复了。很多团队第一反应会先怀疑 ADC、滤波器、CORDIC、补偿参数，甚至把问题先归到“芯片磁滞”上。TDK 今年两次公开更新把这件事说得比以前直接得多：3 月 9 日更新了 “Stray-field compensation by TMR sensor”，4 月 1 日更新了 “TMR Angle Sensors Selection Guide”。

两页放在一起看，信号已经非常明确：主流厂商现在公开讨论的重点，不再只是裸芯片精度，而是系统里的杂散场、结构磁路、机械失准和运行历史如何共同改写角度结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIUjDBcnsWVVsGjkdicWngzooMW2afMQYYWclxfjLVw7z4rPRtEbsgrVgNheDcdgH4TibeqYUNB2A6npJ4CmaH6UhtC6Uv01duVaI/640?wx_fmt=png&from=appmsg)

### 一、磁编码器真正测到的，不是角度，而是局部磁场方向

磁编码器并不直接“看见角度”。它先测磁体在传感器位置产生的磁场分量，再把磁场翻译成角度。最简化的二维模型可以写成：

然后再由芯片或 MCU 做：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIX27x2JMJticUV7957nyqqr9icZYJC5kl92dCiaz2icac1nbStfsdGVPNGiars06Rk8pwEzHZdJCA6VM85ibBhWpnUQ89FbY2xORnLOM/640?wx_fmt=png&from=appmsg)

这一步看着简单，后面所有麻烦都藏在这里。因为只要传感器位置的总磁场被改写，哪怕机械角度没变，最后算出来的角度也会变。TDK 这次把杂散场补偿单独拿出来讲，本身就说明它默认的误差模型，已经不是“单一芯片误差”，而是“信号场 + 外扰场 + 结构畸变 + 温度/寿命效应”的叠加问题。Selection Guide 里也已经把数字产品的 pre-calibration、in-application calibration、static compensation、dynamic compensation 明确分层写出来了。

### 二、同一个机械角度，为什么系统却可能读出两个不同答案

很多人第一次遇到正反转误差不一致，会本能地问：磁铁不是已经回到同一个角度了吗，为什么读数还会不一样？

因为同一个机械角度，不一定对应同一个局部磁场。更完整地写，传感器实际看到的是：

这里的

 是外部附加杂散场， 则是钢轴、轴承、螺丝、支架、铁芯端部等铁磁件把磁路二次改写后的结果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWFU1SYGBebVljFIV8tNLpia57uyuUukE8d1RfWadvoHLGmb2oR0SJeGCM6rWibUutQ3aP6n5WsVhXV5IOBqQrre8SAEUOcww6FU/640?wx_fmt=png&from=appmsg)

TDK 相关专利已经把这个点写得很清楚：铁磁轴会把原本外部“均匀”的杂散场，在局部空间里扭成“不均匀”的分量。也就是说，系统最麻烦的地方，常常不是多了一个固定偏场，而是外界干扰被结构重新塑形成了位置相关的局部场。

这也是为什么很多看上去像“芯片问题”的现场症状，主因其实可能在结构里。你以为是算法不稳，实际上可能是旁边那根钢轴把共模外扰改成了局部非共模；你以为是滤波器没调好，实际上可能是支架和轴承先把磁路的对称性破坏了。这个判断不是情绪化归因，而是专利文本直接给出的物理前提。

### 三、TDK 这次真正公开的重点，不是公式花不花，而是结构条件先不先成立

很多人盯着 TDK 那页杂散场补偿，第一眼只看公式。其实这次最值钱的，不是式子，而是它先把“结构怎么摆”说穿了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXssG2Qrb0ny5MKCJICrvNsufm4C9qZsdzyyAEaLic4m7edKVMwic55g5S1bkKC0bpnOrE8N1grDmQ1f1uQgOrLjBlo2Cib3NiaWLY/640?wx_fmt=png&from=appmsg)

在同轴方案里，TDK 明确写到：两颗传感器布在 PCB 两侧，并与旋转磁体共轴；这样两颗传感器看到的 stray-field noise 基本同相、同级别。然后再通过板厚，让两颗传感器接收到的目标磁体场强形成固定比例，并建议

，TDK 直接把这叫作 gradiometer design。更关键的是，它还给了一个具体仿真例子：在 Br=330 mT、单极对圆柱磁体  mm、杂散场 4 kA/m（约等效 5 mT）、 mT、 mT、间隙 1.0 mm、 的条件下，角度误差从单传感器的  压到双传感器补偿后的 。这不是“调一调权重”，而是结构先把问题变成可消元的样子，算法才有意义。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIV4dIzpw2QViaI1gsUjI5IoeILUS1b49k02LqN0D0hke6IjEtGb4ibQ4gNm3bVbwsNXTDs4ZX5mAh0SmfsicZaMMJeHKv0ialGtL0s/640?wx_fmt=png&from=appmsg)

离轴方案里，TDK 说得同样直接：把两个传感器放在相对于目标磁信号 180° 反相的位置，此时两者对 stray field 的响应仍近似同相同级别；再通过 differential output 增强信号、压制杂散场噪声。换句话说，离轴补偿也不是“多放几个点，再让算法神奇收尾”，而是先让目标信号走差模、让干扰尽量走共模。

所以，这次 TDK 真正公开承认的，是一句行业里很多人嘴上不愿明说的话：**补偿不是先有算法，再去要求结构配合；而是先把结构做成“可补偿”的结构，算法才配拥有名字。** 这句话是我基于 TDK 页面内容做的归纳，但它和页面给出的 on-axis / off-axis 条件是完全一致的。

### 四、那条核心公式，本质上到底在消什么

TDK 给出的同轴补偿式是：

看上去像个经验加权，其实本质是一阶共模干扰消元。

把第

 个传感器接收到的场写成：

那么它算出来的角度是：

如果外部附加场不算太大，可以做一阶展开。令

则有近似关系：

于是：

再设

就得到：

两式相减：

所以：

这就是 TDK 公式的物理核心：**同一股外部干扰，对强信号造成的小角度偏差和对弱信号造成的大角度偏差，按比例组合后，一阶项可以直接抵消。** TDK 页面还特别强调，这个补偿是“with each sample of a sensor signal”完成的，因此可以覆盖高动态场景，也能补偿 DC 和 AC stray fields。它不是先转一圈存查表，而是在每个采样点现场做消元。

### 五、这套方法为什么不是万能药：它最怕“共模假设”先崩

差分补偿最容易被写得过度乐观，好像一多传感器，世界就干净了。

其实它最脆弱的地方恰恰很清楚：它要求多个传感器在同一时刻看到的是近似相同的外部干扰，也就是共模前提还成立。一旦钢轴、轴承、螺丝、支架、铁芯端部把原本均匀的外部场空间扭曲，变成了局部不均匀分量，那么原来那种“目标信号走差模、干扰走共模”的假设就先碎了。US20220393554A1 对这个问题写得非常直接：ferromagnetic shaft 会 spatially distort an external homogeneous magnetic stray field，从而引入 inhomogeneous stray field component。到了这一步，差分不是没用，而是它不再能把问题一次性吃干净。

所以现场真要排查，最该先看的常常不是寄存器，而是磁路边界：钢轴是不是太近，轴承位置有没有把对称性打歪，螺丝和支架是不是把原本可共模处理的外扰重新塑形成局部场。如果这些前提不成立，后面再漂亮的补偿公式，也只是补一个不稳定系统。

### 六、行业更深的一条路已经出现：不是只抵消杂散场，而是把杂散场本身测出来

TDK 这次公开的主线仍然是多传感器几何与差分补偿。但从专利路线看，行业已经在往更深的一步走：不只是想办法让杂散场“被抵消”，而是让杂散场本身变成可观测量。

US12215973B2 的做法很典型。它把一个 operating in saturation 的角度传感器，和一个 operating in linear operation 的磁场传感器放在同一系统里。前者负责测转角，后者负责直接估计外部 stray field；然后控制器基于线性通道测出来的外扰信息，去补偿饱和角度通道的角度误差。专利里还明确提到 quasi-static stray field、autocalibration、以及由线性传感器提取的 offset information 和 amplitude information。它已经不是“我猜有干扰，再去差分抹掉”，而是“我先把干扰测出来，再把它作为状态量喂进补偿链”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXW4ELT4a9k3N3xtFwLhlB6ABZH0q7dCo14YiaOmjkluCGKRsmfqzjSogibXyLicghpaeGHwH5HOpVsMT0kr65STkW2N3WYuMcv8U/640?wx_fmt=png&from=appmsg)

这条路线的意义非常大。因为它意味着未来高端磁角度系统的竞争，越来越不像“谁家 xMR 单点精度更漂亮”，而更像“谁能更早把外扰提升为可观测、可建模、可验证的系统变量”。从系统工程角度看，这比再卷半位分辨率更值钱。

### 七、把 TDK 近几年的产品演进串起来看，路线其实很清楚

如果只盯 2026 年这两次更新，很容易误以为 TDK 是突然开始重视杂散场。

其实不是。Selection Guide 已经把它的产品层级写得很清楚：前面是 TAS214x、TAS414x、TAB4140、TAA6140 这类高灵敏度模拟 TMR 角度传感器，主打 SIN/COS、宽温、宽磁场和低漂移；后面是 TAD214x、TAD4140 这类数字产品，已经明确写出 pre-calibrated、in-application calibration、static compensation、dynamic compensation。数字产品里，代表性的 room-temperature standard angle accuracy 已经做到

，全温区 standard angle accuracy 也给到了  到  这一档。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIUIGYMZMS9qQBfMM3tjPbB5YWClG0vYHD5PAO8Xic0KAchCu43V4lJSnHiak14u7RCTVN7jKSmkYsic24k9gWiaMIorZZAuyRamHl8/640?wx_fmt=png&from=appmsg)

这条演进线翻译成人话其实很简单：

从前卖的是“我这颗 TMR 裸桥很灵”；
后来卖的是“我这颗芯片内部补偿更多了”；
现在开始卖的是“我知道结构会怎么把你搞坏，我还能在系统层把外扰压下去”。

这就是为什么我会说，TDK 这次真正值得行业警觉的，不是一条公式，而是它把竞争重心从“裸芯片精度”公开推向了“系统解释力”。这个结论是基于产品层级、补偿分层和杂散场页面合在一起做的归纳。

### 八、这件事对行业最现实的提醒：下一轮不是卷位数，是卷谁先把边界讲清楚

对客户来说，真正痛的从来不是“静态精度少了半位”，而是这些问题没人能提前讲明白：

为什么正反转曲线不一样；
为什么换向时突然跳一下；
为什么实验室里好好的，一上整机就坏相；
为什么结构一叠起来，速度纹波突然变丑；
为什么问题明明出在磁路边界，最后却总有人先去改滤波器和寄存器。

谁能把这些问题在设计前期讲透，谁就更像系统供应商。谁还只会甩一张静态精度表，谁就还停留在卖零件。

所以，TDK 最近这两次更新真正值得行业重视的，不是“又秀了一下补偿公式”，而是它公开承认了一件不太浪漫、但非常值钱的事实：**很多时候，先让系统失控的，不是算法，也不是 ADC，而是旁边那几颗沉默的铁件。** 这句话不是原文直引，而是对 TDK 页面和相关专利共同指向的工程现实所做的总结。

真正高端的产品，不是“在理想条件下很准”。
真正高端的产品，是“在不理想的现场里，知道自己为什么会不准，还能把这份不准压下去”。
