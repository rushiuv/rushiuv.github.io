---
title: "iC-MU"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 39
seed_count: 5
lastmod: "2026-10-24"
description: "iC-MU是iC-Haus的磁性离轴绝对值编码芯片，利用两条不同周期的磁码道及游标关系获得绝对位置，同时对周期信号进行细分。"
official_url: "https://www.ichaus.de/product/ic-mu/"
related_companies: ["iC-Haus"]
datasheet_url: "https://www.ichaus.de/product/ic-mu/"
datasheet_label: "官网文档入口"
wiki_category: "双码道与绝对位置"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/ic-mu-official.png"
product_image_caption: "iC-MU128 产品图；iC-MU 系列当前入口代表成员"
product_image_source: "https://www.ichaus.de/product/ic-mu128/"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 感知方式 | 双码道磁检测与游标绝对位置解算 |
| 安装 | 离轴，需匹配双码道磁环 |
| 输出 | 绝对值及增量位置接口 |
| 当前产品入口 | iC-MU128；该成员主码道极宽 1.28 mm |

参数依据：[原厂产品页或对应资料](https://www.ichaus.de/product/ic-mu/)。

## 产品功能与测量链

iC-MU使用两条不同周期的磁码道获得离轴绝对位置，单码道细分与两码道消歧分别承担局部精度和整圈定位。磁环是测量系统的一部分。

## 接入与配置

原有iC-MU标签与当前iC-MU128入口需要区分。主码道单极宽1.28mm是该成员几何条件，不能将不同极宽成员当成只换软件的替代件。

## 使用与验证

装配需同时满足两道读头的气隙、径向位置和磁信号质量。验证既要看细分角度残差，也要查整圈码道配对是否发生跳区。

## 官方资料

- [iC-MU 原厂资料入口](https://www.ichaus.de/product/ic-mu/)
- [官网文档入口（官方入口）](https://www.ichaus.de/product/ic-mu/)

当前原厂链接跳转 iC-MU128，1.28 mm 极宽仅属于该成员；规格下载可能需要原厂授权。
