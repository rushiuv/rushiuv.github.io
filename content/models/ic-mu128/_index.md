---
title: "iC-MU128"
description: "双磁道离轴绝对位置器件，需配套主磁道与游标磁道。"
wiki: true
wiki_type: "model"
wiki_rank: 253
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["iC-Haus"]
wiki_category: "数字角度"
catalog_vendor: "iC-Haus"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["iC-MU128"]
official_url: "https://www.ichaus.de/product/ic-mu128/"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 磁栅几何 | 主磁道单极宽1.28mm |
| 结构 | 集成双磁道霍尔扫描 |
| 信号调理 | 偏置、幅值和相位校正 |
| 资料边界 | 原厂英文页的完整手册需申请；中文公开产品摘要补充下列编码与输出选项 |
| 局部细分 | 实时12bit、滤波14bit，公开中文产品摘要 |
| 绝对位置位数 | 16/32/64主磁道极对对应最高18/19/20bit，依磁环与配置 |
| 接口 | SPI、BiSS、SSI；ABZ；UVW，按配置及引脚复用 |
| ABZ可编程范围 | FlexCount 1～65536 CPR；计数口径按手册，勿直接当四倍频步数 |
| UVW | 电机1～16对极可配置 |
| 配置加载 | 外部EEPROM，多主I²C接口 |

参数依据：[原厂产品页或对应资料](https://www.ichauschina.com/products/enc_mag.htm)。

## 产品功能与测量链

iC-MU128需要主磁道与游标磁道配套，主磁道单极宽1.28mm约束读头与磁环的几何匹配。它适用于需要中空空间的离轴布局。

## 接入与配置

偏置、幅值和相位校正针对信号链中的相应误差，不能直接替代整圈磁化误差验收。两道都应在全圈维持有效信号。

## 使用与验证

配套磁环的极数、两道关系及允许气隙应依原厂方案确认。完整手册需授权时，本页仅使用公开产品摘要列明的编码与接口能力，不补未经核对的绝对精度、磁场或最高速度保证值。

## 官方资料

- [iC-MU128 官方资料](https://www.ichaus.de/product/ic-mu128/)
- [官方补充资料1](https://www.ichauschina.com/products/enc_mag.htm)
