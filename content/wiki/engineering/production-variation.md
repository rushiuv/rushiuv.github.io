---
title: 样机误差很小，为什么量产还需要另一张分布图？
description: 用误差传播与Cpk算例分开单件、参考不确定度和过程变差，避免由一次合格推出批量保证。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D12
guide_group: 测量与统计
weight: 112
related_basics:
- resolution-accuracy
- inl
- mounting
related_model_slugs: []
related_guides:
- noise-statistics
- calibration-validation
keywords:
- 过程能力
- Cpk
- 变差预算
- 误差预算
---

一套装配调得很准，回答了“这套条件下测到了什么”。批量交付还要回答：换磁体、PCB、工装和批次以后，误差分布会怎样变化。

仍用归一化角度u，一圈为1。将输出写成 \(u=f(x_1,\ldots,x_n)\)，输入可包含气隙、安装偏移和校准残差。小扰动下：

\[
s_u^2\approx\sum_i c_i^2s_i^2+2\sum_{i<j}c_ic_j\operatorname{Cov}(x_i,x_j),\qquad c_i=\frac{\partial f}{\partial x_i}.
\]

这是[NIST不确定度传播](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)中的一阶形式。把它用于批量变差模型时，还需说明每一项来自跨件分布、同件重复测量还是参考系统；三者不能不加区分地放进同一σ。

## 两项相同误差，不一定按根号二合成

合成设两个误差贡献的标准差均为0.0001圈。独立时，合成为0.000141圈，即0.0509°；若完全正相关且作用方向相同，合成为0.0002圈，即0.072°。共同温度、共同工装或共同参考，会让“独立相加”的假设失效。

零均值也不表示没有风险。若不同批次分别偏向两侧，把数据混在一个直方图里，会丢掉时间与批次身份；一颗反复测得很稳，则没有提供跨件分布。

## Cpk必须带着过程条件

对稳定、近似正态且规格已明确的过程，能力指数可写成：

\[
C_{pk}=\min\left(\frac{U-\mu}{3s},\frac{\mu-L}{3s}\right).
\]

合成设误差规格为±0.001圈，均值0.0001圈、s=0.0002圈，则Cpk=1.5。[NIST过程能力说明](https://itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm)同时给出稳定性、分布和样本条件；这个1.5不是对所有行业自动生效的放行许可，更不是“每颗都合格”的证明。

若过程在漂移，或者混入两群不同均值的数据，先按来源和时间检查过程图，再判断该用什么模型。[NIST控制图入口](https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc3.htm)对应的是监测过程变化，不能由单个能力数字替代。

Cpk的规格边界由产品要求给定，不应看完这一批数据再移动上下限。把超限样本先剔除，或只挑校准最好的工位计算，也会改变所代表的过程；这种数字即使算术正确，也不能回答原先的批量问题。

实际落地先保留样品、批次、工位、温度和校准版本身份，再分别估计重复性与跨件变差。报告能力估计时写出样本量、规格、分布和置信条件；参考测量能力不足或过程尚不稳定，就先收敛这两项。继续压低一颗样机的最优误差，不能替代批量证据。
