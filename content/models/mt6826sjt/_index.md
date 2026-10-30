---
title: MT6826SJT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 408
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6826SJT 是MT6826S系列的QFN24成员，保留AMR角度感知及数字/增量输出路径；QFN封装与完整预设需作为独立设计对象。
official_url: https://www.novosns.com/product/MT6826SJT-ACD
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6826S
- MT6826SJT
- MT6826SJT-ACD
- MT6826SJT-AKD
- MT6826SJT-STD
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/ec2add0a8a6fdc81.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XxYybQMMFotD7Kxh3H3cFkdBnMb.png
series_parent: mt6826s
---

## 核心参数与配置

以下为官网目录中 **MT6826SJT-ACD** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 工业编码器 |
| 封装 | QFN24 |
| 目录等级 | Industrial |
| 数字接口 | 4-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 15bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~16pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~4096lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <120,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 2μs~10μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## QFN24成员要先核引脚与地回路

本型号不是TSSOP16的SGT封装改名。应按QFN24引脚、裸露焊盘和电源回路设计PCB，再决定输出组合；共享产品图片不能证明两个封装可互换。

## 绝对角度可给增量计数建立基准

SPI读取和ABZ跟踪共用同一角度链，系统可用绝对读数建立启动位置，但仍要处理主控计数器启用时刻、方向和Z参考。它们有助于交叉检查通信，不能据此构成独立传感冗余。

## 保留STD与其他完整预设

目录列出不同SJT订货号，公开矩阵未逐项解释全部上电预设。固件应回读实际配置并保存对应记录，不把不同预设混成一颗固定功能器件。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6826SJT-ACD](https://www.novosns.com/product/MT6826SJT-ACD) | QFN24；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |
| [MT6826SJT-AKD](https://www.novosns.com/product/MT6826SJT-AKD) | QFN24；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |
| [MT6826SJT-STD](https://www.novosns.com/product/MT6826SJT-STD) | QFN24；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6826SJT-ACD)
- [MT6826S_Datasheet_Rev.1.1-CN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf)
- [MT6826S_Datasheet_Rev.1.1-EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
