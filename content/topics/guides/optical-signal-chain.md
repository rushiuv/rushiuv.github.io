---
title: 光电流变大，为什么反而读不准？
description: 从直流光电流占用摆幅入手，分清光学接收、跨阻放大、采样和细分的职责。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: R07
guide_group: 光学与电感
weight: 107
related_basics:
- optical-encoder
- inl
- angle-noise
related_model_slugs:
- pnh3348
- ic-pz
- ktm5800
- smd-01b
related_guides:
- channel-angle-harmonics
- optical-tolerance-evidence
- reflective-code-validation
keywords:
- 光学前端
- PD
- TIA
- 饱和
- 细分
aliases:
- /wiki/engineering/optical-signal-chain/
topic_method: true
editorial_image: images/editorial/chromeos-optical-20261024.webp
editorial_image_alt: 光学测量的场景示意
---




把LED电流调大，SIN/COS幅值先增加，随后波形变平、角度误差变大。此时继续加细分位数没有用：有效信息可能在到达ADC之前已经被削掉。

## 直流也占用放大器摆幅

光电检测到的信号可写成 \(I(u)=I_0+I_1\cos(2\pi u)\)，其中 \(u\) 是一个光栅周期内的归一化位移。理想跨阻级为：

\[
V(u)=V_b-R_f I(u)
\]

作一个完全设定的电路算例：偏置 \(V_b=2.5\) V，允许输出0.2～3.1 V，\(R_f=100\) kΩ，直流20 µA，交流峰值2 µA。输出是0.5 V附近的±0.2 V，范围0.3～0.7 V，仍在允许窗口。

若光照整体翻倍，直流40 µA、交流4 µA，理想输出中心变成−1.5 V。这已经越界。即使真实电路把电压限制在下电源附近，ADC仍能得到“很稳定”的数字，却不能恢复原来的正弦。

## 四级信号要分开看

| 环节 | 先检查什么 |
| --- | --- |
| 光学与PD | 直流、调制度、光斑覆盖和受光权重 |
| 跨阻放大 | 输出余量、负载、噪声、稳定性与建立时间 |
| ADC采样 | 共模、量程、通道时差及是否削顶 |
| 角度细分 | 幅相失配、周期内残差、无效输入处理 |

增大 \(R_f\) 同样会放大直流与交流，而且还会改变与输入电容有关的稳定性和带宽。上面的理想乘法只用于检查摆幅，不是跨阻电路完整设计公式。

## 哪一段先变坏，就在哪里找证据

固定机械位置和后端增益，分档改变光量，保存每级可访问节点的直流、交流峰值和波形。若跨阻输出已削平，就先恢复余量；若模拟波形完整而数字值贴边，再查ADC。不要只存最终角度，否则无法判断信息在哪一级丢失。

光照更强有时有利于信噪比，但直流处理、输入电容与输出余量必须同时允许。反射绝对码还要看亮暗对比，不能用光电流总和替代可判读能力。

具备直流消除或自动增益的前端可以扩大适用范围，但还要检查其可跟踪范围、启动过程和光量突变后的恢复时间。控制环把输出拉回中间电平，不等于此前的削顶样本已经有效；恢复期间的角度应按具体器件状态处理。

## 公开依据

- [TI SBOA324A：交流耦合跨阻放大电路](https://www.ti.com/lit/an/sboa324a/sboa324a.pdf)，展示直流处理、反馈与稳定性设计。
- [iC-Haus PNH公开功能摘要](https://www.ichauschina.com/PNH_factsheet_CN)，用于区分光学前端与后级位置处理。本文电流和摆幅均为设定算例。
