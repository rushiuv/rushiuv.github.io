---
title: "TMR 不是霍尔的高级版!! 一个告诉你在第几格，一个告诉你在第几度"
date: 2026-08-10T00:30:00+08:00
slug: "qxZg_5qP73aXrJaMZE2YCQ"
description: "霍尔开关回答\"转子在第几个 60° 区间\"，TMR 角度传感器回答\"磁场现在指向多少度\"——这不是低配和高配，是两种完全不同的位置反馈。"
original: "https://mp.weixin.qq.com/s/qxZg_5qP73aXrJaMZE2YCQ"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIU1w7IPzYiag9M3vBQ6tvPTU0rflfGeKb7hIuRCibb9WLOibpRdnO9HWSsEprfGpHVvwkFEZeDrZ25plHYFQzHO3K48SNU9OEVEVo/640?wx_fmt=png&from=appmsg)

工程手记 · 汽车电子

## TMR 不是霍尔的高级版
一个告诉你在第几格，一个告诉你在第几度

霍尔开关回答"转子在第几个 60° 区间"，TMR 角度传感器回答"磁场现在指向多少度"——这不是低配和高配，是两种完全不同的位置反馈。

上周帮朋友看一颗汽车油泵电机的方案，他开口就问：

"能不能给我找一颗**最好的霍尔开关**？"

我看了一眼他的控制框图：电流环、位置环、Park 变换都画上了，显然准备做带位置传感器的 FOC。

我说，这不是"霍尔够不够好"的问题。你现在需要的不是一个更好的霍尔开关，而是**另一种信息**。

三颗开关型霍尔告诉控制器：**转子已经走进了下一个换相区间。**

TMR 角度传感器告诉控制器：**磁场现在指向多少度。**

一个回答"**第几格**"，一个回答"**第几度**"。这不是低配和高配的区别，而是两种完全不同的位置反馈。

### 01先把"霍尔"两个字说清楚

严格地说，不能简单地把霍尔和 TMR 对立起来。霍尔是一种**磁敏原理**——除了只能输出 0 和 1 的霍尔开关，也有能够连续测量磁场方向的二维、三维霍尔角度芯片。

反过来，TMR 角度芯片也不一定非要输出高分辨率角度。有些数字 TMR 产品同样可以输出 UVW，模拟三霍尔换相信号。

所以这篇文章真正比较的是：

三颗开关型霍尔构成的六步换相反馈，与输出 sin/cos 的 TMR 连续角度反馈。

### 02三颗霍尔，到底知道多少角度？

典型无刷直流电机在定子上放置三颗霍尔开关。转子永磁体旋转时，每颗霍尔只输出两种状态：磁场超过正向阈值输出 1，落到反向阈值以下输出 0。

三路信号组合后理论上有八种状态。其中 000 和 111 通常不是正常换相状态，剩下六种有效组合对应一圈电角度中的**六个区间**。每相邻两个换相沿之间相差约 **60° 电角度**。

也就是说，当霍尔状态为某个组合时，控制器能知道转子进入了第几个换相区间，却不知道它在这个区间里的准确位置——它可能刚刚越过边界，也可能已经走到区间中央。从霍尔状态本身看，这两种位置完全一样。

这并不是霍尔"精度差"，而是六步换相根本不需要更多信息。控制器只需要在正确的区间给两相绕组通电，第三相悬空，就能让电机转起来。

电梯按钮也是这样。亮着"3"，只说明电梯在三楼，不会告诉你轿厢停在三楼地板上方 2 mm，还是下方 3 mm。对乘客来说，这些信息没有必要。

三霍尔便宜、直接、鲁棒，正是因为它只回答控制器真正需要的六个状态。（TI：Hall Sensor-Based Trapezoidal Control）

### 03TMR 读到的不是"格子"，而是磁场方向

TMR 角度传感器走的是另一条路线。芯片内部通常布置两组互相正交的惠斯通电桥。当轴端磁铁旋转时，芯片所在位置的平面磁场方向也随之旋转，两组桥分别产生近似正弦和余弦的差分信号：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIViak1lPRdtmbAn5rSgLAnsEgjoQVibJozpl2ibLuvXtd523SCibnAh4rlN8bViaqdEt5ga2DFNIM7IictKricuT4BWr0uhicmzwBqvGuU/640?wx_fmt=png&from=appmsg)

其中 **A、B** 是两路幅值；**Osin、Ocos** 是直流偏移；**Φ** 是两路相对于理想 90° 正交关系的相位误差。

经过偏移、增益和相位补偿后，控制器用 atan2 解算磁场方向：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXg8SUGCpwC2E1WOIl4hcsh4IrGVPUx0uslpplj9x5bShx3qCDcccBApKLK9SbKxhjUVF6wgM1hKhCWVnAYdcIzqtP6WZl6NtE/640?wx_fmt=png&from=appmsg)

如果轴端使用一颗对径二极充磁磁铁，这个角度通常对应转轴的机械角度。电机控制所需的电角度，还要根据极对数和零位关系换算：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWV7AVtFGiaqbYJXDngNydSlwgOmrZyL1sU2p1icASaLCicDzgehsnlAlUeen0VIwgK3aYCibeeYHD0T0SFFfBol2QEZjEJRXf1ZfU/640?wx_fmt=png&from=appmsg)

**p** 是电机极对数，**θ0** 是磁铁零位、传感器零位与电机磁极零位之间的安装偏置。这一步很重要：TMR 并不是把"绝对电角度"直接从芯片里吐出来，它先测磁场方向，系统再把磁场方向翻译成机械角度或电角度。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIXjllAgWUgLH9VJI4trXdb3TgO1erZZM5zGYOyb1zKRjHWYQNdyRMFGzfQatZcEiaEwPmGlKOyPj5czK66XD4Rtibb83g2hARuFk/640?wx_fmt=jpeg&from=appmsg)

图：TMR 自由层磁化方向跟随外部磁场旋转，实现连续 360° 角度检测（来源：TDK）

### 04TAS2142：信号大到可以直接进 ADC

TMR 的物理基础是磁隧道结。两层铁磁材料之间夹着极薄的绝缘势垒：一层磁化方向固定（钉扎层），另一层跟随外部磁场转动（自由层）。平行时电子更容易穿过势垒，反平行时隧穿概率下降，器件电阻随之改变。

在简化的 Jullière 模型下，TMR 比率可以写成：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVpPYancgiaUkpHEzKG8u4onfO7BIPOsYQSC1zZsGfCpRT4ySfzqpJ9iaUB7xyMg2kIIXwCABBQc4SEs6AJGtXfIuGIXbkjSCGJo/640?wx_fmt=png&from=appmsg)

真正落到产品上，TMR 最直观的优势不是公式，而是**输出幅度**。以 TDK TAS2142-AAAC 为例，其内部包含两组全桥，直接输出差分 sin/cos 信号：

✅ 5 V 供电时，差分输出典型值 **3.0 Vpp**（信号大到可直接进 ADC，通常不需要再加低噪声放大器）
✅ 推荐供电 3.0～5.5 V；推荐磁场 20～80 mT（80～120 mT 可工作但精度下降）
✅ 工作温度 −40～150°C，通过 **AEC-Q100 Grade 0**
✅ 推荐磁场和全温范围内，补偿后角度误差最大 **±0.6°**

TDK 的对比资料给出的典型结果是：其 TMR 输出约为 AMR 的 20 倍、GMR 的 6 倍。这里比较的是特定 TDK 产品与其选取的传统器件，不应外推成所有产品的统一比例，但足以解释为什么 TMR 可以获得如此大的桥路输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIXYpaUMYfBzxnVNHA8zD2iaWlHHuT8vRZWYNzTUoX9CibzN7BCicVBUwfEELsI7157Y10aGM718MYoEicSLN6HV9jX5H8PfkibJwOTw/640?wx_fmt=jpeg&from=appmsg)

图：TDK 对 AMR、GMR、TMR 的结构、输出及温度特性比较（来源：TDK）

不过，3.0 Vpp 不等于拿回来就有 ±0.6°。TAS2142 数据手册给出的正交角范围是 87°～93°，两路幅值同步比 97%～103%，初始差分 Offset 为 ±5 mV/V。因此数据手册中的角度精度有一个不可忽略的前提：

它是在 Offset、Gain 和 Phase 补偿之后得到的。

### 050.2 mm 真正说明了什么？

在我们接触过的一套磁铁、气隙和封装结构中，磁铁轴心与芯片中心偏离超过约 0.2 mm 后，非线性误差开始明显上升。0.2 mm，大约只有两张普通打印纸叠起来那么厚。

这个数字很抓人，但必须说清楚：**它不是所有 TMR 传感器的通用红线**。磁铁直径、厚度、气隙、磁化均匀性、芯片感应区位置和目标角度精度不同，允许偏心量也会完全不同。

TDK 官方给出的一个特定轴端布局案例中，当传感器与磁铁端面间隙为 2.0 mm 时，允许旋转轴偏移达到 ±1.8 mm，角度误差仍能控制在 0.1° 以内。

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIWhyJiaDKHrcFyUqPc3hur3OVzcNVcqdib0Qg11z5vF90V9IBdtlTibhSKLTvz00ykichJTVeCkjwsU0sBeo2pybnNsP9KkNH12Dtw/640?wx_fmt=jpeg&from=appmsg)

图：TDK 给出的轴端磁铁布置示例（该结果只对相应磁铁、气隙和结构成立，不能直接移植到其他设计）

这张图恰恰说明：**偏心容差不是由"TMR"三个字决定的，而是由整个磁路几何共同决定的**。磁铁轴心和芯片中心错开后，芯片测到的不再是转轴中心处的理想磁场方向，而是偏移位置处的局部磁场方向。磁场分布足够均匀，偏一点未必产生严重误差；磁铁尺寸小、气隙不合理或磁化不均匀，0.2 mm 也可能已经让误差明显增大。

所以，真正应该写进图纸的不是一句"偏心不得超过 0.2 mm"，而是：

在指定磁铁、指定气隙和指定温度范围下，经过最坏公差组合后，系统角度误差不得超过多少度。

0.2 mm 是机械尺寸，最终要验收的是角度误差。

### 06霍尔也不对偏心免疫

三霍尔为什么看起来没有那么怕偏心？不是因为霍尔原理天然免疫机械错位，而是因为六步换相对位置信息的要求更低。对三颗开关型霍尔来说，只要磁场还能可靠越过开关阈值，六个换相沿没有偏移到不可接受的程度，电机就能正常换相。同样的偏心可能使霍尔换相点偏移几度，却未必让电机停止转动。

但对于连续角度反馈，这几度误差会直接进入电角度：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVYOboMQic5abcStkrADqGiaLENsRItFKEic7r88SicLnUT6A9iczn5VAiauH8ic3SLHqwDl6rxdSMNhBiabDGSac9MJf96dbjfukFiajOk/640?wx_fmt=png&from=appmsg)

假设电机有 7 对极，机械角度误差 0.5°，对应的电角度误差就是：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVZdjJPkG0xibojQficKqDpXFaBY9ibEiaqY934nHQAjmvjznI0gVtIckN5aDbdaaZuDZGdmcGqgOJca0DxUqbSJibeAB0mGY3sJVnM/640?wx_fmt=png&from=appmsg)

这个误差进入 Park 变换后，会使原本应该落在 q 轴上的电流投影到 d 轴，带来额外损耗、转矩下降和转矩纹波。

所以不是"TMR 比霍尔娇贵"，而是连续角度反馈承诺了更多信息，系统自然要为这些信息的准确性支付更严格的磁路和装配代价。

### 07一圈校准能救静态偏心，救不了会变化的偏心

面对 sin/cos 畸变，最常见的第一步是做 Offset 和 Gain 校准。电机慢速、稳定地旋转一圈，分别记录两路信号的最大值和最小值：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVpFicMMK6KUdtM1T1YLQiaWiaFsb0RmgS3ZESGiaMyvQ4L6tnia7pjH79xicONMqIApNQ6phvdQu89DViajicJPicsJvPPJuUibHWrMAAf4/640?wx_fmt=png&from=appmsg)

余弦通道同理，随后归一化。如果两路不严格正交，还要进一步估计相位误差 Φ。这套方法可以把偏移的圆拉回原点，把椭圆拉回接近圆形，并修正一部分稳定的低阶畸变。

如果机械偏心造成的误差在每一圈都稳定重复，还可以记录角度误差曲线，通过谐波模型或查找表继续补偿。TDK 的数字 TMR 产品也明确提供 Static Compensation，用于处理磁铁和传感器机械错位产生的角度误差。

因此，"校准救不了机械偏心"并不准确。更准确的边界是：

校准能处理稳定、可观测、可重复的机械误差，却很难彻底处理运行中不断变化的机械误差。

如果轴承游隙使磁铁中心随载荷摆动，塑料支架在高低温下发生不同方向的变形，或者转子在高速下出现动态跳动，那么出厂校准记录的是状态 A，实际运行时面对的却可能是状态 B。此时问题不在于校准算法够不够复杂，而在于被校准的对象已经变了。这才是 TMR 角度系统量产时真正麻烦的地方。

### 08油泵电机究竟该选什么？

回到开头那颗汽车油泵电机。我没有直接给朋友推荐"最好的霍尔"，而是让他先回答三个问题。

第一问：你究竟采用什么控制方式？

六步方波换相 → 三颗霍尔开关通常够用；带位置传感器的 FOC → 需要连续电角度（TMR、连续角度 Hall、AMR、旋变、编码器均可）；无感 FOC → 走反电势/磁链观测器/高频注入，是另一条技术路线。

第二问：你需要的是机械角度，还是电角度？

轴端二极磁铁配合 TMR 得到的通常是机械角度，乘以极对数再叠加零位偏置才是电角度。极对数多时，机械端很小的角度误差也会被放大，磁铁定位、芯片定位和电角度零位标定必须放在同一条误差链中讨论。

第三问：机械误差是否稳定重复？

真正需要关注的不是机构能不能机械对中到一个孤立的数字，而是剩余误差能不能被稳定地测出来、记下来，并在温度、振动和寿命周期中继续成立。一个静态偏心 0.3 mm 但每圈高度重复的系统，可能可以通过 LUT 做得很准；另一个室温时只有 0.1 mm 但高温和载荷下不断漂移的系统，反而更难补偿。

到了这里，传感器选型已经不再是比较两张 datasheet。它是在比较**两套系统的误差预算**。

### 09TMR 真正赢的，不是把霍尔换成高级材料

TMR 的大磁阻变化率带来了更高输出、更好的信噪比和较低的温度漂移。但这并不意味着把三颗霍尔拆掉、换上一颗 TMR，电机就会自动获得高精度角度。

三霍尔系统只承诺六个换相区间。TMR 连续角度系统承诺一整圈的磁场方向。后者提供的信息更多，也会把过去隐藏在"还能正常换相"背后的所有问题全部暴露出来：磁铁是否均匀、气隙是否合理、轴端是否偏心、零位是否准确、误差是否随温度和振动变化。

"给我找最好的霍尔开关"暴露出的，不是客户不懂哪家器件性能更好，而是他还没有决定：控制器究竟需要知道转子在第几格，还是在第几度。

一格与一度之间，隔着的不是一种更高级的磁性材料。

隔着的是整个位置反馈系统。

◆ ◆ ◆

如是有为 · 编码器芯片研发工程师手记

![](https://mmbiz.qpic.cn/mmbiz_jpg/DBrlpXS1RIXFSZIXcp9SHNjpKwz68oj9eVLoY8W0un85VHRrh6ZDiaZFv9gds8TCwHcDwawNnJwfG7IlOwQKPYeMPFD6UvNdnXBia5sT0icCNQ/640?wx_fmt=jpeg&from=appmsg)

图：轴端磁铁旋转，TMR 芯片输出随磁场方向变化的 sin/cos 信号
