---
title: 恒速外推补得准，为什么加速时还会落后？
description: 用归一化角度的泰勒展开分开固定延迟、预测残差与真实滤波器动态。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D05
guide_group: 时间与动态
weight: 105
related_basics:
- latency
- resolution-accuracy
related_model_slugs:
- as5047p
- mlx90382
related_guides:
- spi-data-age
- sample-time-contract
keywords:
- 延迟补偿
- 加速度
- 动态验收
- 预测
aliases:
- /wiki/engineering/dynamic-latency-test/
topic_method: true
---


一条角度链在恒速测试中没有明显滞后，仍不足以判断换向和加速性能。恒速只检验了一种输入：位置随时间匀速增加。

设归一化位置 \(u\) 以圈计，系统当前拿到 \(\tau\) 秒前的值。纯延迟、匀速且没有补偿时，误差为 \(v\tau\)。合成设3000rpm，即50圈/秒，延迟100µs，对应0.005圈，也就是1.8°。它是模型算例，不是哪颗芯片的实测误差。

## 外推使用哪一刻的速度

在旧测量时刻 \(t_0\)，用当时的速度估计 \(\hat v(t_0)\) 预测到现在：

\[
\hat u(t_0+\tau)=u(t_0)+\hat v(t_0)\tau.
\]

若这段时间内加速度 \(a\) 恒定，则真实位置还多出 \(a\tau^2/2\)。因此真实值减预测值为：

\[
r=\frac12a\tau^2-\delta v\tau,\qquad
\delta v=\hat v(t_0)-v(t_0).
\]

合成设 \(a=1000\) 圈/秒²、\(\tau=100\) µs、速度估计无误，残差是 \(5\times10^{-6}\) 圈，即0.0018°。把τ放大十倍，加速度残差放大一百倍。这里必须使用旧时刻速度；换一种速度定义，推导也要重写。

## 内部滤波不能一律当纯延迟

[AS5047P手册](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5047p-datasheet-en.pdf)区分动态补偿相关指标；[Allegro A31315延迟说明](https://www.allegromicro.com/-/media/files/application-notes/an296263-a31315-signal-path-delay-for-a31315-3d-sensor.pdf?sc_lang=en)将信号链中的滤波与处理环节分别讨论。它们说明要看具体结构和配置，不能把一款产品的补偿方法代入另一款。

纯延迟模型保持输入幅度、只改变相位；低通或跟踪滤波器还会改变幅值和瞬态。仅用一个固定τ解释所有动作，是一个可以被扫频或阶跃数据否定的假设。最高转速同样要结合数据手册条件，不能替代动态准确度曲线。

换算到电机电角时，还要乘实际电机极对数；这与磁环的电周期数不是同一个概念。比较器件时先保留机械圈数和秒，再在最终结果处换算。否则一次极对数混用，就能把原本不大的时间残差放大成看似严重的角度问题，也会把补偿量配错。

实际验收至少保留三组动作：恒速看平均相位差，限幅正弦看幅值和相位，受控加速看瞬态残差。三组使用同一滤波档、参考轴和时间对齐规则，并标明输入到输出的起止事件。电机无法产生理想阶跃时，应记录真实参考运动，不能将指令曲线充当已实现的真值。
