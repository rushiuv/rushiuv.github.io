---
title: 校准保存成功以后，下一次上电还可信吗？
description: 区分位翻转、写入中断和错误内容合法写入，用公开双页机制设计可验证的保存流程。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: D11
guide_group: 校准与配置
weight: 111
related_basics:
- crc
- self-calibration
- singleturn-multiturn
related_model_slugs:
- stm32
related_guides:
- calibration-evidence
- calibration-validation
related_applications:
- servo-motor
- robot-joint
keywords:
- 非易失存储
- 掉电恢复
- 校准保存
- ECC
aliases:
- /wiki/engineering/calibration-data-integrity/
topic_method: true
---


主控回读到了新零点，只证明当前某处能读出新值。它是否已经持久保存、掉电后会选哪一份记录，还要看另外两段流程。

把错误先分三类：保存后某些位翻转；编程或擦除途中断电；主机按完整流程写入了本来就错误的内容。三类都能改变最终参数，但防护手段不同。

## 校验保护的是哪一层

| 错误模型 | 需要的对应防护 |
| --- | --- |
| 记录位损坏 | 按码距和错误模型设计检错/纠错 |
| 更新被中断 | 保留旧有效记录与可恢复提交状态 |
| 错误内容合法写入 | 写入资格、范围和版本一致性检查 |

CRC能发现所覆盖记录的一类损坏，却无法判断主机给出的零点是否符合机械位置。ECC也不能可靠包办所有写入中断。[ST AN4894 Rev12第13页](https://www.st.com/resource/en/application_note/dm00311483.pdf#page=13)明确讨论了这个限制，并采用记录校验和启动恢复等配套机制。

## 双份不是复制两遍就结束

公开EEPROM仿真使用至少两页及页状态。借这个思路，可以给系统自己的配置记录设计：保留旧有效记录，先写候选新记录，校验后提交，重新上电再按版本与有效状态选择。具体擦写粒度、提交标志和掉电恢复必须与存储器能力匹配，不能宣称任意双份都会原子更新。

用一个合成32字节记录做软件故障注入即可先验证规则：在写载荷、写校验、写提交状态前后逐处模拟中断。重启后允许读到旧完整记录或新完整记录，不能混用半份旧系数与半份新系数；两份均无效时，应明确报告配置不可用。

低电压还会影响CPU执行与存储操作，不能只等软件最后一条命令。[Microchip的EEPROM防损坏说明](https://onlinedocs.microchip.com/oxy/GUID-80B1922D-872B-40C8-A8A5-0CBE009FD908-en-US-3/GUID-9B9FF69A-6479-4CE8-95C1-C6BB144DA410.html)要求按具体器件条件处理欠压与复位；其行为不能直接套给另一颗芯片。

## 保存次数也要算进寿命

合成设每天20次参数更新，十年约 \(20\times365\times10=73000\) 次逻辑写入。这还未计重试、迁移和底层写放大。它不是某型号寿命结论；需要再按实际耐久条件、写入分布与存储管理换成每个单元的负担。

实际放行应依次留下运行配置回读、持久记录校验、冷启动选择和校准结果复测。写入成功提示、重启后参数存在、机械误差满足要求，是三种证据，不能合成一个绿色勾。
