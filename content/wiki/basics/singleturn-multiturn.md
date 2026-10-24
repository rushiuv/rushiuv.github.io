---
title: 单圈与多圈：掉电后怎样知道转过几圈
description: 把圈内角度与圈数拆开，区分存储、备用电源、齿轮与自供能计圈。
date: '2026-10-16T10:00:00+08:00'
lastmod: '2026-10-24'
layout: basic-single
basic_entry: true
basic_group: 认识编码器
weight: 3
related_basics:
- absolute-incremental
- resolution-accuracy
- interfaces
related_topics:
- 多圈编码器
related_model_slugs: []
related_guides:
- calibration-data-integrity
- sample-time-contract
- batteryless-multiturn
related_applications:
- gearbox
- robot-joint
---



单圈编码器描述一圈内的位置。轴从30°转到390°，单圈结果仍是30°。多圈系统需要同时给出圈内角度和圈数，才能区分这两个机械位置。

## 总位置由两部分组成

设圈数为 \(k\)，圈内角度为 \(\theta\)，在定义好零点和正方向后：

\[
\Theta=360^\circ k+\theta
\]

例如第12圈的90°对应总位置4410°。这是计算示例，并非某个产品的计圈范围。多圈字段的位数决定可表示的圈数范围，单圈字段的位数决定圈内数字刻度。

## 保存圈数，不等于记录掉电运动

把圈数写入非易失存储器，只能记住写入时的状态。如果掉电后轴继续转动，而计圈机构没有工作，重新读取旧记录仍会少算这段运动。需要回答的是：**无主电源时，谁在检测跨圈，谁给它供能？**

| 实现方式 | 断电运动信息来自哪里 | 需要看清的条件 |
|---|---|---|
| 机械齿轮计圈 | 齿轮位置随轴改变 | 机械范围、寿命和装配 |
| 电池或备用电源计圈 | 低功耗检测与计数链继续运行 | 电池预算、最高计圈转速、低压行为 |
| Wiegand等自供能计圈 | 转动触发的能量脉冲及方向判别 | 反转、启动边界和产品规定的运动条件 |

这些路线不能由“免电池”三个字互相替代。具体产品还要核对计圈范围、溢出、预置和故障诊断。

## 关节上还差一个坐标关系

若多圈编码器位于减速器电机侧，总角度经过传动比换算后才能对应输出端。传动背隙与弹性不会因为圈数被保存而消失。

[POSITAL：多圈Kit编码器与Wiegand供能](https://www.posital.com/en/products/kit-encoders)；[SSI Kit编码器手册](https://dms.posital.com/pdf/manual-kit-ktd-s1.pdf)给出了具体产品的接口和计圈实现。

## 验收要包含无主电源时的运动

[POSITAL德文Wiegand说明](https://www.posital.com/media/posital_media/documents/flyer_wiegand_sensor/flyer_Wiegand-Sensors_de.pdf)介绍Wiegand脉冲用于信号及能量采集，并用于免电池多圈；这不等于任意存储器都会自行计圈。可做合成验收动作：记录12.25圈，切主电源后再正转两圈，恢复后检查是否为14.25圈，同时测试产品规定的反转边界。若仍回到12.25圈，最多说明读到了旧值，尚未证明断电期间正确计圈。结合[配置完整性](/topics/guides/calibration-data-integrity/)及[减速器坐标](/applications/gearbox/)分别验证记录、计圈与传动换算。
