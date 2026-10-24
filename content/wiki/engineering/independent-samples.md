---
title: 读取一万次，为什么只得到一百份信息？
description: 用重复保持和协方差算例解释有效样本数，并检查噪声分析有没有静默失效。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D02
guide_group: 测量与统计
weight: 102
related_basics:
- angle-noise
- latency
related_model_slugs: []
related_guides:
- noise-statistics
- velocity-noise
keywords:
- 独立样本
- 重复读取
- 自相关
- Allan偏差
---

传感器每毫秒更新一次，主控每10微秒读取一次。一秒能收到十万帧，却至多只有一千次内部更新。没有检查数据身份就按帧数估计平均收益，会把同一结果重复计算。

以下用归一化角度误差 \(e\) 表示圈数。对 \(N\) 个零均值读数，均值方差为：

\[
\operatorname{Var}(\bar e)=\frac1{N^2}\sum_{i=1}^{N}\sum_{j=1}^{N}C_{ij},\qquad C_{ij}=\operatorname{Cov}(e_i,e_j).
\]

只有各次独立、方差相同，才化成 \(\sigma^2/N\)。这是把[NIST不确定度传播中的协方差](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty)用于等权均值后的结果。

## 复制不会增加测量

合成例：100个独立读数，每个标准差为 \(10^{-4}\) 圈。平均后标准差是 \(10^{-5}\) 圈，即0.0036°。把每个读数复制100次，文件变成10000行，平均结果仍然相同。若按10000个独立样本计算，会错误地预报0.00036°，乐观十倍。

但“读数相同”也不证明没有更新：真实静止输入经量化后能连续输出同一码。辨认新样本应优先看更新标志、样本计数或已核对的时刻，不能只数码值变化。

数据身份还应跨过通信层核对：递增的主机接收序号，只证明收到新报文，不证明传感器完成了新转换。若只有接收时间而没有更新标志，可改变读取间隔，检查重复结构是否随之变化，再与手册刷新定义对照。单靠“这一段码值没变”作删除或去重，会把真实的静止停留也删掉。

## 平均也能快过根号N

两点同方差、相关系数为 \(\rho\) 时，两点均值的标准差是 \(\sigma\sqrt{(1+\rho)/2}\)。合成设 \(\rho=-0.5\)，结果为 \(0.5\sigma\)，优于独立时的 \(0.707\sigma\)。所以看到收益快过 \(\sqrt N\)，应检查负相关或噪声整形，而不是直接判计算错。[NIST自相关方法](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm)要求保留等间隔时间条件。

长时间漂移可再用分块均值差观察；采用Allan类指标时，要声明输入究竟是角度、相位还是频率，不能照搬时钟曲线斜率给磁体老化定性。[NIST SP1065](https://www.nist.gov/publications/handbook-frequency-stability-analysis)提供数据类型与分析方法的对应关系。

实际分析先核时间戳是否递增、记录是否完整，再画自相关和不同平均窗的散布。遇到全常数、有效样本不足或采集时间未知，应输出“无法估计”及原因；不能把空数组、NaN或拟合失败自动填成零噪声。这是分析程序自身也必须通过的测试。
