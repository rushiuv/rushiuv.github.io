---
title: "EPFL 这次做了一颗接近 4 kV 的 GaN 晶体管"
date: 2026-09-16T15:37:00+08:00
slug: "iYCa5Fh3Qd_M1P3fQyZSLA"
description: "它最有意思的地方不是单纯把耐压做高。普通 GaN 器件关断以后，电荷不平衡，电压容易集中在局部，最后从那个地方先击穿。EPFL 这次利用 GaN 自身的极化，在电子层旁边又形成一层正电荷，让两边尽量配平，于是几千伏电压可以沿器件慢慢摊开，而…"
original: "https://mp.weixin.qq.com/s/iYCa5Fh3Qd_M1P3fQyZSLA"
companies: ["EPFL"]
tags: ["GaN"]
---

它最有意思的地方不是单纯把耐压做高。普通 GaN 器件关断以后，电荷不平衡，电压容易集中在局部，最后从那个地方先击穿。EPFL 这次利用 GaN 自身的极化，在电子层旁边又形成一层正电荷，让两边尽量配平，于是几千伏电压可以沿器件慢慢摊开，而不是全挤在一个点上。这个结构叫 intrinsic polarization superjunction，iPSJ，而且不用传统化学掺杂。现在常见商用 GaN 大约还是 600～650 V，这个结构已经做到五倍以上。

这种器件真往电机驱动里走，旁边有些芯片的日子其实会更难。

功率管耐压越来越高是一回事，开关沿越来越快又是另一回事。母线旁边一开一关，dv/dt、共模电流、地弹、线缆耦合一起出来。编码器就在电机屁股后面，模拟前端可能还在认真分辨那一点点 Hall、TMR 或光电信号，旁边已经是几百伏甚至上千伏的快速边沿。

所以以后看一个编码器，只看 16 bit、多少转、INL 多小，可能还不够。

示波器上真正难看的，往往是功率管一翻转，角度刚好跳了一下。

EPFL 这颗器件离编码器还很远，但如果高压 GaN 真继续往前走，编码器的 EMC 指标大概也不会原地等着。

![](/images/wx/aadc753532cb3c84175dc7d68f21052c.jpg)

![](/images/wx/a6b10b9a7f157a7377576fab4713e39e.jpg)

![](/images/wx/6236daa05d301fb2f415dd13682a8812.jpg)

![](/images/wx/35798cb8f7217d7c32af65d11ccdd43d.webp)

![](/images/wx/803240ca1dcf92bfa1a69ef061f2c44e.webp)
