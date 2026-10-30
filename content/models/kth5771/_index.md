---
title: KTH5771
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5771 是面向摇杆与操纵输入的三轴Hall传感器，公开v1.0手册首页提供双路模拟输出，并通过中点、外圈校准和磁场分量比值处理完成机构输入映射。
wiki_rank: 305
catalog_type: 线性磁场
wiki_category: 线性磁场
official_url: https://chat.connteck.com/products/3d-hall/KTH5771/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5771/
search_aliases:
- KTH5771
datasheet_url: https://chat.connteck.com/downloads/KTH5771/KTH5771_Datasheet_v1.0.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/joystick-original.jpg
product_image_caption: KTH5771 原厂摇杆应用示意，公开说明书第1页
product_image_source: https://chat.connteck.com/downloads/KTH5771/KTH5771_Datasheet_v1.0.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 感知与转换 | XYZ三轴Hall；内部16 bit ADC；首页功能说明；ADC内部位数不等于16位机械位置精度（手册第1页） |
| 输出 | 双路模拟输出；首页功能说明；未据此增加UART、差分四路或具体摆幅规格（手册第1页） |
| 主电源 | 2.8～5.5 V；首页工作范围；尚未核读完整电参数表（手册第1页） |
| 工作温度 | −40～85°C；首页功能说明；不增加车规或高温等级（手册第1页） |
| 休眠功耗 | 2.4 µA；首页休眠模式说明；不是快速回报模式电流，也不是整机待机电流（手册第1页） |
| 快速回报 | 超过1 kHz；首页快速模式回报率说明；不作为完整链路延时或全条件最小速率保证（手册第1页） |
| 标定与角度计算 | 中点、外圈校准；基于Bz/Bx和Bz/By的ATAN处理；首页功能说明；机构装配标定仍需执行（手册第1页） |

## 双路模拟输出先匹配主控ADC

v1.0手册首页确认双路模拟输出。接入原电位器输入电路时，应进一步核对输出摆幅、负载、ADC参考电压与采样保持要求；本次没有完整核读电参数表，不把网页的差分四路或UART介绍当成已确认接口。

## 中点与外圈需要分别校准

手册首页列出中点、外圈校准，并介绍基于Bz/Bx和Bz/By的ATAN处理。机构回中、磁体高度和倾斜会改变这些比值，装配后应记录中心、轴向端点和斜向轨迹，避免把芯片出厂处理当作整机免校准。

## 休眠电流与快速模式分开预算

首页的2.4µA休眠说明和超过1kHz快速回报率属于不同模式。电池设计应把唤醒、测量、模拟输出负载及主控采样计入同一周期，再验证响应和平均电流，不能把最低功耗配最高刷新率。


## 公开资料与型号核对

本页优先采用目视核读的原PDF v1.0首页功能说明；只确认XYZ、内部16bitADC和双路模拟输出。

网页UART、差分输出具体通道和摆幅未由本次PDF读页证实，不增加保证；价格低20%不采用。

休眠2.4µA与快速回报超过1kHz是不同模式；未完整核读电参数表、阈值或封装。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5771_Datasheet_v1.0.pdf](https://chat.connteck.com/downloads/KTH5771/KTH5771_Datasheet_v1.0.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5771/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

