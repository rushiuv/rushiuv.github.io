---
title: KTM2802P
description: KTM2802P是AMR气缸位置开关，利用磁阻感应判断带磁活塞的位置，以PNP输出向控制端报告检测状态。
catalog_vendor: 昆泰芯
catalog_type: AMR气缸位置开关
catalog_form: 芯片
wiki: true
wiki_type: model
model_card: true
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
official_url: https://chat.connteck.com/products/industrial/
---

KTM2802P是昆泰芯的AMR气缸位置开关，利用磁阻感应判断带磁活塞的位置，以PNP输出向控制端报告检测状态。

## 工作方式

活塞磁体经过传感器时，磁场改变触发输出。它提供位置状态，适合行程端点或特定位置检测；不能直接作为连续位移数值使用。

## 主要参数

| 项目 | 型号参数 |
| --- | --- |
| 产品名称 | KTM2802P (KTM2802PNP) - AMR Cylinder Position Detection Sensor (PNP Open-Drain) |
| 供电电压 | 3.3 ~ 32 V |
| 工作温度 | -40 ~ 105 °C |
| 典型工作电流 | 70 uA |
| 封装 | HFBP2*3-6L |
| 引脚数 | 7 |
典型工作电流用于理解耗电水平；不同工作模式、采样周期与外部负载会改变整机电流。封装名称和引脚数量用于初选，PCB设计仍应核对具体订货型号的引脚与尺寸。
## 型号差异
KTM2802P对应目录中的KTM2802PNP命名；KTM2802N为NPN输出，两者的负载接法和接收端逻辑适配不同。目录封装名与引脚数存在不一致，落板须以封装图和引脚表为准。
## 接入要点
PNP输出向负载提供电流，接收端与负载回路应按PNP接法设计，不能照搬NPN下拉接口。供电旁路、负载电流和控制器输入门限都需要共同核对。
## 产品资料
[昆泰芯产品分类](https://chat.connteck.com/products/industrial/) · [完整选型表](https://chat.connteck.com/selector/)
数据手册：当前无可列出的公开PDF链接，接口时序、磁阈值与完整电气条件请向原厂确认。
