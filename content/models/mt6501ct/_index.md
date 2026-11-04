---
title: MT6501CT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 420
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6501CT 是MT6501汽车AMR角度系列的SOP8成员，输出侧重模拟曲线、PWM与SPI；不提供目录未列的ABZ或UVW路径。
official_url: https://www.novosns.com/product/MT6501CT-AAV-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6501
- MT6501CT
- MT6501CT-AAV-R
- MT6501CT-ABD-R
- MT6501CT-ACD-R
- MT6501CT-ADD-R
- MT6501CT-ADV-R
- MT6501CT-AED-R
- MT6501CT-AFD-R
- MT6501CT-AGD-R
- MT6501CT-AHD-R
- MT6501CT-AHV-R
- MT6501CT-AJD-R
- MT6501CT-AKD-R
- MT6501CT-ALD-R
- MT6501CT-AMD-R
- MT6501CT-AND-R
- MT6501CT-AOD-R
- MT6501CT-APD-R
- MT6501CT-P1K-R
- MT6501CT-P1KA-R
- MT6501CT-P1KB-R
- MT6501CT-P1KC-R
- MT6501CT-P250-R
- MT6501CT-P250V-R
- MT6501CT-P500-R
- MT6501CT-PAD-R
- MT6501CT-PBD-R
- MT6501CT-PBF-R
- MT6501CT-PJ1-R
- MT6501CT-PJ2-R
- MT6501CT-PJ3-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
---

## 核心参数与配置

以下为官网目录中 **MT6501CT-AAV-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Automotive |
| PWM输出 | Yes；官网目录标注，适用于上述订货配置 |
| Digital Interface | SPI；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | No；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | No；官网目录标注，适用于上述订货配置 |
| Angle Accuracy | <±1.5°；官网目录标注，适用于上述订货配置 |
| Analog Output Curve Programming | Any 4-point Programming；官网目录标注，适用于上述订货配置 |
| Redundant Package Option | Yes；官网目录标注，适用于上述订货配置 |
| Output Overvoltage Protection | 18V；官网目录标注，适用于上述订货配置 |
| ISO26262 | No；官网目录标注，适用于上述订货配置 |
| Automotive Qualification | Yes；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~150；官网目录标注，适用于上述订货配置 |
| 目录供电 | 4.5~5.5；官网目录标注，适用于上述订货配置 |
| Magnetic Sensing Principle | AMR；官网目录标注，适用于上述订货配置 |

## 模拟曲线先适配机构量程

目录列任意四点曲线编程，可用于把角度范围映射到接收器要求的电压或PWM范围。应明确端点、有效区和故障区，并独立验证点间行为，不能把曲线编程理解成整个机构已完成精度校准。

## 小封装与冗余选项不能混成一个料号

目录有冗余封装选项字段，但CT成员采用SOP8；双芯结构、独立供电或诊断能力必须看完整订货资料。两路相似输出也不能自动认定为功能安全冗余。

## 模拟读数与SPI配置分开验收

主控若运行中采样模拟电压、调试时使用SPI，应分别检查ADC参考和串行状态。官网对部分CT预设不推荐新设计，采购时以完整OPN为准，不把共用品名MT6501当作单一固定配置。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Not Recomended for New Designs | MT6501CT-AAV-R、MT6501CT-ABD-R、MT6501CT-AKD-R、MT6501CT-PBD-R |
| Active | MT6501CT-ACD-R、MT6501CT-ADD-R、MT6501CT-ADV-R、MT6501CT-AED-R、MT6501CT-AFD-R、MT6501CT-AGD-R、MT6501CT-AHD-R、MT6501CT-AHV-R、MT6501CT-AJD-R、MT6501CT-ALD-R、MT6501CT-AMD-R、MT6501CT-AND-R、MT6501CT-AOD-R、MT6501CT-APD-R、MT6501CT-P1K-R、MT6501CT-P1KA-R、MT6501CT-P1KB-R、MT6501CT-P1KC-R、MT6501CT-P250-R、MT6501CT-P250V-R、MT6501CT-P500-R、MT6501CT-PAD-R、MT6501CT-PBF-R、MT6501CT-PJ1-R、MT6501CT-PJ2-R、MT6501CT-PJ3-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6501CT-AAV-R](https://www.novosns.com/product/MT6501CT-AAV-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-ABD-R](https://www.novosns.com/product/MT6501CT-ABD-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-ACD-R](https://www.novosns.com/product/MT6501CT-ACD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-ADD-R](https://www.novosns.com/product/MT6501CT-ADD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-ADV-R](https://www.novosns.com/product/MT6501CT-ADV-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AED-R](https://www.novosns.com/product/MT6501CT-AED-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AFD-R](https://www.novosns.com/product/MT6501CT-AFD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AGD-R](https://www.novosns.com/product/MT6501CT-AGD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AHD-R](https://www.novosns.com/product/MT6501CT-AHD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AHV-R](https://www.novosns.com/product/MT6501CT-AHV-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AJD-R](https://www.novosns.com/product/MT6501CT-AJD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AKD-R](https://www.novosns.com/product/MT6501CT-AKD-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-ALD-R](https://www.novosns.com/product/MT6501CT-ALD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AMD-R](https://www.novosns.com/product/MT6501CT-AMD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AND-R](https://www.novosns.com/product/MT6501CT-AND-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-AOD-R](https://www.novosns.com/product/MT6501CT-AOD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-APD-R](https://www.novosns.com/product/MT6501CT-APD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P1K-R](https://www.novosns.com/product/MT6501CT-P1K-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P1KA-R](https://www.novosns.com/product/MT6501CT-P1KA-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P1KB-R](https://www.novosns.com/product/MT6501CT-P1KB-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P1KC-R](https://www.novosns.com/product/MT6501CT-P1KC-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P250-R](https://www.novosns.com/product/MT6501CT-P250-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P250V-R](https://www.novosns.com/product/MT6501CT-P250V-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-P500-R](https://www.novosns.com/product/MT6501CT-P500-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-PAD-R](https://www.novosns.com/product/MT6501CT-PAD-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-PBD-R](https://www.novosns.com/product/MT6501CT-PBD-R) | SOP8；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-PBF-R](https://www.novosns.com/product/MT6501CT-PBF-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-PJ1-R](https://www.novosns.com/product/MT6501CT-PJ1-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-PJ2-R](https://www.novosns.com/product/MT6501CT-PJ2-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501CT-PJ3-R](https://www.novosns.com/product/MT6501CT-PJ3-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |

“Not Recommended for New Designs”表示该完整订货号不推荐用于新设计，不代表全部预设停产。请结合表内仍为Active的版本核对供应与配置。

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

同型号不同预设的生命周期可能不同，供货与新设计适用性按具体OPN查询。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6501CT-AAV-R)
- [DatasheetCN)MT6501_Rev.1.9.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf)
- [MT6501_Rev.1.9.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
