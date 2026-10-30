---
title: WIN48系列
wiki: true
wiki_type: model
catalog_type: 完整编码器
catalog_form: 完整编码器
wiki_rank: 148
seed_count: 1
lastmod: '2026-10-30'
description: WIN48是锐鹰分体式机械多圈绝对编码器系列，强调薄型结构和无电池多圈位置保持，用于精密运动反馈。
official_url: https://www.reagles.cn/
related_companies:
- 锐鹰
datasheet_url: https://www.reagles.cn/uploads/Download/20240723/092834205ac8885.pdf
datasheet_label: 官方数据手册
wiki_category: 机械多圈位置保持
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
product_image: /images/wiki/win48-product.png
product_image_caption: WIN48 原厂手册产品／安装图（PDF 第 1 页）
product_image_source: https://www.reagles.cn/uploads/Download/20240723/092834205ac8885.pdf
catalog_level: 系列
search_aliases:
- WIN48系列
---

WIN48采用分体式机械多圈结构。当前收录手册对应G12S17配置，尺寸与位数只在这一版本范围内使用。

## 型号与核心异同

| 已确认配置（非完整订货号） | 单圈／多圈 | 外形条件 | 未展开的差异 |
| --- | --- | --- | --- |
| WIN48 G12S17 | 17位／12位 | 直径48.2mm、高15.5mm，按该尺寸图 | 通信及完整订货后缀 |
| 其他WIN48配置 | 按对应版本 | 不沿用G12S17尺寸 | 尚未逐项取得成员资料 |

## 共同条件与参数依据

- **结构**：分体式机械多圈，无计圈电池

## 接口与安装

本页所附G12S17版本为12位多圈与17位单圈，不能把其他WIN48变体的单圈码宽或通信配置直接套入。直径48.2mm、高15.5mm同样限于该尺寸图。

## 动态与装配验证

验证应包含无电源正反转、重新上电读取、多圈回绕和机械零点保持。机械多圈免电池维护，不意味着无需检查磨损、冲击和安装应力；接口线序与控制器协议仍需逐版确认。

## 官方资料

- [WIN48 原厂资料入口](https://www.reagles.cn/)
- [WIN48 数据手册（官方 PDF）](https://www.reagles.cn/uploads/Download/20240723/092834205ac8885.pdf)

此处尺寸和位数来自 WIN48 的 17 位版本手册，未混用其他 23 位版本参数。
