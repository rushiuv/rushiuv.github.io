---
title: "AS5048A"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 55
seed_count: 3
lastmod: "2026-10-24"
description: "AS5048A是14位在轴磁角度传感器，通过SPI读取绝对位置；与AS5048B共享官方手册，但主数字通信接口不同。"
official_url: "https://www.infineon.com/part/AS5048A"
related_companies: ["英飞凌"]
related_models: ["AS5048B"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5048a-as5048b-datasheet-en.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/as5048a-official.jpg"
product_image_caption: "AS5048A 原厂产品页所列 TSSOP-14 封装示意（封装共用图）"
product_image_source: "https://www.infineon.com/part/AS5048A"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 绝对角度分辨率 | 14 位 |
| 主数字接口 | SPI |
| 其他位置输出 | PWM |
| 磁路 | 轴端两极磁体 |
| 系列区别 | AS5048B 的主数字接口为 I²C |
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

AS5048A在轴测量两极磁体方向，14位全圈共有16384个位置码。SPI承担读角度和配置，PWM把位置变为占空比；两种接口的量化、传输时间与主控采集方式不同。

## 安装、接口与配置

接入SPI时应按本型号命令、返回帧和错误信息处理数据。PWM应捕获完整周期及高电平宽度，读取频率高于PWM更新频率时并不会得到更多独立角度样本。置零只改变起点，不消除磁体偏心造成的误差。

## 校准与选型验证

磁体应对准敏感中心，并在全圈和温度变化下保持规定磁场。与AS5048B替换时首先核对引脚和主数字接口；A版SPI驱动不能直接用于B版I²C。角度误差需用独立参考测量，不能用末位是否跳动判断精度。

## 官方资料

- [AS5048A 原厂资料入口](https://www.infineon.com/part/AS5048A)
- [AS5048A 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5048a-as5048b-datasheet-en.pdf)
