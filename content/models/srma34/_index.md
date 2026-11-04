---
title: SRMA34系列
description: 分体式磁电绝对编码器，公开资料包含单圈与多圈配置。
wiki: true
wiki_type: model
wiki_rank: 262
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 锐鹰
wiki_category: 旋转编码模块
catalog_vendor: 锐鹰
catalog_type: 旋转编码模块
catalog_form: 编码模块
search_aliases:
- SRMA34
- SRMA34系列
official_url: https://www.reagles.cn/index/product_detail/content/10121.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

SRMA34为分体磁电绝对值编码模块。应先区分单圈、多圈与低温成员，再核对驱动器报文及断电行为。

## 型号与核心异同

| 目录型号／配置 | 位置内容 | 温度／选型区别 |
| --- | --- | --- |
| SRMA34 单圈17bit配置 | 圈内绝对位置 | 标准系列−20～105°C |
| SRMA34 M16S17Bit配置 | 16bit多圈＋17bit单圈 | 计圈与断电行为依具体订货号 |
| SRMAE34低温成员 | 位数与协议按对应手册 | 低温款，不能沿用标准温度结论 |

## 共同条件与参数依据

- **形态**：分体磁电编码模块
- **资料版本**：官网资料中心列系列规格书V2.0；具体供电、协议依订货号
- **通信／速率**：RS485，2.5Mbps
- **电源／电流**：5V±5%；72mA典型
- **湿度／防护**：90%RH，无结露；依电机后盖防护
- **线长**：官网特性列最长50m，须满足相应线缆、供电及通信条件

## 接口与安装

RS485为物理通信形式，具体报文需与驱动器匹配。官网50m线长信息应结合供电压降、线缆、终端和EMC条件评估，不能单独保证任意现场布线均可靠。

## 动态与装配验证

标准系列温度为−20～105°C，资料中心另列低温款SRMAE34，须按完整料号选型。安装后检查跨零、方向与上电位置恢复，多圈状态的断电行为也需确认具体计圈方式。

## 官方资料

- [SRMA34系列 官方资料](https://www.reagles.cn/index/product_detail/content/10121.html)
- [官方补充资料1](https://www.reagles.cn/index/specification.html)
