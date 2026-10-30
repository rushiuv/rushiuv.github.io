---
title: MT6728QC
wiki: true
wiki_type: model
model_card: true
wiki_rank: 435
lastmod: '2026-10-30'
catalog_type: 编码器信号处理
catalog_form: 芯片
wiki_category: 编码器信号处理
description: MT6728QC 是QFN48封装的差分正余弦插补细分器，处理外部模拟周期信号并产生角度或增量输出；未集成磁体、磁敏阵列或光电探测器。
official_url: https://www.novosns.com/product/MT6728QC-STD
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6728
- MT6728QC
- MT6728QC-STD
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/PdwKbt7WZoFHgOxflFMcexsmnof.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/7bdfbafacaf78d0c.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/DTmCbc32Jo1O0ex8RpvcuGUTnlc.png
---

## 核心参数与配置

以下为官网目录中 **MT6728QC-STD** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 外置正余弦解码/插补细分器 |
| 目录类别 | 位置传感器专用芯片 |
| 封装 | QFN48 |
| 目录等级 | Industrial |
| Resolution | 21 bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~63Polarity/Cycle；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit/cycle；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~16384 Pulse/<br>cycle；官网目录标注，适用于上述订货配置 |
| Power Consumption | 20mA；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |
| Type | Encoder<br>Decoding Chip；官网目录标注，适用于上述订货配置 |

## 先定义外部输入的来源和周期

来源可以是符合其输入条件的正余弦信号链，具体幅度、共模和相位范围要看手册。官网没有把本器件定义为完整光电编码器，不能把“可用于编码链”改成内部已具备光学检测。

## 高细分只发生在已知周期内

官网介绍对外部输入补偿解码，再输出每周期的高线数AB。若输入来自多极磁环或光栅，跨周期唯一位置仍需要计数或粗位置来源，细分码宽不能单独提供全圈上电绝对性。

## Z参考与AB输出同时验证

官网提到Z参考可从外部输入获取，因此参考标记的机械位置、阈值和延时应与插补后的AB一致。测试应覆盖参考附近的往返、掉电重启及高速通过，检查是否出现整周期位置跳变。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6728QC-STD](https://www.novosns.com/product/MT6728QC-STD) | QFN48；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/PdwKbt7WZoFHgOxflFMcexsmnof.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/IazpbkU4uo8tXDxPRVlczy18nQc.pdf) |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

官网原文为外部差分正余弦插补器，不是集成光电探测器；未将其捏造成光电编码器。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6728QC-STD)
- [MT6728_Rev.1.0_CN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/PdwKbt7WZoFHgOxflFMcexsmnof.pdf)
- [MT6728_Rev.1.0_EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/IazpbkU4uo8tXDxPRVlczy18nQc.pdf)
- [位置传感器专用芯片目录](https://www.novosns.com/position-sensor-assp)
