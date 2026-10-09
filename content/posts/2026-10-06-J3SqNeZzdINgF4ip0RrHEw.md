---
title: "iC‑PZ2656：22 bit 输出、18 bit 精度、±70 µm 光学基准，这三组数字到底在说什么"
date: 2026-10-06T12:55:00+08:00
slug: "J3SqNeZzdINgF4ip0RrHEw"
description: "光学编码器里最容易让人误判的，不是某个公式，而是把不同层级的数字放在同一张表里比较。"
original: "https://mp.weixin.qq.com/s/J3SqNeZzdINgF4ip0RrHEw"
companies: ["ST"]
tags: ["非线性校准", "AI"]
---

![](/images/wx/874657b6306f598b23bef685bea2ed69.webp)

光学编码器里最容易让人误判的，不是某个公式，而是把不同层级的数字放在同一张表里比较。

iC‑PZ2656 同时写着： 22 bit、 18 bit、 ±70 µm。

三个数字都对，但它们根本不是在回答同一个问题。

iC‑Haus 的 **iC‑PZ2656** 很适合把这个问题拆清楚。配合 26 mm 的 PZ03S 码盘时，公开资料给出 **256 CPR + 14 bit 插值**，最终形成 **22 bit 单圈位置**；同一套资料又给出 **Absolute Sensor Accuracy = ±1 LSB at 18 bits**；封装图里还写了 sensor pattern 相对 backside pad 中心的 **±70 µm / ±1°** 公差。

|

22 bit

输出分辨率

 |

18 bit

绝对精度口径

 |

±70 µm

光学基准公差

 |

01 / RESOLUTION

### 22 bit，不是一条 22 bit 的码道

看到“22 bit absolute encoder”，最容易产生的误解，是以为码盘上真的存在 **222** 个彼此独立的绝对位置。

iC‑PZ2656 不是这个结构。

256 CPR × 214 = 222

256 CPR 本身就是 8 bit，因为：

28 = 256

一圈 256 个原生周期，每个周期覆盖：

360° / 256 = 1.40625°

低 14 bit 则来自对一个原生周期内部相位的进一步插值。于是 22 bit 的本质，不是“码盘刻了四百多万个绝对格子”，而是：

粗绝对位置 + 周期波形相位插值 = 22 bit

这也解释了为什么后面会出现 offset、gain、phase、track alignment、eccentricity 这么多校准项：**14 个低位是从模拟波形里插出来的。**

02 / TWO POSITION DOMAINS

### 它实际上同时在读两套位置

第一套是 **PRC track**，负责粗绝对位置；第二套是 **incremental track**，产生周期性的精细相位。

|

PRC

回答“我大概在哪一段”

 |

Incremental

回答“我在这一段里走到哪”

 |

两套位置最终必须无缝拼起来。拼错一个原生周期，错误就不是 0.31 arcsec，而是接近 **1.40625°**。

所以 iC‑PZ2656 才会专门提供 **AI_PHASE、AI_SCALE** 这一层 digital adjustment。它修的不是普通的 SIN/COS 椭圆，而是 **PRC 与 incremental track 的空间对齐关系**。

一个很关键的细节：调整 AI_PHASE / AI_SCALE 后，原来的 ST_OFF、MT_OFF、ABZ_OFF、UVW_OFF 以及偏心相关参数都可能需要重新确认。说明这些参数并不是平行关系，而是有明确校准层级。

03 / RESOLUTION ≠ ACCURACY

### 22 bit 的一个 LSB 很小，但系统误差并不会跟着变小

Δθ22 = 360° / 222
≈ 0.00008583°
≈ 0.309 arcsec

可是 interpolator 的电气特性里，在 ideal waveform 条件下，Absolute Angle Accuracy / INL 给到的是 **0.5°e**。注意单位是电角度，不是机械角度。

0.5°e / 256 = 0.001953°m
0.001953° × 3600 ≈ 7.03 arcsec
7.03 / 0.309 ≈ 22.8

也就是说，仅看这一项特定条件下的 interpolator INL，它对应的量级就已经是 **二十多个 22-bit LSB**。

这不能直接和 factsheet 里的 18 bit accuracy 硬拼，因为测试定义与条件并不完全相同。但两者共同指向一个非常清楚的结论：

22 bit 是输出分辨率。
它从来不是 22 bit 绝对准确度。

04 / ±70 µm

### ±70 µm 到底有多大？先换算成一个原生光学周期

偏心校准章节给出了 26 mm 系统的一个关键几何参数：

ropt,AB = 10700 µm

也就是 AB 光学轨道的有效半径约 **10.7 mm**。如果把 70 µm 简化为沿切向的整体位移，对应几何角度约：

Δθ ≈ 70 / 10700
≈ 0.00654 rad
≈ 0.375°

这当然**不是**“iC‑PZ2656 误差 0.375°”。这种整体切向偏移首先更接近零位变化，可以通过 preset / ST_OFF 重新定义。

真正有意思的是把它换算成**一个原生光学周期的空间长度**。

p = 2π × 10.7 mm / 256
≈ 262.6 µm

70 / 262.6 ≈ 0.267
0.267 × 360° ≈ 96°e

也就是说，**±70 µm 已经接近一个原生光学周期的四分之一**。对 256 CPR 的相位系统，这绝对不是一个可以随便忽略的封装小数字。

05 / ANALOG CALIBRATION

### 第一层校准：先把四路光电信号修成人样

iC‑PZ2656 不是简单地输入一对 SIN / COS。框图里可以看到四路光电信号：**DPCOS、DNCOS、DPSIN、DNSIN**，先形成差分 COS / SIN，再进入后面的相位计算。

C = AC cos θ + OC
S = AS sin(θ + φ) + OS

于是三类最基本的一阶错误就出来了：offset 把圆心推出原点；gain mismatch 把圆拉成椭圆；phase error 让本该正交的两轴发生倾斜。

| **COS_OFF / SIN_OFF** 修正两路 DC offset |
| **SC_GAIN** 修正两路幅值失配 |
| **SC_PHASE** 修正正交相位误差 |

这一层没修好，14 bit 插值器不会“智能地把它修正”，只会把一个已经偏心、已经拉伸、已经倾斜的椭圆**插得特别细**。

06 / CALIBRATION SPEED

### 连校准转速都写出来了：这已经开始影响产线

AUTO_ADJ_ANA 不是静止按一下按钮。对于 26 mm 的典型系统，默认设置下，模拟自动校准最低速度约 **75 rpm**；手册给出的示例是在 **450 rpm** 下约 **2.0 s** 完成。

第一次模拟自动校准结束后，插值滤波配置还要进入另一个状态：IPO_FILT1 从启动阶段使用的 **0x6E** 改成 **0xEA**，IPO_FILT2 保持 **0x4**。

这已经直接影响量产 fixture：要有驱动电机、要控制速度、要覆盖足够相位、要留出校准时间、还要考虑 EEPROM / 参数保存流程。

07 / DIGITAL ALIGNMENT

### 第二层校准：把 PRC 和增量码道真正对齐

模拟波形修好了，PRC 与 incremental track 仍然可能存在空间 misalignment。所以还有 **AUTO_ADJ_DIG**，对应 **AI_PHASE** 与 **AI_SCALE**。

对 26 mm 系统，默认参数下数字自动校准最低约 **90 rpm**；450 rpm 的例子约 **2.67 s**。已经校准过的系统还可以用 AUTO_READJ_DIG 去修较小的后续变化。

零位偏移和“粗细码道拼接错误”不是同一种问题。前者可以重新定义 mechanical zero；后者如果不修，直接会出现在 coarse / fine 的拼接边界。

08 / ECCENTRICITY

### 第三层校准：偏心只抓最主要的一阶正弦项

iC‑PZ2656 对码盘偏心并没有做一张巨大 LUT，而是抓一圈一次的主要成分，用 **ECC_AMP** 与 **ECC_PHASE** 表达。

e(θ) = Ae sin(θ + φe)

这正好对应圆盘偏心最主要的一阶几何结果。但它也意味着：码盘刻线误差、局部污染、高次谐波、轴承周期误差、玻璃应力或复杂结构变形，不可能全靠 ECC_AMP / ECC_PHASE 两个参数解决。

这项校准对运动状态还更敏感：最低速度约 **30 rpm**；默认参数下，手册示例为 **900 rpm、约 17 s**，并特别强调 **constant speed and steady state**。

原因很直接：芯片要从整圈数据里找一个低频正弦位置误差。如果真实电机速度本身就在周期性变化，速度纹波就可能混进偏心估计里。

09 / MAX SPEED

### 56250 rpm 为什么这么怪？因为它正好对应 240 kHz

iC‑PZ2656 + PZ03S 给出的最大转速是 **56250 rpm**。这个数字不圆，但乘上原生 256 CPR 就很漂亮：

56250 / 60 × 256
= 240000 Hz
= 240 kHz

再回头看 interpolator / ABZ 相关电气条件，就能看到 **fsin ≤ 240 kHz** 这一边界。

256 CPR → 正余弦频率 → 240 kHz → 插值器边界 → 56250 rpm

10 / WHAT ±70 µm REALLY MEANS

### ±70 µm 真正暴露的，不是“精度差”

iC‑PZ2656 的产品架构从一开始就在承认误差存在。

| **sensor pattern ↔ package** 制造与基准公差 |
| **SIN / COS** offset、gain、phase |
| **PRC ↔ Incremental** 粗细码道对齐 |
| **Disc eccentricity** 一阶偏心补偿 |
| **Mechanical zero** 最后单独定义零位 |

所以这三个数字没有互相打脸。

**22 bit** 是数字表示能力；
**18 bit** 是绝对测量能力的一个规格口径；
**±70 µm** 是封装机械基准到真实光学结构之间的制造基准公差。

真正的编码器设计，就是把这三个世界接在一起。

公开资料

iC‑Haus iC‑PZ Series Datasheet / Factsheet：iC‑PZ2656 的 256 CPR、22 bit、PRC + incremental 架构、插值器、自动校准、偏心补偿、最大转速及 sensor pattern 公差等。

文中的 70 µm → 0.375°、70 µm → 96°e 等为基于公开几何参数的量级换算，用于解释层级关系，不代表 iC‑PZ2656 最终角度误差。
