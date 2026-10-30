---
title: KTM28系列
description: AMR与ASIC组合的气缸位置检测芯片，提供二线或三线开关应用路径。
wiki: true
wiki_type: model
wiki_rank: 205
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 磁开关
catalog_vendor: 昆泰芯
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- KTM2801
- KTM2802
- KTM28系列
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/hvcpDetectionSensor/index.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

KTM28面向气缸端位磁检测。两个基础成员同列AMR与调理ASIC路线，但现有目录没有完整说明NPN/PNP及二线/三线与成员的映射。

## 型号与核心异同

| 具体型号 | 共同检测任务 | 尚需落实的配置 |
| --- | --- | --- |
| KTM2801 | 全极气缸端位事件检测 | 输出接线、NPN/PNP及二线/三线版本 |
| KTM2802 | 全极气缸端位事件检测 | 输出接线、NPN/PNP及二线/三线版本 |

## 共同条件与参数依据

- **技术路线**：AMR与信号调理ASIC组合
- **供电口径**：产品介绍3～30V；选型表3～32V，正式设计按具体手册
- **平均电流**：官网目录70µA，按对应工作条件
- **工作频率**：官网目录4kHz
- **动作/释放场**：官网目录±18/±16Gs
- **输出**：开漏；NPN/PNP、二线/三线应用按成员与手册
- **温度/封装**：−40～105°C；HFBP 2×3mm-6L

## 气缸检测测的是端位事件

KTM28通过活塞磁体产生的磁场判断到位，不连续输出活塞毫米位置。磁敏元件、阈值和调理电路集成在芯片内，但外部保护、负载和接线方式仍由应用电路决定。

## NPN与PNP要看负载位置

输出类型应按具体手册电路选择：负载接在电源侧还是地侧，会改变接线和控制器输入要求。二线供电与三线独立输出也不能仅凭同系列名称互换。

## 磁门限和现场距离

±18/±16Gs来自官网选型表，不能直接转换为气缸槽内的动作距离。缸体材料、活塞磁环、安装槽和传感器方向都会改变敏感点的磁场，应使用目标气缸验证。

## 验收与电源

先收敛30V/32V供电口径，再检查输出负载和保护电路。测试往返动作点、临界抖动、最高活塞速度与电源变化；目录4kHz只是器件频率条件，不直接保证任何气缸运动轨迹都不漏检。

## 官方资料

- [KTM28系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/hvcpDetectionSensor/index.html)
