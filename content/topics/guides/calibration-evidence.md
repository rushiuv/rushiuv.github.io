---
title: 把李萨如椭圆变圆，为什么角度还会错？
description: 以MLX90382公开资料区分幅相自校准、整圈线性化与零点设置，说明各自观察到什么。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D08
guide_group: 校准与配置
weight: 108
related_basics:
- self-calibration
- inl
- magnetic-encoder
related_model_slugs:
- mlx90382
related_guides:
- calibration-validation
- calibration-data-integrity
related_applications:
- robot-joint
keywords:
- 自校准
- 李萨如
- 非线性校准
- 线性化
aliases:
- /wiki/engineering/calibration-evidence/
topic_method: true
---


两路正余弦的李萨如图从椭圆变成圆，说明一部分幅相失配得到改善。但圆上每一点究竟对应多少机械角，仍需要另一条证据。

用归一化机械角 \(u\) 表示一圈，设两路信号为：

\[
x=A\cos[2\pi g(u)]+b_x,\qquad
y=B\sin[2\pi g(u)]+b_y.
\]

去掉偏置、校正幅值后，轨迹可以成为圆。若磁路引入的角度映射 \(g(u)\) 不是u，atan2得到的仍是 \(g(u)\)，而非真实机械角。

## 一个形状完全正确的反例

合成设 \(g(u)=u+0.001\sin(2\pi u)\)。它仍是一组理想正余弦，李萨如图没有幅差和偏置；最大角度偏差却为0.001圈，即0.36°。仅看圆的形状，无法知道该把这份机械映射误差补到哪里。

所以“自动”应拆成三个问题：修正哪种误差、使用什么观测约束、最终靠什么验证。它不是“无需任何运动条件”的同义词。

## 同一颗器件也能有两条校准链

[MLX90382 Rev1.0手册第21页](https://www.melexis.com/-/media/files/documents/datasheets/mlx90382-datasheet-melexis.pdf#page=21)分别描述运动中跟踪I/Q相对灵敏度与正交度的自校准，以及16点角度线性化。前者观察信号失配；后者以角度误差曲线定义补偿，两者不是同一功能。

[原厂EoL应用笔记Rev001第36页](https://www.melexis.com/-/media/files/documents/application-notes/application-note-programming-and-eol-calibration-via-spi.pdf#page=36)说明线性化误差曲线的测量条件和表值处理。这里引用的是具体下载版本，不将另一份文档的转速、点数或失败标志搬来共用。

## 选型表只需问到这四项

| 校准内容 | 需要确认的证据 |
| --- | --- |
| 偏置、幅值、正交度 | 覆盖了哪些信号轨迹，是否满足算法条件 |
| 整圈角度线性化 | 误差相对哪把机械角度参考测得 |
| 零点与方向 | 如何定义起点，是否改变误差形状 |
| 保存与验收 | 写到哪里，重启后怎样独立复测 |

“完成”标志只证明对应流程进入某个状态，不自动给出全温整机精度；失败也不能在没有手册依据时一律解释成速度不稳。

实际比较应保留校准前后整圈残差、磁体与装配条件，再使用未参与建表且参考明确的数据复测。若设备受机械限位，先确认它能否完成要求的运动覆盖，再讨论校准时间快不快。
