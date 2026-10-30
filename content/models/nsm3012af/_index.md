---
title: NSM3012AF
wiki: true
wiki_type: model
model_card: true
wiki_rank: 431
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3012AF 是汽车Hall角度AF成员的检索分组，收录Q0SPR与Q1SPR；完整资格尾部必须保留，不能以代表详情统一两种等级。
official_url: https://www.novosns.com/product/NSM3012AF-Q0SPR
related_companies:
- 纳芯微
search_aliases:
- NSM3012AF
- NSM3012AF-Q0SPR
- NSM3012AF-Q1SPR
- NSM301x-Q
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
---

## 核心参数与配置

以下为官网目录中 **NSM3012AF-Q0SPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Automotive |
| PWM输出 | Yes；官网目录标注，适用于上述订货配置 |
| Digital Interface | SPI；官网目录标注，适用于上述订货配置 |
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

## Q0与Q1不能靠共享摘要合并

两种OPN在目录有各自条目，而代表详情复用系列文字。本页仅保留实际记录，不从Q0/Q1字符自行推导完整温区或认证结论，正式选型需核对各自资格与手册版本。

## SPI数据与输出曲线分别验证

目录列SPI与PWM及模拟曲线编程，主控要区分角度数据读取、输出参数配置和运行状态。先固定最终使用通道，再验证上电加载、断电保存及角度到输出的比例。

## 三点目录与四段系列说明不拼接

目录三点编程与系列详情四段拟合不是同一字段，尚不能证明AF版本具备两者全部能力。以实际寄存器和所选预设为依据，避免把共享文案变成额外功能。

## 型号与资格版本

本页按核心前缀提供检索入口。Q0、Q1、IND、STD及其他配置串保留在完整订货号中，不能把某一行的车规等级、封装或输出推广到整个分组。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3012AF-Q0SPR](https://www.novosns.com/product/NSM3012AF-Q0SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3012AF-Q1SPR](https://www.novosns.com/product/NSM3012AF-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 资料边界

model仅作检索分组键；本文不删除NSM完整订货号中的Q0/Q1/IND/STD资格或配置部分。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3012AF-Q0SPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
