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

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感知方式 | 电感式位置检测 |
| 数字位置分辨率 | 22 位 |
| 输入结构 | 双输入 |
| 外部结构 | PCB 线圈与金属靶，依原厂应用设计 |
| 推荐供电 | 4.5～5.5 V，典型5 V |
| 工作温度／封装 | −40～125°C；TSSOP16 |
| 接口 | SPI或SSI，帧内容可配置 |
| 位置误差 | 每输入通道±0.36°电角，±3σ含噪声；LFC=0及延时补偿、理想无偏置信号和规定动态条件 |
| 延时补偿 | 原厂特性列<1 µs；不含接口与主控处理 |
| 噪声（室温典型） | LFC=0/1/2：0.025°电角RMS；LFC=3/4：0.035°；LFC=5/6/7：0.055/0.075/0.100° |
| 工作电流上限 | LC振荡关闭、无MISO负载且fAC≤10MHz时12 mA；Q=18且fAC≤20MHz时20 mA |
| 校准 | 每输入通道16点线性化，机械角与电角换算需按线圈周期 |

参数来源：本页所列[原厂产品资料与手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf)。

资料定位：MLX90520 Rev.001（2026-01-20）第1、9～10页；特别保留°electrical，不改写为机械整圈误差。

## 工作方式与型号定位

MLX90520采用外部PCB线圈与导电目标物，位置来自目标物对电磁耦合的调制。它不需要把永磁体放在芯片上方，磁角度器件的气隙与工作磁场表不能直接用于此方案。

## 安装、接口与配置

双输入用于处理相应线圈信号及游标位置关系。22位描述数字位置表达，机械精度还取决于线圈、目标形状、偏心、倾斜和校准条件。

## 校准与选型验证

样机应按原厂应用设计匹配激励、接收线圈及目标，并扫描气隙、径向偏心和金属邻近物影响。验证既看细分误差，也看游标绝对位置是否跳区；不能只看静止读数末位是否平稳。

## 官方资料

- [MLX90520 原厂资料入口](https://www.melexis.com/en/product/MLX90520/22-bit-Inductive-position-sensor-dual-input)
- [MLX90520 数据手册（官方 PDF）](https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf)
