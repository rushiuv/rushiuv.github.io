---
title: "TMR2102／2103／2104"
description: "中等量程TMR线性全桥器件，成员灵敏度与工作场强不同。"
wiki: true
wiki_type: "model"
wiki_rank: 234
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "线性磁场"
catalog_vendor: "多维科技"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["TMR2102","TMR2103","TMR2104"]
official_url: "https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 结构 | X轴敏感全桥输出 |
| 场强范围 | 2102／2103目录±30Gs；2104目录±80Gs |
| TMR2102封装 | SOP-8／DFN-8 |
| 系统接口 | 须外部放大、采样与标定，不直接输出位移码 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html)。

## 工作方式与型号定位

TMR2102、2103与2104提供X轴全桥模拟输出，2102/2103目录量程±30Gs，2104为±80Gs。它们与大场强208x系列的输入范围不同。

## 安装、接口与配置

更窄量程与灵敏度需结合磁路选择，避免正常行程进入饱和。放大器增益还要给零场偏置和温度变化留余量，而不是只放大室温时的最大差分信号。

## 校准与选型验证

TMR2102有SOP8与DFN8选件，焊盘和敏感点位置应核对。验收保存原始桥压、供电和参考场，区分传感器线性、放大器误差与后端ADC误差，再建立最终机械量映射。

## 官方资料

- [TMR2102／2103／2104 官方资料](https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html)
