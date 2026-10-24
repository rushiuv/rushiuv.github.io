---
title: "MLX90381"
wiki: true
wiki_type: "model"
catalog_type: "模拟角度"
catalog_form: "芯片"
wiki_rank: 132
seed_count: 1
lastmod: "2026-10-24"
description: "MLX90381 是 Melexis 小型 Triaxis 磁解析器，输出供外部采样解算的模拟角度信号，适用于紧凑电机位置反馈。"
official_url: "https://www.melexis.com/en/product/mlx90381/triaxis-magnetic-pico-resolver"
related_companies: ["Melexis"]
datasheet_url: "https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381"
datasheet_label: "官网文档入口"
wiki_category: "模拟角度信号与外部解算"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mlx90381-application.png"
product_image_caption: "MLX90381 电机位置检测应用示意；来源为该型号原厂宣传页"
product_image_source: "https://media.melexis.com/-/media/files/documents/product-flyers/mlx90381-product-flyer-melexis.pdf"
---

## 核心性能

### 产品介绍

MLX90381是Melexis的Triaxis磁pico-resolver，面向紧凑旋转测量，提供供后续处理的磁角度信号。小封装有助于嵌入空间有限的机电系统。 [官方资料](https://www.melexis.com/en/product/mlx90381/triaxis-magnetic-pico-resolver)

### 核心参数

- **器件类型** Triaxis 磁性 pico-resolver
- **位置输出** 模拟角度信号
- **安装特点** 小型封装，适合紧凑电机布置

### 接口与输出

MLX90381 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **位置输出** 模拟角度信号

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

磁敏元件随磁场方向改变输出，芯片向外提供正余弦或相关模拟信号。主控或后级细分器采样这些信号，计算相位，再结合零点与机械关系得到位置。模拟输出把部分信号处理责任留给了系统。

两路信号理想情况下幅值匹配且正交，实际需要处理零点偏移、增益差和相位偏差。接地、参考电压、输入滤波和ADC建立时间也会改变采样结果。

### 典型应用与使用条件

ADC位数描述数字化粒度，不能直接当作角度精度。不同通道错时采样，在快速旋转时可能产生新的相位误差；校准数据则必须对应实际磁体与装配状态。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [MLX90381 原厂资料入口](https://www.melexis.com/en/product/mlx90381/triaxis-magnetic-pico-resolver)
- [官网文档入口（官方入口）](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381)
