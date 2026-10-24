---
title: "HAL9303R"
wiki: true
wiki_type: "model"
wiki_rank: 121
seed_count: 1
lastmod: "2026-10-24"
description: "HAL9303R是深圳霍尔微电子官网的线性霍尔传感器，其模拟输出随敏感面上的磁场强度变化，应用可涉及摇杆和磁位移检测。"
official_url: "https://www.szhall.cn/products/250.html"
wiki_category: "线性磁场与位移映射"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/hal9303r-official.png"
product_image_caption: "HAL9303R 原厂产品页的霍尔器件封装组图，非单一订货封装"
product_image_source: "https://www.szhall.cn/products/250.html"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 厂家 | 深圳霍尔微电子 |
| 感应类型 | 线性霍尔 |
| 输出 | 模拟磁场信号 |
| 应用方向 | 摇杆、磁位移检测 |
| 工作电压 | 1.6～3.6V，官网产品页 |
| 供电电流 | VCC=1.8V时IDD<1.5mA，原厂页面口径 |
| 零磁场输出 | 约VCC/2 |
| 感应极性 | TO/SW标记面N极增强时输出升高，SO封装极性相反；依封装核对 |
| 工作温度 | −40～150°C |
| 封装选项 | SOT-23/SO、DFNWB1616/SW、TO-92S/UA |

参数依据：[原厂产品页或对应资料](https://www.szhall.cn/products/250.html)。

## 产品功能与测量链

HAL9303R输出磁场相关的模拟电压，可配磁体用于摇杆或位移检测。输出反映敏感方向上的磁场，不直接等于角度或毫米。

## 接入与配置

摇杆磁路需在全行程保持足够的电压变化，同时避开输出饱和。零场电压、灵敏度和输出摆幅应与控制器ADC的量程、参考及采样阻抗匹配。

## 使用与验证

目前不能从同名或相邻线性霍尔料号借用带宽与温度参数。实际验证需给出磁体极性、距离、行程、负载和温度，保留电压到机械位置的标定曲线。

## 官方资料

- [HAL9303R 原厂资料入口](https://www.szhall.cn/products/250.html)
