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

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 器件类型 | Triaxis 磁性 pico-resolver |
| 位置输出 | 模拟角度信号 |
| 安装特点 | 小型封装，适合紧凑电机布置 |
| 推荐供电 | 3.1～3.6 V（3.3V版本）；4.5～5.5 V（5V版本） |
| 工作电流 | 3.3V典型4.2 mA、最大5 mA；5V典型4.5 mA、最大5.5 mA；不含输出负载 |
| 工作温度 | −40～160°C |
| 输出刷新 | 典型2 µs；每分量1 µs顺序测量 |
| 跟踪延迟 | FILT=0/2/31分别典型5/7/37 µs；含滤波，非2µs刷新 |
| 磁场档位 | 中场10～70 mT，高场40～160 mT；依版本与轴配置 |
| 输出噪声上限 | 低/中/高带宽5/10/15 mV RMS；B=0、3.3V及第11页指定灵敏度 |
| 角速度口径 | >50,000 e-rpm，指Hall敏感板上的电角转速 |
| 封装 | DFN6-LW，2 × 2.5 × 1 mm |
| 编程 | 板上I²C编程；不是数字角度读取接口 |
| 误差条件 | 未经外部校正：35°C±10°、全温±15°；外部动态幅相/偏置补偿后误差另依中/高场及轴配置，不能直接以1°覆盖全部配置 |

参数来源：本页所列[原厂产品资料与手册](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381)。

资料定位：MLX90381 Rev.003（2026-09-03）第1、10～15页。5V版本为后续扩充；旧Rev.002仅3.3V，不混写。

## 工作方式与型号定位

MLX90381是小封装Triaxis磁解析器，输出两路可选磁场轴的模拟信号，后级MCU完成角度计算。I²C用于板上编程，不应被误写成正常数字角度输出接口。

## 安装、接口与配置

2µs输出刷新与ADC采样、滤波及主控运算分别占用时间。选择XY、XZ或ZY平面以及灵敏度档后，应按磁路核对10～70mT中场或40～160mT高场范围。

## 校准与选型验证

对电机反馈应组合评估模拟共模、采样同步与高温表现。可编程增益和带宽要留下配置；最终模块仍需校准及整圈验证，器件ASIL-B SEooC定位也不自动等于整机达到相应安全等级。

## 官方资料

- [MLX90381 原厂资料入口](https://www.melexis.com/en/product/mlx90381/triaxis-magnetic-pico-resolver)
- [官网文档入口（官方入口）](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381)

- [现行Rev.003手册入口（含5V版）](https://www.melexis.com/en/documents/documentation/datasheets/datasheet-mlx90381)
