---
title: KTAx333系列
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTAx333 是精密运算放大器系列入口，来源详情对应 KTA333 单通道型号；用于传感器调理时，需把失调、带宽、共模范围与负载放在同一电路中评估。
wiki_rank: 320
catalog_type: 模拟信号链
wiki_category: 模拟信号链
official_url: https://chat.connteck.com/products/signal-chain/KTA333/
catalog_source: https://chat.connteck.com/products/signal-chain/KTA333/
search_aliases:
- KTAx333
datasheet_url: https://conntek.github.io/files/KTAx333%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/ktax333-original-figure.png
product_image_caption: KTAx333 系列引脚与标记信息（原手册第2页）
product_image_source: https://conntek.github.io/files/KTAx333%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf#page=2
catalog_level: 系列
---

KTAx333是低失调运放系列，KTA333为单通道，KTA2333为双通道。先确定通道数和封装，再按负载、闭环增益及误差预算判断是否适合传感器前端。

## 型号与核心异同

| 具体订货型号 | 通道数 | 封装 | 资料与供货口径 |
| --- | --- | --- | --- |
| KTA333-ST5 | 单通道 | SOT23-5 | 按当前订货状态 |
| KTA333-SF5 | 单通道 | SOT353-5 | Rev1.0标少量样品；当前另核 |
| KTA333-SC5 | 单通道 | SC70-5 | Rev1.0标少量样品；当前另核 |
| KTA333-SP8 | 单通道 | SOP-8 | Rev1.0标少量样品；当前另核 |
| KTA2333-MP8 | 双通道 | MSOP-8 | 按当前订货状态 |
| KTA2333-DZ8 | 双通道 | DFN2020-8 | Rev1.0带星号；当前另核 |
| KTA2333-SP8 | 双通道 | SOP-8 | 按当前订货状态 |

订货表依据公开Rev1.0第12页；历史样品标记不是当前生命周期结论。

## 电气参数及其条件

- **供电**：单电源1.8～5.5 V；双电源±0.9～±2.75 V；推荐工作条件与应用指南；不能把6.5V绝对最大值作为工作电源（手册第4、8页）
- **工作温度**：−40～125 °C；额定温度范围（手册第4、5页）
- **输入失调电压**：典型2 µV，最大10 µV；VS=5 V，TA=25°C、VCM=VS/2、VOUT=VS/2，除特别说明外（手册第1、5页）
- **输入失调漂移**：典型0.02 µV/°C，最大0.05 µV/°C；TA=−40～125°C；电参数表（手册第1、5页）
- **输入共模范围**：(V−)−0.1 V～(V+)+0.1 V；电参数表第5页；不能把该工作范围当作允许输入保护电流的范围（手册第5、8页）
- **距电源轨的输出余量**：表列30 mV、70 mV；应用指南描述小于100 mV；RL=10 kΩ；30mV与70mV的典型/最大属性有待原表确认（手册第5、8页）
- **静态电流**：单通道表列17 µA；双通道表列30 µA；IO=0 A，TA=−40～125°C；单/双通道分别计，不将30µA当每通道（手册第1、5页）
- **增益带宽积**：表列350 kHz；CL=100 pF；TA=25°C、VCM=VS/2、VOUT=VS/2，除特别说明外（手册第5页）
- **压摆率**：表列0.16 V/µs；G=1；电参数表默认条件（手册第5页）
- **低频输入噪声**：表列1.1 µV峰峰值；频带0.1～10 Hz；不能改成RMS噪声（手册第1、5页）
- **启动至额定失调精度**：约200 µs；应用指南；电参数表开通时间条件VS=+5 V（手册第5、8页）
- **失调校正周期**：10 µs；手册第8页斩波自校准机制，不代表输出建立时间（手册第8页）
- **电源旁路建议**：0.1 µF，靠近供电脚；应用指南建议；不同电路仍需确认负载和稳定性（手册第8页）

## 用完整误差预算判断前端是否合适

输入失调只是一项误差，还需计算偏置电流与源阻抗、反馈电阻、参考电压、温漂和ADC。先把闭环增益及输入信号确定下来，再将误差折回输入端比较。

增益带宽、传感器阻抗和负载电容会改变建立时间与稳定性。光电二极管TIA还需评估输入电容和反馈网络；低失调或轨到轨标签不能证明适合任意负载。

轨到轨输出仍有距电源轨的余量，摆幅数据以10kΩ负载为条件。驱动ADC时应复核稳定性、建立时间和饱和恢复；分流电阻测流需要接入被测回路，不属于天然无侵入测量。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://chat.connteck.com/products/signal-chain/KTA333/)
- [数据手册原链接](https://conntek.github.io/files/KTAx333%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
