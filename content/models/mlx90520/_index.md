---
title: "MLX90520"
wiki: true
wiki_type: "model"
catalog_type: "信号处理"
catalog_form: "芯片"
wiki_rank: 61
seed_count: 3
lastmod: "2026-10-24"
description: "MLX90520是Melexis的电感式位置传感器，采用外部PCB线圈及导电目标物，双输入结构用于角度测量和游标位置处理。"
official_url: "https://www.melexis.com/en/product/MLX90520/22-bit-Inductive-position-sensor-dual-input"
related_companies: ["Melexis"]
datasheet_url: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf"
datasheet_label: "官方数据手册"
wiki_category: "电感与电涡流测角"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mlx90520-datasheet-figure.png"
product_image_caption: "mlx90520 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf"
---

## 核心性能

### 产品介绍

MLX90520是Melexis的电感式位置传感器，采用外部PCB线圈及导电目标物，双输入结构用于角度测量和游标位置处理。 [官方资料](https://www.melexis.com/en/product/MLX90520/22-bit-Inductive-position-sensor-dual-input)

### 核心参数

- **感知方式** 电感式位置检测
- **数字位置分辨率** 22 位
- **输入结构** 双输入
- **外部结构** PCB 线圈与金属靶，依原厂应用设计

### 接口与输出

MLX90520 当前公开资料没有给出可独立核对的数字通信或脉冲接口细节。若器件提供模拟量、开关量或模块级连接，应按官方引脚／线缆定义接入；在取得型号级手册前，本页不补造协议、速率或电平。

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

发射线圈产生交变磁场，导电靶标随轴移动，改变接收线圈中的耦合信号。接收通道得到与位置相关的周期信号，后续电路再进行解调和角度运算。因此线圈和靶标属于测量系统的一部分。

如果使用两条不同周期的码道，可以利用它们的相位关系识别绝对位置；但线圈周期、安装半径和靶标图形必须配套。无永磁体减少了对目标磁铁的依赖，并不表示完全不受电磁和机械环境影响。

### 典型应用与使用条件

气隙变化、偏心、倾斜、附近金属和PCB工艺会影响信号。校准可以补偿稳定、可重复的部分，机械变化和温度引起的结构漂移仍应在整机上测试。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [MLX90520 原厂资料入口](https://www.melexis.com/en/product/MLX90520/22-bit-Inductive-position-sensor-dual-input)
- [MLX90520 数据手册（官方 PDF）](https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf)
