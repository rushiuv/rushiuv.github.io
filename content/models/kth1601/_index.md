---
title: KTH1601
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH1601 是全极性微功耗霍尔开关，公开手册首页明确采用CMOS推挽输出；采样频率、磁门限和封装应按完整型号一起选择。
wiki_rank: 313
catalog_type: 磁开关
wiki_category: 磁开关
official_url: https://chat.connteck.com/products/switches/KTH1601/
catalog_source: https://chat.connteck.com/products/switches/KTH1601/
search_aliases:
- KTH1601
datasheet_url: https://chat.connteck.com/downloads/KTH1601/KTH1601_Datasheet_CN.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/kth1601-browser-original.jpg
product_image_caption: KTH1601 原厂SOT-23-3L封装图，公开手册第1页
product_image_source: https://chat.connteck.com/downloads/KTH1601/KTH1601_Datasheet_CN.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 器件与输出 | 全极性霍尔开关；CMOS推挽输出；首页明确CMOS推挽，不沿用网页开漏输出介绍（手册第1页） |
| 主电源 | 1.6～5.5 V；推荐供电范围，按完整订货版本确认（手册第1页） |
| 典型功耗工作点 | 5 Hz版本1.6 µA；20 Hz版本3.3 µA；VDD=1.8 V；两个采样版本，不与最高响应同时使用（手册第1页） |
| 动作门限档 | 22 Gs、33 Gs、46 Gs可选；首页BOP可选档，最低/典型/最大窗口及BRP仍需对应手册表格确认（手册第1页） |
| 温度与封装 | −40～85°C；SOT-23-3L、SOT-553、TO-92S；按完整订货型号选择封装与引脚，不推定相互兼容（手册第1页） |
| ESD | HBM 8 kV；首页器件声明，不是整机ESD测试结果（手册第1页） |

## 先判断动作逻辑再选磁体

单极、全极和锁存的释放行为不同。设计门磁或翻盖检测时，应记录磁体靠近与离开的全路径，以及两种极性下的输出，避免把一次“有磁翻转”误当成完整逻辑确认。

## 低功耗以可检测事件为代价核算

周期采样器件可能在磁体快速通过时错过短事件。电池预算与响应时间应一起检查，依据实际开合速度、磁场有效区长度和工作模式选择采样档，而非只采用最低电流。

## 输出类型影响上拉与待机电流

本型号公开手册首页明确CMOS推挽。接收端电平、负载与供电仍需核对，不能按开漏器件直接添加上拉并假定支持任意外部电压。不同封装的引脚应分别对照，不以外形相近认定可直接替换。


## 公开资料与型号核对

KTH1601公开手册第1页列CMOS推挽输出与1.6～5.5V供电；网页另有开漏和1.7V下限标注，接口设计应使用所选完整型号的电磁参数表。

按完整型号、等级和版本选择手册。

- [KTH1601_Datasheet_CN.pdf](https://chat.connteck.com/downloads/KTH1601/KTH1601_Datasheet_CN.pdf)

[来源产品页](https://chat.connteck.com/products/switches/KTH1601/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

