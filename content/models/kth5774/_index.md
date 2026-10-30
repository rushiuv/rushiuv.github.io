---
title: KTH5774
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5774 面向摇杆和操纵杆，公开v1.3手册首页列出UART/I²C数字接口、双路模拟输出以及中点和外圈多点校准，适合评估不同主控的输入路径。
wiki_rank: 307
catalog_type: 线性磁场
wiki_category: 线性磁场
official_url: https://chat.connteck.com/products/3d-hall/KTH5774/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5774/
search_aliases:
- KTH5774
datasheet_url: https://chat.connteck.com/downloads/KTH5774/KTH5774_Datasheet_v1.3.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/joystick-original.jpg
product_image_caption: KTH5774 原厂摇杆应用示意，公开说明书第1页，与KTH5771说明书共用同图
product_image_source: https://chat.connteck.com/downloads/KTH5774/KTH5774_Datasheet_v1.3.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 感知与转换 | XYZ三轴Hall；内部16 bit ADC；首页功能说明；非16位机械精度保证（手册第1页） |
| 应用与输出 | 摇杆/操纵杆；数字UART与I²C；双路模拟输出；首页功能说明；不扩展为四路差分输出或已确认全部输出可同时开启（手册第1页） |
| 数字接口 | UART波特率可编程；I²C快速模式400 kHz；首页功能说明；具体寄存器、引脚复用和时序尚未完整核读（手册第1页） |
| 主电源 | 2.8～5.5 V；首页工作范围；尚未核读完整电参数表（手册第1页） |
| 工作温度 | −40～85°C；首页功能说明；不增加车规等级（手册第1页） |
| 校准 | 中点、外圈多点校准；首页功能说明；需按实际磁体与机构执行（手册第1页） |
| 坐标控制 | 直角坐标控制与极坐标控制为应用控制方式；不据首页应用描述断言芯片寄存器直接提供极坐标数据（手册第1页） |

## 数字与模拟路径各有接入条件

v1.3手册首页列UART可编程波特率、I²C快速400kHz和双路模拟输出。数字帧、模拟摆幅、引脚复用和能否同时启用仍应按完整手册核对；不能把这组功能直接写成无需改动旧电位器电路。

## 多点校准对应实际摇杆机构

首页列出中点与外圈多点校准。装配后应分别检查回中偏移、各方向满量程和斜向轨迹，并保存磁体与机构对应的配置；同一芯片用于不同控制板，也需要统一中心、方向、端点和死区定义。

## 坐标控制方式与寄存器输出分开

手册首页将直角坐标和极坐标作为应用控制方式介绍。应用可以在主控中完成坐标变换，不能仅凭该介绍认定芯片寄存器直接输出极坐标；具体字段、比例和更新方式需要回到通信协议确认。


## 公开资料与型号核对

参数优先采用原PDF v1.3首页：XYZ、内部16bitADC、I²C400kHz、UART与双路模拟；网页12bit框图和1MHz I²C不采用。

首页没有确认四路差分、全部输出同时工作或芯片寄存器直接输出极坐标，不增加这些能力。

尚未核读完整电参数表、阈值、车规或封装；电位器直替和主控无需改动不作为兼容保证。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5774_Datasheet_v1.3.pdf](https://chat.connteck.com/downloads/KTH5774/KTH5774_Datasheet_v1.3.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5774/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

