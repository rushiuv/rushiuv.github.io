---
title: RMS变小了，噪声就变小了吗？
description: 用四个合成误差读数分开偏置、标准差和峰峰值，避免把统计口径变化当性能改善。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D01
guide_group: 测量与统计
weight: 101
related_basics:
- angle-noise
- resolution-accuracy
related_model_slugs:
- ktm5800
- ktm5900
related_guides:
- independent-samples
- atan2-quantization
related_applications:
- servo-motor
- robot-joint
keywords:
- RMS
- 标准差
- 峰峰值
- 噪声测试
aliases:
- /wiki/engineering/noise-statistics/
topic_method: true
---


校准后RMS变小，首先要问：减少的是固定偏置，还是读数波动？同一组角度数据，两个问题会给出不同答案。

先把角度换成圈数 \(u=\theta/360^\circ\)，误差取 \(e_i=\operatorname{wrap}(u_i-u_{\rm ref})\)，其中 \(\operatorname{wrap}(x)=x-\lfloor x+1/2\rfloor\)。以下只讨论误差远离半圈边界的序列。

## 四个读数，三种结果

取合成误差 \(e=[0.00025,0.00035,0.00025,0.00035]\) 圈。用分母 \(N\) 定义这份有限记录的总体标准差 \(\sigma_N\)：

\[
\mu=\frac1N\sum e_i,\qquad
R=\sqrt{\frac1N\sum e_i^2},\qquad
R^2=\mu^2+\sigma_N^2.
\]

| 统计量 | 计算结果 |
| --- | --- |
| 平均误差 | 0.00030圈，即0.108° |
| 总体标准差 | 0.00005圈，即0.018° |
| RMS | 约0.00030414圈，即0.10949° |
| 峰峰值 | 0.00010圈，即0.036° |

若只把固定零点减去0.108°，RMS降到0.018°，总体标准差却完全没变。这次改善修正了偏置，没有降低波动。若使用分母 \(N-1\) 的样本标准差，结果约为0.02078°；它与表中总体标准差也不能混写。[NIST的尺度统计量定义](https://www.itl.nist.gov/div898/handbook/eda/section3/eda356.htm)明确区分标准差和极差。

再看表中峰峰值0.036°，它只是这四个合成读数的跨度，并不等于六倍总体标准差0.108°。这组数据根本没有被设成高斯随机抽样。把仪器显示的峰峰值一律除六，既换了统计模型，也没有给出观察长度。对同一份原始记录重算，是核对软件统计栏含义的直接办法。

## 峰峰值不是固定倍数的σ

峰峰值只取记录里的两个极端。记录延长，会给新的极端更多出现机会；滤波和相关性又会改变有效观察次数。正态分布没有有限的幅度边界，因此“6σ”并不保证每一份长记录都落在宽度6σ内。[NIST正态分布定义](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm)可用于重算尾部概率，但不能反推出某厂商一定测过多少个点。

反例也要保留：转动误差中的周期波形，去掉均值后仍在标准差里；它不因此变成随机噪声。测静止噪声和测整圈误差，应使用不同动作与参考。

实际对比先保存同一窗口的原始数据，同时报告均值、样本量、标准差分母、峰峰值、采样率和滤波配置。再检查时间曲线，确认没有缓慢漂移或明显周期项。只抄一个最小RMS，无法说明改进发生在哪一层。

[下载这四个合成读数](/downloads/noise-statistics-four-points.csv)，取数值列后可用[统计工具](/topics/guides/measurement-tools/)复算。
