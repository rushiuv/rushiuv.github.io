---
title: 两路一起变小不改角度，为何温漂仍然变大？
description: 公共幅度缩放可以约掉，但偏置、相对增益、噪声和饱和不会一起消失。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: R12
guide_group: 几何与解算
weight: 112
related_basics:
- amr
- tmr
- angle-noise
- self-calibration
related_model_slugs:
- kmz60
- mlx90381
- tmr3081
related_guides:
- channel-angle-harmonics
- optical-signal-chain
keywords:
- 温漂
- 正余弦
- 偏置
- 增益失配
- 噪声
---

SIN/COS随温度一起变小，反正切里的公共倍数可以约掉。这句话正确，却不能推出“幅度温漂不会影响系统角度”：真实链路还有偏置、噪声与有限输出范围。

## 只有公共的非零比例因子会消掉

令归一化位置为u，理想两路为 \(x=A\cos(2\pi u)\)、\(y=A\sin(2\pi u)\)。当 \(k>0\) 时：

\[
\operatorname{atan2}(ky,kx)=\operatorname{atan2}(y,x)
\]

因此相同的正比例幅度变化不改角度。若两路缩放不同，或还残留偏置，这个等式就不再描述完整信号。

## 一毫伏偏置，在小信号下更贵

设两路基波峰值都是100mV，仅y通道残留+1mV偏置。小扰动下：

\[
\delta u\simeq\frac{b_y\cos(2\pi u)}{2\pi A}
\]

峰值约0.00159圈，即0.573°。若温度只让两路基波同时降到50mV，而这1mV偏置没有一起减小，峰值约变成1.146°。公共幅度本身仍可约掉，变大的是偏置相对基波的比例。

这不是某个AMR器件的温漂指标，只是设定信号的计算。两路各自的偏置方向也会改变角误差相位，不能只测总幅度预测温漂。

## 相对增益与随机噪声分开看

若x通道增益比y大1%，一阶模型会产生约0.286°峰值的二次角误差。若是两路同增益变化，则没有这一项。两者都叫“增益温漂”，对角度的影响却不同。

固定的输入噪声也会在基波减小时占更大比例。反过来，幅度过大导致放大器或ADC削顶，同样破坏角度；因此系统需要的是有效信号窗口，而不是单纯追求幅度越稳或越大。

## 温箱里至少保存四个量

在固定机械位置与多个整圈采样中，分别记录两路偏置、基波幅值、幅值比，以及对独立参考的角度残差。保持相同带宽、ADC参考和采样顺序，检查升温与降温是否一致。

先判断公共变化还是差分变化，再决定校准对象。只测桥阻温度系数，或只展示最终角度的静止标准差，都不足以解释整圈角温漂。

如果ADC参考也随电源变化，比例式输出中的某些公共变化会在采样比值里进一步抵消；若参考独立或只影响一条通路，结果又不同。测温漂时应保存传感器供电和ADC参考电压，避免把采样系统的比例变化全部算成磁敏元件漂移。

## 公开依据

- [ADI AN-1314：AMR信号与幅相处理](https://www.analog.com/en/resources/app-notes/an-1314.html)。
- [Melexis MLX90381数据手册](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381)，区分输出偏置、灵敏度与温度指标。本文毫伏数值与1%为独立设定算例。
