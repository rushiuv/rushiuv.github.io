---
title: "MLX90380"
wiki: true
wiki_type: "model"
catalog_type: "模拟角度"
catalog_form: "芯片"
wiki_rank: 131
seed_count: 1
lastmod: "2026-10-24"
description: "MLX90380是Melexis预编程磁解析器，通过磁场检测提供与旋转角度相关的模拟正余弦输出，可供控制系统后续解算。"
official_url: "https://www.melexis.com/en/product/MLX90380/Preprogrammed-Magnetic-Resolver"
related_companies: ["Melexis"]
datasheet_url: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90380-datasheet-melexis.pdf"
datasheet_label: "官方数据手册"
wiki_category: "模拟角度信号与外部解算"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mlx90380-datasheet-figure.jpg"
product_image_caption: "mlx90380 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90380-datasheet-melexis.pdf"
---

## 核心性能

### 产品介绍

MLX90380是Melexis预编程磁解析器，通过磁场检测提供与旋转角度相关的模拟正余弦输出，可供控制系统后续解算。 [官方资料](https://www.melexis.com/en/product/MLX90380/Preprogrammed-Magnetic-Resolver)

### 核心参数

- **器件类型** Triaxis 磁解析器
- **输出** 比例式模拟正弦／余弦
- **测量轴** 可选 X/Y、X/Z、Z/Y 等配置
- **安装** 轴端或穿轴／离轴布局
- **封装选项** 单 die SOIC-8、双 die TSSOP-16

### 接口与输出

MLX90380 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 比例式模拟正弦／余弦

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

磁敏元件随磁场方向改变输出，芯片向外提供正余弦或相关模拟信号。主控或后级细分器采样这些信号，计算相位，再结合零点与机械关系得到位置。模拟输出把部分信号处理责任留给了系统。

两路信号理想情况下幅值匹配且正交，实际需要处理零点偏移、增益差和相位偏差。接地、参考电压、输入滤波和ADC建立时间也会改变采样结果。

### 典型应用与使用条件

ADC位数描述数字化粒度，不能直接当作角度精度。不同通道错时采样，在快速旋转时可能产生新的相位误差；校准数据则必须对应实际磁体与装配状态。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [MLX90380 原厂资料入口](https://www.melexis.com/en/product/MLX90380/Preprogrammed-Magnetic-Resolver)
- [MLX90380 数据手册（官方 PDF）](https://www.melexis.com/-/media/files/documents/datasheets/mlx90380-datasheet-melexis.pdf)
