---
title: NSM3502
wiki: true
wiki_type: model
model_card: true
wiki_rank: 419
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: NSM3502 是双码道游标Hall离轴编码器的检索分组，保留IND-Q1QWAR与STD-Q1QWAR完整配置；两种OPN目录参数相同不证明内部预设相同。
official_url: https://www.novosns.com/product/NSM3502-IND-Q1QWAR
related_companies:
- 纳芯微
search_aliases:
- NSM3502
- NSM3502-IND-Q1QWAR
- NSM3502-STD-Q1QWAR
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/AgawbuVmLoE8A2xS2CpcwMzonPf.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/7bdfbafacaf78d0c.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/NaIRbbdtFoRioRxZf7FcFqconbe.png
---

## 核心参数与配置

以下为官网目录中 **NSM3502-IND-Q1QWAR** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器 |
| 封装 | QFN48 |
| 目录等级 | Industrial |
| 数字接口 | 4-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 22bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~64pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~65536lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | ＜24000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 5us；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 双码道解决跨磁极位置关系

官网说明集成双码道Hall阵列，主码道面向2mm极距，通过游标算法组合绝对位置。磁环或磁尺必须匹配两条码道的几何关系，不能只按主码道周期设计后期待芯片自动识别全部位置。

## 极对数、线数与速度共同配置

官方介绍支持多种磁环极对数以及ABZ、SPI、PWM、UART、UVW路径。实际系统应先选磁环，再换算输出边沿频率和主控处理能力，不能把目录22bit码宽作为每一种磁环和转速下的有效精度。

## IND与STD保留为独立配置

本页分组不删除IND/STD或Q1QWAR部分。目录未展示二者参数差异，不代表上电预设、校准流程或资格均相同；正式采用前逐项核对，系列共享图片也不能代替完整封装和敏感点资料。

## 型号与资格版本

本页按核心前缀提供检索入口。Q0、Q1、IND、STD及其他配置串保留在完整订货号中，不能把某一行的车规等级、封装或输出推广到整个分组。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [NSM3502-IND-Q1QWAR](https://www.novosns.com/product/NSM3502-IND-Q1QWAR) | QFN48；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/AgawbuVmLoE8A2xS2CpcwMzonPf.pdf) |
| [NSM3502-STD-Q1QWAR](https://www.novosns.com/product/NSM3502-STD-Q1QWAR) | QFN48；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/AgawbuVmLoE8A2xS2CpcwMzonPf.pdf) |

## 资料边界

model仅作检索分组键；本文不删除NSM完整订货号中的Q0/Q1/IND/STD资格或配置部分。

IND与STD都在连字符之后，按用户规则合并为NSM3502，但保留两种完整OPN，不能忽略配置差异。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/NSM3502-IND-Q1QWAR)
- [NSM3502_Datasheet_V1.0_CN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/AgawbuVmLoE8A2xS2CpcwMzonPf.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
