---
title: "SS49E"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 142
seed_count: 1
lastmod: "2026-10-24"
description: "SS49E 在本站对应 Honeywell SS39ET／SS49E／SS59ET 系列的线性霍尔器件，以比例式模拟电压输出磁场信息。"
official_url: "https://automation.honeywell.com/us/en/products/sensing-solutions/sensors/magnetic-sensors/linear-and-angle-sensor-ics"
wiki_category: "线性磁场与位移映射"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心性能

### 产品介绍

SS49E在此按Honeywell的SS39ET／SS49E／SS59ET小型线性霍尔产品理解，通过模拟输出反映磁场分量。它常被用作线性霍尔原理的例子。 [官方资料](https://automation.honeywell.com/us/en/products/sensing-solutions/sensors/magnetic-sensors/linear-and-angle-sensor-ics)

### 核心参数

- **感知方式** 线性霍尔
- **输出** 随供电成比例的模拟电压
- **对应原厂** Honeywell SS39ET／SS49E／SS59ET 产品资料

### 接口与输出

SS49E 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 随供电成比例的模拟电压

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

线性磁场传感器把某一方向的磁通密度转换为电信号。磁体移动会改变该分量，但场强与机械位移通常不是简单线性关系，系统需根据磁路建立转换曲线。

单个输出可能同时受距离、方向和背景场影响。只有限定机械自由度并完成标定，才能把它稳定解释为键程、摇杆位置或其他位移量。

### 典型应用与使用条件

比例式输出可以在合适供电参考下减轻一部分电源变化影响，但不能消除零点、灵敏度温漂和ADC误差。比较噪声时，也要同时确认带宽与磁场灵敏度。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [SS49E 原厂资料入口](https://automation.honeywell.com/us/en/products/sensing-solutions/sensors/magnetic-sensors/linear-and-angle-sensor-ics)
