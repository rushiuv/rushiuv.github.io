---
title: NSM3011AD
wiki: true
wiki_type: model
model_card: true
wiki_rank: 430
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3011AD-Q1SPR是汽车Hall角度成员，目录列PWM及输出曲线编程，接口与资格适用该完整型号。
official_url: https://www.novosns.com/product/NSM3011AD-Q1SPR
related_companies:
- 纳芯微
search_aliases:
- NSM3011AD
- NSM3011AD-Q1SPR
- NSM301x-Q
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
---

## 核心参数与配置

以下为官网目录中 **NSM3011AD-Q1SPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Automotive |
| PWM输出 | Yes；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | No；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | No；官网目录标注，适用于上述订货配置 |
| Angle Accuracy | <±1.0°；官网目录标注，适用于上述订货配置 |
| Analog Output Curve Programming | Any 3-point Programming；官网目录标注，适用于上述订货配置 |
| Output Overvoltage Protection | 6.5V；官网目录标注，适用于上述订货配置 |
| ISO26262 | No；官网目录标注，适用于上述订货配置 |
| Automotive Qualification | Yes；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |
| Magnetic Sensing Principle | Differential hall；官网目录标注，适用于上述订货配置 |

## 先按Q1SPR的输出字段接入

本组目录列PWM，而Digital Interface字段为横线，不能直接用系列简介中的SPI/OWI给它补一个运行时SPI读角接口。配置通信是否存在、如何使用，应由本完整型号手册确认。

## 模拟曲线编程按接收器要求验证

目录列任意三点输出曲线编程，系列详情却用四段拟合表述，两种来源需要保留，不能混成同一个节点数保证。应核对实际寄存器定义，再对机构端点、点间曲线和故障区分别验收。

## Q1资格不扩展为功能安全等级

官网汽车资格与ISO26262分别列示，本组不能由车规定位推出ASIL结果。系统需要明确异常输出的识别和后续控制动作，并保存对应资格文件。

## 型号与资格版本

完整订货号中的Q0、Q1、IND、STD等字符区分资格或配置；温区、封装与输出功能按订货表对应行选择。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3011AD-Q1SPR](https://www.novosns.com/product/NSM3011AD-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 版本与适用条件

NSM成员的完整资格与配置由订货号定义，型号前缀相同不表示各后缀规格相同。

这些OPN的目录参数相同，寄存器预设、包装和其他功能仍应按完整订货号确认。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3011AD-Q1SPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
