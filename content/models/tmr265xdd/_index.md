---
title: TMR265xDD系列
description: 带信号调理与温度补偿配置的TMR线性场系列，按成员区分量程。
wiki: true
wiki_type: model
wiki_rank: 232
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 多维科技
wiki_category: 线性磁场
catalog_vendor: 多维科技
catalog_type: 线性磁场
catalog_form: 芯片
search_aliases:
- TMR2651DD
- TMR2652DD
- TMR2653DD
- TMR265xDD系列
official_url: https://www.dowaytech.com/TMR2651DD-TMR-Linear-Sensors.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

TMR265xDD在磁敏桥路后集成信号调理。当前逐项参数集中在TMR2651DD，另外两款不能直接沿用其量程、频响与非线性。

## 型号与核心异同

| 具体型号 | 场强范围 | 频响 | 供电与封装 |
| --- | --- | --- | --- |
| TMR2651DD | ±1000Gs | DC～2MHz | 典型3.3V／5V；DFN6L，3 × 2 × 0.75mm |
| TMR2652DD | 成员资料待核 | 成员资料待核 | 成员资料待核 |
| TMR2653DD | 成员资料待核 | 成员资料待核 | 成员资料待核 |

## 共同条件与参数依据

- **共同方向**：经调理的磁场相关电压输出
- **可编程项目**：灵敏度、零偏、温度补偿
- **TMR2651DD敏感轴**：X轴
- **TMR2651DD非线性**：官网特性列0.5%；仅限该成员及适用条件

## 接入电路与配置

本页能直接核对的±1000Gs与DC～2MHz属于TMR2651DD，不能扩展成全系列共同性能。输出反映磁场，固定电压输出方式也要与后端参考电压安排一致。

## 标定与应用验证

高频响应用应检查模拟带宽、负载与PCB噪声，低频应用则关注零点和温漂。参数编程之后需要在正负场和温度下复测，不能用室温零点正确证明整量程线性及温补都正确。

## 官方资料

- [TMR265xDD系列 官方资料](https://www.dowaytech.com/TMR2651DD-TMR-Linear-Sensors.html)
