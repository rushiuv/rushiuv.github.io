---
title: "SROA48"
wiki: true
wiki_type: "model"
catalog_type: "完整编码器"
catalog_form: "完整编码器"
wiki_rank: 95
seed_count: 2
lastmod: "2026-10-24"
description: "SROA48是锐鹰整体式机械多圈绝对编码器，使用机械多圈结构保存转数状态，不依赖维护电池完成其多圈位置表达。"
official_url: "https://www.reagles.cn/"
related_companies: ["锐鹰"]
datasheet_url: "https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf"
datasheet_label: "官方数据手册"
wiki_category: "机械多圈位置保持"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/sroa48-product.png"
product_image_caption: "SROA48 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf"
---

## 核心性能

### 产品介绍

SROA48是锐鹰整体式机械多圈绝对编码器，使用机械多圈结构保存转数状态，不依赖维护电池完成其多圈位置表达。 [官方资料](https://www.reagles.cn/)

### 核心参数

- **多圈结构** 整体式机械多圈，无需计圈电池
- **单圈分辨率** 23／25 位版本
- **多圈分辨率** 12 位
- **通信选项** RS485、BiSS-C，依订货码

### 接口与输出

SROA48 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **通信选项** RS485、BiSS-C，依订货码

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

机械传动把多次旋转映射到一组不同的机械状态，读出这些状态后恢复圈数。断电时机械状态仍随轴运动，因此可减少依赖维护电池的电子计数环节。

单圈位置描述当前一圈内的角度，多圈部分表示编码范围内的转数，两者相加形成总位置。多圈范围是有限的，越过编码范围后如何处理，应由控制系统明确。

### 典型应用与使用条件

无电池减少电池维护，并不等于无需机械寿命评估。齿轮回差、磨损、冲击、安装公差和读取一致性仍可能影响结果；重复定位与绝对精度也应分开。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [SROA48 原厂资料入口](https://www.reagles.cn/)
- [SROA48 数据手册（官方 PDF）](https://www.reagles.cn/en/uploads/Download/20241108/1658028d0cd2258.pdf)
