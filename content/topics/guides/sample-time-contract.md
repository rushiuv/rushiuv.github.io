---
title: 两路角度要相减，先签清楚哪一刻
description: 以BiSS的LAT事件为入口，将采样、处理、到达和使用时刻写成可验证的时间约定。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D07
guide_group: 时间与动态
weight: 107
related_basics:
- interfaces
- spi-ssi
- latency
- crc
related_model_slugs:
- mlx90382
related_guides:
- spi-data-age
- velocity-noise
related_applications:
- servo-motor
- robot-joint
- linear-motor
keywords:
- 同步采样
- 时间戳
- 数据有效性
- 双编码器
aliases:
- /wiki/engineering/sample-time-contract/
topic_method: true
---


两路角度都正确，运动时相减仍能多出一个差值：两路看见的不是同一瞬间。提高串口速率，只能缩短部分传输时间，不能自动统一测量事件。

设真实归一化角度为 \(u(t)\)，速度 \(v\) 以圈/秒计。两路有效测量时刻相差 \(\Delta t\)，短时间匀速近似下，额外角差为：

\[
\delta u_{\rm time}\approx v\Delta t.
\]

合成例：50圈/秒、相差3µs，对应0.00015圈，即0.054°。轴静止时这一项为零，因此静态比较一致，无法证明运动中同步。

## 协议事件是一条起点

[BiSS-C D2第9—10页](https://biss-interface.com/wp-content/uploads/2024/07/BiSS_C_protocol_D2en.pdf#page=9)定义首个MA上升沿LAT，触发从机锁存或生成过程数据，并允许处理后再发送。[BiSS Concept A5第3页](https://biss-interface.com/wp-content/uploads/2025/07/BiSS_Interface_Concept_appnote_A5en.pdf#page=3)将锁存、线路延时补偿和从机处理分开。

这说明接口可以定义同步事件；但LAT不是“所有模拟前端零延迟”。从触发到生成有效数据的响应，还需对应设备手册和配置来说明。线路延时补偿也不能顺带消掉前端滤波的未知时间。

## 一份够用的时间约定

| 必填项 | 要写到可检查的程度 |
| --- | --- |
| 有效测量事件 | 模拟采样、寄存器快照或补偿后等效时刻 |
| 时基与身份 | 谁的时钟、时间单位、帧号与更新关系 |
| 使用年龄 | 到达和控制使用分别距测量多久 |
| 有效性 | 状态与角度是否同周期，超时如何标记 |

这是系统记录格式，不是新增协议。位置、状态与时间三者配套，才知道某一帧该怎样解释。CRC正确却已经过期的数据，应保留原测量时刻，不能因重读成功就改标成“现在”。

## 验收要让同步假设有机会失败

先用共同参考运动，同时记录两路物理触发、报文和任务使用事件。改变总线负载与读取顺序，再比较时间偏差分布。随后加入上电首帧、停更与超时，检查状态和帧号能否区分有效新样本、旧样本与无效数据。

不能直接观察有效测量事件时，应通过有时间基准的已知输入变化辨认响应，并保留无法分离的误差。把“接收完成”当成“测量发生”，即使主机时钟完全同步，也会把链路差异重新写进角差。
