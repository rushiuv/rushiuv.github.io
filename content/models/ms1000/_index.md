---
title: "MS1000"
wiki: true
wiki_type: "model"
wiki_rank: 133
seed_count: 1
lastmod: "2026-10-24"
description: "MS1000 是 Safran 的电容式 MEMS 加速度计系列，提供模拟输出，不同成员覆盖 ±2 g 至 ±100 g 量程。"
official_url: "https://www.safran-group.com/products-services/ms1000-tactical-grade-mems-accelerometer"
wiki_category: "加速度与惯性测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 器件类型 | 单轴模拟加速度计系列 |
| 系列量程 | ±2 g 至 ±100 g，参数依成员 |
| ±2 g 档长期零偏重复性 | 0.24 mg |
| ±2 g 档运行偏置稳定性 | 3 µg |
| ±2 g 档噪声 | 7 µg/√Hz |
| 测量轴／输出 | 单轴，差分模拟±2.7V；内置自检与温度传感器 |
| 供电 | MS1002表：3.2～3.4V，3.3V典型；20°C条件除另说明 |
| 电流 | MS1002表：2.3mA典型、4mA最大，按数据手册条件 |
| 频率响应 | MS1002、MS1005的−3dB频率200Hz；不扩展到所有成员 |
| 封装／尺寸 | LCC20陶瓷密封，9×9×3.5mm |
| 工作温度 | −40～125°C；具体温度性能按各成员参数表 |

参数依据：[原厂产品页或对应资料](https://www.safran-group.com/download/media/413479)。

## 产品功能与测量链

MS1000为模拟输出电容式MEMS加速度计系列，用来测量比力和振动。系列量程从±2g延伸到±100g，不同量程对应不同成员，不能把±2g的噪声参数套给全系列。

## 接入与配置

±2g档的长期零偏重复性0.24mg、运行偏置稳定性3µg与噪声密度7µg/√Hz是不同时间尺度和统计定义。若计算某带宽内的随机噪声，应先明确频率响应及等效噪声带宽。

## 使用与验证

模拟接入需将供电、输出摆幅、ADC参考和抗混叠滤波一起核对。验收分静态重力翻转、温度零偏、比例因子和振动频响；单次静止平均不能证明长期漂移和冲击恢复均合格。

## 官方资料

- [MS1000 原厂资料入口](https://www.safran-group.com/products-services/ms1000-tactical-grade-mems-accelerometer)

- [MS1000数据手册30S.MS1000.H.08.23，第1～3页](https://www.safran-group.com/download/media/413479)
