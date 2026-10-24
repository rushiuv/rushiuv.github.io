---
title: "MA900"
description: "差分磁场架构的角度芯片，主打杂散磁场抑制；官网当前标为Pre-Release。"
wiki: true
wiki_type: "model"
wiki_rank: 225
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA900"]
official_url: "https://www.monolithicpower.com/en/products/sensors/ma900.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
product_status: "Pre-Release"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 产品状态 | Pre-Release，不能据此认定已量产或稳定供货 |
| 输出 | SPI或I²C、ABZ、UVW，按配置 |
| 供电／封装 | 3.3V／5V；QFN-16 |
| 噪声口径 | ±0.02° RMS@3kHz是噪声项目，不能当绝对精度 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/products/sensors/ma900.html)。

## 工作方式与型号定位

MA900采用差分磁场测量架构，定位于存在杂散场的位置检测。差分抑制针对特定空间场分布，不能据此推导对任意近场磁体或铁磁结构都免疫。

## 安装、接口与配置

官方页面标注Pre-Release，设计采用前应确认正式规格、样品与交付状态。SPI或I²C、ABZ及UVW是可选输出，实际组合需要按订货及引脚配置确定。

## 校准与选型验证

±0.02°RMS@3kHz属于噪声口径，不能写成绝对准确度。验证应分别施加规定外场和安装偏差，记录误差随角度、频率及温度的变化；正式手册未给出的保证范围不由发布前产品摘要补出。

## 官方资料

- [MA900 官方资料](https://www.monolithicpower.com/en/products/sensors/ma900.html)
