---
title: MT6511CT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 422
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6511CT 是SOP8封装的差分Hall汽车角度器件，目录列SPI/SENT、模拟曲线与多类位置输出；先按完整预设选择系统真正使用的通道。
official_url: https://www.novosns.com/product/MT6511CT-AED-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6511
- MT6511CT
- MT6511CT-AED-R
- MT6511CT-PMP-R
- MT6511CT-SPH-R
- MT6511CT-SPI-R
- MT6511CT-SPICH-R
- MT6511CT-STD-R
- MT6511CT-STP-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
---

## 核心参数与配置

以下为官网目录中 **MT6511CT-AED-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | SOP8 |
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

## SENT与SPI面向不同接收链

SPI通常由主控发起读取，SENT需要接收器按其编码和状态字段解析。应根据线缆、主控外设及诊断要求选择接口，再核对所选CT预设；目录把接口并列不证明全部信号可同时启用。

## 多点映射与传感非线性不同

官网列任意多点或等分分段输出曲线编程。它可以把机构角度映射到指定传递函数，仍需验证噪声、迟滞与全温误差，不将输出曲线节点数直接换算成准确度。

## SOP8约束输出组合

目录列ABZ、UVW等系列能力，实际可引出的组合受八脚封装及预设限制。应先确定接收器需要连续角度、位置脉冲还是换向相，再逐脚核对；功能安全标签还需正式资料支撑。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6511CT-AED-R](https://www.novosns.com/product/MT6511CT-AED-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511CT-PMP-R](https://www.novosns.com/product/MT6511CT-PMP-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511CT-SPH-R](https://www.novosns.com/product/MT6511CT-SPH-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511CT-SPI-R](https://www.novosns.com/product/MT6511CT-SPI-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511CT-SPICH-R](https://www.novosns.com/product/MT6511CT-SPICH-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511CT-STD-R](https://www.novosns.com/product/MT6511CT-STD-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |
| [MT6511CT-STP-R](https://www.novosns.com/product/MT6511CT-STP-R) | SOP8；Automotive；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6511CT-AED-R)
- [MT6511_Datasheet_Rev.1.3.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Os0abZrRvoUzKpx8NrfcmuWJnOd.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
