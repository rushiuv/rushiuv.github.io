---
title: "我在德国听 iC-Haus 讲掉电多圈编码器：真"
date: 2026-09-30T09:12:00+08:00
slug: "5O4b75NhJjgISc7SRyrbxA"
description: "德国 Jena 的 MagSense 2026 会场，我听完 iC-Haus 的报告，脑子里一直甩不掉一个数字：140 nJ。"
original: "https://mp.weixin.qq.com/s/5O4b75NhJjgISc7SRyrbxA"
companies: ["iC-Haus"]
tags: ["多圈编码器"]
---

德国 Jena 的 MagSense 2026 会场，我听完 iC-Haus 的报告，脑子里一直甩不掉一个数字：140 nJ。

机器彻底断电后，轴要是被人转了，编码器得记住到底在第几圈。行业里常见的是机械齿轮和后备电池，他们走第三条路——靠轴自己动来发电。

但这点电根本不够维持芯片活着。一次脉冲的典型能量才 140 纳焦耳，连 ADC 和接口都拉不起来。它只能像张一次性车票：轴动一下，芯片醒过来，记个 +1 或 -1，马上接着睡。

真正难搞的不是高速，而是断电后轴在边界附近来回抖。往前一点、退回来，再往前一点。这点能量够不够它判断方向、确认是真动作，再把状态安全写进去？

下一代 PME 如果把这些全吞进一颗 SoC，机器人关节这种怕电池又没空间的地方，估计会爱死它。

![](/images/wx/af66972cda0bd87fd9e51bb4522885da.webp)

![](/images/wx/9c7ffbe6ea31889adeccc827a747667e.webp)

![](/images/wx/f2e3dc862b77abe6e8d8f30f1925b2c8.webp)

![](/images/wx/6d7d9311d5c7a700f8c3232b11248788.webp)

![](/images/wx/985c4117daef0064cbf5c3757049f54d.webp)

![](/images/wx/57d64c301de7dedd18b5c3b70a4397b2.webp)
