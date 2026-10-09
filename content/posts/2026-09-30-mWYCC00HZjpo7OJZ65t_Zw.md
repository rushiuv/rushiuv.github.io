---
title: "做光学编码器才知道： PD 和 CMOS，在中国"
date: 2026-09-30T15:41:00+08:00
slug: "mWYCC00HZjpo7OJZ65t_Zw"
description: "最近研究光学编码器芯片，听到一句黑话差点笑出声：“这到底是 CMOS 还是 PD？”"
original: "https://mp.weixin.qq.com/s/mWYCC00HZjpo7OJZ65t_Zw"
tags: ["光电编码器"]
---

最近研究光学编码器芯片，听到一句黑话差点笑出声：“这到底是 CMOS 还是 PD？”

PD 是感光二极管，CMOS 是一套工艺。更要命的是，CMOS 像素里本来就包着 PD。这就像问一辆车“到底是四缸还是汽油车”。

但工程现场有意思就在这儿。大家嘴里的“PD”，其实是指 PD + 跨阻放大器 + 缓冲器 这条连续模拟读出路线。光一变，前端信号跟着变。

而大家说的“CMOS”，实际是指 CMOS 有源像素。它把感光、积分、寻址全塞进像素，能保留更丰富的空间信息。

千万别觉得 CMOS 就高级。有人一听“阵列”“数字”就自带优越感，纯属想多了。CMOS 有复位噪声，PD 也有暗电流散粒噪声。问题没消失，只是换了一拨找上门。

所以别被名字唬住。最后还得看那几个不性感的问题：噪声多少？带宽多少？温漂多少？

![](/images/wx/b626cec8752b1a2419ed30d917c38d58.jpg)

![](/images/wx/e45069520cb5db207a2024b45d9e0cf2.webp)

![](/images/wx/31186b649812cd54c2c70cadcf33c103.webp)

![](/images/wx/5bf4fb88288e09917ca826f5b7007c04.webp)
