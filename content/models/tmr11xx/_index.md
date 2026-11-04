---
title: TMR11xx系列
description: 单极TMR位置开关器件组，连续感测和占空比采样版本需分开选择。
wiki: true
wiki_type: model
wiki_rank: 235
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 磁开关
catalog_vendor: 多维科技
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- TMR1102
- TMR1148
- TMR1162
- TMR11xx系列
official_url: https://www.dowaytech.com/sensor/switch_sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR11xx用于单极磁状态检测。三款首先要区分输出级和感测方式：连续感测的电流不能与间歇采样的平均电流直接排名。

## 型号与核心异同

| 具体型号 | 输出级 | 感测方式 | 目录电流 |
| --- | --- | --- | --- |
| TMR1102 | 推挽 | 连续感测 | 典型1.5µA |
| TMR1148 | 开漏 | 连续感测 | 典型1.5µA |
| TMR1162 | 开漏 | 占空比采样 | 200nA，采样条件另核对 |

## 共同条件与参数依据

- **连续感测成员供电**：TMR1102／TMR1148目录为1.8～5.5V；TMR1162按其独立手册确认。
- **检测方向**：按磁场敏感轴及磁体极性布置

## 接入电路与配置

开漏接入需要外部上拉，推挽则应确认电平兼容。连续版1.5µA与1162的200nA属于不同工作方式，后者还需核对采样周期是否能捕捉应用中的最短磁事件。

## 标定与应用验证

单极开关需要匹配磁体极性与敏感方向，动作点和释放点组成磁滞窗口。验收应同时测靠近、离开和温度变化，避免只用一块强磁铁证明会翻转，却没有确定实际安装公差。

## 官方资料

- [TMR1102／1148／1162 官方资料](https://www.dowaytech.com/sensor/switch_sensors.html)
