---
title: "AS5048B"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 78
seed_count: 2
lastmod: "2026-10-24"
description: "AS5048B是14位在轴磁角度传感器，主数字接口为I²C。"
official_url: "https://www.infineon.com/part/AS5048B"
related_companies: ["英飞凌"]
related_models: ["AS5048A"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5048a-as5048b-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/as5048b-official.jpg"
product_image_caption: "AS5048B 原厂产品页所列 TSSOP-14 封装示意（封装共用图）"
product_image_source: "https://www.infineon.com/part/AS5048B"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 绝对角度分辨率 | 14 位 |
| 主数字接口 | I²C |
| 其他位置输出 | PWM |
| 磁路 | 在轴安装 |
| 系列区别 | AS5048A 使用 SPI，不能直接复用其通信程序 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |
| 工作供电 | 5V模式4.5～5.5 V；3.3V模式3.0～3.6 V |
| 供电电流上限 | 15 mA，工作条件表 |
| 温度与模式 | 5V模式−40～150°C；3.3V模式最高125°C |
| 工作磁场 | 30～70 mT，典型50 mT |
| 输出采样率 | 典型11.25 kHz，范围10.2～12.4 kHz |
| 系统传播延迟 | 典型100 µs，范围90.7～110.2 µs |
| PWM频率 | 典型1 kHz，范围0.907～1.102 kHz |
| 输出噪声 | 典型0.06° RMS，14位约2.73 LSB，按手册表条件 |
| INL（最佳安装） | 25°C最大±0.8°；全温最大±1° |
| INL（偏心条件） | 最大±1.2°；N35H磁体Ø8×3mm、X/Y偏移500µm、Z间距2000µm及规定温度 |
| 启动时间 | 最大10 ms |
| 封装 | TSSOP-14，5 × 6.4 mm |

参数来源：本页所列[原厂产品资料与手册](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5048a-as5048b-datasheet-en.pdf)。

资料定位：AS5048A/AS5048B v1-11（2018-01-29）正文第7～8页工作条件/系统表、第10页供电图；当前PDF前置两页英飞凌说明。

## 工作方式与型号定位

AS5048B通过I²C读取在轴磁体的14位绝对角度，适合已有I²C总线的位置节点。I²C角度与PWM输出共用测量结果，但接收端所用的时间基准不同。

## 安装、接口与配置

多器件共用I²C时，应确认地址配置、上拉、电平和总线电容。角度高低字节按手册规定组合，避免自行把不同测量时刻拼成一个数；总线事务耗时也应计入控制器使用位置的总延迟。

## 校准与选型验证

机械零点、编程零点和输出方向需要留下对应关系。更换AS5048A会改变主数字接口，不能仅改器件名继续使用原程序。验证应分别检查全圈连续性、跨零读取和掉电重启后的配置保持。

## 官方资料

- [AS5048B 原厂资料入口](https://www.infineon.com/part/AS5048B)
- [AS5048B 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5048a-as5048b-datasheet-en.pdf)
