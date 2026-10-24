---
title: "PNH3348"
wiki: true
wiki_type: "model"
catalog_type: "光学编码"
catalog_form: "芯片"
wiki_rank: 93
seed_count: 2
lastmod: "2026-10-24"
description: "PNH3348 对应 iC-Haus 的 iC-PNH3348 三通道相位阵光学编码前端，配合匹配码盘与后级细分器使用。"
official_url: "https://www.ichauschina.com/PNH_factsheet_CN"
related_companies: ["iC-Haus"]
datasheet_url: "https://www.ichauschina.com/PNH_factsheet_CN"
datasheet_label: "官方数据手册"
wiki_category: "光学读头与码盘"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/pnh3348-datasheet-figure.png"
product_image_caption: "iC-PNH3348 原厂资料中的光学应用与产品图"
product_image_source: "https://www.ichauschina.com/PNH_factsheet_CN"
---

## 核心性能

### 产品介绍

PNH3348在此指iC-Haus的iC-PNH3348相位阵游标光学编码芯片。它读取匹配码盘的多条光学码道，输出供后续细分的信号，具有EncoderBlue相关版本背景。 [官方资料](https://www.ichauschina.com/PNH_factsheet_CN)

### 核心参数

- **前端结构** 三通道相位阵
- **输出** 模拟正余弦及辅助码道
- **绝对位置** 与匹配码盘、后级插值处理配套
- **光源** EncoderBlue 相关版本，按具体芯片版本匹配 LED

### 接口与输出

PNH3348 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 模拟正余弦及辅助码道

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

光源照射码盘，明暗结构改变落在光电元件上的光强，读头把这些变化转换成模拟周期信号或数字边沿。相位阵、差分检测和多码道用于改善信号质量或识别绝对位置。

读头、光源、码盘与机械间隙共同构成光学系统。反射式与透射式结构不能只因使用同类芯片就互换；波长、数值孔径与码道尺寸也会影响可读信号。

### 典型应用与使用条件

光源老化、污染、倾斜和装配误差可能同时改变信号幅度与波形。自动增益可以维持幅度，却不一定恢复已丢失的对比度和信噪比，故障门限与最终位置质量应分别检查。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [PNH3348 原厂资料入口](https://www.ichauschina.com/PNH_factsheet_CN)
- [PNH3348 数据手册（官方 PDF）](https://www.ichauschina.com/PNH_factsheet_CN)
