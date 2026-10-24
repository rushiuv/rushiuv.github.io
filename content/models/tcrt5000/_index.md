---
title: "TCRT5000"
wiki: true
wiki_type: "model"
wiki_rank: 143
seed_count: 1
lastmod: "2026-10-24"
description: "TCRT5000是Vishay反射式光学传感器，集成红外发射器和光电晶体管，适用于反射变化和标记检测。"
official_url: "https://www.vishay.com/zh/product/83760/"
datasheet_url: "https://www.vishay.com/docs/83760/tcrt5000.pdf"
datasheet_label: "官方数据手册"
wiki_category: "反射检测与条纹读取"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tcrt5000-datasheet-figure.jpg"
product_image_caption: "tcrt5000 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.vishay.com/docs/83760/tcrt5000.pdf"
---

## 核心性能

### 产品介绍

TCRT5000是Vishay反射式光学传感器，集成红外发射器和光电晶体管，适用于反射变化和标记检测。 [官方资料](https://www.vishay.com/zh/product/83760/)

### 核心参数

- **结构** 红外发射器与光电晶体管
- **检测方式** 反射式光学检测
- **输出** 光电晶体管信号
- **版本** TCRT5000 与 TCRT5000L 的机械引脚形式不同

### 接口与输出

TCRT5000 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **输出** 光电晶体管信号

### 工作原理

以下解释本类器件在系统中的一般工作方式，具体集成功能以本型号官方资料为准。

红外LED照亮目标，光电晶体管感受返回的光强。反射信号随目标距离、颜色、材料和方向改变，后续电路可以通过阈值检测边沿，或通过ADC读取连续幅值。

用于码盘时，必须确保亮暗图案在实际红外波长下有足够反差。人眼看起来很黑的墨水可能仍强烈反射红外，因此纸张打印效果不能直接证明读头可用。

### 典型应用与使用条件

LED电流、环境光、工作间隙和接收电路会影响信号范围。输出饱和可能掩盖明暗差别，阈值太靠近噪声则会造成多计数或漏计数。

要把产品放进实际设备，还要确认数据对应的物理位置和时刻。传感器读数、接口传输和控制器使用并非同一个环节；读数更新并不一定意味着刚完成一次新测量。协议校验可以发现部分传输错误，无法发现全部机械安装变化。

比较两个备选型号时，应在相同输入、温度、带宽和校准状态下看结果。分辨率、噪声、重复性与绝对误差各有定义；目录页的典型值也不应改写成每颗样品、所有条件下的保证值。某一功能能配置，不表示所有输出可以同时工作。

## 官方资料

- [TCRT5000 原厂资料入口](https://www.vishay.com/zh/product/83760/)
- [TCRT5000 数据手册（官方 PDF）](https://www.vishay.com/docs/83760/tcrt5000.pdf)
