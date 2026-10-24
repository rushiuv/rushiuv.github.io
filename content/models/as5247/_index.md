---
title: "AS5247"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 114
seed_count: 1
lastmod: "2026-10-24"
description: "AS5247是双芯片在轴磁角度传感器，将两套角度测量通道放入同一封装，为需要通道比较的系统提供基础。"
official_url: "https://www.infineon.com/part/AS5247"
related_companies: ["英飞凌"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5247-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/as5247-official.jpg"
product_image_caption: "AS5247 原厂产品／封装图"
product_image_source: "https://www.infineon.com/part/AS5247"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 测量结构 | 同一封装内双 die、双角度通道 |
| 绝对角度分辨率 | 14 位 |
| 安装方式 | 在轴磁体 |
| 系统用途 | 双路位置读取与通道比较 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |
| 5V工作供电 | 4.5～5.5 V |
| 3.3V常规模式 | 3.0～3.6 V，−40～125°C；扩展150°C需按手册设置对应位及电压条件 |
| 工作磁场 | 35～70 mT，芯片表面规定测量几何；低于35mT噪声性能下降 |
| ABI分辨率 | 512脉冲/圈=2048步/圈；可选256脉冲/圈=1024步/圈 |
| UVW | 1～7对极可编程 |
| 供电电流上限 | 每die 15 mA；双die合计应乘2 |
| 噪声上限 | NOISESET=0：0.068° RMS；NOISESET=1：0.082° RMS，均为原表Max列，按手册磁场条件 |
| INL（最佳安装，25°C） | 最大±0.9° |
| 封装 | TSSOP-28，双die |

参数来源：本页所列[原厂产品资料与手册](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5247-datasheet-en.pdf)。

资料定位：AS5247 v1-10（2016-12-05）正文第1、7～8页，供电扩展温度条件不得省略。

## 工作方式与型号定位

AS5247将两套角度测量通道放入同一封装，为双路位置读取和一致性检查提供器件基础。它的价值在于系统可以比较通道，而不只是把输出位数相加。

## 安装、接口与配置

两通道共用被测磁体时，磁体松动、安装整体偏移及外部磁场属于需要检查的共因问题。两路角度一致只能说明通道相互接近，不能单独证明它们都与机械真值一致。

## 校准与选型验证

接入需分别核对两路供电、接口、零点和数据时间。验收应包含通道差随温度和转速的变化以及故障处理；若用于安全架构，还需结合原厂安全文档，不能仅凭双die结构宣布整机满足功能安全。

## 官方资料

- [AS5247 原厂资料入口](https://www.infineon.com/part/AS5247)
- [AS5247 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5247-datasheet-en.pdf)
