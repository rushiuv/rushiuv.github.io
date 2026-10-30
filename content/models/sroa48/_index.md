---
title: SROA48系列
wiki: true
wiki_type: model
catalog_type: 完整编码器
catalog_form: 完整编码器
wiki_rank: 95
seed_count: 2
lastmod: '2026-10-30'
description: SROA48是锐鹰整体式机械多圈绝对编码器，使用机械多圈结构保存转数状态，不依赖维护电池完成其多圈位置表达。
official_url: https://www.reagles.cn/
related_companies:
- 锐鹰
datasheet_url: https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf
datasheet_label: 官方数据手册
wiki_category: 机械多圈位置保持
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
product_image: /images/wiki/sroa48-product.png
product_image_caption: SROA48 原厂手册产品／安装图（PDF 第 1 页）
product_image_source: https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf
catalog_level: 系列
search_aliases:
- SROA48系列
---

SROA48是整体式机械多圈编码器系列。单圈23位与25位是不同配置，多圈12位及通信后缀需要分别落实到订货码。

## 型号与核心异同

| 配置（非完整料号） | 单圈 | 多圈 | 通信选择 |
| --- | --- | --- | --- |
| 23位单圈配置 | 23位 | 12位 | RS485或BiSS-C，按订货码 |
| 25位单圈配置 | 25位 | 12位 | RS485或BiSS-C，按订货码 |

## 共同条件与参数依据

- **多圈结构**：整体式机械多圈，无需计圈电池

## 接口与安装

单圈23/25位与多圈12位属于不同字段，机械多圈范围也不是无限。控制器需定义越界与跨范围回绕行为，避免长行程运动时软件把回绕当成真实反转。

## 动态与装配验证

整体式外壳减少了分体安装步骤，但轴连接、联轴器、轴向力和径向力仍影响使用。选RS485或BiSS-C时核对订货码，不能因为位宽相同就认为协议可替换。

## 官方资料

- [SROA48 原厂资料入口](https://www.reagles.cn/)
- [SROA48 数据手册（官方 PDF）](https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf)
