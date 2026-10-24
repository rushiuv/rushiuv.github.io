---
title: "MLX90316"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 89
seed_count: 2
lastmod: "2026-10-24"
description: "MLX90316是Melexis基于Triaxis技术的旋转位置传感器，测量磁场方向并输出与角度有关的信号，常用于非接触式角度检测。"
official_url: "https://www.melexis.com/en/product/MLX90316/Triaxis-mainstream-rotary-position-sensor-IC-Analog-PWM-SPI"
related_companies: ["Melexis"]
datasheet_url: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90316-datasheet-melexis.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mlx90316-datasheet-figure.jpg"
product_image_caption: "mlx90316 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90316-datasheet-melexis.pdf"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 磁检测 | Triaxis 三维磁感应 |
| 输出选项 | 模拟量、PWM 或数字接口，依完整订货后缀 |
| 编程 | 可编程传输曲线 |

参数来源：本页所列[原厂产品资料与手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90316-datasheet-melexis.pdf)。

## 工作方式与型号定位

MLX90316利用Triaxis检测磁场方向，并把位置转换为所选输出。它适合非接触位置传感，模拟、PWM和数字接口需要按完整订货后缀确认。

## 安装、接口与配置

可编程传输曲线用于把机械行程映射到电气输出。确定输入角度、输出斜率、限幅和诊断区后，控制器才有明确的电压或占空比到位置关系，不能只用满量程比例换算。

## 校准与选型验证

磁体结构与感应平面决定实际可用的角度范围。验证需包含端点、过零、温度及气隙变化，并检查异常场或供电条件下输出如何表达；不能把正常范围内的平滑曲线等同于故障可检测。

## 官方资料

- [MLX90316 原厂资料入口](https://www.melexis.com/en/product/MLX90316/Triaxis-mainstream-rotary-position-sensor-IC-Analog-PWM-SPI)
- [MLX90316 数据手册（官方 PDF）](https://www.melexis.com/-/media/files/documents/datasheets/mlx90316-datasheet-melexis.pdf)
