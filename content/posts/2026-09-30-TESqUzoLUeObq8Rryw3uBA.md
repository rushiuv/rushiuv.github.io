---
title: "做光学编码器才知道： PD 和 CMOS，在中国居然是这么分的"
date: 2026-09-30T09:10:00+08:00
slug: "TESqUzoLUeObq8Rryw3uBA"
description: "OPTICAL ENCODER · SENSOR FRONT-END"
original: "https://mp.weixin.qq.com/s/TESqUzoLUeObq8Rryw3uBA"
companies: ["昆泰芯"]
tags: ["光电编码器"]
---

![](/images/wx/c24e4db208f64800b87afd5e196bd3d9.webp)

OPTICAL ENCODER · SENSOR FRONT-END

## 做光学编码器才知道：
PD 和 CMOS，居然是这么分的

最近看到昆泰芯发布 KTO9348 光学编码器，我又顺着这个东西往光编芯片里面钻了一层。

上一篇我写了光学编码器里的“光敏单元”。一个看起来不起眼的感光区域，宽一点、窄一点、偏一点，最后居然都可能跑到正余弦信号的 3 次、5 次谐波里去。

本来以为已经够折腾了。结果继续往里面看，我又碰到一句让我第一反应有点嫌弃的话：

“这个到底是 CMOS，还是 PD？”

我心想：这又是什么中国工程师黑话？PD 是 Photodiode；CMOS 是一套器件和工艺体系。更要命的是，所谓 CMOS Pixel 里面本来就有 PD。

这就像一本正经地问：**“你这辆车到底是四缸，还是汽油车？”**

但工程现场最有意思的地方就在这里：有些话从教科书上看像胡说八道，工程师之间却偏偏都知道对方在说什么。按我接触到的 KTO 系列方案，它走的是 **PD → 跨阻级（TIA）→ Buffer** 这条连续模拟读出路线；而另外一些人口中的“CMOS”，实际是在说 **CMOS Active Pixel** 一类结构。

### 01 先看 PD + TIA + Buffer：看着直接，真正做好一点也不简单

PD 接收经过码盘调制后的光，先产生光电流。一定工作区间内，可以近似写成：

Iph = RλPopt

这里最容易被一句“PD 后面接个 Buffer”掩盖掉的是：**PD 首先给的是光电流，而不是一个现成的电压。**因此前面通常先要有跨阻级完成 I/V 转换，再由 Buffer 隔离并驱动后级。PD 本身还有结电容，感光节点也存在寄生电容，所以跨阻级的带宽、稳定性和噪声都会直接进入角度链路。

![](/images/wx/c42106f812063cb93ad33f419f6ddeee.webp)

所以从系统视角看，这条链路非常直白：**光 → PD → TIA（I/V）→ Buffer → 后级模拟处理。**它很符合模拟工程师的直觉：光在变，前端信号跟着变。

#### PD 做大一点，不就更好吗？

光不够，最朴素的想法就是把 PD 做大。面积上去，接收到的光更多；但与此同时：

CPD ↑

也跟着来了。于是速度、节点带宽、噪声和寄生效应一起找上门。这也是上一篇讨论“光敏单元宽度”为什么不能只从几何光学看：一个尺寸同时牵着光学积分、谐波、光电流、结电容、带宽和噪声。

**光编真正麻烦的地方：**光学、器件、模拟电路和算法，根本没法真正切开。

### 02 再看 CMOS Pixel：拆开以后，里面还是 PD

所谓 CMOS Pixel 最容易让人误会的地方就在这里：把它拆开，PD 还在。真正多出来的是围绕 PD 的有源读出结构。

经典 3T Active Pixel 可以抽象成：**PD + Reset + Source Follower + Select**。

![](/images/wx/039b993554be5bcd204a0e1018e1250c.webp)

#### Reset：先把 Pixel “清零”

Reset 先把 Pixel node 拉到已知状态，然后关掉。此后 PD 在一段时间内积累光生电荷：

Qph = IphTint

ΔVpix ≈ IphTint / Cpix

这两条式子一出来，两种架构的味道马上不一样了。PD + TIA + Buffer 更接近“**现在的光是什么样**”；CMOS Pixel 天然带着 **Reset → Integration → Readout**，更像“**这一段时间一共收到了多少光**”。时间正式进入了测量链。

#### Source Follower：别碰我的 Pixel Node

Pixel node 很娇气。Source Follower 做的核心事情就是阻抗变换和隔离：前面的节点负责保存信号，后面的 column bus 不要直接伸手进去乱摸。当然它自己也会带来 offset、1/f noise、gain variation——工程从来都是解决一个问题，再顺手领两个问题回家。

#### Select：现在轮到谁讲话

SEL 打开，这个 Pixel 接入 column bus；SEL 关闭，下一个来。于是大量 Pixel 可以组织成阵列：

P0, P1, P2, … , PN−1

这才是 CMOS Pixel 真正有意思的地方。不是“CMOS 比 PD 高级”，而是它把**感光、积分、缓冲、寻址**组织进了 Pixel，于是可以保留更丰富的空间采样信息。

### 03 千万别再说“CMOS 肯定比 PD 高级”

看到 CMOS、Array、Digital 几个词，有些人马上产生一种莫名其妙的技术优越感：“那这个肯定更先进吧？”

**谁告诉你的？**

CMOS Pixel 有 reset noise、kT/C noise；PD 照样有 dark current、shot noise、responsivity mismatch；Source Follower 又带来 offset、1/f noise、gain mismatch；阵列再送你 PRNU、DSNU、column mismatch。

**问题没有消失。**只是换了一群问题。

所以判断一种光编架构，最后还是那几个一点都不性感的问题：噪声多少？带宽多少？温漂多少？面积多少？功耗多少？最终角度误差多少？量产以后还能剩多少？这些东西不会因为名字里多了一个 CMOS 就自动变好。

### 04 “CMOS 还是 PD”，到底是不是胡说？

从半导体器件分类来说，不严谨。CMOS Pixel 里面照样有 PD。

但放进光学编码器工程语境里，我现在已经能听懂这句黑话真正想问什么：

你是直接把 PD 感光节点的变化读出来，还是把 PD 做进一个可复位、可积分、可寻址的 Active Pixel，再组织成阵列读出来？

这么翻译以后，一下就合理了。

上一篇，我还在研究：**光到底落在哪里？**

这一篇继续往硅里面走：**光落下来以后，电路到底怎么接？**

而下一层更有意思。不管前面怎么接，光学编码器最后都不要光，不要电流，也不要电压。它只要一个东西：**角度。**

这些光电信号，到底怎么一步一步被榨成一个高分辨率绝对角度？
这个才开始进入光学编码器芯片真正有意思的地方。

本文讨论的是光学编码器中常见的工程架构叫法。电路图为概念级示意，用于说明信号链差异，不代表任何具体产品的晶体管级内部实现。
