---
title: KTH5772
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5772 是摇杆输入用三轴Hall传感器，公开v1.0手册介绍内部16位ADC、UART及I²C数字接口和可配置回报率；实际手感由机构、配置与标定共同决定。
wiki_rank: 306
catalog_type: 线性磁场
wiki_category: 线性磁场
official_url: https://chat.connteck.com/products/3d-hall/KTH5772/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5772/
search_aliases:
- KTH5772
datasheet_url: https://chat.connteck.com/downloads/KTH5772/KTH5772_Datasheet_v1.0.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/joystick-original.jpg
product_image_caption: KTH5772 原厂摇杆应用示意，公开说明书第2页，与KTH5771说明书共用同图
product_image_source: https://chat.connteck.com/downloads/KTH5772/KTH5772_Datasheet_v1.0.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 感知与转换 | XYZ三轴Hall；内部16 bit ADC；第1—2页概述；不能把有效数据量或ADC位数写成机械准确度（手册第1、2页） |
| 数字接口 | UART可编程波特率；I²C快速模式400 kHz；第1—2页功能说明；UART具体波特率范围未在本次读页中核实（手册第2页） |
| 主电源 | 2.8～5.5 V；第2页主要特性工作范围；尚未核读完整电参数表（手册第2页） |
| 工作温度 | −40～85°C；第2页主要特性功能说明；不增加车规等级（手册第2页） |
| 休眠功耗 | 2.4 µA；第2页主要特性休眠模式说明；不与最高回报率写成同一工作点（手册第2页） |
| 回报率 | 可配置，最高超过1 kHz；第1—2页功能说明；需结合配置、通信与主控采样验收（手册第2页） |
| 数据口径 | 概述称有效数据量超过4096；概述说明，不转换为绝对12位精度、有效位数或噪声保证（手册第1、2页） |

## 数据量不是机械位置精度

v1.0手册概述写内部16bitADC及有效数据量超过4096，二者分别描述内部转换和输出数据口径，不能据此写成16位机械精度或绝对12位准确度。机构中心稳定性、噪声和全行程线性应以实际输出与运动参考比较。

## 数字通信与回报周期一起安排

目视读页确认UART波特率可编程、I²C快速模式400kHz，回报率可配置且最高超过1kHz。主控应按实际帧长、更新节拍和总线占用安排读取，不能从总线时钟或回报率独自推断完整输入延时。

## 休眠与动作响应是两个工作点

手册首页的2.4µA属于休眠说明；快速动作时还要计算测量、通信和主控处理功耗。应以目标手柄的扫描节拍验证唤醒后的首个有效数据以及快速往返、斜向满推和回中，避免扩大死区掩盖装配或映射误差。


## 公开资料与型号核对

参数优先采用原PDF v1.0第1—2页可见说明：内部16bitADC、UART可编程、I²C400kHz；网页框图12bit及I²C1MHz不作为本页依据。

有效数据量超过4096不改写为绝对12位精度，内部ADC位数也不等于机械位置准确度。

尚未核读完整电参数表，不采用网页无需整机校准、千万元寿命或任意方案直接升级的保证。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5772_Datasheet_v1.0.pdf](https://chat.connteck.com/downloads/KTH5772/KTH5772_Datasheet_v1.0.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5772/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

