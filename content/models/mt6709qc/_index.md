---
title: MT6709QC
wiki: true
wiki_type: model
model_card: true
wiki_rank: 434
lastmod: '2026-10-30'
catalog_type: 编码器信号处理
catalog_form: 芯片
wiki_category: 编码器信号处理
description: MT6709QC 是QFN48封装的外部正余弦角度解码芯片，接收线性Hall产生的模拟信号；它本身不等于集成磁敏元件的绝对角度传感器。
official_url: https://www.novosns.com/product/MT6709QC-STD
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6709
- MT6709QC
- MT6709QC-STD
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/ZMKGbLDV5oqeE9xMt4OcXAFmndc.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/7bdfbafacaf78d0c.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/Ghdxb9VfOo57XoxOChCc68p5nMd.png
---

## 核心参数与配置

以下为官网目录中 **MT6709QC-STD** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 外置正余弦解码/插补细分器 |
| 目录类别 | 位置传感器专用芯片 |
| 封装 | QFN48 |
| 目录等级 | Industrial |
| Resolution | 17 bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~63Polarity/Cycle；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit/cycle；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~2500 Pulse/<br>cycle；官网目录标注，适用于上述订货配置 |
| Power Consumption | 20mA；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |
| Type | Encoder<br>Decoding Chip；官网目录标注，适用于上述订货配置 |

## 传感单元在芯片之外

官网描述由外部线性Hall围绕单对极磁环产生差分正余弦输入。系统需要同时设计传感器供电、安装相位、输入幅度和共模，先检查原始信号轨迹，再评估解码后的角度。

## 零偏、增益与相位分别影响解码

外部四路信号的失配会进入计算链，不能仅凭解码器码宽判断整机准确度。调试记录应保留各路输入、转动方向及整圈轨迹，并按手册实施相应补偿。

## 输出单位按每周期解释

目录ABZ、UVW和PWM以周期表达，主控应明确传感器磁周期与机械一圈的关系。若改变磁体结构，位置比例和电角换向配置也要随之核对，不能沿用原比例。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6709QC-STD](https://www.novosns.com/product/MT6709QC-STD) | QFN48；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/ZMKGbLDV5oqeE9xMt4OcXAFmndc.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/XCk7btIiBofFcXx8MuNcyrcWnMg.pdf) |

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

这些OPN的目录参数相同，寄存器预设、包装和其他功能仍应按完整订货号确认。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6709QC-STD)
- [MT6709_Rev.1.0_CN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/ZMKGbLDV5oqeE9xMt4OcXAFmndc.pdf)
- [MT6709_Rev.1.0_EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/XCk7btIiBofFcXx8MuNcyrcWnMg.pdf)
- [位置传感器专用芯片目录](https://www.novosns.com/position-sensor-assp)
