---
title: "D435i"
wiki: true
wiki_type: "model"
wiki_rank: 79
seed_count: 2
lastmod: "2026-10-24"
description: "D435i是RealSense深度相机，在D435深度测量能力基础上加入IMU。"
official_url: "https://www.realsenseai.com/products/depth-camera-d435i/"
related_companies: ["Intel"]
datasheet_url: "https://www.realsenseai.com/wp-content/uploads/2022/04/Intel-RealSense-D400-Series-Datasheet-April-2022-v2.pdf"
datasheet_label: "官方数据手册"
wiki_category: "深度视觉与惯性数据"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心性能

### 产品介绍

D435i是RealSense深度相机，在D435深度测量能力基础上加入IMU。它属于完整视觉模组，不是编码器芯片，历史Intel标识应与当前RealSense支持入口分开。 [官方资料](https://www.realsenseai.com/products/depth-camera-d435i/)

### 核心参数

- **模组构成** 双目深度相机与 IMU
- **数据支持** RealSense SDK 2.0
- **输出数据** 深度与惯性数据，支持时间戳
- **连接方式** USB；可用数据模式取决于连接条件

### 接口与输出

D435i 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出数据** 深度与惯性数据，支持时间戳

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

双目深度系统利用两个视角的对应关系估计距离，主动投射纹理可帮助某些低纹理场景。IMU提供角速度和加速度信息，帮助算法理解相机运动，但它自身也有偏置与噪声。

深度图、彩色图和IMU的坐标与采样节奏可能不同，需要通过外参和时间戳对齐。看见同一个数据包，并不代表所有物理量在同一瞬间被测得。

### 典型应用与使用条件

日光、反光、低纹理、遮挡与运动会影响有效深度。标称范围应保留目标材质和环境条件；机器人采用某款相机也不等于它的关节位置传感采用同一技术。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [D435i 原厂资料入口](https://www.realsenseai.com/products/depth-camera-d435i/)
- [D435i 数据手册（官方 PDF）](https://www.realsenseai.com/wp-content/uploads/2022/04/Intel-RealSense-D400-Series-Datasheet-April-2022-v2.pdf)
