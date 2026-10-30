---
title: TMR210x系列
description: 中等量程TMR线性全桥器件，成员灵敏度与工作场强不同。
wiki: true
wiki_type: model
wiki_rank: 234
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 线性磁场
catalog_vendor: 多维科技
catalog_type: 线性磁场
catalog_form: 芯片
search_aliases:
- TMR2102
- TMR2103
- TMR2104
- TMR210x系列
official_url: https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR210x提供X轴全桥模拟输出。先按磁路的最大场强选量程，再安排增益、共模和偏置裕量。

## 型号与核心异同

| 具体型号 | 目录场强范围 | 输出 | 已确认封装 |
| --- | --- | --- | --- |
| TMR2102 | ±30Gs | X轴全桥 | SOP-8／DFN-8 |
| TMR2103 | ±30Gs | X轴全桥 | 本页资料未列明 |
| TMR2104 | ±80Gs | X轴全桥 | 本页资料未列明 |

## 共同条件与参数依据

- **系统接口**：须外部放大、采样与标定，不直接输出位移码

## 接入电路与配置

更窄量程与灵敏度需结合磁路选择，避免正常行程进入饱和。放大器增益还要给零场偏置和温度变化留余量，而不是只放大室温时的最大差分信号。

## 标定与应用验证

TMR2102有SOP8与DFN8选件，焊盘和敏感点位置应核对。验收保存原始桥压、供电和参考场，区分传感器线性、放大器误差与后端ADC误差，再建立最终机械量映射。

## 官方资料

- [TMR2102／2103／2104 官方资料](https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html)
