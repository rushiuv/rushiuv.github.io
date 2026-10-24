---
title: "AEDR-850x"
wiki: true
wiki_type: "model"
catalog_type: "光学编码"
catalog_form: "芯片"
wiki_rank: 110
seed_count: 1
lastmod: "2026-10-24"
description: "AEDR-850x是Broadcom反射式光学增量编码器系列，将LED和光检测电路集成在同一小型封装，并提供正交及索引输出。"
official_url: "https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102"
related_companies: ["Broadcom"]
wiki_category: "光学读头与码盘"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/aedr-850x-official.jpg"
product_image_caption: "AEDR-8500 原厂产品图；AEDR-850x 系列代表成员"
product_image_source: "https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102"
---

## 核心性能

### 产品介绍

AEDR-850x是Broadcom反射式光学增量编码器系列，将LED和光检测电路集成在同一小型封装，并提供正交及索引输出。 [官方资料](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102)

### 核心参数

- **感知结构** 集成 LED 与光检测电路的反射式光学读头
- **输出** A/B 正交信号及第三路索引
- **配套** 反射码盘或码尺
- **系列选件** 分辨率与插值倍率随完整型号变化

### 接口与输出

AEDR-850x 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** A/B 正交信号及第三路索引

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

光源照射码盘，明暗结构改变落在光电元件上的光强，读头把这些变化转换成模拟周期信号或数字边沿。相位阵、差分检测和多码道用于改善信号质量或识别绝对位置。

读头、光源、码盘与机械间隙共同构成光学系统。反射式与透射式结构不能只因使用同类芯片就互换；波长、数值孔径与码道尺寸也会影响可读信号。

### 典型应用与使用条件

光源老化、污染、倾斜和装配误差可能同时改变信号幅度与波形。自动增益可以维持幅度，却不一定恢复已丢失的对比度和信噪比，故障门限与最终位置质量应分别检查。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [AEDR-850x 原厂资料入口](https://www.broadcom.com/products/motion-control-encoders/incremental-encoders/reflective-encoders/aedr-8500-102)
