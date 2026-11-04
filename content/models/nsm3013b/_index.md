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
description: NSM3013B是Hall角度B成员，目录列UVW和PWM输出，工业与汽车版本采用各自完整订货配置。
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

A/B成员的差异应查具体选型定义；工业目录未列连续串行读角协议。驱动开发应先核对B成员的通信与配置方式，不能仅因同系列有SPI字样就复用其他成员寄存器。

## 工业与汽车版本

DSPR与Q1SPR的资格和应用条件按完整后缀分别定义；系列图片与公共特性不足以确定每个B成员版本的全部规格。

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

完整订货号中的Q0、Q1、IND、STD等字符区分资格或配置；温区、封装与输出功能按订货表对应行选择。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3013B-DSPR](https://www.novosns.com/product/NSM3013B-DSPR) | SOP8；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3013B-Q1SPR](https://www.novosns.com/product/NSM3013B-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 版本与适用条件

NSM成员的完整资格与配置由订货号定义，型号前缀相同不表示各后缀规格相同。

工业和汽车版本分别使用对应完整订货号、资格文件和手册条件。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3013B-DSPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
