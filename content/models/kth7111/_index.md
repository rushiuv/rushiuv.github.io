---
title: "KTH7111"
description: "KTH7111 是支持离轴测量的 16 位霍尔磁编码器，集成 ANLC 自动非线性校准，适用于磁饼、磁环位置反馈。"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 20
seed_count: 10
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7111%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7111 数据手册"
document_version: "KTH7111 官方公开手册，33 个 PDF 页面；参数采用型号专用手册，不套用系列汇总表"
model_card: true
product_image: "/images/wiki/kth7111-diagram.webp"
product_image_caption: "图片来源：KTH7111 官方数据手册，第 5 个 PDF 页面，功能框图局部。"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7111%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位，360°；理想码距约0.005493°，计算值不是精度 |
| 安装/INL | 在轴或离轴；离轴校准后优于±0.2°，手册条件 |
| 工作供电 | 关键表3.0～5.0V；特性页3.3～5V，使用对应电气条件 |
| 磁场条件 | 30～150mT，典型60mT；关键指标表 |
| 典型电流 | 16mA@3.3V，关键指标表 |
| 典型启动 | 20ms；实际启动配置需核对 |
| 数据更新 | 1µs，不能直接当成任意运动下完整链路延时 |
| 噪声 | 0.015°（1σ），关键指标表 |
| 最高转速 | 120000rpm，按手册工作条件 |
| 温度 | −40～125°C |
| SPI/SSI | 三线SPI最高10Mbps；SSI最高5Mbps |
| ABZ | 4～16384步/圈，可配置；步数不是脉冲线数 |
| UVW | 1～32对极，按输出复用配置 |
| PWM | 12位角度；约120Hz～3.8kHz可编程，兼作校准状态 |
| 封装 | QFN 3×3mm-16L |
| 存储/校验 | MTP；角度读取带8位CRC，按协议处理 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7111%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 为什么用于离轴

KTH7111以霍尔方式感知平面磁场，并提供面向离轴安装的ANLC补偿。离轴结构可为中空轴让出空间，但磁环场分布、径向位置和气隙会改变整圈误差，不能把在轴磁饼条件直接沿用。

## 五种输出不是五套独立引脚

SPI、SSI、ABZ、UVW和PWM需要结合MODE、IO_MUX等配置读取引脚说明。ABZ的16384步/圈与脉冲线数应分开；UVW极对数则与电机换向关系匹配，不等于磁环的全部编码信息。

## 校准怎样验收

ANLC完成后保存配置，再用独立参考记录全圈正反转误差。静态校准结果与运动延时是两项指标，应在既定滤波和转速下分别测量。PWM作为状态输出时，主控也不能继续把占空比都解释为角度。

## 接入与启动

三线SPI的双向线换向、帧长度和CRC需按手册实现；总线速率不是内部刷新率。典型启动20ms也不意味着上电第一帧立即可用。磁场、温度、气隙和输出模式应与验收记录一起保存。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html)
- [下载KTH7111 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7111%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- 资料版本：KTH7111 官方公开手册，33 个 PDF 页面；参数采用型号专用手册，不套用系列汇总表
