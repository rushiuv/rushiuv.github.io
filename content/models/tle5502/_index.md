---
title: TLE5502系列
wiki: true
wiki_type: model
catalog_type: 模拟角度
catalog_form: 芯片
wiki_rank: 144
seed_count: 1
lastmod: '2026-10-30'
description: TLE5502是英飞凌基于TMR技术的磁角度传感器系列，以模拟正余弦信号为主要输出，供外部控制器采样解算。
official_url: https://www.infineon.com/technology-news/2026/infpss202606-102
related_companies:
- 英飞凌
datasheet_url: https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle5502d-datasheet-en.pdf
datasheet_label: 对应版本手册
wiki_category: 模拟角度信号与外部解算
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
product_image: /images/wiki/tle5502-datasheet-figure.jpg
product_image_caption: TLE5502D 原厂手册封装图；对应 D 后缀双通道器件
product_image_source: https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle5502d-datasheet-en.pdf
catalog_level: 系列
search_aliases:
- TLE5502系列
---

本页采用TLE5502D双通道手册。两个已确认S0002／S0003版本的桥路引脚形式不同，供电与磁场条件也只在对应手册范围内使用。

## 型号与核心异同

| 具体版本 | 桥路／引脚形式 | 共同结构 |
| --- | --- | --- |
| TLE5502D S0002 | 解耦P/N桥 | 双die；PG-VQFN16 |
| TLE5502D S0003 | SIN/COS桥引脚 | 双die；PG-VQFN16 |

## 共同条件与参数依据

- **感应技术**：TMR
- **输出**：模拟正弦／余弦信号
- **处理**：外部 ADC 采样与角度解算
- **推荐供电**：2.7～5.5 V
- **工作磁场**：20～80 mT，需满足温度与磁体温度系数曲线
- **扩展磁场**：80～130 mT时输出幅度可低于规定最小值，不等同正常保证区
- **环境温度**：−40～150°C
- **角速度**：功能范围最高1×10^6 °/s；按手册第9页
- **输出幅度特征**：最高0.33 V/V，比例式差分模拟桥输出
- **安全条件**：ASIL-D SEooC能力需外部安全机制；并非整机认证

## 接入电路与配置

模拟接入应同时检查共模、摆幅、负载和采样同步。正余弦波形看似平滑仍会有幅差、偏置及正交误差，后端补偿需要相应原始数据。

## 标定与应用验证

双通道可用于比较，但共用磁体和装配会引入共因误差。验证应包括每通道整圈误差、通道差与温度变化，以及外场、供电和断线时的行为，不能以两路一致代替机械参考。

## 官方资料

- [TLE5502 原厂资料入口](https://www.infineon.com/technology-news/2026/infpss202606-102)
- [对应版本手册（PDF）](https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle5502d-datasheet-en.pdf)

下载件对应 TLE5502D；其中双通道及供电条件不代表所有 TLE5502 成员。
