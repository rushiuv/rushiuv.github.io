---
title: KTH5701
wiki: true
wiki_type: model
catalog_type: 线性磁场
catalog_form: 芯片
wiki_rank: 22
seed_count: 9
lastmod: '2026-10-30'
description: KTH5701 是面向位置检测的三轴数字霍尔传感器；它提供磁场信息，摇杆、旋钮和位移输出仍取决于磁体几何、测量配置与标定。
official_url: https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html
related_companies:
- 昆泰芯
datasheet_url: https://chat.connteck.com/downloads/KTH5701/KTH5701AQ1_DS_CN_V2.0.pdf
datasheet_label: 数据手册原链接
wiki_category: 三轴磁场测量
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
model_card: true
product_image: /images/wiki/kth5701-product.png
product_image_caption: KTH5701 原厂手册产品／安装图（PDF 第 1 页）
product_image_source: https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5701/
search_aliases:
- KTH5701
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 器件类型 | 三轴数字线性霍尔，XYZ场强采集 |
| 数字转换 | 16位ADC；不能写成16位机械位置精度 |
| 供电 | 2.8～5.5V |
| 通信 | I²C、SPI |
| 场强范围 | 系列目录XY典型±130mT；Z典型±80mT |
| 工作频率 | 系列目录1000Hz；按测量模式确认 |
| 低功耗口径 | 系列目录待机1.4µA；5Hz约25.2µA、25Hz约113.7µA |
| 模式 | 连续、唤醒睡眠、单次测量 |
| 角度处理 | CORDIC输出选项，平面和版本按对应手册 |
| 温度/封装 | 系列目录−40～125°C；QFN 3×3mm-16L；DFN 2×2.5mm-8L适用等级另核对 |
| 等级区别 | AQ1与AQ2/AQ3分别使用对应原厂手册 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf)。

## 从三轴磁场到机械位置

KTH5701首先提供磁场信息。用于摇杆、旋钮或直线位移时，磁体和运动轨迹决定XYZ如何变化，再由所选平面或主控算法转换为目标位置。场强ADC位数不能直接当作毫米或角度准确度。

## 功耗随测量模式变化

连续采样、单次触发和低频唤醒不是同一个工作点。目录同时给待机电流与不同采样频率下的平均电流，电池寿命核算应按真实采样计划和总线活动计算，不能把最低电流配最高刷新率。

## 版本与接口的检查

AQ1、AQ2/AQ3的温度和封装可选范围需分别核对。读取XYZ与读取CORDIC角度也有不同数据含义；主控应保存所用轴、方向、符号和量程设置，避免把芯片坐标误当成机构坐标。

## 验证重点

静止记录三轴零偏和噪声，运动时记录全行程矢量轨迹。对磁体偏移、倾斜、温度和外部磁场分别做扰动，检查映射是否仍单调；只在一个姿态标定，不能证明整个摇杆工作域有效。

## 两轴角度与场强位移的区别

由两个场分量求角度时，要处理轴间零点、增益及芯片坐标与机构坐标的关系；由磁场估计距离，则需要另一条场强随位移的标定曲线。两类输出不能共用一个未经验证的比例换算。选择测量轴数量和采样模式时，还应核对一次转换过程能否满足目标动作的时间要求。

## 官方资料

- [KTH5701 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html)
- [KTH5701 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf)

## 选型补充

### 从三轴磁场得到机构位置

XYZ 是芯片坐标下的磁场分量。由两个分量计算旋转角度，与由磁场幅值估计位移，是两种不同映射；设计时应先明确敏感平面、方向和量程，再把输出与机构基准对应起来。

### AQ 等级和测量模式分开选

AQ1 与 AQ2/AQ3 各有资料入口，温度、封装和电气条件应按完整订货型号核对。连续测量、单次触发和低频唤醒也对应不同功耗，不能把最低休眠电流与最高刷新率写成同一个工作点。

### 记录整段磁场轨迹

用于换挡器或摇杆时，除了中心零偏，还要检查全部位置的场分量、饱和裕量和运动单调性。温度、装配偏移和外部磁场分别施加扰动，才能判断原标定在机构容差内是否仍有效。


## 公开资料与型号核对

博客既有原厂资料与 Design Center 在量程、测量速率及功耗口径上不同，应保留各自版本与条件，不能择优拼接。

来源竞品表把三轴加速度计列为磁传感器功能替代，不能直接采用该替换结论。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5701AQ1_DS_CN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5701/KTH5701AQ1_DS_CN_V2.0.pdf)
- [KTH5701AQ2AQ3_DS_CN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5701/KTH5701AQ2AQ3_DS_CN_V2.0.pdf)
- [KTH5701AQ1_DS_EN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5701/KTH5701AQ1_DS_EN_V2.0.pdf)
- [KTH5701AQ2AQ3_DS_EN_V2.0.pdf](https://chat.connteck.com/downloads/KTH5701/KTH5701AQ2AQ3_DS_EN_V2.0.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5701/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)
