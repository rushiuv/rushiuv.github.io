---
title: "TLE5502"
wiki: true
wiki_type: "model"
catalog_type: "模拟角度"
catalog_form: "芯片"
wiki_rank: 144
seed_count: 1
lastmod: "2026-10-24"
description: "TLE5502是英飞凌基于TMR技术的磁角度传感器系列，以模拟正余弦信号为主要输出，供外部控制器采样解算。"
official_url: "https://www.infineon.com/technology-news/2026/infpss202606-102"
related_companies: ["英飞凌"]
datasheet_url: "https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle5502d-datasheet-en.pdf"
datasheet_label: "对应版本手册"
wiki_category: "模拟角度信号与外部解算"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tle5502-datasheet-figure.jpg"
product_image_caption: "TLE5502D 原厂手册封装图；对应 D 后缀双通道器件"
product_image_source: "https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle5502d-datasheet-en.pdf"
---

## 核心性能

### 产品介绍

TLE5502是英飞凌基于TMR技术的磁角度传感器系列，以模拟正余弦信号为主要输出，供外部控制器采样解算。 [官方资料](https://www.infineon.com/technology-news/2026/infpss202606-102)

### 核心参数

- **感应技术** TMR
- **输出** 模拟正弦／余弦信号
- **处理** 外部 ADC 采样与角度解算
- **所附资料** TLE5502D 双通道版本手册

### 接口与输出

TLE5502 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 模拟正弦／余弦信号

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

磁敏元件随磁场方向改变输出，芯片向外提供正余弦或相关模拟信号。主控或后级细分器采样这些信号，计算相位，再结合零点与机械关系得到位置。模拟输出把部分信号处理责任留给了系统。

两路信号理想情况下幅值匹配且正交，实际需要处理零点偏移、增益差和相位偏差。接地、参考电压、输入滤波和ADC建立时间也会改变采样结果。

### 典型应用与使用条件

ADC位数描述数字化粒度，不能直接当作角度精度。不同通道错时采样，在快速旋转时可能产生新的相位误差；校准数据则必须对应实际磁体与装配状态。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [TLE5502 原厂资料入口](https://www.infineon.com/technology-news/2026/infpss202606-102)
- [对应版本手册（PDF）](https://www.infineon.com/assets/row/public/documents/24/49/infineon-tle5502d-datasheet-en.pdf)

下载件对应 TLE5502D；其中双通道及供电条件不代表所有 TLE5502 成员。
