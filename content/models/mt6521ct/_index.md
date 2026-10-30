---
title: MT6521CT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 424
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6521CT 是SOP8封装的MT652x水平Hall与聚磁片角度/位置系列成员，可按配置检测不同磁场平面；具体平面与输出组合需对应完整型号核对。
official_url: https://www.novosns.com/product/MT6521CT-STD-Q-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6521
- MT6521CT
- MT6521CT-STD-Q-R
- MT6521CT-STP-Q-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
series_parent: mt6521
---

## 核心参数与配置

以下为官网目录中 **MT6521CT-STD-Q-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Automotive |
| PWM输出 | Yes；官网目录标注，适用于上述订货配置 |
| Digital Interface | SPI，SENT；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | No；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | Yes；官网目录标注，适用于上述订货配置 |
| Angle Accuracy | <±1.0°；官网目录标注，适用于上述订货配置 |
| Analog Output Curve Programming | Any 8-point Programming or 17-point piece-wise-linear Programming；官网目录标注，适用于上述订货配置 |
| Redundant Package Option | Yes；官网目录标注，适用于上述订货配置 |
| Output Overvoltage Protection | 18V；官网目录标注，适用于上述订货配置 |
| ISO26262 | Yes；官网目录标注，适用于上述订货配置 |
| Automotive Qualification | Yes；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~160；官网目录标注，适用于上述订货配置 |
| 目录供电 | 4.5~5.5；官网目录标注，适用于上述订货配置 |
| Magnetic Sensing Principle | 3D HALL(XY,XZ,YZ)；官网目录标注，适用于上述订货配置 |

## 检测平面不能由系列简介代选

官网将MT652x描述为可根据型号配置检测XY、XZ或YZ平面，但本次公开字段没有逐一说明6521/6522/6523与平面的对应表。因此保留本完整型号，实际选型先核对敏感平面及磁体运动，不能自行给它指定某一平面。

## SOP8封装的接入取舍

CT成员把平面检测能力放入八脚封装，设计前先确定SPI/SENT、模拟或UVW哪条路径是主任务，避免在有限引脚下假设系列所有输出同时存在。

## 曲线映射、资格与预告配置分别核对

目录列多点映射和汽车相关字段，参数仍要带完整OPN及手册条件。本组同时有Active与Preview的预设，未发布预设不能因同前缀其他料在供货而改写为Active。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Active | MT6521CT-STD-Q-R |
| Preview | MT6521CT-STP-Q-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6521CT-STD-Q-R](https://www.novosns.com/product/MT6521CT-STD-Q-R) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/LGpzbWCZnosP54x3qnScgyBanOc.pdf) |
| [MT6521CT-STP-Q-R](https://www.novosns.com/product/MT6521CT-STP-Q-R) | SOP8；Automotive；Preview；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/LGpzbWCZnosP54x3qnScgyBanOc.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

同一归一型号不同OPN生命周期不同；逐条保留，不能整体标Active。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6521CT-STD-Q-R)
- [Datasheet(CN)MT652x_Datasheet_Rev.1.2.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf)
- [MT652x_Datasheet_Rev.1.2.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/LGpzbWCZnosP54x3qnScgyBanOc.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
