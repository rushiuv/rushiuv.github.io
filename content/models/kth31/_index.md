---
title: KTH31系列
description: KTH31XX 是比例式线性霍尔系列，输出电压随磁场变化，可用于磁场测量或机构位移的前端感知；灵敏度档和机械映射需要分开选。
wiki: true
wiki_type: model
wiki_rank: 206
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 线性磁场
catalog_vendor: 昆泰芯
catalog_type: 线性磁场
catalog_form: 芯片
search_aliases:
- KTH3101
- KTH3102
- KTH3103
- KTH3105
- KTH31XX
- KTH31xx
- KTH3110
- KTH3113
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
model_card: true
datasheet_url: https://conntek.github.io/files/KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
datasheet_label: 数据手册原链接
catalog_source: https://chat.connteck.com/products/linear/KTH31XX/
product_image: /images/catalog/kth31-package.png
product_image_caption: KTH31 系列封装示意，原手册第1页；按完整后缀选择封装
product_image_source: https://conntek.github.io/files/KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
catalog_level: 系列
aliases:
- /models/kth31xx/
---

KTH31是比例式线性霍尔系列，六个成员主要以灵敏度和可用磁场范围区分。先根据磁路最大场强选档，再检查供电、输出摆幅与噪声。

## 六个型号的核心差异

| 具体型号 | 灵敏度：3.3V（mV/Gs） | 灵敏度：5V（mV/Gs） | 典型磁场范围 | 典型输出噪声 |
| --- | --- | --- | --- | --- |
| KTH3101 | 最小0.93、典型1.00、最大1.07 mV/Gs | 最小1.40、典型1.50、最大1.61 mV/Gs | 典型±1400 Gs（3.3 V）；典型±1500 Gs（5.0 V） | 典型2.4 mV RMS |
| KTH3102 | 最小1.53、典型1.65、最大1.76 mV/Gs | 最小2.33、典型2.50、最大2.67 mV/Gs | 典型±840 Gs（3.3 V）；典型±900 Gs（5.0 V） | 典型3 mV RMS |
| KTH3103 | 最小2.10、典型2.25、最大2.41 mV/Gs | 最小3.16、典型3.40、最大3.68 mV/Gs | 典型±620 Gs（3.3 V）；典型±660 Gs（5.0 V） | 典型3.5 mV RMS |
| KTH3105 | 最小3.07、典型3.30、最大3.53 mV/Gs | 最小4.65、典型5.00、最大5.35 mV/Gs | 典型±420 Gs（3.3 V）；典型±450 Gs（5.0 V） | 典型4.8 mV RMS |
| KTH3110 | 最小6.14、典型6.60、最大7.06 mV/Gs | 最小9.30、典型10.00、最大10.70 mV/Gs | 典型±210 Gs（3.3 V）；典型±225 Gs（5.0 V） | 典型7.2 mV RMS |
| KTH3113 | 最小8.28、典型8.90、最大9.52 mV/Gs | 最小12.56、典型13.50、最大14.45 mV/Gs | 典型±150 Gs（3.3 V）；典型±165 Gs（5.0 V） | 典型8.6 mV RMS |

灵敏度列保留最小、典型与最大值，条件为TA=25°C；磁场范围分别对应3.3V与5.0V，均为典型值。噪声为3.3V、25°C下的RMS值，未叠加外部RC滤波。依据原厂手册第6～8页。

## 共用电气与安装条件

- **工作供电**：3.0～5.5 V；典型3.3 V；工作状态；电参数表总条件TA=−40～125°C，除特别说明外（手册第6页）
- **工作温度**：−40～125 °C；系列推荐工作范围；不能用结温或贮存温度替代（手册第1、5页）
- **供电电流（3.3V）**：典型4.5 mA，最大5.5 mA；VDD=3.3 V，B=0 Gs，TA=25°C（手册第6页）
- **供电电流（5V）**：典型5.4 mA，最大6.5 mA；VDD=5.0 V，B=0 Gs，TA=25°C（手册第6页）
- **带宽**：典型30 kHz；电参数表总条件TA=−40～125°C，VDD=3.0～5.5 V；不与外置RC后的带宽混用（手册第6页）
- **上电时间**：典型20 µs，最大40 µs；TA=25°C；其余依电参数表默认条件（手册第6页）
- **最大负载电容**：10 nF；电参数表最大列；外置RC应用电路另按手册第11页（手册第6页）
- **静态电压（3.3V）**：最小1.630 V，典型1.650 V，最大1.670 V；VDD=3.3 V，B=0，TA=25°C（手册第7页）
- **静态电压（5V）**：最小2.475 V，典型2.500 V，最大2.525 V；VDD=5.0 V，B=0，TA=25°C（手册第7页）
- **输出电压线性范围**：0.25 V～VDD−0.25 V；TA=−40～125°C，VDD=3.0～5.5 V，除特别说明外（手册第7页）
- **灵敏度线性误差**：−1.5%～+1.5%；磁参数表最小/最大列；TA=−40～125°C，VDD=3.0～5.5 V，除特别说明外（手册第7页）
- **封装引脚**：SOT23：VDD=1、OUT=2、GND=3；DFN1616/TO-92S：VDD=1、GND=2、OUT=3；按手册封装与俯视图，不能按三脚器件习惯统一接线（手册第2、3页）

## 从磁场到ADC读数

器件输出首先表达敏感轴上的磁场。位移、开度或电流由外部磁路映射；磁体全行程应保持所需的单调关系，并留出供电、气隙和温度变化的裕量。灵敏度更高不代表同一机械行程精度必然更好。

比例式输出需连同ADC参考核算。共用参考可以减少部分供电变化影响，但传感器与ADC的压降、地回路及滤波仍会引入误差。样机应保存零场电压、端点电压、ADC原始码及磁体位置，再检查整段行程残差。

## 版本与替换时要确认什么

公开手册列六档成员；Design Center提到“七档”，本页不把3.3V与5V下的同一成员另算一档。工作电源采用手册3.0～5.5V口径，详情页引脚说明另写4.5～5.5V的冲突需随正式版本确认。

换封装先重核引脚：SOT23的OUT为2脚、GND为3脚；DFN1616和TO-92S则为GND 2脚、OUT 3脚。网站旧图中的三轴ADC框图不用于解释本系列。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html)
- [数据手册原链接](https://conntek.github.io/files/KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
