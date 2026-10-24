---
title: "SROA48"
wiki: true
wiki_type: "model"
catalog_type: "完整编码器"
catalog_form: "完整编码器"
wiki_rank: 95
seed_count: 2
lastmod: "2026-10-24"
description: "SROA48是锐鹰整体式机械多圈绝对编码器，使用机械多圈结构保存转数状态，不依赖维护电池完成其多圈位置表达。"
official_url: "https://www.reagles.cn/"
related_companies: ["锐鹰"]
datasheet_url: "https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf"
datasheet_label: "官方数据手册"
wiki_category: "机械多圈位置保持"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/sroa48-product.png"
product_image_caption: "SROA48 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 多圈结构 | 整体式机械多圈，无需计圈电池 |
| 单圈分辨率 | 23／25 位版本 |
| 多圈分辨率 | 12 位 |
| 通信选项 | RS485、BiSS-C，依订货码 |

参数依据：[原厂产品页或对应资料](https://www.reagles.cn/)。

## 产品功能与测量链

SROA48将机械多圈结构与单圈角度检测组合，通过机械状态保留转数，因此不需要维护计圈电池。它仍需正常供电才能通过电子接口输出位置。

## 接入与配置

单圈23/25位与多圈12位属于不同字段，机械多圈范围也不是无限。控制器需定义越界与跨范围回绕行为，避免长行程运动时软件把回绕当成真实反转。

## 使用与验证

整体式外壳减少了分体安装步骤，但轴连接、联轴器、轴向力和径向力仍影响使用。选RS485或BiSS-C时核对订货码，不能因为位宽相同就认为协议可替换。

## 官方资料

- [SROA48 原厂资料入口](https://www.reagles.cn/)
- [SROA48 数据手册（官方 PDF）](https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf)
