---
title: 直线电机：测局部磁场，不等于知道全行程位置
description: 短行程磁体跟踪与光栅尺反馈各有边界，周期歧义、拼接和热膨胀需要单独预算。
date: '2026-10-18T10:00:00+08:00'
lastmod: '2026-10-24'
layout: application-single
application_entry: true
application_group: 工业与运动
weight: 208
related_basics:
- optical-encoder
- absolute-incremental
- latency
reference_topic: 直线电机
related_guides:
- thermal-cycle-reversibility
- parameter-conditions
- linear-scale-thermal
- reference-recovery
related_model_slugs:
- ktm5800
- resolute-rl
- smd-01b
---



直线电机需要知道动子相对导轨的位置，而不是某根轴转了几圈。磁场跟踪、磁尺和光栅尺都能进入位置反馈设计，但量程、周期与安装条件不同，不能用一个“高分辨率”把它们归为同一方案。

## 短行程磁体与长尺不是一个几何问题

TI TMAG5170可读取三轴磁场，原厂还给出多传感器线性位置参考设计。单个磁体从传感器旁经过时，磁分量随位置变化，可在已验证的局部区间估位；若两个位置产生近似相同的分量，就需要增加信息，而不是继续提高ADC位数。

Renishaw ATOM属于光学增量编码器系统，可配线性标尺。读头、标尺和接口构成完整路线，并非可直接替代TMAG5170的裸芯片。[昆泰芯KTM5800](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/absoluteangledivider/index.html)则处在读出链的另一层：它对外部传感器的差分正余弦信号进行细分，原厂列出光栅、磁栅等适配路线，不是单颗芯片直接测出长行程距离。

因此三者分别是局部磁场测量、完整光学尺系统与正余弦细分前端。比较前先核对传感头、标尺周期、输入幅值、周期累计和参考建立方式。采用KTM5800也不会自动消除磁尺周期歧义或提供掉电后的完整直线坐标；增量位置如何建立参考，仍须由整套系统解决。

## 一个周期内很细，整条尺仍有另一笔误差

假设标尺周期为40微米，每周期细分成400份，数字格距是0.1微米。这只是计算示例；不能据此宣布全行程精度为0.1微米。尺长误差、热膨胀、细分非线性、阿贝偏置和导轨姿态都可能进入工作点误差。

## 验证要回到实际测量线

检查读头与尺的间距、倾斜、污染和电缆，同时记录采样、控制和驱动更新时序。长行程或多传感器拼接要验证跨区连续性、反向、掉电恢复及缺码表现；不能只展示一段平滑曲线。位置尺离加工点越远，结构转角造成的位移差越需要单独计算。换路线时先核对坐标与参考方式，再比较分辨率。

## 原厂资料

- [TI TMAG5170及线性位置参考设计入口](https://www.ti.com/product/TMAG5170)
- [Renishaw ATOM光学增量系统](https://www.renishaw.com/en/atom-optical-incremental-encoder-series--37564)


## 热起来后位置偏了，尺和基座要一起量

[Renishaw热安装白皮书](https://www.renishaw.com/en/white-paper-mounting-encoder-scales-for-optimum-thermal-performance--44316)说明，标尺材料与固定方式共同影响热行为。先读[光学编码器](/wiki/basics/optical-encoder/)与[安装关系](/wiki/basics/mounting/)，不要把单周期细分能力当成长行程热稳定性。

自设均匀自由膨胀的0.5m尺，热膨胀系数10µm/(m·°C)，升温10°C，长度变化为50µm；这不是ATOM系统的精度规格，约束安装后也不能照搬该值。测量时同时记录尺、基座和工作点温度，保留独立位移参考；若回到同温仍有残余，按[温度循环回测](/topics/guides/thermal-cycle-reversibility/)排查装配和基准，而非直接增加温补点。比较不同尺之前，用[参数条件核对](/topics/guides/parameter-conditions/)确认基准温度、安装状态及允许误差。
