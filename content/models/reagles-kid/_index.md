---
title: KID系列
description: 异侧中空双编码器，集成双读头并通过单接口传输两路位置。
wiki: true
wiki_type: model
wiki_rank: 258
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 锐鹰
wiki_category: 旋转编码模块
catalog_vendor: 锐鹰
catalog_type: 旋转编码模块
catalog_form: 编码模块
search_aliases:
- KID
- KID系列
official_url: https://www.reagles.cn/index/product_detail/content/10159.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

锐鹰KID是异侧双编码器模块，用一个通信接口传送关节两端位置。当前公开表未展开完整订货成员，以下按两端测量通道比较，不将通道名当型号。

## 型号与核心异同

| 通道（非独立型号） | 输出码宽 | 技术表重复定位 | 共同接口 |
| --- | --- | --- | --- |
| 电机端 | 23bit；有效分辨率另列>17bit | ≤±10角秒 | RS485，2.5Mbps |
| 减速机端 | 23bit；有效分辨率另列>17bit | ≤±8角秒 | 同一通信接口 |

## 共同条件与参数依据

- **最高主轴转速**：≤6000rpm，官网技术表
- **工作温度**：−20～105°C

## 接口与安装

23bit是输出码宽，官网同时列有效分辨率大于17bit。电机端≤±10角秒、减速机端≤±8角秒是重复定位项目，不应改写成两端绝对精度或扭矩精度。

## 动态与装配验证

装配时应分别记录两端机械零点、方向和减速比。用角差估算弹性扭转时，还需辨识回差、摩擦和结构刚度；接口共用也不能据此认定已提供同步扭矩输出。

## 官方资料

- [锐鹰KID系列 官方资料](https://www.reagles.cn/index/product_detail/content/10159.html)
