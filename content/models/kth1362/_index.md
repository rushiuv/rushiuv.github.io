---
title: KTH1362
description: KTH1362是X轴全极霍尔开关，检测X轴方向的磁场阈值，用数字状态报告磁体是否进入感应区域。
catalog_vendor: 昆泰芯
catalog_type: X轴全极霍尔开关
catalog_form: 芯片
wiki: true
wiki_type: model
model_card: true
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
official_url: https://chat.connteck.com/products/switches/
---

KTH1362是昆泰芯的X轴全极霍尔开关，检测X轴方向的磁场阈值，用数字状态报告磁体是否进入感应区域。

## 工作方式

X轴指敏感方向，全极表示两种磁极均可参与触发，不表示任意空间方向具有相同响应。设计时先对齐芯片敏感轴与磁体运动路径，再根据最差气隙检查阈值裕量。

## 主要参数

| 项目 | 型号参数 |
| --- | --- |
| 产品名称 | KTH1362 Series - X-Axis Omni-Polar Hall Switch (NMOS Open-Drain) |
| 供电电压 | 2.5 ~ 5.5 V |
| 工作温度 | -40 ~ 125 °C |
| 典型工作电流 | 5.1 uA |
| 封装 | SOT-23-3L |
| 引脚数 | 3 |
典型工作电流用于理解耗电水平；不同工作模式、采样周期与外部负载会改变整机电流。封装名称和引脚数量用于初选，PCB设计仍应核对具体订货型号的引脚与尺寸。
## 型号差异
型号末尾字母属于产品标识，选型和替换时应保留。供电、温度和封装相近不代表输出极性、阈值或引脚完全相同。
## 接入要点
本型号名称明确为开漏输出。输出拉低时由芯片吸收负载电流，释放后由上拉建立高电平；上拉电压、阻值与接收端门限需要同时满足。低功耗采样器件还需检查短时磁场是否能被采样捕捉。
## 产品资料
[昆泰芯产品分类](https://chat.connteck.com/products/switches/) · [完整选型表](https://chat.connteck.com/selector/)
数据手册：当前无可列出的公开PDF链接，接口时序、磁阈值与完整电气条件请向原厂确认。
