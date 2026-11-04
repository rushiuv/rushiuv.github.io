---
title: MS1000系列
wiki: true
wiki_type: model
wiki_rank: 133
seed_count: 1
lastmod: '2026-10-30'
description: MS1000 是 Safran 的电容式 MEMS 加速度计系列，提供模拟输出，不同成员覆盖 ±2 g 至 ±100 g 量程。
official_url: https://www.safran-group.com/products-services/ms1000-tactical-grade-mems-accelerometer
wiki_category: 加速度与惯性测量
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
catalog_level: 系列
search_aliases:
- MS1000系列
---

MS1000是单轴模拟MEMS加速度计系列。系列覆盖±2g至±100g，但本页已核对的细项主要来自MS1002；不同量程不能共用其噪声与零偏结论。

## 型号与核心异同

| 已确认成员／档位 | 已核对内容 | 不能外推的项目 |
| --- | --- | --- |
| MS1002 | 供电3.2～3.4V；电流典型2.3mA、最大4mA；−3dB频率200Hz | 按20°C及手册其他条件读取 |
| MS1005 | −3dB频率200Hz | 其余成员电气参数分别核对 |
| ±2g档（完整型号按订货表） | 长期零偏重复性0.24mg；运行偏置稳定性3µg；噪声7µg/√Hz | 不作为全系列共同性能 |

## 共同条件与参数依据

- **器件类型**：单轴模拟加速度计系列
- **系列量程**：±2 g 至 ±100 g，参数依成员
- **测量轴／输出**：单轴，差分模拟±2.7V；内置自检与温度传感器
- **封装／尺寸**：LCC20陶瓷密封，9×9×3.5mm
- **工作温度**：−40～125°C；具体温度性能按各成员参数表

## 接口与安装

±2g档的长期零偏重复性0.24mg、运行偏置稳定性3µg与噪声密度7µg/√Hz是不同时间尺度和统计定义。若计算某带宽内的随机噪声，应先明确频率响应及等效噪声带宽。

## 动态与装配验证

模拟接入需将供电、输出摆幅、ADC参考和抗混叠滤波一起核对。验收分静态重力翻转、温度零偏、比例因子和振动频响；单次静止平均不能证明长期漂移和冲击恢复均合格。

## 官方资料

- [MS1000 原厂资料入口](https://www.safran-group.com/products-services/ms1000-tactical-grade-mems-accelerometer)

- [MS1000数据手册30S.MS1000.H.08.23，第1～3页](https://www.safran-group.com/download/media/413479)
