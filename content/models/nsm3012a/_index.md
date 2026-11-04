---
title: NSM3012A
wiki: true
wiki_type: model
model_card: true
wiki_rank: 414
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3012A是Hall角度A成员，提供DSPR、Q0SPR、Q1SPR及QSPR等配置，各版本的温区、接口与资格分别定义。
official_url: https://www.novosns.com/product/NSM3012A-DSPR
related_companies:
- 纳芯微
search_aliases:
- NSM3012A
- NSM3012A-DSPR
- NSM3012A-Q0SPR
- NSM3012A-Q1SPR
- NSM3012A-QSPR
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

以下为官网目录中 **NSM3012A-DSPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器、汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Industrial |
| 数字接口 | 3-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 11~14bit；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <10,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 10μs~120μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 相同前缀下先分资格版本

本组同时出现在工业与汽车目录，而且汽车订货尾部不止一种。公开代表说明不足以解释Q0、Q1和QSPR的全部差异，任何温区和可靠性结论都必须回到完整订货号与对应文件。

## 可编程曲线要匹配被测机构

系列说明中的分段拟合可以调整角度到输出的映射，但各预设的节点定义与误差条件应分别核对。应先固定机构有效行程和接收器量程，再对点间误差和回程进行验证。

## 状态诊断与测量有效性分开

系列介绍有异常诊断及磁场相关功能，应核对本完整版本如何给出状态、主控如何识别无效读数，以及故障时输出如何表示；不要只接角度数据而忽略状态路径。

## 订货版本之间的差别

### 等级

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Industrial | NSM3012A-DSPR |
| Automotive | NSM3012A-Q0SPR、NSM3012A-Q1SPR、NSM3012A-QSPR |

### category

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 工业编码器 | NSM3012A-DSPR |
| 汽车角度传感器 | NSM3012A-Q0SPR、NSM3012A-Q1SPR、NSM3012A-QSPR |

### PWM输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 11~14bit | NSM3012A-DSPR |
| Yes | NSM3012A-Q0SPR、NSM3012A-Q1SPR、NSM3012A-QSPR |

### UVW增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| - | NSM3012A-DSPR |
| No | NSM3012A-Q0SPR、NSM3012A-Q1SPR、NSM3012A-QSPR |

### ABZ增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| - | NSM3012A-DSPR |
| No | NSM3012A-Q0SPR、NSM3012A-Q1SPR、NSM3012A-QSPR |

## 型号与资格版本

完整订货号中的Q0、Q1、IND、STD等字符区分资格或配置；温区、封装与输出功能按订货表对应行选择。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3012A-DSPR](https://www.novosns.com/product/NSM3012A-DSPR) | SOP8；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3012A-Q0SPR](https://www.novosns.com/product/NSM3012A-Q0SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3012A-Q1SPR](https://www.novosns.com/product/NSM3012A-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3012A-QSPR](https://www.novosns.com/product/NSM3012A-QSPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 版本与适用条件

NSM成员的完整资格与配置由订货号定义，型号前缀相同不表示各后缀规格相同。

工业和汽车版本分别使用对应完整订货号、资格文件和手册条件。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3012A-DSPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
