---
title: CRC通过之后，位置还要过三道检查
description: 用合成冻结、偏置和启动故障，区分帧完整、新鲜、器件状态与位置可信。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: E09
guide_group: 接入与诊断
weight: 90
related_basics:
- crc
- latency
related_model_slugs:
- admt4000
related_guides:
- first-power-interface
- safety-evidence-levels
- system-acceptance-record
- sample-time-contract
- calibration-data-integrity
related_applications:
- robot-joint
- servo-motor
- pneumatic-cylinder
keywords:
- CRC
- 数据新鲜度
- 位置有效性
aliases:
- /wiki/engineering/position-validity-state/
topic_method: true
---


合法帧可以装着旧角度，也可以装着偏移后的角度。控制器要给数据安排明确的使用状态，而不是把CRC通过直接翻译成“位置可信”。

## 分层记录，才能知道漏掉了什么

| 检查层 | 能观察什么、仍有什么盲点 |
| --- | --- |
| 帧完整性 | CRC与帧格式；不能独立证明测量正确 |
| 数据新鲜度 | 转换计数、采样时间及更新事件；相同角度码不一定是旧帧 |
| 器件状态 | 启动、供电、幅值等已规定诊断；未覆盖的故障仍可能存在 |
| 外部一致性 | 与独立参考或可验证运动约束比较；共享磁体、支架或算法可能产生共因 |

例如[ADMT4000 Rev.C读取章节](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)SPI响应中包含2bit转换计数及CRC，计数会循环；它与另一个8bit的CNVCNT寄存器不是同一字段。隔了整周期再读到相同计数，不能单凭它判定没有更新；读取角度与绝对角度还需遵守同一事务的要求。具体诊断要按器件手册实现，不能把通用表当成任何芯片都具备的功能清单。

## 三次软件注入，不冒充器件故障

在离线回放或与执行器隔离的测试环境中，制作三段**合成数据**：

1. 让角度与帧序号冻结，但持续生成正确CRC。应由新鲜度规则发现；只验CRC会漏过。
2. 每帧角度增加固定1°偏置，序号照常前进。新鲜度仍通过；只有已建立参考的交叉比较能看见它。
3. 保留数据帧，置入手册定义的未就绪或故障状态。验证应用是否拒绝把这帧作为新位置使用，并保留首次异常时间。

超时阈值需从系统允许数据龄期倒推。假设项目自行限定有效位置龄期为200µs，就应记录起算事件与超时后状态，不能把200µs推广成编码器通用限值。恢复也要定义：重新就绪、配置确认、参考一致，哪些满足后才允许重新使用。

[TI功能安全资料](https://www.ti.com/technologies/functional-safety.html)将分析、诊断说明和认证文档分别列项，说明单一诊断功能不能替代完整证据。本页的注入检查只验证软件分支是否执行，不给诊断覆盖率或安全等级；涉及这些结论时继续核[安全证据范围](/topics/guides/safety-evidence-levels/)。
