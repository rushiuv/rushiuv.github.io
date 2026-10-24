---
title: 直线尺装在铝梁上，纳米分辨率为何仍挡不住热误差？
description: 用热膨胀和基准位置的设定算例，分开尺本体、安装约束与工作点位移。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
topic_method: true
plan_id: G01
guide_group: 环境与验收
weight: 150
related_basics:
- mounting
- resolution-accuracy
related_model_slugs:
- resolute-rl
- sin60
related_applications:
- linear-motor
related_guides:
- thermal-cycle-reversibility
- parameter-conditions
keywords:
- 直线尺装在铝梁上
- 环境与验收
---

读数每次只跳1nm，机器工作点仍会随温度移动。分辨率描述数字刻度；长尺热变形取决于材料、温差、固定点及尺与基体怎样传力。

## 先问尺能不能自由伸长

自由、均匀温升的简化模型是 \(\Delta L=\alpha L\Delta T\)。设一米尺、温升10°C，若自设尺材系数为10µm/(m·°C)，长度变化100µm。这个算例不是任何型号的保证值。

若基体自设为23µm/(m·°C)，两者自由伸长差为130µm。但不能把130µm直接填成最终读数误差：尺若被连续约束、只设一端热基准或允许滑移，长度变化、应力和误差分布都不同。

## 基准点放哪，误差从哪长起

理想均匀温差、单点基准且自由伸长时，位置x的变化与离热基准距离成比例。基准在行程中央，端部到基准的距离比全长短；但这只是几何分布变化，不等于热膨胀被消除，也未处理温度梯度和工作点到读头的阿贝偏置。

安装验收应记录：尺材、基体、约束方式、热基准、测温点和参考位置。再做受控温度变化，比较多个行程点，而不是只看一个零点。补偿表必须对应这些条件；更换夹持或重粘码尺后要重新验证。

## 原厂资料怎样用

[Renishaw热安装白皮书（英文，2019）](https://www.renishaw.com/en/white-paper-mounting-encoder-scales-for-optimum-thermal-performance--44316)明确把材料与安装方式共同纳入热行为。[光学编码器FAQ](https://www.renishaw.com/en/optical-encoders-frequently-asked-questions--34674)区分胶粘、夹持、FASTRACK等不同尺型安装。它们提供分类依据，不支持把某个标尺的热膨胀系数移给所有读头。

例如[RESOLUTE](/models/resolute-rl/)的输出分辨率、周期内误差和所配码尺的每米精度需分别读取。真正要比较的是当前装配、温场和参考下的长度误差，不是哪个规格表的小数位最多。
