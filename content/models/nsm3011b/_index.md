---
title: NSM3011B
wiki: true
wiki_type: model
model_card: true
wiki_rank: 412
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3011B 分组对应Hall角度系列B成员，包含DSPR和Q1SPR；完整工业/汽车资格及具体输出条件见订货表，B不能当作可省略的包装字符。
official_url: https://www.novosns.com/product/NSM3011B-DSPR
related_companies:
- 纳芯微
search_aliases:
- NSM3011B
- NSM3011B-DSPR
- NSM3011B-Q1SPR
- NSM301x
- NSM301x-Q
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
series_parent: nsm301x
---

## 核心参数与配置

以下为官网目录中 **NSM3011B-DSPR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器、汽车角度传感器 |
| 封装 | SOP8 |
| 目录等级 | Industrial |
| 数字接口 | 3-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 11~14bit；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <10,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 10μs~120μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 先锁定B成员的输出传递函数

系列介绍支持分段拟合与模拟/PWM输出，但公开摘要没有给出A、B逐项差异。接入控制器前应核对B成员的默认曲线、零点和方向，并在有效行程两端检查接收器的故障判断窗口。

## DSPR与Q1SPR不能共用资格承诺

两个完整订货号分属工业和汽车目录。即便目录电气字段相同，也不能据此合并资格、失效诊断或可靠性文件；板卡记录应保存实际订货号。

## 供电比例与ADC参考要一致

若采用模拟输出，接收端参考、地回路和传感器供电变化会共同影响读数。应按B成员手册确认是否及如何使用比例测量，不能只按系列DAC位数宣称系统分辨率。

## 订货版本之间的差别

### 等级

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Industrial | NSM3011B-DSPR |
| Automotive | NSM3011B-Q1SPR |

### category

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 工业编码器 | NSM3011B-DSPR |
| 汽车角度传感器 | NSM3011B-Q1SPR |

### PWM输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| 11~14bit | NSM3011B-DSPR |
| Yes | NSM3011B-Q1SPR |

### UVW增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| - | NSM3011B-DSPR |
| No | NSM3011B-Q1SPR |

### ABZ增量输出

| 目录标注 | 适用完整订货号 |
| --- | --- |
| - | NSM3011B-DSPR |
| No | NSM3011B-Q1SPR |

## 型号与资格版本

本页按核心前缀提供检索入口。Q0、Q1、IND、STD及其他配置串保留在完整订货号中，不能把某一行的车规等级、封装或输出推广到整个分组。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3011B-DSPR](https://www.novosns.com/product/NSM3011B-DSPR) | SOP8；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |
| [NSM3011B-Q1SPR](https://www.novosns.com/product/NSM3011B-Q1SPR) | SOP8；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf) |

## 资料边界

model仅作检索分组键；本文不删除NSM完整订货号中的Q0/Q1/IND/STD资格或配置部分。

同一归一型号跨工业与汽车目录；需按完整订货号核对Q0/Q1/工业等级与所用手册，不能把代表工业详情扩展为所有车规配置。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3011B-DSPR)
- [NSM3011_3012_3013_Datasheet_V1.0_CN-715.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)
- [NSM3011_3012_3013_DatasheetV1.0EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AXgrbYeOooyjNbxyorqcTYgLnMh.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
