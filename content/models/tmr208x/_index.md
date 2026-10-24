---
title: "TMR2083／2084"
description: "大磁场量程TMR全桥器件组，适合由外部电路读取模拟桥压。"
wiki: true
wiki_type: "model"
wiki_rank: 233
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "线性磁场"
catalog_vendor: "多维科技"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["TMR2083","TMR2084"]
official_url: "https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 结构 | 全桥，X轴敏感 |
| 场强范围 | 2083目录±500Gs；2084目录±400Gs |
| TMR2083封装 | SOT23-5 |
| 电源边界 | 被动桥路驱动条件不等于带ADC数字芯片的工作条件 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html)。

## 工作方式与型号定位

TMR2083与2084是X轴敏感的模拟全桥器件，分别面向目录±500Gs和±400Gs场强范围。桥压需要后端放大与采样，不包含数字磁场码或机械位置解算。

## 安装、接口与配置

桥路供电影响输出幅度与自热，放大器应检查输入共模、偏置和噪声。大范围并不意味着全范围始终具有相同线性误差，实际工作区还应对照正式手册。

## 校准与选型验证

位置应用需要磁体与机械行程的映射，电流应用还要考虑导体和磁路。验证先做零场、正负场扫描及温度测试，再讨论位移或电流误差，不能将ADC位数当作传感器本身精度。

## 官方资料

- [TMR2083／2084 官方资料](https://www.dowaytech.com/sensor/linear_magnetic_field_sensors.html)
