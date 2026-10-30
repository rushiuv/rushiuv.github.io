---
title: KTH5761
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5761AQ3 是带温度输出的三轴数字Hall传感器，V2.0手册首页提供I²C、周期循环和单次测量路径，可用于摇杆、线性位置与非接触磁场感知。
wiki_rank: 304
catalog_type: 线性磁场
wiki_category: 线性磁场
official_url: https://chat.connteck.com/products/3d-hall/KTH5761/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5761/
search_aliases:
- KTH5761
datasheet_url: https://chat.connteck.com/downloads/KTH5761/KTH5761AQ3_DS_CN_V2.0.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/kth5761-browser-original.jpg
product_image_caption: KTH5761 原厂功能框图，AQ3公开手册第1页；接口按正文I²C说明
product_image_source: https://chat.connteck.com/downloads/KTH5761/KTH5761AQ3_DS_CN_V2.0.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 感知与转换 | XYZ三轴磁场、温度输出；内部16 bit ADC；AQ3 V2.0首页说明；ADC位数不是机械位置准确度（手册第1页） |
| 典型磁场量程 | XY典型±65 mT；Z典型±40 mT；首页标注典型量程；不扩大为所有配置和温度下的保证（手册第1页） |
| 接口 | 标准I²C；首页正文说明；不根据框图MISO/CS标签推断支持SPI（手册第1页） |
| 模式 | 周期循环测量、单次测量；首页功能说明；具体周期、电流和转换时间尚未完整核读（手册第1页） |
| 供电 | 主电源2.8～5.5 V；IO供电可低至1.8 V；两类电源区分；不能写为1.8V主电源工作（手册第1页） |
| 温度与封装 | −40～85°C；DFN2×2.5-8L；限AQ3 V2.0首页对应等级和封装，不外推其他等级（手册第1页） |
| 应用定位 | 摇杆、线性位置、非接触磁场感知；首页应用路径，实际位置映射由磁体与机构决定；不局限于手表（手册第1页） |

## 场强与温度先对应目标机构

AQ3 V2.0首页给出XYZ磁场和温度输出，XY典型量程±65mT、Z典型±40mT。它测的是磁场，摇杆和位移仍需要机构对应的轨迹或标定曲线；量程也不能直接换算成角度或毫米行程。

## 周期循环与单次测量各自安排

周期循环适合按节拍更新，单次测量可由主控在需要时发起。选择前应先确定动作响应与功耗预算，再核对相应转换、传输和唤醒条件；本次只读到手册首页，未把空闲电流或网页转换时间写成完整电气保证。

## I²C和IO电源分开核对

首页正文确认标准I²C。主电源2.8～5.5V与最低1.8V的IO电源属于不同条件，低压主控的上拉电源和断电行为应按对应手册核对。框图中的MISO、CS标签不能独自证明该型号提供SPI协议。

## 小封装服务多种感知机构

AQ3首页对应DFN2×2.5-8L和−40～85°C，不只面向手表。用于摇杆、直线机构或磁接近感知时，应分别检查磁体方向、全行程单调性和装配偏移，避免把同一磁场映射直接复制到不同机构。


## 公开资料与型号核对

本页优先采用目视核对的KTH5761AQ3 V2.0原PDF首页，限AQ3后缀；尚未完整核读电参数表。

正文只确认标准I²C，不从框图MISO/CS标签增加SPI能力；网页其他电流、转换时间或性能条件不作为本次已核读参数。

应用包括摇杆、线性位置与非接触磁场感知，不把产品限制为手表专用；ADC16位不等于机械位置精度。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5761AQ3_DS_CN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5761/KTH5761AQ3_DS_CN_V2.0.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5761/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

