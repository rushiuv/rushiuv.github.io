---
title: MT6826SGT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 407
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6826SGT 是MT6826S AMR角度系列的TSSOP16型号，面向增量反馈及四线SPI读取，适合把输出线数与目标转速一起配置。
official_url: https://www.novosns.com/product/MT6826SGT-ACD-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6826S
- MT6826SGT
- MT6826SGT-ACD-R
- MT6826SGT-AKD-R
- MT6826SGT-AKH-R
- MT6826SGT-APH-R
- MT6826SGT-STD-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/c7e90e5222cb61b2.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/ABPwbOVGbocqAPxpD51c2RJbn8b.png
series_parent: mt6826s
---

## 核心参数与配置

以下为官网目录中 **MT6826SGT-ACD-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 工业编码器 |
| 封装 | TSSOP16 |
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

## 高速与高线数需要共同核算

ABZ线数越高，主控每秒需要接收的边沿越密。应由实际转速换算基础频率和四倍频计数率，再比较芯片输出、接收器和计数器能力，不能把目录最大线数与最大转速直接同时采用。

## GT与JT不能只按系列名换板

本型号为TSSOP16，SJT成员为QFN24。两者即使目录参数接近，焊盘、引脚和布局仍要分别核对。SGT与SJT的具体引脚按各自封装资料选择。

## 动态延时看最终工作配置

目录延时以区间展示，不能把最快数值当作所有速度与滤波配置的固定值。测试时同步记录位置参考、SPI读数或AB边沿，确认控制器实际得到的位置时间戳。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6826SGT-ACD-R](https://www.novosns.com/product/MT6826SGT-ACD-R) | TSSOP16；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |
| [MT6826SGT-AKD-R](https://www.novosns.com/product/MT6826SGT-AKD-R) | TSSOP16；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |
| [MT6826SGT-AKH-R](https://www.novosns.com/product/MT6826SGT-AKH-R) | TSSOP16；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |
| [MT6826SGT-APH-R](https://www.novosns.com/product/MT6826SGT-APH-R) | TSSOP16；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |
| [MT6826SGT-STD-R](https://www.novosns.com/product/MT6826SGT-STD-R) | TSSOP16；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf) |

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

这些OPN的目录参数相同，寄存器预设、包装和其他功能仍应按完整订货号确认。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6826SGT-ACD-R)
- [MT6826S_Datasheet_Rev.1.1-CN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Fl4kbt78Zo59Hxx3EbecPPldnOe.pdf)
- [MT6826S_Datasheet_Rev.1.1-EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/IhywbstEKoQqmcxud7JcXPDJngb.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
