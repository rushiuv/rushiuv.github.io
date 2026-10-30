---
title: MT6701QT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 402
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6701QT 是MT6701系列的QFN16成员，提供与CT不同的封装和引脚资源；接口与初始化预设仍以完整订货号核对。
official_url: https://www.novosns.com/product/MT6701QT-A16
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6701
- MT6701QT
- MT6701QT-A16
- MT6701QT-A32
- MT6701QT-A64
- MT6701QT-A800
- MT6701QT-A900
- MT6701QT-A9D
- MT6701QT-AAD
- MT6701QT-ABD
- MT6701QT-ACD
- MT6701QT-ACE
- MT6701QT-ACS
- MT6701QT-P500
- MT6701QT-STD
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/36ddf827b24fee09.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/RFHEbF85Io209CxN8y7ciOPKnSf.png
series_parent: mt6701
---

## 核心参数与配置

以下为官网目录中 **MT6701QT-A16** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器 |
| 封装 | QFN16 |
| 目录等级 | Industrial |
| 数字接口 | I²C;SSI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~16pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~1024lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <55,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | <5μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## QFN16的意义是引脚资源与布局变化

QT与CT同属MT6701，但封装、焊盘和可用引脚应分别确认。替换板卡不能仅按14bit和相同系列名迁移，尤其要核对增量、换向与串行接口是否复用。

## 数字角度和增量边沿使用不同主控资源

绝对角度用于上电读取，ABZ用于边沿计数，PWM需要捕获周期与占空比。应按控制任务选一条主路径，并统一方向、零点和启动时刻，避免把同源输出误认作相互独立的冗余。

## 订货预设不能从名称猜功能

官网列出STD及多种预设OPN。目录相同不证明上电默认寄存器相同，应回读并记录实际模式；官方共享图片也不能代替QT封装图和焊盘尺寸。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6701QT-A16](https://www.novosns.com/product/MT6701QT-A16) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-A32](https://www.novosns.com/product/MT6701QT-A32) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-A64](https://www.novosns.com/product/MT6701QT-A64) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-A800](https://www.novosns.com/product/MT6701QT-A800) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-A900](https://www.novosns.com/product/MT6701QT-A900) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-A9D](https://www.novosns.com/product/MT6701QT-A9D) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-AAD](https://www.novosns.com/product/MT6701QT-AAD) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-ABD](https://www.novosns.com/product/MT6701QT-ABD) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-ACD](https://www.novosns.com/product/MT6701QT-ACD) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-ACE](https://www.novosns.com/product/MT6701QT-ACE) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-ACS](https://www.novosns.com/product/MT6701QT-ACS) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-P500](https://www.novosns.com/product/MT6701QT-P500) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |
| [MT6701QT-STD](https://www.novosns.com/product/MT6701QT-STD) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6701QT-A16)
- [MT6701_Datasheet_Rev.1.9.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/XltRb0nAToicoixcUp7c5OIqn3b.pdf)
- [MT6701_Datasheet_Rev.1.9_中文版.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/M7hob1brwoHm6tx8gGgc156nn5c.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
