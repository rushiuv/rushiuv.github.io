---
title: "MXC3638AL"
wiki: true
wiki_type: "model"
wiki_rank: 135
seed_count: 1
lastmod: "2026-10-24"
description: "MXC3638AL是美新的低功耗三轴电容加速度计，具有FIFO、运动检测与唤醒功能，面向汽车钥匙等电池供电系统。"
official_url: "https://www.memsic.com/cn/capacitive-accelerometer-85"
related_companies: ["美新半导体"]
datasheet_url: "https://www.memsic.com/Public/Uploads/uploadfile/files/20220119/MXC3638ALDatasheet.pdf"
datasheet_label: "官方数据手册"
wiki_category: "加速度与惯性测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mxc3638al-product.png"
product_image_caption: "MXC3638AL 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.memsic.com/Public/Uploads/uploadfile/files/20220119/MXC3638ALDatasheet.pdf"
---

## 核心性能

### 产品介绍

MXC3638AL是美新的低功耗三轴电容加速度计，具有FIFO、运动检测与唤醒功能，面向汽车钥匙等电池供电系统。 [官方资料](https://www.memsic.com/cn/capacitive-accelerometer-85)

### 核心参数

- **感知结构** 三轴电容加速度计
- **量程** ±2／4／8／12／16 g
- **数字接口** I²C、SPI
- **FIFO** 32 样本
- **功能** 运动检测与唤醒
- **封装** 2 × 2 mm
- **输出位数** 产品页列 8／10／12 位配置；新闻所述 16 bit 未作统一口径

### 接口与输出

MXC3638AL 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **数字接口** I²C、SPI
- **输出位数** 产品页列 8／10／12 位配置；新闻所述 16 bit 未作统一口径

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

MEMS加速度计利用微结构对惯性力的响应形成电信号，经调理后输出与加速度相关的数据。它同时响应重力和运动引起的比力，所以姿态与加速度需要结合场景或其他传感器解释。

将加速度积分为速度和位置时，零偏会随时间积累。低噪声有助于短时测量，长期稳定性、温度与安装应力则影响更长时间的结果，两者不是同一个指标。

### 典型应用与使用条件

量程、带宽、噪声密度、偏置稳定性和重复性需要分别比较。较大冲击量程不会自动拥有最低噪声，小量程的最好数据也不能直接用于全部系列成员。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [MXC3638AL 原厂资料入口](https://www.memsic.com/cn/capacitive-accelerometer-85)
- [MXC3638AL 数据手册（官方 PDF）](https://www.memsic.com/Public/Uploads/uploadfile/files/20220119/MXC3638ALDatasheet.pdf)
