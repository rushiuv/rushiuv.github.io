---
title: "iC-MU"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 39
seed_count: 5
lastmod: "2026-10-24"
description: "iC-MU是iC-Haus的磁性离轴绝对值编码芯片，利用两条不同周期的磁码道及游标关系获得绝对位置，同时对周期信号进行细分。"
official_url: "https://www.ichaus.de/product/ic-mu/"
related_companies: ["iC-Haus"]
datasheet_url: "https://www.ichaus.de/product/ic-mu/"
datasheet_label: "官网文档入口"
wiki_category: "双码道与绝对位置"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/ic-mu-official.png"
product_image_caption: "iC-MU128 产品图；iC-MU 系列当前入口代表成员"
product_image_source: "https://www.ichaus.de/product/ic-mu128/"
---

## 核心性能

### 产品介绍

iC-MU是iC-Haus的磁性离轴绝对值编码芯片，利用两条不同周期的磁码道及游标关系获得绝对位置，同时对周期信号进行细分。 [官方资料](https://www.ichaus.de/product/ic-mu/)

### 核心参数

- **感知方式** 双码道磁检测与游标绝对位置解算
- **安装** 离轴，需匹配双码道磁环
- **输出** 绝对值及增量位置接口
- **当前产品入口** iC-MU128；该成员主码道极宽 1.28 mm

### 接口与输出

iC-MU 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 绝对值及增量位置接口

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

单条周期码道只能给出一个周期内的相位，同样的读数在一圈中可能重复出现。两条不同周期的码道形成额外的相位关系，系统先识别所在区间，再把细分相位合成为绝对位置。

粗位置判断与细相位测量承担不同任务。细分位数增加，不会自动降低粗码判别的错误概率；安装偏差、通道失配或某一路信号过弱，都可能在区间判断处造成比普通噪声更大的位置跳变。

### 典型应用与使用条件

磁环、码道周期、读头几何与解算规则必须一起设计。最终分辨率无法反向唯一推出极对数，也不能仅凭同一家公司的专利确认量产型号结构。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [iC-MU 原厂资料入口](https://www.ichaus.de/product/ic-mu/)
- [官网文档入口（官方入口）](https://www.ichaus.de/product/ic-mu/)

当前原厂链接跳转 iC-MU128，1.28 mm 极宽仅属于该成员；规格下载可能需要原厂授权。
