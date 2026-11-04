---
title: MAQ8xx系列
description: 带磁性按压检测的8位角度器件组，三款输出选择不同。
wiki: true
wiki_type: model
wiki_rank: 224
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- MPS
wiki_category: 数字角度
catalog_vendor: MPS
catalog_type: 数字角度
catalog_form: 芯片
search_aliases:
- MAQ800
- MAQ820
- MAQ850
- MAQ8xx系列
official_url: https://www.monolithicpower.com/en/maq800.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

MAQ8xx面向旋钮角度与磁性按压检测。三款共同提供8位角度与按压功能，输出组合随型号选择。

## 型号与核心异同

| 具体型号 | 共同功能 | 区别／选型重点 |
| --- | --- | --- |
| MAQ800 | 8位角度与按压检测 | 基础成员，接口细节按其原厂页 |
| MAQ820 | 8位角度与按压检测 | 带ABZ输出 |
| MAQ850 | 8位角度与按压检测 | 带PWM输出 |

## 共同条件与参数依据

- **车规**：官方标注AEC-Q100；不等于整机安全认证

## 接入电路与配置

MAQ820增加ABZ，MAQ850提供PWM，选择时按主控需要确定成员。三款功能不能相加后写成每颗都具备；同一系列的封装与可用引脚也需分别核对。

## 标定与应用验证

旋转时磁体气隙变化会影响按压阈值，按下时也会改变角度噪声。应组合测试旋转、按压与倾斜，核对误触发、阈值回差和温度影响；器件车规资格不能代替整机交互与安全验收。

## 官方资料

- [MAQ800／820／850系列 官方资料](https://www.monolithicpower.com/en/maq800.html)
- [官方补充资料1](https://www.monolithicpower.com/en/maq820.html)
- [官方补充资料2](https://www.monolithicpower.com/en/maq850.html)
