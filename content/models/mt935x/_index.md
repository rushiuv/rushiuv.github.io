---
title: MT935x系列
description: 带可控休眠的低压线性霍尔系列，正常工作时输出与磁场成比例的电压。
wiki: true
wiki_type: model
wiki_rank: 245
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 麦歌恩
- 纳芯微
wiki_category: 线性磁场
catalog_vendor: 麦歌恩
catalog_type: 线性磁场
catalog_form: 芯片
search_aliases:
- MT935X
- MT935x系列
official_url: https://www.magntek.com.cn/136/95
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

MT935x面向低压模拟磁场检测。现有资料能够区分工作与休眠状态，但未给出可逐项核对的完整成员清单；下表比较工作配置，不把状态名写成可订货型号。

## 型号与核心异同

| 配置（非具体料号） | 响应磁场 | 输出状态 | 发布页电流 |
| --- | --- | --- | --- |
| 正常工作 | 响应 | 有效模拟输出 | 约2mA |
| SLEEP休眠 | 不响应 | 高阻 | 约50µA |

## 共同条件与参数依据

- **供电**：1.7～3.6V

## 接入电路与配置

供电1.7～3.6V适合低压节点，但ADC输入、上拉与关断顺序仍要检查。休眠输出高阻时，采样节点可受泄漏或保持电荷影响，主控应避免把该电压解释成有效位置。

## 标定与应用验证

唤醒后需要等待信号稳定，再采集磁场相关电压。功耗评估应加入唤醒和测量时间；位置应用还需测试不同气隙、温度与运动速度下的输出映射，而不是只测静止工作电流。

## 官方资料

- [MT935x系列 官方资料](https://www.magntek.com.cn/136/95)
