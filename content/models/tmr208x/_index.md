---
title: TMR208x系列
description: 大磁场量程TMR全桥器件组，适合由外部电路读取模拟桥压。
wiki: true
wiki_type: model
wiki_rank: 233
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 线性磁场
catalog_vendor: 多维科技
catalog_type: 线性磁场
catalog_form: 芯片
search_aliases:
- TMR2083
- TMR2084
- TMR208x系列
official_url: https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR208x是X轴敏感的模拟全桥系列，两个成员的目录场强范围不同。后端仍需放大、采样并建立磁场到机械量的映射。

## 型号与核心异同

| 具体型号 | 目录场强范围 | 输出 | 已确认封装 |
| --- | --- | --- | --- |
| TMR2083 | ±500Gs | X轴全桥 | SOT23-5 |
| TMR2084 | ±400Gs | X轴全桥 | 本页资料未列明 |

## 共同条件与参数依据

- **电源边界**：被动桥路驱动条件不等于带ADC数字芯片的工作条件

## 接入电路与配置

桥路供电影响输出幅度与自热，放大器应检查输入共模、偏置和噪声。大范围并不意味着全范围始终具有相同线性误差，实际工作区还应对照正式手册。

## 标定与应用验证

位置应用需要磁体与机械行程的映射，电流应用还要考虑导体和磁路。验证先做零场、正负场扫描及温度测试，再讨论位移或电流误差，不能将ADC位数当作传感器本身精度。

## 官方资料

- [TMR2083／2084 官方资料](https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html)
