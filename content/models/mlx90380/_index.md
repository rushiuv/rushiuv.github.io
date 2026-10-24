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

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 器件类型 | Triaxis 磁解析器 |
| 输出 | 比例式模拟正弦／余弦 |
| 测量轴 | 可选 X/Y、X/Z、Z/Y 等配置 |
| 安装 | 轴端或穿轴／离轴布局 |
| 封装选项 | 单 die SOIC-8、双 die TSSOP-16 |
| 推荐供电 | 3.135～3.6 V（3.3V配置）或4.5～5.5 V（5V配置） |
| 工作电流上限 | 3.3V配置9 mA；5V配置10 mA，不含OUT1/2外部负载 |
| 工作温度 | −40～150°C |
| 输出刷新周期 | 典型4 µs；各磁场分量2 µs，顺序测量 |
| 跟踪延迟 | 高/中/低带宽典型12/29.5/74 µs；最大17.5/38/85.5 µs |
| 可编程满量程磁场 | 10～70 mT，依选件 |
| 输出摆幅／线性 | 10%～90%VDD范围内线性优于0.5%；5%～95%VDD范围内优于1.5% |
| 封装 | SOIC8单die；TSSOP16双die |

参数来源：本页所列[原厂产品资料与手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90380-datasheet-melexis.pdf)。

资料定位：MLX90380 Rev.11（2021-06）第1、13～15页；刷新周期和跟踪延迟分别列出。

## 工作方式与型号定位

MLX90380输出与磁场角度相关的模拟正弦和余弦，控制器在外部完成采样和角度计算。它被称为磁解析器，但接线和信号条件不应直接套用传统绕线旋变。

## 安装、接口与配置

XY、XZ和ZY感应组合用于匹配轴端或穿轴磁路。感应轴选错时，电压仍随运动变化，却不能获得正确的机械角度映射。单die与双die封装也要按具体版本接入。

## 校准与选型验证

同步ADC、前端滤波及比例式参考决定系统误差。先保存两路电压与李萨如轨迹，再处理偏置、幅差和正交误差；最终整圈精度还要与机械参考比较，不能只凭两路波形近似正弦判定。

## 官方资料

- [MLX90380 原厂资料入口](https://www.melexis.com/en/product/MLX90380/Preprogrammed-Magnetic-Resolver)
- [MLX90380 数据手册（官方 PDF）](https://www.melexis.com/-/media/files/documents/datasheets/mlx90380-datasheet-melexis.pdf)
