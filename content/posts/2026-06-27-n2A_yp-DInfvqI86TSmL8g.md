---
title: "汇川 23bit／26bit 绝对值伺服编码器标称高精度，但插值 DNL 和采样延迟，会让速度环把最后几位角度噪声放大成电流啸叫"
date: 2026-06-27T00:00:00+08:00
slug: "n2A_yp-DInfvqI86TSmL8g"
description: "我第一次认真看汇川伺服编码器参数时，注意力不是停在“23bit”“26bit”这几个字上。汇川 SV660ND 页面写得很明确：它配合 MS1 系列高响应伺服电机，采用 23 位圈绝对值编码器，强调运行安静平稳、定位控制更加精准。MS1-R…"
original: "https://mp.weixin.qq.com/s/n2A_yp-DInfvqI86TSmL8g"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWl4ictLJrWnRAiaj27NDUZPpn1T6U0xpmD5ibscf7ictaODVYBPxRI6GKc9I04Pgh5PjWLYL4oF2swS0M4gEm48vOMsOmevs13JHc/640?wx_fmt=png&from=appmsg)

##

## 汇川 23bit/26bit 绝对值伺服编码器标称高精度，但插值 DNL 和采样延迟，会让速度环把最后几位角度噪声放大成电流啸叫

### 一、我看汇川 23bit/26bit，第一眼不是兴奋，是想知道最后几位干不干净

我第一次认真看汇川伺服编码器参数时，注意力不是停在“23bit”“26bit”这几个字上。汇川 SV660ND 页面写得很明确：它配合 MS1 系列高响应伺服电机，采用 **23 位圈绝对值编码器**，强调运行安静平稳、定位控制更加精准。MS1-R 系列资料里又能看到 **26 位多圈绝对值编码器**、功能安全型 26 位多圈绝对值编码器这些配置。再往传感器侧看，汇川 EA38 系列直接叫**伺服整体式光编码器**，特点写的是高精度、高响应、高可靠性、低速度波动，主要用在 100 及以上大基座伺服电机上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIW3LFvwTQop5oS98N6K9gH9XnUwp85xSXcgVXJDgnzFiaNibicj2eydWHKWVEcwZX0ynZ0Bicb5pYAPjAvaCdcXXQPicvfkxl3lbVnE/640?wx_fmt=png&from=appmsg)

这些词放在一起，其实挺有压力的。23bit/26bit 不是单独给样本看的，它最后要进速度环、进电流环、进机械结构。汇川把编码器分辨率推上去，驱动器带宽和电机响应也跟着上去，编码器最后几位就不再是“数字末尾的小抖动”。它会被速度估算拿去差分，会被速度环当成真实反馈，会被电流环变成电流纹波。

我做编码器方向，会本能地盯三个地方：**sin/cos 圆不圆，插值 DNL 细不细，角度数据晚不晚。**

23bit/26bit 是最后吐出来的数字。编码器芯片里真正难看的东西，往往藏在它前面：光源照度不均、码盘刻线误差、PD 阵列失配、TIA offset、sin/cos 幅值不等、相位不是 90°、ADC 采样时刻不一致、插值查表不连续。它们都不一定让编码器报错，但会让最后几位角度变成“看似有效、其实带脾气”的数字。

### 二、插值 DNL 像一把不等距的尺，汇川高响应伺服会把它摸出来

我更愿意把插值 DNL 想成一把尺子。标称 23bit 或 26bit 时，每一小格都应该一样宽。现实里不是这样。某几格宽一点，某几格窄一点，电机慢慢转过去时，反馈角度不是匀速爬，而是一顿一顿地过这些细小台阶。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIV7jrazMYxogKFlzXlz0g5940Uu2IAdnc3IvibmAMiamH4iajNcBCjG1JEJlQL5Sy6uv2eN20NvFCgOxw27miacEp23DjhV6pTaBPs/640?wx_fmt=png&from=appmsg)

理想 sin/cos 很漂亮：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qks3jr8VoPv8T0mQyhBM3f1Ze5h3hM4icIWS4jOBicyzziaMfnuECm9QHqtDickSWC7O2R5TbiageRkykcIia2YOJtK562Nf953N9ePic5GSuXk1tQ/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5aI3bvD3jzzj7JsenZVqjES29Rib2Ga4cPDa9b0hT9g1UWbRIdVL7iasiav0M1QDG8CPcCZFhkk260SBDRDrwkt9UCtvtX9LcbgxhT3g3XG1gXg/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4QwdDw1CfxmmLQ3F4APvVDjiajav4XyeQgicNO1mwCSXvdNiaYEicdgoSEcYEK8EyVicMf8b9zSFt2qqGhRiaTgasrCwnEawGbmFtSNmqM0qIqSRaQ/640?wx_fmt=svg&from=appmsg)

但实验台上看到的波形更像：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7Fno25L19bicc7Wf7GBohHreHW5hmHoruQVRmRG3wTqwnDzcVpiaJN5qzJnplOxD4dromqBgLup5B6jzR3u3YrzDNpypOc9Xpu6wME4JKdzkMg/640?wx_fmt=svg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5glqicAzPPn9DWdxunNlhicg9zjeaduCdiaXmlQQtY8rrDnx2XJKrCrkn9IokCptJ6icdb03xXWJg5Eyo50qtekym9JaVibme6iajINjGNmayexNNg/640?wx_fmt=svg&from=appmsg)

这里 (Os,Oc) 是 offset，(ΔAs,ΔAc) 是幅值误差，(ϕ) 是正交相位误差，(ns,nc) 是噪声。把 (C) 放横轴、(S) 放纵轴，理想情况下是一只圆。offset 一来，圆偏心；幅值失配一来，圆变椭圆；相位不正交，圆开始歪。atan2 仍然能算出角度，但角度已经带了周期性误差。TI 的 Sin/Cos 编码器设计资料专门讨论过 offset、增益误差、相位偏移、迟滞、传播延迟、采样和锁存不同步这些误差来源；HEIDENHAIN 也提到，插值误差会影响定位精度，并恶化速度稳定性和可听噪声。

这个地方很像做芯片调试时的一种尴尬：静态看角度，误差不大；低速匀速转起来，速度纹波冒出来；再把伺服刚性调硬一点，电机开始有细碎声音。你说它坏了吗？没坏。你说它好吗？速度环已经开始嫌弃它了。

我见过很多人喜欢问“到底差几个 bit”。但我觉得更刺人的问题是：**这几个 bit 是等距的吗？** 如果插值 DNL 没压住，最后几位不是精度，而是把光学前端的非理想切成了更细的噪声。

这也是为什么汇川 EA38 那句“低速度波动”我会多看一眼。低速度波动不是靠通信口多吐几位就能换来的，它要光学扫描、模拟前端、插值算法和时序锁存一起干净。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWkS5OXYFrDk4yoMRVHsoKLwm30XtpVgbURUTcyvz70ibicdVBUPrYoUUNibaYABe1viaAgo2TORS5QVGuibj8rOsY7ibk15ibq7MZ8aw/640?wx_fmt=png&from=appmsg)

### 三、最后几位角度噪声进了速度环，就不再是“最后几位”

编码器里一点点角度毛刺，进伺服以后会被速度估算放大。最简单的速度估算就是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5jzgrh4c6fYJ1yMMHFs0l3RibOTqSqMhpcWDok3QGCDeHbDonDMgicOsQvQfVylwIlPXM5XlBGSfbz4K9DFPtxb6sfjkh9zZKVxVwmsOPcuLgA/640?wx_fmt=svg&from=appmsg)

这个公式很温柔，也很残酷。温柔在于它简单；残酷在于 (T_s) 很小的时候，位置里一点点抖动，被一除就变成速度尖刺。

如果角度误差里有一个周期项：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7qks3jr8VoPia3cnLPTjJMCI1LGKA0nclRG8LibSoIUN1RBaWcdwU5a2gdRvaAP0YF4AtMUKlQ5EBrCMtWCMtBib7QeLC4tibxdbgIMzbBgGiaQicw/640?wx_fmt=svg&from=appmsg)

速度误差近似就是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM599OzjVEFklPtaLpU8meib7uLZMG34SZ8OjaRHTCn29DOYb733ICkdiayXMynAeK5NNT8eO9MABAE8CTF3eRyjYlFJ82ZbVB2qicdavjWL9cbjw/640?wx_fmt=svg&from=appmsg)

这个式子就是我对“高位数编码器为什么还会啸叫”的理解。误差幅值 (E) 可能很小，小到静态定位报告里不好看出来；但谐波阶次 (N) 和转速 (\omega) 会把它抬进速度环。速度环一看反馈在抖，就会补电流。电流一补，电机就有声音。机械刚性越高、负载越轻、速度环越硬，这个声音越容易被听见。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWsfPtCicU2iawIqnUGEkesKTblfkvNQyIJibJPY6hCD6XusibuNvicicqtsf1JYyicxbeWErTSXp697M0wAUUkSWt7WcgFXJLftOdHr8/640?wx_fmt=png&from=appmsg)

之前看 LinuxCNC 论坛，有个讨论很有意思：用户说位置反馈看起来正常，但速度反馈噪声很明显。PLCtalk 里也有人把速度分辨率说得很直白：如果 1ms 里只差 1 个 count，换算出来就是 1000 counts/s 的速度分辨率。它们不是汇川的案例，但那种“位置看着正常，速度反馈已经粗糙”的感觉，和伺服现场很接近。

再看 Practical Machinist 里那些编码器反馈导致振动的机床讨论，或者 Control.com 里绝对值 Gray Code 编码器计数乱跳的老帖，我会有同一种感觉：编码器问题很少穿着“编码器芯片问题”的衣服出现。它经常穿成速度毛刺、轴振、偶发跳码、调不顺的刚性、某个速度段的啸叫。

所以我看汇川 23bit/26bit，不会只问“分辨率够不够”。我更想知道：最后几位角度噪声的谱长什么样？是白噪声，还是跟光栅周期、码盘偏心、插值表、ADC 采样有关的周期误差？白噪声还能滤，周期误差进速度环以后，会像一根小刺，固定在某些转速和某些机械角度上扎人。

### 四、采样延迟更阴：角度没错，只是晚了半拍

噪声容易被看到，延迟更阴。因为延迟不一定让角度数值错，它只是让角度对应的时间错了。

光学编码器从光到数字，中间不是一瞬间。光电二极管输出电流，TIA 转成电压，滤波，ADC 或比较器采样，插值 ASIC 算角度，粗细码融合，CRC 打包，串行通信发给驱动器，驱动器再锁存到控制周期里。每一级都要时间。

固定延迟还好，系统可以补。麻烦的是延迟会变：光强低时平均窗口可能变长，噪声大时数字滤波可能更重，某些协议帧错了要重同步，驱动器侧采样刚好跨过控制周期边界。于是编码器给出的 (θ) 是对的，但它对应的是 (

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6OBPpNBN5yrULMpPia6hgdYKYSFAI4dC9ibLmOIyp6kMNutOxZUNX9l8iaWp2Y9ouY2vPmWOwELXOmCtAGsDlOkR32sVQjQJuxvGib2vkiaWwVwQg/640?wx_fmt=svg&from=appmsg)

) 时刻。

频域里可以粗略写：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM6HdhBfcZBAneskhRfnR1TyoqvaOibl72PCsXZOpnSDSwSQRE0dr6lgCxr5C2iccA4T6Hk5Yvb5hIXrSMqAd6icP9dLONKic0g5GEZDOMdd6gtEKQ/640?wx_fmt=svg&from=appmsg)

在控制带宽附近，相位损失近似是：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM4WRWVacpdyeMXlxicYCvVAQVkf51IKJFrrmMmcPLIPeYwSIXJWmOicClnZ4v3I0IG1IJcf08ebCgf7icklp6lbFyGwgITpzibibVluQoZORSwSiaSg/640?wx_fmt=svg&from=appmsg)

汇川这种高响应伺服，带宽越往上走，编码器延迟越不像小事。几十微秒在慢系统里可能被糊过去，在高刚性伺服里就会变成相位裕度上的一口缺口。

绝对值编码器还有一个更细的时间问题：粗码和细分必须在同一个时间意义上成立。可以抽象成：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7rr16GcKibv5hjAXmKpfNj4aib3fickicHMx9zR9Hgufh4b4kuqUov7rD2Gzv11MJmEcJbJPiciarsJv3b2yDh5m2PqMD25yP8NTSUiaS6BOvXN13sQ/640?wx_fmt=svg&from=appmsg)

这里的 (W) 是一致性窗口。粗码道告诉你在哪个区间，细分角告诉你区间内的位置。如果粗码已经跨界，细分还没跨；或者细分已经跨界，粗码还没翻，系统就会看到一次“不一致”。这不是计算能力不够，而是时间没对齐。

只要存在锁存偏差：

![](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM7auCjXzhXOWD89eXQF3sTJ45466KGPn9mQkRfdlhJX2ZJqAhNesicLTp5VpVZC0RUWe3kzBZURW2hHxMzIVgiau1nZxysCjfw4kTMeycoylU2A/640?wx_fmt=svg&from=appmsg)

转速一上来，(\Delta t) 就会变成角度误差。位数越高，窗口越细，粗细一致性的容错越紧。23bit/26bit 听起来是位数问题，做进去以后，其实是时间问题、相位问题和前端噪声问题。

昆泰芯 KTO9512 可以顺手放在这里看一眼。它的公开资料里写到，KTO9512 是游标绝对值光学旋转编码器 IC，集成高清相位阵列光电传感器，输出正弦/余弦信号，可通过三通道 Nonius 插值实现最高 24bit 单圈位置分辨率。这个信息我不会拿来做产品对比，我更愿意把它当成一个信号：现在的高位数光编芯片，早就不是“读一个码盘、算一个角度”这么简单，而是多路相位关系、低噪声前端、插值一致性和时间锁存一起决定单圈角度能不能站住。

### 五、我对汇川高位数编码器的真实看法：位数只是门票，可信角度才是壁垒

汇川把 23bit/26bit 放进伺服系统，我觉得方向是对的。伺服要安静、要平稳、要高响应，编码器不可能停在低分辨率时代。只是从编码器芯片角度看，位数只是门票，真正的壁垒在“可信角度”。

我说的可信角度，不是一个抽象词。它应该能回答这些很小的问题：

-

sin/cos 幅值现在有没有塌？

-

offset 校正量有没有漂？

-

相位误差是不是突然变大？

-

插值 DNL 有没有某个机械角度特别坏？

-

粗码和细分的一致性窗口有没有被擦边？

-

角度数据对应的采样时刻是不是稳定？

-

CRC 错误是不是集中在某些转速或某些电磁环境下？

-

编码器端供电有没有出现很短的低谷？

这些东西不一定适合写在宣传页第一行，但它们决定伺服工程师在现场是“换线、换驱动器、换电机、调刚性”，还是能直接看到编码器链路哪一层在发抖。

我现在越来越觉得，高可靠光学编码器最值钱的地方不是最后多给几位，而是能把位置值背后的状态说出来。角度是结果，光强、幅值、相位、offset、DNL、延迟、同步、一致性窗口，才是结果背后的证据。

所以这篇聊汇川 23bit/26bit，我并不想把结论落在“高位数有没有用”。高位数当然有用。只是高位数进了高响应伺服以后，编码器就没有资格只做一个安静吐数的黑盒了。

它吐出的每一帧角度，最后都会被速度环追问一句：**你准不准，我还能补；你晚不晚、抖不抖、每一小格是不是一样宽，这才决定电机是安静转过去，还是在最后几位里唱出来。**
