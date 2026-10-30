---
title: NSM3011L
wiki: true
wiki_type: model
model_card: true
wiki_rank: 413
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3011L 是本次目录中的Hall角度L成员检索分组，收录NSM3011L-DSPR工业订货号；没有据此补出未列的Q0/Q1汽车版本。
official_url: https://www.novosns.com/product/NSM3011L-DSPR
related_companies:
- 纳芯微
search_aliases:
- NSM3011L
- NSM3011L-DSPR
- NSM301x
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
series_parent: nsm301x
---

## 核心参数与配置

以下为官网目录中 **NSM3011L-DSPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器 |
| 封装 | SOP8 |
| 目录等级 | Industrial |
| 数字接口 | 3-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 11~14bit；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <10,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 10μs~120μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 工业成员按实际接口路径接入

代表目录列三线SPI及PWM相关字段，系列详情还介绍模拟与编程功能。主控设计应区分读取、配置和模拟采样各自所需条件，不能从同系列文案推断任意接口同时工作。

## L成员差异不从字母猜

官网本次没有独立解释L与A/B的全部差别。选型时记录完整L-DSPR以及默认输出模式，保留系列共性与成员限定，避免把字母当成只有包装差异。

## 更新与噪声使用同一配置评价

目录延时以区间列示，输出抖动和响应需要在最终滤波设置下同时观察。旋钮或机构慢动时的稳定与快速动作滞后应分别测试，而不是从14位目录码宽直接推断手感。

## 型号与资格版本

本页按核心前缀提供检索入口。Q0、Q1、IND、STD及其他配置串保留在完整订货号中，不能把某一行的车规等级、封装或输出推广到整个分组。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3011L-DSPR](https://www.novosns.com/product/NSM3011L-DSPR) | SOP8；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 资料边界

model仅作检索分组键；本文不删除NSM完整订货号中的Q0/Q1/IND/STD资格或配置部分。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3011L-DSPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
