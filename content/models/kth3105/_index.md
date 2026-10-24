---
title: "KTH3105"
series_parent: "kth31"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 125
seed_count: 1
lastmod: "2026-10-24"
description: "KTH3105属于昆泰芯比例式线性霍尔相关产品，传感链将磁通密度变化转换为模拟电压，可用于位置或磁场检测。"
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html"
related_companies: ["昆泰芯"]
wiki_category: "线性磁场与位移映射"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心性能

### 产品介绍

KTH3105属于昆泰芯比例式线性霍尔相关产品，传感链将磁通密度变化转换为模拟电压，可用于位置或磁场检测。 [官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html)

### 核心参数

- **所属产品线** KTH31 线性霍尔
- **输出量** 磁场相关的模拟电压
- **型号选择** 灵敏度、零场电压及封装按 KTH3105 对应手册

### 接口与输出

KTH3105 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出量** 磁场相关的模拟电压

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

线性磁场传感器把某一方向的磁通密度转换为电信号。磁体移动会改变该分量，但场强与机械位移通常不是简单线性关系，系统需根据磁路建立转换曲线。

单个输出可能同时受距离、方向和背景场影响。只有限定机械自由度并完成标定，才能把它稳定解释为键程、摇杆位置或其他位移量。

### 典型应用与使用条件

比例式输出可以在合适供电参考下减轻一部分电源变化影响，但不能消除零点、灵敏度温漂和ADC误差。比较噪声时，也要同时确认带宽与磁场灵敏度。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [KTH3105 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html)
