---
title: AEDR-850x系列
wiki: true
wiki_type: model
catalog_type: 光学编码
catalog_form: 芯片
wiki_rank: 110
seed_count: 1
lastmod: '2026-10-30'
description: AEDR-850x是Broadcom反射式光学增量编码器系列，将LED和光检测电路集成在同一小型封装，并提供正交及索引输出。
official_url: https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102
related_companies:
- Broadcom
wiki_category: 光学读头与码盘
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
product_image: /images/wiki/aedr-850x-official.jpg
product_image_caption: AEDR-8500 原厂产品图；AEDR-850x 系列代表成员
product_image_source: https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102
catalog_level: 系列
search_aliases:
- AEDR-850x系列
---

AEDR-850x是集成LED与光检测的反射式增量读头系列。当前资料入口对应AEDR-8500-102，其它完整后缀尚未逐项核实，不从通配系列名补造型号。

## 型号与核心异同

| 已确认资料入口型号 | 共同测量链 | 选件需核对 |
| --- | --- | --- |
| AEDR-8500-102 | 外部反射码盘／码尺 → 读头 → 正交与索引输出 | 线距、插值、LED驱动及安装间隙 |

## 共同条件与参数依据

- **感知结构**：集成 LED 与光检测电路的反射式光学读头
- **输出**：A/B 正交信号及第三路索引
- **配套**：反射码盘或码尺
- **系列选件**：分辨率与插值倍率随完整型号变化

## 接口与安装

码盘线距、反射层和读头几何必须与具体后缀匹配。电气插值增加输出计数，不会消除码盘偏心、安装倾斜和表面污染造成的周期误差。

## 动态与装配验证

验证时分别检查A/B相位、占空比、索引位置及最高速度下的边沿质量。分辨率、LED驱动和允许间隙需按完整型号确认，不能用850x系列名直接下单。

## 官方资料

- [AEDR-850x 原厂资料入口](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102)
