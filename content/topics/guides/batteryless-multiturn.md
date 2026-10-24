---
title: 免电池多圈记住了圈数，为什么接口仍要供电？
description: 把事件供能、圈数状态、单圈角度与上电恢复分开验收，不把脉冲能量当连续电源。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
topic_method: true
plan_id: G03
guide_group: 校准与配置
weight: 150
related_basics:
- singleturn-multiturn
- absolute-incremental
related_model_slugs:
- posital-ktd-s100b-1609
- admt4000
related_applications:
- robot-joint
- closed-loop-stepper
- water-meter
related_guides:
- calibration-data-integrity
- position-validity-state
keywords:
- 免电池多圈记住了圈数
- 校准与配置
editorial_image: images/editorial/chromeos-magnetic-20261024.webp
editorial_image_alt: 位置反馈器件的装配场景示意
---


“断电还能记圈”指某条状态链在没有主供电时继续工作，不意味着角度测量、处理和串行通信都持续获得电源。选型要分别检查圈数怎样更新、单圈怎样读取、上电后怎样对齐。

## 一次脉冲能量，不是连续功率

[POSITAL德文Wiegand说明](https://www.posital.com/de/wiegand-sensors)描述磁极性转换产生脉冲，脉冲既可当事件，也可为低功耗电路提供能量。其能量对低速的特性，不能推导为静止时仍无限提供平均功率。

设每个有效事件可用能量为E、事件率为f，平均输入功率上限先看 \(P=Ef\)，还要扣转换和储能损耗。f趋近零，平均功率也趋近零；单次翻转的脉冲仍可能足以完成一次受设计约束的状态更新。这里没有给任何实物E值，也不据此承诺供电能力。

## 圈数与单圈不是同一个数

以归一化连续位置 \(U=n+u\) 表示，n为整数圈数，u为圈内位置。即使n在掉电期间被正确保存，接口恢复后仍要把它与同一机械状态下的u配对；方向、溢出和Preset也需要定义。

[POSITAL德文Kit目录](https://www.posital.com/de/products/kit-encoders)说明免电池、免齿轮的多圈路线；但一个[明确订货号](/models/posital-ktd-s100b-1609/)同时仍列4.5～5.5V供电及正常电流。这不是矛盾，而是事件计数与正常读数链路的职责不同。

## 用动作验证，而不是只断电等一会儿

保留上电前状态，断电后分别做整圈、跨边界小幅来回、低速反向与指定范围运动，再读取圈数、单圈、状态和首次有效时刻。每项动作必须在具体器件允许磁路、速度和电源条件内，不能从技术族介绍导出任意磁场下都不会漏计。

若需与其他多圈机制比较，应按原厂规定分别设计动作，不把Wiegand测试假设套到所有器件。[配置与恢复验证](/topics/guides/calibration-data-integrity/)可记录一致性，但不能代替具体计圈机制的证据。
