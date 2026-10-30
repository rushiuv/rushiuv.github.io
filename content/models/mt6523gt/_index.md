---
title: MT6523GT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 429
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6523GT 是TSSOP16封装的MT652x水平Hall与聚磁片角度/位置系列成员，可按配置检测不同磁场平面；具体平面与输出组合需对应完整型号核对。
official_url: https://www.novosns.com/product/MT6523GT-STD-Q-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6523
- MT6523GT
- MT6523GT-STD-Q-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/c7e90e5222cb61b2.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/ABPwbOVGbocqAPxpD51c2RJbn8b.png
---

## 核心参数与配置

以下为官网目录中 **MT6523GT-STD-Q-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | TSSOP16 |
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

## TSSOP16封装的接入取舍

GT版本为TSSOP16，布局需依据本封装引脚和敏感位置；共享系列图片只能说明来源，不能证明GT与CT具有相同敏感中心。

## 曲线映射、资格与预告配置分别核对

目录列多点映射和汽车相关字段，参数仍要带完整OPN及手册条件。输出映射只定义传递函数，温漂、磁路误差及故障响应仍需单独验证；目录ISO26262标记不等于整机安全等级。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6523GT-STD-Q-R](https://www.novosns.com/product/MT6523GT-STD-Q-R) | TSSOP16；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/LGpzbWCZnosP54x3qnScgyBanOc.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6523GT-STD-Q-R)
- [Datasheet(CN)MT652x_Datasheet_Rev.1.2.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/PgkFb2I4ioeiFKxvAAjc5gwpnCh.pdf)
- [MT652x_Datasheet_Rev.1.2.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/LGpzbWCZnosP54x3qnScgyBanOc.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
