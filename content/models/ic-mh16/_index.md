---
title: "iC-MH16"
description: "集成霍尔传感阵列的12位角度编码器，兼有增量与换相输出。"
wiki: true
wiki_type: "model"
wiki_rank: 250
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["iC-Haus"]
wiki_category: "数字角度"
catalog_vendor: "iC-Haus"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["iC-MH16"]
official_url: "https://www.ichaus.de/product/ic-mh16/"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 角度细分 | 12位，4096步 |
| 输出 | ABZ、UVW、BiSS／SSI，按配置 |
| 换相 | UVW最多16对极仿真 |
| 资料边界 | 公开产品特性可查，完整规格下载可能需原厂授权 |
| 最高转速 | 公开产品摘要列200000rpm，仍需按分辨率及输出配置核对 |
| 增量边沿速率 | 最高16MHz，边沿速率不等于每相周期频率 |
| 增量电气 | RS422兼容ABZ输出 |
| 非易失配置 | ZAP存储配置，编程方式依正式手册 |
| 认证版本 | 中文官网列QFN28WF-5×5为AEC-Q100 Grade 1；不扩展到任意封装 |

参数依据：[原厂产品页或对应资料](https://www.ichauschina.com/products/enc_mag.htm)。

## 产品功能与测量链

iC-MH16把霍尔阵列、角度细分与编码输出集成在一起。12位对应4096步，ABZ、UVW和串行绝对值输出分别用于计数、换向与上电位置读取。

## 接入与配置

UVW最多16对极仿真是电机换向配置，不表示磁体必须具有16对极。配置要与真实电机极对数及机械零点一致，否则角度读数正确也会换向错误。

## 使用与验证

BiSS/SSI与增量输出应按具体工作模式核对。测试需覆盖上电首次有效数据、跨零计数、Z相及最高速度下边沿，完整电气保证值以获准使用的手册为准。

## 官方资料

- [iC-MH16 官方资料](https://www.ichaus.de/product/ic-mh16/)
- [官方补充资料1](https://www.ichauschina.com/products/enc_mag.htm)
