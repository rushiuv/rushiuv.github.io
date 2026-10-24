---
title: "iC-TW29"
wiki: true
wiki_type: "model"
catalog_type: "信号处理"
catalog_form: "芯片"
wiki_rank: 81
seed_count: 2
lastmod: "2026-10-24"
description: "iC-TW29是iC-Haus用于正余弦编码器信号的细分与处理芯片。"
official_url: "https://www.ichaus.de/product/ic-tw29/"
related_companies: ["iC-Haus"]
datasheet_url: "https://www.ichaus.de/product/ic-tw29/"
datasheet_label: "官网文档入口"
wiki_category: "正余弦信号细分"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/ic-tw29-official.png"
product_image_caption: "iC-TW29 原厂产品／封装图"
product_image_source: "https://www.ichaus.de/product/ic-tw29/"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 输入 | 外部编码器的模拟正余弦信号 |
| 位置处理 | 26 位编码器处理 |
| 输出 | ABZ、UVW、BiSS，分辨率可独立配置 |
| 多圈 | 可接外部圈数信息 |

参数依据：[原厂产品页或对应资料](https://www.ichaus.de/product/ic-tw29/)。

## 产品功能与测量链

iC-TW29接收外部正余弦信号并处理位置，26位描述其编码器处理能力。它不包含外部磁环、光学码盘或相应敏感读头。

## 接入与配置

先按输入幅度、共模、差分结构及频率核对前端，再配置ABZ、UVW和BiSS输出。输入周期数与每周期细分位数共同决定机械位置表达。

## 使用与验证

接入外部圈数时需要核对单圈跨零的同步关系。验收应同时保存原始SIN/COS、处理后的角度与输出计数，以区分前端失真、细分设置和串行传输问题。

## 官方资料

- [iC-TW29 原厂资料入口](https://www.ichaus.de/product/ic-tw29/)
- [官网文档入口（官方入口）](https://www.ichaus.de/product/ic-tw29/)

iC-TW29 完整规格下载可能需登录及原厂授权，产品页保留公开入口。
