---
title: MT6511GT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 423
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6511GT 是差分Hall汽车角度系列的TSSOP16型号，提供SPI/SENT及模拟、PWM和增量相关路径，适合比较控制读取与诊断配置的组合。
official_url: https://www.novosns.com/product/MT6511GT-LFC-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6511
- MT6511GT
- MT6511GT-LFC-R
- MT6511GT-PMP-R
- MT6511GT-SPI-R
- MT6511GT-STD-R
- MT6511GT-STP-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/c7e90e5222cb61b2.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/ABPwbOVGbocqAPxpD51c2RJbn8b.png
---

## 核心参数与配置

以下为官网目录中 **MT6511GT-LFC-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | TSSOP16 |
| 目录等级 | Automotive |
| PWM输出 | Yes；官网目录标注，适用于上述订货配置 |
| Digital Interface | SPI，SENT；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | Yes；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | Yes；官网目录标注，适用于上述订货配置 |
| Angle Accuracy | <±1.0°；官网目录标注，适用于上述订货配置 |
| Analog Output Curve Programming | Any 8-point Programming or 17-point piece-wise-linear Programming；官网目录标注，适用于上述订货配置 |
| Redundant Package Option | Yes；官网目录标注，适用于上述订货配置 |
| Output Overvoltage Protection | 30V；官网目录标注，适用于上述订货配置 |
| ISO26262 | Yes；官网目录标注，适用于上述订货配置 |
| Automotive Qualification | Yes；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~150；官网目录标注，适用于上述订货配置 |
| 目录供电 | 4.5~5.5；官网目录标注，适用于上述订货配置 |
| Magnetic Sensing Principle | Differential hall；官网目录标注，适用于上述订货配置 |

## GT封装资源用于具体接口方案

与CT不同的封装资源需要在原理图上落实：数据、编程、模拟和换向信号各占用哪些脚，哪些功能复用，都应以GT手册确认。不能因为目录列Yes就把所有输出同时画出。

## 输出保护不等于系统瞬态验收

目录有输出过压保护字段，该字段描述器件相关条件，不能直接代替线束短接、供电瞬态和接收端保护验证。应结合负载及故障电压分别检查传感器和主控输入。

## 保留角度路径与安全文件边界

SENT状态、故障诊断、冗余封装选项和ISO26262标签分别需要实际定义与正式文件。系统应说明故障发现后采取什么动作，不能把器件标签直接写成整机ASIL结果。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6511GT-LFC-R](https://www.novosns.com/product/MT6511GT-LFC-R) | TSSOP16；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511GT-PMP-R](https://www.novosns.com/product/MT6511GT-PMP-R) | TSSOP16；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511GT-SPI-R](https://www.novosns.com/product/MT6511GT-SPI-R) | TSSOP16；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511GT-STD-R](https://www.novosns.com/product/MT6511GT-STD-R) | TSSOP16；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511GT-STP-R](https://www.novosns.com/product/MT6511GT-STP-R) | TSSOP16；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6511GT-LFC-R)
- [MT6511_Datasheet_Rev.1.3.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
