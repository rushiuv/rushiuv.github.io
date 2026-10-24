---
title: "TMR2617S"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 145
seed_count: 1
lastmod: "2026-10-24"
description: "TMR2617S在此对应多维官网的TMR2617S-AAC线性磁场传感器。"
official_url: "https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html"
related_companies: ["多维科技"]
wiki_category: "线性磁场与位移映射"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tmr2617s-official.jpg"
product_image_caption: "TMR2617S 原厂产品／封装图"
product_image_source: "https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html"
---

## 核心性能

### 产品介绍

TMR2617S在此对应多维官网的TMR2617S-AAC线性磁场传感器。它属于线性磁场产品线，不能因为TMR前缀就视为数字角度编码器。 [官方资料](https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html)

### 核心参数

- **对应型号** TMR2617S-AAC
- **感应技术** TMR 线性磁场检测
- **测量输出** 磁场分量

### 接口与输出

TMR2617S 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **测量输出** 磁场分量

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

线性磁场传感器把某一方向的磁通密度转换为电信号。磁体移动会改变该分量，但场强与机械位移通常不是简单线性关系，系统需根据磁路建立转换曲线。

单个输出可能同时受距离、方向和背景场影响。只有限定机械自由度并完成标定，才能把它稳定解释为键程、摇杆位置或其他位移量。

### 典型应用与使用条件

比例式输出可以在合适供电参考下减轻一部分电源变化影响，但不能消除零点、灵敏度温漂和ADC误差。比较噪声时，也要同时确认带宽与磁场灵敏度。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [TMR2617S 原厂资料入口](https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html)
