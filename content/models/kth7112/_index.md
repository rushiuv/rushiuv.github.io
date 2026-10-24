---
title: "KTH7112"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 126
seed_count: 1
lastmod: "2026-10-24"
description: "KTH7112是昆泰芯KTH71系列中针对在轴应用的自校准磁编码器。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7112%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth7112-datasheet-figure.jpg"
product_image_caption: "kth7112 原厂手册插图（PDF 第 4 页）"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7112%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位，360°；理想码距约0.005493°，计算值不是精度 |
| 安装/INL | 在轴；产品特点校准后<±0.07°；关键表另列±0.1°，条件不合并 |
| 工作供电 | 关键表3.0～5.0V、典型3.3V；特性页3.3～5V，分别保留 |
| 磁场条件 | 30～150mT，典型60mT；关键指标表 |
| 典型电流 | 16mA（3.3V），关键指标表 |
| 典型启动 | 20ms；实际启动配置需核对 |
| 数据更新 | 1µs，不能直接当成任意运动下完整链路延时 |
| 噪声 | 0.015°（1σ），关键指标表 |
| 最高转速 | 120000rpm，按手册工作条件 |
| 温度 | −40～125°C |
| SPI | 三线，Mode3；最高10Mbps；16位角度+8位CRC |
| SSI | 最高5Mbps |
| ABZ | 4～16384步/圈，支持绝对位置启动功能 |
| UVW | 1～32对极，可编程 |
| PWM | 12位角度；约120Hz～3.8kHz可编程，可指示校准状态 |
| 封装 | QFN 3×3mm-16L |
| 保存 | ANLC系数及配置存入MTP |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7112%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 与7111的边界

KTH7112面向在轴应用，不把KTH7111的离轴精度转写为本型号保证。校准后±0.07°属于产品特点给出的在轴条件，其他概述里的“优于±0.1°”应保留原语境，不能当成两项可任意互换的保证值。

## SPI接入与校验

手册规定三线SPI、CPOL=1及CPHA=1，读角度和寄存器提供8位CRC。该三线接法不应按并联CS的通用从机拓扑直接照搬；多器件连接应按手册方案确认数据线与控制关系。

## ABZ上电启动功能

绝对位置启动可在上电后以一段AB脉冲表达位置。接收端必须区分启动补发与正常运动计数，确认方向和计数初始化；不能只看到AB脉冲就将其全部用于运行速度估计。

## 从校准到整机

先固定磁体、轴线和气隙，再按ANLC流程运行并保存。重新上电复测零点、正反转残差和PWM模式。1µs更新、SPI传输与滤波响应分别进入控制时序，不应压成一个未经验证的“零延迟”结论。

## 官方资料

- [KTH7112 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html)
- [KTH7112 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7112%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
