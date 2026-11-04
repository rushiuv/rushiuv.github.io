---
title: TMR300x系列
description: 双桥模拟角度器件组，主要区别是桥阻、适用磁场与封装选项。
wiki: true
wiki_type: model
wiki_rank: 226
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 模拟角度
catalog_vendor: 多维科技
catalog_type: 模拟角度
catalog_form: 芯片
search_aliases:
- TMR3002
- TMR3004
- TMR3005
- TMR300x系列
official_url: https://www.dowaytech.com/sensor/angle_sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR300x输出模拟SIN/COS，桥阻与磁场窗口是成员之间最直接的区别。选型需要同时匹配磁体和后端输入阻抗。

## 型号与核心异同

| 具体型号 | 目录桥阻 | 工作场强 | 输出 |
| --- | --- | --- | --- |
| TMR3002 | 350kΩ | 70～400Gs | 模拟差分 |
| TMR3004 | 15kΩ | 150～1100Gs | 模拟差分 |
| TMR3005 | 多阻值版本，按完整型号 | 200～800Gs | 模拟差分 |

## 共同条件与参数依据

- **测量范围**：360°磁场方向，模拟差分输出，后端须采样解算
- **边界**：不是内部输出数字角度的编码器ASIC

## 接入电路与配置

桥阻从350kΩ到15kΩ及多阻值选件差异很大，应同时考虑驱动电流、输入偏置及采样建立时间。相同供电下不能假定各成员具有相同输出负载能力。

## 标定与应用验证

70～400Gs、150～1100Gs与200～800Gs分别属于所列成员。选择磁体应按对应窗口验证全圈幅度，校准则先处理桥路偏置和幅相失配，再测机械角度残差。

## 官方资料

- [TMR3002／3004／3005 官方资料](https://www.dowaytech.com/sensor/angle_sensors.html)
