---
title: NSM301x系列
description: 带片内增益与零位配置的霍尔角度器件组，按成员选择输出功能。
wiki: true
wiki_type: model
wiki_rank: 247
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 纳芯微
wiki_category: 数字角度
catalog_vendor: 纳芯微
catalog_type: 数字角度
catalog_form: 芯片
search_aliases:
- NSM3011
- NSM3012
- NSM3013
official_url: https://www.novosns.com/industrial-encoder
document_version: 官方公开PDF，核对：2026-10-18；版本见下文
model_card: true
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf
datasheet_label: NSM3011A等成员参考手册（PDF）
catalog_level: 系列
---

NSM301x用于Hall角度检测。当前目录中的完整A、B、L、S、AD、AF、BF、BZ等成员及资格后缀应分别保留，不能用无后缀的历史系列名代替订货定义。

## 型号与核心异同

| 型号与完整订货配置 | 等级／封装 | 目录数字接口 | 核心分辨率 / PWM | UVW |
| --- | --- | --- | --- | --- |
| [NSM3011A](/models/nsm3011a/)<br>NSM3011A-DSPR | Industrial；SOP8 | 3-wire SPI | 14bit / 11~14bit | - |
| [NSM3011A](/models/nsm3011a/)<br>NSM3011A-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3011B](/models/nsm3011b/)<br>NSM3011B-DSPR | Industrial；SOP8 | 3-wire SPI | 14bit / 11~14bit | - |
| [NSM3011B](/models/nsm3011b/)<br>NSM3011B-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3011L](/models/nsm3011l/)<br>NSM3011L-DSPR | Industrial；SOP8 | 3-wire SPI | 14bit / 11~14bit | - |
| [NSM3012A](/models/nsm3012a/)<br>NSM3012A-DSPR | Industrial；SOP8 | 3-wire SPI | 14bit / 11~14bit | - |
| [NSM3012A](/models/nsm3012a/)<br>NSM3012A-Q0SPR<br>NSM3012A-Q1SPR<br>NSM3012A-QSPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3012B](/models/nsm3012b/)<br>NSM3012B-DSPR | Industrial；SOP8 | 3-wire SPI | 14bit / 11~14bit | - |
| [NSM3012B](/models/nsm3012b/)<br>NSM3012B-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3012S](/models/nsm3012s/)<br>NSM3012S-DSPR | Industrial；SOP8 | 3-wire SPI | 14bit / 11~14bit | - |
| [NSM3013A](/models/nsm3013a/)<br>NSM3013A-DSPR | Industrial；SOP8 | - | 14bit / 11~14bit | 1~8pole pairs programmable |
| [NSM3013A](/models/nsm3013a/)<br>NSM3013A-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | Yes |
| [NSM3013B](/models/nsm3013b/)<br>NSM3013B-DSPR | Industrial；SOP8 | - | 14bit / 11~14bit | 1~8pole pairs programmable |
| [NSM3013B](/models/nsm3013b/)<br>NSM3013B-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | Yes |
| [NSM3011AD](/models/nsm3011ad/)<br>NSM3011AD-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3012AF](/models/nsm3012af/)<br>NSM3012AF-Q0SPR<br>NSM3012AF-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3012BF](/models/nsm3012bf/)<br>NSM3012BF-Q0SPR<br>NSM3012BF-Q0SWR<br>NSM3012BF-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |
| [NSM3012BZ](/models/nsm3012bz/)<br>NSM3012BZ-Q1SPR | Automotive；SOP8 | 目录未列明 | 目录未列明 / Yes | No |


表中使用各成员页已整理的目录字段，缺少字段表示目录未列明，并非已经证明不支持该功能。DSPR、Q1SPR等完整后缀的工业／汽车等级、预设和资格仍按对应订货行确认。A/B等名称接近，也不足以证明只有料号文字不同。

## 从输出需求确定配置

先确定主控运行时读取模拟电压、PWM还是数字角度，再核对编程接口是否也能作为连续数据口。NSM3013A/B目录另列UVW路径，位置标定与换向相序需要分别确认方向和零点。

历史EN1.0手册中，NSM3013的SON可检测Z向场强阈值，且需按手册关闭AGC。这条条件保留在历史版本范围内，不直接套到表中每个带后缀的新成员。

## 型号资料与版本

每个型号入口保留完整OPN、官网和对应手册。工业代表配置的参数不为汽车版本背书，14位码宽也不代表整机14位准确度；正式设计应使用选定版本的接口时序、输出传递函数及资格文件。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://www.novosns.com/industrial-encoder)
- [NSM3011A等成员参考手册（PDF）](https://wwwapi.novosns.com/dms/userfiles/docs/Qtsqb2adCoN0gQx6PylcDoOXnGd.pdf)

- [历史EN1.0系列手册](https://www.novosns.com/Public/Uploads/uploadfile3/files/20220726/NSM3011_3012_3013_DatasheetV1.0EN.pdf)
