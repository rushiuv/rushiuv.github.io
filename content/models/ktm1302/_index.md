---
title: KTM1302
description: KTM1302是全极TMR磁开关，把磁场是否越过开关阈值转换为数字状态，可用于接近、开合和位置状态检测。
catalog_vendor: 昆泰芯
catalog_type: 全极TMR磁开关
catalog_form: 芯片
wiki: true
wiki_type: model
model_card: true
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
official_url: https://chat.connteck.com/products/switches/
---

KTM1302是昆泰芯的全极TMR磁开关，把磁场是否越过开关阈值转换为数字状态，可用于接近、开合和位置状态检测。

## 工作方式

全极检测允许两种磁极参与触发，但触发距离仍取决于磁体和感应方向。主控读取的是开关状态，不是连续角度或绝对距离；装配误差和杂散磁场需要纳入阈值裕量。

## 主要参数

| 项目 | 型号参数 |
| --- | --- |
| 产品名称 | KTM1302 Series - Omni-Polar TMR Magnetic Switch |
| 供电电压 | 1.8 ~ 5.5 V |
| 工作温度 | -40 ~ 125 °C |
| 典型工作电流 | 160 nA |
| 封装 | SOT-23-3L |
| 引脚数 | 3 |
典型工作电流用于理解耗电水平；不同工作模式、采样周期与外部负载会改变整机电流。封装名称和引脚数量用于初选，PCB设计仍应核对具体订货型号的引脚与尺寸。
## 型号差异
型号末尾字母属于产品标识，选型和替换时应保留。供电、温度和封装相近不代表输出极性、阈值或引脚完全相同。
## 接入要点
输出端应按实际输出级连接接收器。开漏输出需要合适的上拉与负载，推挽输出则需核对高低电平及允许电流；未确认输出级前，不宜照搬另一型号的接法。低功耗器件的采样间隔会影响可捕捉的短时磁场事件，工作电流不能代替响应时间指标。
## 产品资料
[昆泰芯产品分类](https://chat.connteck.com/products/switches/) · [完整选型表](https://chat.connteck.com/selector/)
数据手册：当前无可列出的公开PDF链接，接口时序、磁阈值与完整电气条件请向原厂确认。
