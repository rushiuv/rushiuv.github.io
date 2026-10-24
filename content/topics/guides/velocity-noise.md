---
title: 速度差分里的根号2，什么时候该留下？
description: 将位置噪声与端点时间抖动分开预算，用相关系数解释速度噪声的变化。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D04
guide_group: 测量与统计
weight: 104
related_basics:
- angle-noise
- latency
- abz
related_model_slugs: []
related_guides:
- independent-samples
- sample-time-contract
keywords:
- 速度估计
- 时间抖动
- 协方差
- 差分
aliases:
- /wiki/engineering/velocity-noise/
topic_method: true
---


同一个静止角度噪声，控制周期缩短后，直接差分的速度反而更抖。原因先藏在分母里，还藏在前后两点是否相关。

先展开归一化角度 \(u\)，速度 \(v=du/dt\) 的单位为圈/秒。固定采样间隔 \(T\) 下，估计 \(\hat v=(u_k-u_{k-1})/T\)。若两次位置噪声同为标准差 \(\sigma_u\)，相邻相关系数为 \(\rho_u\)：

\[
\sigma_{v,u}=\frac{\sigma_u}{T}\sqrt{2(1-\rho_u)}.
\]

独立时 \(\rho_u=0\)，根号2必须保留。合成设 \(\sigma_u=10^{-5}\) 圈、\(T=1\) ms，速度标准差约0.01414圈/秒，即0.849rpm。只把T缩短一半而单次噪声不变，结果增大一倍。

## 时间误差要另开一行

若真实采样时刻为 \(kT+\epsilon_k\)，却仍用固定T作分母，匀速、小抖动条件下，速度误差约为 \(v(\epsilon_k-\epsilon_{k-1})/T\)。因此：

\[
\sigma_{v,t}\approx\frac{|v|\sigma_t}{T}\sqrt{2(1-\rho_t)}.
\]

[NIST传播公式](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)中的协方差不能省略；[ADI MT-007](https://www.analog.com/media/en/training-seminars/tutorials/MT-007.pdf)则解释了采样时间误差为何随输入变化率转为幅度误差。

合成设3000rpm、\(T=1\) ms、\(\sigma_t=1\) µs。独立端点给约4.24rpm；若 \(\rho_t=0.75\)，则约2.12rpm。相关系数在−1到1之间时，该根号因子可在0到2之间，不能无条件限制为1到 \(\sqrt2\)。

这里的ρ描述相邻两点，不能从整个记录的一个总体标准差推出来。固定时间偏移可在差分中抵消，周期性调度却会在不同频率上留下结构；“延时很大”和“延时在变化”不是同一种速度误差。记录噪声时，还应分开平均速度偏差与围绕均值的随机散布。

换成跨多拍求速度，相当于同时改变时间窗和两个端点的相关性。应按新的间隔重新计算，而不是把单拍结果机械地除以平均次数。若角度仍按0到1圈存储，先处理跨圈连续性；跨过零点的一次整圈假跳，会压过这里讨论的全部小噪声。

## 平滑的代价也要记录

实际时间戳若准确对应真实采样事件，改用实测间隔可去掉理想匀速例中的这项分母误差；若时间戳只是“接收完成”，却不能补回未知的前端采样时间。

位置噪声与时间抖动只有在互不相关时，才可按方差相加。相关滤波、量化台阶或周期调度会破坏简单白噪声模型。实验应同时保存位置、有效采样时刻和控制使用时刻，报告相邻相关性；再比较直接差分与固定响应条件下的速度估计。显示更平稳，还需确认延迟有没有一起变大。
