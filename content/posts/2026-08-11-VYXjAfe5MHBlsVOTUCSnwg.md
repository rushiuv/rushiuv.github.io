---
title: "激光打标机金属上飞快写字？振镜只摆 ±10°，昆泰芯哪颗编码器最合适？"
date: 2026-08-11T00:00:00+08:00
slug: "VYXjAfe5MHBlsVOTUCSnwg"
description: "ENGINEER'S NOTE · 编码器一线手记"
original: "https://mp.weixin.qq.com/s/VYXjAfe5MHBlsVOTUCSnwg"
---

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXh7fy3icwHCwPpER0n9GGu6J2d23gjQ9saMqPoUwSabbRohft6yMSFzhQwYyw3iajXm9bxohr6BPIelhEY0c0v93WoTblNQQmmw/640?wx_fmt=png&from=appmsg)

ENGINEER'S NOTE · 编码器一线手记

## 振镜只摆 ±10°，昆泰芯哪颗编码器最合适？

读完一篇振镜伺服文章，[北四环德彪 ](https://mp.weixin.qq.com/s?__biz=MzAxOTc1MDE2Ng==&mid=2650274144&idx=1&sn=17aacffdc4dd5f9e9820cf9997d7b53c&scene=21＃wechat_redirect)写的, 我没有先盯 PID、陷波和前馈，反而盯住了最不起眼的那只“眼睛”：**位置传感器。**

我最后最想先试的，不是参数最“豪华”的 KTM5900，而是 KTM5200。真正决定振镜位置反馈的，不是 bit 数本身，而是小角度有效信息、带内噪声、群延迟、温漂，以及一个磁方案特有的问题：**电机漏磁会不会制造“假角度”。**

### 01｜先用大白话说：振镜到底是什么？

激光打标机为什么能在金属上飞快写字？很多时候，并不是整个激光头在横着跑。真正高速运动的，往往只是里面的两块小镜子。

一块镜子负责 X，一块负责 Y。控制器让两块镜子按照一串角度指令高速摆动，激光点就在工件上“画”出文字、二维码和轮廓。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXAI6uVBNMFOwC8A8TE8Svr1fdJ0J1AmYE031Ff9ejr9GEHdrRiaxTibbIl8AW3yK4FB9Co9FhOv4nexsKpnXVgQdc7PYJYqn3C4/640?wx_fmt=png&from=appmsg)

所以振镜电机可以粗暴理解成：**一台专门负责让小镜子在很小角度内疯狂摆动的伺服电机。**

它不需要连续转圈。镜片机械上可能只摆十几度，但要求极快、极准、停下来不能抖。镜子慢一点，拐角会圆；多冲一点，线条会鼓；X/Y 两轴动态差一点，圆就可能变成椭圆。

### 02｜振镜和普通编码器，产品逻辑根本不同

普通伺服编码器最自然的任务是把整圈 360° 都测准。振镜却恰恰相反：它根本不在乎整圈，只想把中心附近这一小段测得极快、极安静、极稳定。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUbXkpaqVkdpKibIncYicCTeO7WORuqKAWIkSwzGMyBse7gzictcpibEx6ibtFMCOntpYIz9W6nQH4ER7LrYwUH5zTbdIUlj37ftbSQ/640?wx_fmt=png&from=appmsg)

反射镜还有一个很关键的光学关系：**光束偏转角约是镜片机械转角的 2 倍。**因此看起来很大的光学扫描范围，落到轴上，机械角度其实并没有那么大。

### 03｜第一个误区：21 bit，不等于 21 bit 有效信息

以 KTM5200 的 21 bit 绝对角输出为例。如果把它理解为覆盖完整 360°，一个数字 LSB 的角度尺度约为：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIVv7ibfKnbLE8zfKMDmHGgzSiaVwhuNKlNiaicHABic2ed2y1fCAZGEBYibmMJAOz70dZHGXKAMrQaKfP2FccgfYExmLEiciagu9PMgWqo/640?wx_fmt=png&from=appmsg)

看起来已经很细。但如果振镜机械上只使用约 20° 的工作区间，那么真正落在这段范围里的有效码数，只是整圈的一小部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIX3DOtWQXwpPrjgoX4qHRibcXmsm4qIbqKSvT5yJMngfCzESDichOeAfMz0icvQHKzermCXFB13TEGIVwdIjqklNkFF2Gic2Sn1m08/640?wx_fmt=png&from=appmsg)

数字上当然可以重新缩放成 21 bit，但**缩放不会凭空增加物理信息。**这就是为什么把一个为 360° 设计的编码器塞到只摆 ±10° 的振镜上，bit 数很容易产生错觉。

### 04｜第二个误区：真正可怕的不是 INL，而是噪声

KTM5200 公开噪声指标约 0.005°。换成角度尺度：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXQbHghQOhOmuMznMgxoOojicCSWOfIKnjyN4zABzywthmxH2KpJBUXLic21sXia4xLBoWwf1tUvUotRe8KOxwZ421g1fLB0som28/640?wx_fmt=png&from=appmsg)

这个数字比一个 21 bit LSB 大很多。于是立刻出现一个振镜选型里最容易踩的坑：

21 bit output ≠ 21 bit useful information

更麻烦的是，振镜位置环会真的“追”传感器噪声。反馈角度跳一下，控制器并不知道那是噪声，它只会认为镜片位置错了，于是输出电流去纠正。最终，寄存器里的噪声可能被变成真实的镜片抖动。

相比之下，稳定、可重复的静态 INL 反而更容易处理。因为它可以通过 LUT、多项式或整机场校正修掉。**能标定的偏差，通常没有随机噪声那么可怕。**

振镜位置反馈的指标优先级，我会这样看

Noise ＞ Latency / Bandwidth ＞ Drift ＞ Repeatability ＞ Static INL

### 05｜四颗芯片放在一起，我为什么先试 KTM5200

这里不能简单按“谁 bit 多谁赢”排序。更合理的是看它们分别解决什么问题。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWvJXibZw2HbyrrHUbEyZs3Bic2m4nNcwcybnrxU2bnX9mdlRaS6B4uBn0RCO4zFicesF4IfomrWTwpxibnU2YTicFSiaNKzRJOaibXicI/640?wx_fmt=png&from=appmsg)

#### KTH78：够快，但不是我冲高端振镜的第一选择

KTH78 的优势是响应快、刷新率高。但振镜最容易把“刷新率”和“测量带宽”混为一谈：每秒更新一百万次，不代表传感器真的能把一百万赫兹的机械信息准确测出来。真正要看的是有效带宽、群延迟和对应滤波档位下的噪声。

#### KTM5200：最值得先做 feasibility

KTM5200 是 AMR、在轴使用思路清晰，公开角度输出延迟在几微秒量级，而且 AMR 本身具有 180° 周期特征。理想情况下两桥信号可写成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWJo4ERPibQXs7VedvG5icmMVcAb7YMCGH5qlByuw2iaP2xQ5Zd0KRBPBcFbjKoVkGLAkbCw6Hn2SAkicEmDcKnCQ4TkiczDzibAXkro/640?wx_fmt=png&from=appmsg)

这里的 **2θ** 对振镜非常有意思。普通 360° 编码器会嫌 180° ambiguity 麻烦，但振镜只在中心附近摆动，这个问题反而可能根本不存在。更重要的是：机械角变化 1°，原始 AMR 相位变化 2°，天然有一次角度放大。

在中心小角度附近：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVdpdOpjPYJTBCxB4zUjnyaSTAtPO6iaW8iaJpca9N6w9iapqGFBjaRP2TemXgYpMxO2AGKUtdXcydPOsDt0wtT5uJQSM9jswTKy4/640?wx_fmt=png&from=appmsg)

这意味着，如果真为振镜重做专用位置传感器，完全没必要照搬一颗 360° 编码器的完整架构。可以把资源集中到 ±十几度的小范围、低噪声 AFE、高速 ADC 和极低延迟输出上。

#### KTM5300：机械布置更灵活，但第一版反而变量更多

离轴测量能让紧凑结构更好布置，但也会把偏心、磁场梯度、Z 向距离和离轴算法一起带进来。第一轮验证时，我反而更愿意让问题简单一点：先证明磁测角在振镜上能不能活下来，再谈更复杂的机械集成。

#### KTM5900：我最想摸它的动态性能上限

KTM5900 真正吸引我的，不是“24 bit”三个字，而是它背后的高速 sin/cos 信号链：TMR 前端、双高速 SAR ADC、高速数字处理和高速角度输出。这套架构更接近高性能数字振镜需要的动态平台。所以如果 KTM5200 负责回答“这条物理路线能不能做”，KTM5900 更适合回答“动态上限能到哪里”。

### 06｜真正最大的雷：振镜自己就是一台磁电机

这是磁编码器进入振镜最容易被忽略的一关。传感器旁边不是一个安静环境，而是一台高动态力矩电机。传感器看到的总磁场可以粗略写成：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWdRrUubomwKWeEhdehoHicogzg7DV2v7KshkutPqoUJzpLpoX4DkmA3VdXoHUJTkwicGfchuS8A73QMCjlPjg7Bhjx9e9obib35g/640?wx_fmt=png&from=appmsg)

最麻烦的是最后一项。它随着伺服电流变化。振镜大幅跳转时，电流可能快速从 +Imax 翻到 −Imax；如果这股漏磁改变了传感器所看到的磁场方向，芯片可能会认为“轴动了”，其实轴根本没动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXOKqKPLwl1ewKhnTsUjqeLznNNKzamW9aSVgzGcooLC0mgGc1c7THbGPspooKCEtrgJXfjjiciaKWhwDoD1ZstRhzUy2HCob2Iw/640?wx_fmt=png&from=appmsg)

所以一颗磁传感器适不适合振镜，我甚至想新增一个普通编码器 datasheet 很少写的指标：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWsoqyBultOF0MibtIXxlXkKPDnzia7a9fude9wwm2VjGfKA6bRzECaValHmcBJ93OnP8qJ8XP9cOR4Zuz1qEPanKWWHU380lkzY/640?wx_fmt=png&from=appmsg)

也就是：电机电流变化 1 A，到底会制造多少 μrad 的假角度。

### 07｜如果现在给我一台振镜，我先做的不是“测精度”

我会先把轴机械锁死，确保真实角度不动，然后把线圈电流从 −Imax 扫到 +Imax，记录传感器角度是否跟着电流跑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIWYs0ZpXyCNXHeXH2Op9naAAJAQcvQaH1XqkiazBfm7J0ibMUk1ShYyJAlVwzH8qRaMyLK41j9BM5pGnWfyichyFD4BjPcuGKFTEY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIW2KyekJPeJPZ4uZfec8GdIFtbl4dvx3dST7QGCEpHAQLdaqdDAVibByhElqS6fyFkR37lD45JaeYMS81Em8fxV7lur4rueOOho/640?wx_fmt=png&from=appmsg)

第二张图，我会测最低延迟模式下的角度噪声功率谱：

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIX0qXcFh3FMjPxActt7p4ibqK3jpSnaLMFgQe5iburf4QTrc0icUnPFmgUuz3dYs3RLmWrQLrXRBQ0Qx9RcodibAVdUssfgz0icbEOY/640?wx_fmt=png&from=appmsg)

重点盯 0–5 kHz。振镜位置环真正会“吃进去”的，是这个频段里的噪声，不是一个脱离带宽定义的单独 noise 数字。

第三张图测温升过程里的零位漂移：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXw17bJibQVqcGhUS6MtQT2MD7xyTbrbm8icqKgrEU9je0A7JNGWibVvsZbUibt0G4fcCbKm53UCkECRksiaicYTiaq3pukyZxgLQOv9U/640?wx_fmt=png&from=appmsg)

这三张图如果漂亮，才有资格继续谈“昆泰芯能不能做振镜”。

THE REAL PRODUCT DEFINITION

真正适合振镜的，可能一颗都不是。

问题可能不是“KTM5200 和 KTM5900 谁更强”，而是：为什么一定要拿一颗为 360° 电机设计的编码器，去测一个只摆 ±10° 的镜子？

如果真往产品走，我更愿意重新定义一类器件：

GALVO POSITION SENSOR

高速小角度 AMR / TMR 振镜位置传感器

不追求多圈，不追求 360°。把芯片资源全部砸在 正负十几度：低噪声、低群延迟、低温漂、极小附加惯量，以及电机漏磁抑制。

所以，如果今天只允许我拿现成芯片去做第一轮 feasibility，我会先试 **KTM5200**；如果要摸高速数字链路的动态上限，我会认真看 **KTM5900**。

但最终真正值得做的，不是“把现有编码器换个应用场景”，而是一颗只为振镜而生的 Galvo Position Sensor。

注：文中型号参数基于公开资料做工程可行性讨论；振镜整机指标与单芯片指标并非同一统计口径，本文不把二者做简单一一等价比较。最终适配性仍需以锁轴扫电流、动态噪声 PSD、群延迟和温漂实测为准。
