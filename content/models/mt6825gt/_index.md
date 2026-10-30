---
title: MT6825GT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 406
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6825GT 是TSSOP16封装的AMR角度编码器，目录列18位核心角度和可编程增量输出；其与后续MT6835成员应按接口与配置分别比较。
official_url: https://www.novosns.com/product/MT6825GT-A1D-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6825
- MT6825GT
- MT6825GT-A1D-R
- MT6825GT-A1T-R
- MT6825GT-A360-R
- MT6825GT-C1T-R
- MT6825GT-C4D-R
- MT6825GT-CDD-R
- MT6825GT-D1H-R
- MT6825GT-DHV-R
- MT6825GT-E1T-R
- MT6825GT-E2D-R
- MT6825GT-EED-R
- MT6825GT-EEH-R
- MT6825GT-EEN-R
- MT6825GT-J4D-R
- MT6825GT-J4E-R
- MT6825GT-J5D-R
- MT6825GT-K4D-R
- MT6825GT-LL1-R
- MT6825GT-LLD-R
- MT6825GT-M1T-R
- MT6825GT-M2D-R
- MT6825GT-M4D-R
- MT6825GT-M4F-R
- MT6825GT-M4V-R
- MT6825GT-M5D-R
- MT6825GT-M5V-R
- MT6825GT-M5VF-R
- MT6825GT-MM1-R
- MT6825GT-MMD-R
- MT6825GT-PP1-R
- MT6825GT-QQ1-R
- MT6825GT-STD-R
- MT6825GT-STD1-R
- MT6825GT-STF-R
- MT6825GT-STT-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/c7e90e5222cb61b2.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/ABPwbOVGbocqAPxpD51c2RJbn8b.png
---

## 核心参数与配置

以下为官网目录中 **MT6825GT-A1D-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 工业编码器 |
| 封装 | TSSOP16 |
| 目录等级 | Industrial |
| 数字接口 | 3-wire SPI/4-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 18bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~16pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~4096lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <25,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | <2μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.0~5.0；官网目录标注，适用于上述订货配置 |

## 核心角度与PWM位宽各自使用

核心角度、PWM和ABZ线数是不同输出口径。主控若以SPI做上电定位、ABZ做运行跟踪，需要统一零点和方向，并确认复位后增量计数如何重新建立。

## 三线SPI的总线换向要落实

目录列三线及四线SPI，选用共享数据线时须按手册切换驱动方向，避免主控与器件同时驱动。即使两种模式读到相同角度，也不能假设时序、帧长和配置完全一致。

## 升级比较保留既有预设

GT不是可删除的包装尾缀，本页关联MT6825系列而保留完整型号。不同OPN状态混有Active和不推荐新设计，迁移到MT6835时也要重新核对引脚、配置保存和输出比例，不能仅按“升级”字样判断原位替换。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Not Recomended for New Designs | MT6825GT-A1D-R、MT6825GT-A360-R、MT6825GT-C1T-R、MT6825GT-D1H-R、MT6825GT-E2D-R、MT6825GT-EEH-R、MT6825GT-J4E-R、MT6825GT-K4D-R、MT6825GT-LL1-R、MT6825GT-M1T-R、MT6825GT-M2D-R、MT6825GT-M4V-R、MT6825GT-MM1-R、MT6825GT-PP1-R |
| Active | MT6825GT-A1T-R、MT6825GT-C4D-R、MT6825GT-CDD-R、MT6825GT-DHV-R、MT6825GT-E1T-R、MT6825GT-EED-R、MT6825GT-EEN-R、MT6825GT-J4D-R、MT6825GT-J5D-R、MT6825GT-LLD-R、MT6825GT-M4D-R、MT6825GT-M4F-R、MT6825GT-M5D-R、MT6825GT-M5V-R、MT6825GT-M5VF-R、MT6825GT-MMD-R、MT6825GT-QQ1-R、MT6825GT-STD-R、MT6825GT-STD1-R、MT6825GT-STF-R、MT6825GT-STT-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6825GT-A1D-R](https://www.novosns.com/product/MT6825GT-A1D-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-A1T-R](https://www.novosns.com/product/MT6825GT-A1T-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-A360-R](https://www.novosns.com/product/MT6825GT-A360-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-C1T-R](https://www.novosns.com/product/MT6825GT-C1T-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-C4D-R](https://www.novosns.com/product/MT6825GT-C4D-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-CDD-R](https://www.novosns.com/product/MT6825GT-CDD-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-D1H-R](https://www.novosns.com/product/MT6825GT-D1H-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-DHV-R](https://www.novosns.com/product/MT6825GT-DHV-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-E1T-R](https://www.novosns.com/product/MT6825GT-E1T-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-E2D-R](https://www.novosns.com/product/MT6825GT-E2D-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-EED-R](https://www.novosns.com/product/MT6825GT-EED-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-EEH-R](https://www.novosns.com/product/MT6825GT-EEH-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-EEN-R](https://www.novosns.com/product/MT6825GT-EEN-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-J4D-R](https://www.novosns.com/product/MT6825GT-J4D-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-J4E-R](https://www.novosns.com/product/MT6825GT-J4E-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-J5D-R](https://www.novosns.com/product/MT6825GT-J5D-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-K4D-R](https://www.novosns.com/product/MT6825GT-K4D-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-LL1-R](https://www.novosns.com/product/MT6825GT-LL1-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-LLD-R](https://www.novosns.com/product/MT6825GT-LLD-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M1T-R](https://www.novosns.com/product/MT6825GT-M1T-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M2D-R](https://www.novosns.com/product/MT6825GT-M2D-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M4D-R](https://www.novosns.com/product/MT6825GT-M4D-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M4F-R](https://www.novosns.com/product/MT6825GT-M4F-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M4V-R](https://www.novosns.com/product/MT6825GT-M4V-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M5D-R](https://www.novosns.com/product/MT6825GT-M5D-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M5V-R](https://www.novosns.com/product/MT6825GT-M5V-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-M5VF-R](https://www.novosns.com/product/MT6825GT-M5VF-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-MM1-R](https://www.novosns.com/product/MT6825GT-MM1-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-MMD-R](https://www.novosns.com/product/MT6825GT-MMD-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-PP1-R](https://www.novosns.com/product/MT6825GT-PP1-R) | TSSOP16；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-QQ1-R](https://www.novosns.com/product/MT6825GT-QQ1-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-STD-R](https://www.novosns.com/product/MT6825GT-STD-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-STD1-R](https://www.novosns.com/product/MT6825GT-STD1-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-STF-R](https://www.novosns.com/product/MT6825GT-STF-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |
| [MT6825GT-STT-R](https://www.novosns.com/product/MT6825GT-STT-R) | TSSOP16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf) |

“Not Recommended for New Designs”表示该完整订货号不推荐用于新设计，不代表本页全部成员停产。请结合表内仍为Active的版本核对供应与配置。

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

同一归一型号不同OPN生命周期不同；逐条保留，不能整体标Active。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6825GT-A1D-R)
- [DatasheetMT6825_Rev.1.8.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/IJvVbdAIQoQJ8wxFSw1ccWRundc.pdf)
- [MT6825_Rev.1.8.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/CSFRbWrSFomtbyx6BDjc5qVAnbd.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
