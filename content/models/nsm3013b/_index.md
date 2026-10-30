---
title: NSM3013B
wiki: true
wiki_type: model
model_card: true
wiki_rank: 418
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3013B 是Hall角度B成员分组，目录涉及UVW与PWM路径，完整DSPR/Q1SPR版本分别对应工业和汽车选择。
official_url: https://www.novosns.com/product/NSM3013B-DSPR
related_companies:
- 纳芯微
search_aliases:
- NSM3013B
- NSM3013B-DSPR
- NSM3013B-Q1SPR
- NSM301x
- NSM301x-Q
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
series_parent: nsm301x
---

## 核心参数与配置

以下为官网目录中 **NSM3013B-DSPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器、汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Industrial |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 11~14bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~8pole pairs programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <10,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 10μs~120μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## PWM位置与UVW换向使用不同标定

PWM用于表示位置量，UVW用于换向相位。控制器同时使用时，需要统一方向和零点，分别检查PWM比例与换向相序，不能认为两条输出天然使用相同机械参考。

## B成员功能需由具体协议确认

本次公开摘要未展开A/B的全部差异，代表工业数据接口字段也未列连续读角协议。驱动开发应先核对B成员的通信与配置方式，不能仅因同系列有SPI字样就复用其他成员寄存器。

## 汽车与工业条件分表保留

DSPR与Q1SPR虽然共享分组检索入口，资格和应用条件仍按完整后缀。已有系列图片和公共特性不作为B成员每个版本均已独立验证的证据。

## 订货版本之间的差别

### 等级

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Industrial | NSM3013B-DSPR |
| Automotive | NSM3013B-Q1SPR |

### category

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 工业编码器 | NSM3013B-DSPR |
| 汽车角度传感器 | NSM3013B-Q1SPR |

### PWM输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 11~14bit | NSM3013B-DSPR |
| Yes | NSM3013B-Q1SPR |

### UVW增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 1~8pole pairs programmable | NSM3013B-DSPR |
| Yes | NSM3013B-Q1SPR |

### ABZ增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| - | NSM3013B-DSPR |
| No | NSM3013B-Q1SPR |

## 型号与资格版本

本页按核心前缀提供检索入口。Q0、Q1、IND、STD及其他配置串保留在完整订货号中，不能把某一行的车规等级、封装或输出推广到整个分组。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3013B-DSPR](https://www.novosns.com/product/NSM3013B-DSPR) | SOP8；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3013B-Q1SPR](https://www.novosns.com/product/NSM3013B-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 资料边界

model仅作检索分组键；本文不删除NSM完整订货号中的Q0/Q1/IND/STD资格或配置部分。

同一归一型号跨工业与汽车目录；需按完整订货号核对Q0/Q1/工业等级与所用手册，不能把代表工业详情扩展为所有车规配置。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3013B-DSPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
