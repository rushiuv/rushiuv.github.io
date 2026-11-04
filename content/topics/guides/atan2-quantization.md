---
title: 静止时一位不跳，角度为什么仍有量化误差？
description: 从双通道量化推导角度误差，说明整圈RMS、单点偏差与多1.65位的适用条件。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D03
guide_group: 测量与统计
weight: 103
related_basics:
- resolution-accuracy
- angle-noise
related_model_slugs:
- ktm5800
related_guides:
- noise-statistics
- independent-samples
keywords:
- atan2
- ADC量化
- 有效位数
- 静止偏差
aliases:
- /wiki/engineering/atan2-quantization/
topic_method: true
---


把正余弦送进ADC，停止转轴，输出角度可以一位不跳。但这只说明同一输入一直得到同一个数字，不说明它与真实角度一致。

设 \(x=A\cos(2\pi u)\)、\(y=A\sin(2\pi u)\)，\(u\) 以圈计，\(A\) 是每路峰值。两路按相同电压步距 \(q\) 舍入量化，没有削波。小误差线性化得到：

\[
\delta u\approx\frac{-\sin(2\pi u)\delta x+\cos(2\pi u)\delta y}{2\pi A}.
\]

这是[NIST一阶不确定度传播](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)在atan2上的直接应用。

## 平均模型和单点上界不同

若两路量化误差可近似为互不相关的均匀分布，各自RMS为 \(q/\sqrt{12}\)，则角度RMS为：

\[
\sigma_u\approx\frac{q}{2\pi\sqrt{12}A}.
\]

但固定角度、无模拟噪声时，两路量化误差也是固定值，时间平均不会消掉。按每路舍入误差不超过 \(q/2\) 求得的一阶界为 \(|\delta u|\lesssim q/(2\pi\sqrt2 A)\)。它是前述RMS的 \(\sqrt6\) 倍；这是边界估算，不保证扫每个角度都恰好达到。

合成设 \(A/q=2048\)：RMS约 \(2.24\times10^{-5}\) 圈，换成角秒约29.1″；一阶最坏界约71.2″。这些是电信号相位对应的角度，折算机械角还需明确每圈有多少电周期。

## 1.65位从哪里来

定义一把等RMS的角度数字尺，使其步距 \(q_u=\sqrt{12}\sigma_u=q/(2\pi A)\)。若理想N位双极ADC恰好满幅，\(A/q\approx2^{N-1}\)，这把尺的位数为 \(-\log_2q_u\approx N+\log_2\pi\)，即多约1.65位。

这个数依赖满幅、量化模型和“等RMS位数”定义，不是芯片准确度，也不自动等于按频谱测得的ENOB。[ADI MT-001](https://www.analog.com/media/en/training-seminars/tutorials/MT-001.pdf)特别说明量化误差不总与输入无关。

这个推导还有两个容易漏掉的边界。第一，A是每路峰值，不是峰峰值；误填两倍幅值，会把预计角度误差低估一半。第二，q与A必须使用同一电压或ADC码单位。只有一条通道满幅、另一条已经削波时，不能继续按同一个A套公式。

增大幅度通常能缩小量化项，但不能无限加增益。输入接近电源轨、ADC满量程或前级压缩区以后，削波引入的是确定失真，平均不会恢复被截掉的波形。验证幅度收益时，先检查两路各自的最小值、最大值和削波计数，再看角度。这样才能区分“数字尺子更细”和“模拟波形已变形”。

实际验证可先扫整圈，保存原始x/y和角度误差，再固定几个角度重复采样。分别比较空间RMS和时间标准差；加入模拟噪声或再次截位后，重新核对误差相关性，不能继续默认同一模型。
