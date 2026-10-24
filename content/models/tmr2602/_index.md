---
title: "TMR2602"
description: "集成可编程调理ASIC的TMR线性场传感器，支持调节零点与灵敏度。"
wiki: true
wiki_type: "model"
wiki_rank: 231
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "线性磁场"
catalog_vendor: "多维科技"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["TMR2602"]
official_url: "https://www.dowaytech.com/TMR2602-TMR-Linear-Sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 磁场范围 | 目录±25Gs，X轴敏感 |
| 供电／封装 | 3.3V／5V；SOP-8 |
| 配置 | 零场电压、灵敏度可配置，内置OTP |
| 测量边界 | 输出反映磁场，位移测量还需磁路映射 |
| 工作电流 | 官网列3～4 mA，按供电和配置 |
| 零场输出 | 1.65 V或2.5 V，可配置 |
| 保存方式 | OTP，写入流程和次数以正式手册为准 |
| 磁滞口径 | 参数表0.1 Gs；特性区另列0.1/0.5 Gs，条件未统一 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR2602-TMR-Linear-Sensors.html)。

## 工作方式与型号定位

TMR2602在TMR检测后集成可编程调理ASIC，可设置零场输出和灵敏度，并通过OTP保留参数。输出仍是磁场相关的模拟电压，不是SPI位置码。

## 安装、接口与配置

3.3V或5V供电与1.65V/2.5V零场配置要匹配ADC范围。零点和增益可编程不表示误差自然消失；校准需要已知输入场，并检查输出端点和负载。

## 校准与选型验证

目录±25Gs用于描述线性工作范围。位置和电流测量还依赖外部磁路，温补后的磁场性能也不能直接替代整机温漂。保存OTP前应先验证全部配置，写后再测零场、正负场和温度点。

## 官方资料

- [TMR2602 官方资料](https://www.dowaytech.com/TMR2602-TMR-Linear-Sensors.html)
