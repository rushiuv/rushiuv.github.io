---
title: KTH5763
description: KTH5763是昆泰芯面向手表类应用的低功耗3D霍尔角度传感器，用磁场方向变化进行非接触位置检测。
catalog_vendor: 昆泰芯
catalog_type: 3D霍尔角度传感器
catalog_form: 芯片
wiki: true
wiki_type: model
model_card: true
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
official_url: https://chat.connteck.com/products/3d-hall/
---

KTH5763是昆泰芯面向手表类应用的低功耗3D霍尔角度传感器，用磁场方向变化进行非接触位置检测。

## 工作方式

磁体运动改变芯片附近的磁场，器件感知场方向并提供角度相关信息。感应结果依赖磁体、气隙和安装几何；三维磁场感知不表示三个轴均能在任意磁路下输出相同精度的机械角度。

## 主要参数

| 项目 | 型号参数 |
| --- | --- |
| 产品名称 | KTH5763 - Low-Power 3D Hall Angle Sensor (8-bit) |
| 供电电压 | 2.8 ~ 5.5 V |
| 工作温度 | -40 ~ 85 °C |
| 典型工作电流 | 4.89 mA |
| 封装 | DFN2x2.5-8L |
| 引脚数 | 8 |

典型工作电流4.89mA用于理解耗电水平，实际平均功耗还取决于采样、休眠和主控读取方式。

## 型号差异

KTH5763产品名称标注8位，不能套用同系列其它型号的分辨率。DFN2x2.5-8L封装适合紧凑布局，仍需核对引脚与磁体相对位置。

## 接入要点

先确认接口类型、引脚复用和逻辑电平，再安排上电与读取时序。主控刷新周期、器件采样模式和功耗预算应一起设计，不能用典型电流倒推出采样速度。磁体偏心、倾斜和附近铁磁件会影响最终角度表现。

## 产品资料

[昆泰芯3D霍尔产品](https://chat.connteck.com/products/3d-hall/) · [完整选型表](https://chat.connteck.com/selector/)

数据手册：当前无可列出的公开PDF链接，接口时序与完整电气条件请向原厂确认。
