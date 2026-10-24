---
title: "TMR3002／3004／3005"
description: "双桥模拟角度器件组，主要区别是桥阻、适用磁场与封装选项。"
wiki: true
wiki_type: "model"
wiki_rank: 226
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "模拟角度"
catalog_vendor: "多维科技"
catalog_type: "模拟角度"
catalog_form: "芯片"
search_aliases: ["TMR3002","TMR3004","TMR3005"]
official_url: "https://www.dowaytech.com/sensor/angle_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 测量范围 | 360°磁场方向，模拟差分输出，后端须采样解算 |
| 桥阻区别 | TMR3002目录350kΩ；TMR3004为15kΩ；3005另有多阻值版本 |
| 工作场强 | 3002：70～400Gs；3004：150～1100Gs；3005：200～800Gs |
| 边界 | 不是内部输出数字角度的编码器ASIC |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/angle_sensors.html)。

## 工作方式与型号定位

TMR3002、3004与3005采用模拟角度桥路，输出SIN/COS供后级求角。它们不是带SPI和数字滤波的磁编码ASIC，后端采集方式会参与最终系统误差。

## 安装、接口与配置

桥阻从350kΩ到15kΩ及多阻值选件差异很大，应同时考虑驱动电流、输入偏置及采样建立时间。相同供电下不能假定各成员具有相同输出负载能力。

## 校准与选型验证

70～400Gs、150～1100Gs与200～800Gs分别属于所列成员。选择磁体应按对应窗口验证全圈幅度，校准则先处理桥路偏置和幅相失配，再测机械角度残差。

## 官方资料

- [TMR3002／3004／3005 官方资料](https://www.dowaytech.com/sensor/angle_sensors.html)
