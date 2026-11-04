---
title: SIN/COS三次失真，为什么角度里冒出二次和四次？
description: 通道谱与角度谱相差一个阶次；先用小扰动模型辨认映射，再决定测哪里。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: R03
guide_group: 几何与解算
weight: 103
related_basics:
- inl
- angle-noise
- self-calibration
related_model_slugs:
- mlx90381
- ktm5800
related_guides:
- amplitude-temperature-error
- optical-signal-chain
keywords:
- 正余弦
- 谐波
- 失真
- 角度误差
aliases:
- /wiki/engineering/channel-angle-harmonics/
topic_method: true
---


示波器看到SIN/COS的三次谐波，角度残差却出现二次和四次。两张谱并不矛盾：角度由两路信号的比值计算，通道里某一阶的扰动会与基波相乘，产生新的阶次。

## 先说明“几次”按什么周期数

令 \(u\) 为一个信号周期内的归一化位置，\(\theta=2\pi u\)。理想信号为 \(x=A\cos\theta\)、\(y=A\sin\theta\)。对小扰动：

\[
\delta u\simeq\frac{x\delta y-y\delta x}{2\pi A^2}
\]

只给x通道叠加 \(a\cos(m\theta)\)，可得：

\[
\delta u\simeq\frac{a}{4\pi A}
[\sin((m-1)\theta)-\sin((m+1)\theta)]
\]

因此单路三次扰动会同时产生二次与四次角误差。设 \(a/A=1\%\)，两项峰值各约0.2865°电角。这是小扰动计算，不是某颗器件的实测。

## 同一根谱线，不能唯一定位故障

| 通道中的扰动 | 角度中可出现的阶次 |
| --- | --- |
| 单路直流偏置 | 一次 |
| 基波幅值失配 | 二次 |
| 单路二次失真 | 一次、三次 |
| 单路三次失真 | 二次、四次 |

两路同时失真时，各项还会叠加或抵消，不能只拿这张单路表给实物定因。角度出现二次，既可能来自幅差，也可能包含更高阶通道失真的贡献；校正幅差后仍有二次，不证明校准程序一定失败。

## 测试要保存原始两路

在相同转速、温度和采样配置下，同时记录x、y与独立位置参考。先减去偏置、对齐增益，再观察角度谱哪些项改变；随后逐路注入小幅合成扰动，对照其新增阶次。

多周期编码器要先分清电角周期与机械一圈。一个信号周期内的四次，对机械一圈可重复更多次。扰动较大、信号接近零幅或ADC削顶时，一阶展开也会失效，不能继续用0.2865°线性外推。

做频谱时最好按独立参考角度重采样到均匀位置，而非直接对速度不稳的时间序列做FFT。否则转速调制会把一个固定空间阶次摊成边带。还应保留单位和归一化方法：通道谐波占基波百分比，与角度谐波的度数，不是同一纵轴。

## 公开依据

- [ADI AN-1314：AMR角度信号与校准](https://www.analog.com/en/resources/app-notes/an-1314.html)，提供偏置与幅度处理背景。
- [Melexis MLX90381数据手册](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381)，区分模拟输出与外部角度处理。阶次映射由本文模型独立推导。
