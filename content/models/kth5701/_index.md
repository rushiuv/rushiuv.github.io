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

## 官方资料

- [KTH5701 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/57xilie/index.html)
- [KTH5701 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH5701AQ2AQ3_DS_CN.pdf)
