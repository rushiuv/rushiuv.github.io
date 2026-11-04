---
title: NSM3013A
wiki: true
wiki_type: model
model_card: true
wiki_rank: 417
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3013A是带UVW目录路径的Hall角度成员，包含DSPR和Q1SPR配置，换向功能与资格按完整版本确认。
official_url: https://www.novosns.com/product/NSM3013A-DSPR
related_companies:
- 纳芯微
search_aliases:
- NSM3013A
- NSM3013A-DSPR
- NSM3013A-Q1SPR
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

以下为官网目录中 **NSM3013A-DSPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

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

## UVW表达电机电角关系

工业目录为本组列出可编程极对关系，UVW用于换向相序，不等同于ABZ位置计数。接电机时必须确认极对数、方向和机械零点到电角零点的偏置。

## 数据接口空白不能用系列总述补齐

代表工业目录Output Interface字段为横线，而系列摘要泛述SPI/OWI。应区分配置入口与运行角度数据路径，在协议得到确认前不为本成员补造连续SPI读取能力。

## Q1版本的换向配置

DSPR和Q1SPR分别属于工业与汽车版本，目录对UVW字段的表示方式不同；可编程范围、资格及性能应按所选订货行和对应手册使用。

## 订货版本之间的差别

### 等级

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Industrial | NSM3013A-DSPR |
| Automotive | NSM3013A-Q1SPR |

### category

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 工业编码器 | NSM3013A-DSPR |
| 汽车角度传感器 | NSM3013A-Q1SPR |

### PWM输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 11~14bit | NSM3013A-DSPR |
| Yes | NSM3013A-Q1SPR |

### UVW增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 1~8pole pairs programmable | NSM3013A-DSPR |
| Yes | NSM3013A-Q1SPR |

### ABZ增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| - | NSM3013A-DSPR |
| No | NSM3013A-Q1SPR |

## 型号与资格版本

完整订货号中的Q0、Q1、IND、STD等字符区分资格或配置；温区、封装与输出功能按订货表对应行选择。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3013A-DSPR](https://www.novosns.com/product/NSM3013A-DSPR) | SOP8；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3013A-Q1SPR](https://www.novosns.com/product/NSM3013A-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 版本与适用条件

NSM成员的完整资格与配置由订货号定义，型号前缀相同不表示各后缀规格相同。

工业和汽车版本分别使用对应完整订货号、资格文件和手册条件。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3013A-DSPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
