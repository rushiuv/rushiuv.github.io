---
title: "KTH5701"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 22
seed_count: 9
lastmod: "2026-10-24"
description: "KTH5701是数字输出的三轴线性霍尔传感器，可读取XYZ磁场分量，适合摇杆、旋钮和位移感知。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf"
datasheet_label: "官方数据手册"
wiki_category: "三轴磁场测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth5701-product.png"
product_image_caption: "KTH5701 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf"
---

## 核心性能

### 产品介绍

KTH5701是数字输出的三轴线性霍尔传感器，可读取XYZ磁场分量，适合摇杆、旋钮和位移感知。它提供原始磁场测量通道，运动信息的提取仍与磁路和主控算法有关。 [官方资料](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html)

### 核心参数

- **磁场转换** 16 位 ADC
- **通信** I²C、SPI
- **供电范围** 2.8～5.5 V
- **角度功能** 手册列 CORDIC 输出选项，轴平面依版本
- **版本范围** AQ1 与 AQ2／AQ3 需分别核对温度与电气条件

### 接口与输出

KTH5701 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **通信** I²C、SPI
- **角度功能** 手册列 CORDIC 输出选项，轴平面依版本

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

三轴霍尔元件感知磁场在不同方向的分量，芯片对各轴进行转换，再经数字接口交给主控。通过选定轴组合，系统可以观察旋转、靠近、远离或摇杆摆动带来的场变化。它增加了可观测量，但实际运动仍需与磁体几何对应。

由两轴分量计算角度时，主控需要处理零点、轴间增益和安装关系。由场强估计距离时，还需要标定场强随位移的曲线；两种运算不能使用同一套简单比例直接互换。

### 典型应用与使用条件

更高采样率、更多测量轴与更低噪声通常会增加功耗或延长转换过程。电池设备可以间歇采样，快速运动则需要足够及时的测量，具体模式应与动作频率匹配。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [KTH5701 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html)
- [KTH5701 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf)
