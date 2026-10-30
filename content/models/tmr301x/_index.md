---
title: TMR301x系列
description: 覆盖差分与单端输出的TMR模拟角度器件，需按型号选后端采集方式。
wiki: true
wiki_type: model
wiki_rank: 227
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 模拟角度
catalog_vendor: 多维科技
catalog_type: 模拟角度
catalog_form: 芯片
search_aliases:
- TMR3014
- TMR3015
- TMR3016
- TMR3017
- TMR301x系列
official_url: https://www.dowaytech.com/sensor/angle_sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR301x的差分与单端成员需要不同的采集安排。先确定输出形式，再核对桥阻、供电和封装，避免只改料号而沿用前端。

## 型号与核心异同

| 具体型号 | 输出 | 目录桥阻 | 已确认供电／封装 |
| --- | --- | --- | --- |
| TMR3014 | 差分 | 1kΩ | 成员手册核对 |
| TMR3015 | 单端 | 本页资料未列明 | 3～5.5V；DFN4／SOT23-5 |
| TMR3016 | 差分 | 2.5kΩ | 成员手册核对 |
| TMR3017 | 单端 | 200kΩ | 成员手册核对 |

## 共同条件与参数依据

- **测量链**：模拟角度相关信号仍需ADC及角度计算

## 接入电路与配置

差分采样需要关注两端共模，单端采样则要关注地与参考噪声。1kΩ、2.5kΩ及200kΩ桥阻反映不同负载和功耗条件，不能只按最小电流选择而忽略采集阻抗。

## 标定与应用验证

SIN/COS要在相同时间基准下采样，经过偏置、幅差和正交校正后计算角度。整机验证仍需参考角度，校正后的圆轨迹只能说明部分电气失配被处理，不能证明磁体误差已消除。

## 官方资料

- [TMR3014～3017系列 官方资料](https://www.dowaytech.com/sensor/angle_sensors.html)
