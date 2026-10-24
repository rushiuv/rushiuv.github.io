---
title: "iC-TW29"
wiki: true
wiki_type: "model"
catalog_type: "信号处理"
catalog_form: "芯片"
wiki_rank: 81
seed_count: 2
lastmod: "2026-10-24"
description: "iC-TW29是iC-Haus用于正余弦编码器信号的细分与处理芯片。"
official_url: "https://www.ichaus.de/product/ic-tw29/"
related_companies: ["iC-Haus"]
datasheet_url: "https://www.ichaus.de/product/ic-tw29/"
datasheet_label: "官网文档入口"
wiki_category: "正余弦信号细分"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/ic-tw29-official.png"
product_image_caption: "iC-TW29 原厂产品／封装图"
product_image_source: "https://www.ichaus.de/product/ic-tw29/"
---

## 核心性能

### 产品介绍

iC-TW29是iC-Haus用于正余弦编码器信号的细分与处理芯片。它处理外部传感器提供的模拟周期信号，不应写成内部自带磁敏元件的完整磁编码器。 [官方资料](https://www.ichaus.de/product/ic-tw29/)

### 核心参数

- **输入** 外部编码器的模拟正余弦信号
- **位置处理** 26 位编码器处理
- **输出** ABZ、UVW、BiSS，分辨率可独立配置
- **多圈** 可接外部圈数信息

### 接口与输出

iC-TW29 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输入** 外部编码器的模拟正余弦信号
- **位置处理** 26 位编码器处理
- **输出** ABZ、UVW、BiSS，分辨率可独立配置

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

外部读头提供近似正弦与余弦的周期信号，细分芯片进行采样、误差校正与相位计算，在一个信号周期内划出更密的位置刻度。它提高了读数粒度，但没有凭空增加目标物的绝对编码。

若目标在一圈有多个相同周期，还需粗码、索引或另一组不同周期信息来消除歧义。只有周期内角度并不足以在上电时识别完整机械位置。

### 典型应用与使用条件

输入幅值、共模、偏置、正交误差和谐波决定可实现的细分质量。两个ADC是否同步、滤波造成多少延迟以及最大输入频率是多少，会直接影响高速测量。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [iC-TW29 原厂资料入口](https://www.ichaus.de/product/ic-tw29/)
- [官网文档入口（官方入口）](https://www.ichaus.de/product/ic-tw29/)

iC-TW29 完整规格下载可能需登录及原厂授权，产品页保留公开入口。
