---
title: "ADMT4000"
wiki: true
wiki_type: "model"
wiki_rank: 75
seed_count: 2
lastmod: "2026-10-24"
description: "ADMT4000 是 ADI 的无电源多圈磁位置传感器，断电期间仍能记录磁场旋转圈数，上电后通过 SPI 读出多圈绝对位置。"
official_url: "https://www.analog.com/en/products/admt4000.html"
related_companies: ["ADI"]
wiki_category: "多圈与断电位置"
document_version: "Rev.C，2026-07-22"
model_card: true
datasheet_url: "https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf"
datasheet_label: "ADMT4000 数据手册 Rev.C"
---

## 核心性能

### 产品介绍

ADMT4000是ADI的断电保持多圈磁位置传感器，可在器件无电源时记录外部磁场旋转状态，并在上电后通过SPI报告位置。 [官方资料](https://www.analog.com/en/products/admt4000.html)

### 核心参数

- **计圈方式** 器件无电源时仍记录外部磁场转数
- **多圈范围** 46 圈
- **测量更新率** 100 kSPS
- **角度精度** 官网列 ±0.25°
- **工作磁场** 16～31 mT
- **芯片供电** 3.3 V；SPI 接口电平 1.8～5 V
- **结温范围** −40～150°C
- **封装** TSSOP-24；内置温度传感器

### 接口与输出

ADMT4000 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **芯片供电** 3.3 V；SPI 接口电平 1.8～5 V

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

多圈传感器既要知道一圈内的位置，也要保存旋转经过了多少圈。不同器件可能使用磁状态、机械传动或其他方式保存信息，断电期间是否继续响应运动必须看具体型号。

有限圈数编码不能解释成无限累计计数。初始化、复位、旋转方向和越界行为关系到总位置的可信性，尤其在上电后直接恢复运动的系统中需要明确。

### 典型应用与使用条件

单圈分辨率、多圈范围和长期保持属于不同指标。强磁场、外部结构变化或不正确的复位流程可能改变状态，具体诊断与恢复方法必须遵循原厂资料。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [ADMT4000 原厂资料入口](https://www.analog.com/en/products/admt4000.html)
- [官网文档入口（官方入口）](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)
- [ADMT4000 数据手册 Rev.C（官方 PDF）](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)
