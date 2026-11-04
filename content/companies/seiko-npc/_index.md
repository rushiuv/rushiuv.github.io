---
title: 精工NPC
description: Seiko NPC：提供LED与OEIC同封装的反射式光编码器IC，适合理解模拟前端、码尺与外部细分的分工。
wiki: true
wiki_type: company
wiki_rank: 130
seed_count: 0
lastmod: '2026-10-24'
official_url: https://www.npc.co.jp/
wiki_category: 光学编码器IC
related_models:
- SMD-01B
---

精工NPC（セイコーNPC / Seiko NPC）设计、开发、制造和销售半导体产品。编码器产品位于反射式光检测与信号处理这一层；应与外部码尺、细分电路和最终机械系统分开看。

## 从哪条产品线读起

[SMD-01B](/models/smd-01b/)把LED和带PD阵列的OEIC放在一个封装内，输出模拟A/B信号；SMD-04B、SME-08A/B和SM3414B属于其他输出/配置路线，不能从一款的周期、电源和插值方式推给整个系列。原厂日文选型表同时列线性与旋转的应用示例，码尺形态仍需匹配。

阅读时先看[光学信号形成](/topics/guides/optical-signal-chain/)，再看[周期与细分](/topics/guides/rate-budget/)。小封装不等于所有机械安装误差已被芯片消除；产品页的“易安装”也不能替代配套码尺条件。

## 官方资料

- [原厂公司概要（日文）](https://www.npc.co.jp/company/profile/)
- [光编码器选型表（日文）](https://www.npc.co.jp/support/sensor-enc/guide/)
- [光编码器支持与评估码尺（日文）](https://www.npc.co.jp/support/sensor-enc/)
