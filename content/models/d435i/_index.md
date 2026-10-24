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

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 模组构成 | 双目深度相机与 IMU |
| 数据支持 | RealSense SDK 2.0 |
| 输出数据 | 深度与惯性数据，支持时间戳 |
| 连接方式 | USB；可用数据模式取决于连接条件 |
| 深度测量 | 主动双目；双全局快门深度传感器；D435i带6DoF IMU |
| 深度模式 | 1280×720最高30fps；848×480等较低分辨率可达90fps，USB3.1模式表4-2 |
| RGB模式 | 1920×1080为6/15/30fps；960×540等低分辨率可达60fps，不能拼成1080p60 |
| RGB视场 | 相机规格表D435/D435i组：水平69°、垂直42°、对角77°，不是D436/其他机型的90°×65° |
| 深度视场 | Intel独立D435i规格页H87°、V58°；有效视场还随距离变化 |
| 工作距离 | 独立规格页约0.3～3m；手册介绍0.2m至3m以上，受光照与模式影响 |
| 数据连接 | USB3；深度与RGB为独立数据接口，模式按带宽选择 |
| 外形 | 90×25×25mm，D435i相机尺寸 |

参数依据：[原厂产品页或对应资料](https://realsenseai.com/wp-content/uploads/2025/08/Intel-RealSense-D400-Series-Datasheet-August-2025.pdf)。

## 产品功能与测量链

D435i输出环境深度和惯性数据，主要服务定位、建图及运动感知。它不直接测量电机轴角度，不能作为磁编码器的同类分辨率对比项。

## 接入与配置

深度流、彩色流与IMU流有各自的时间戳和坐标系。融合前需要确认外参、时间同步及SDK所用的数据模式，不能只因同属一台相机就默认同步。

## 使用与验证

验收应覆盖实际距离、表面反射、运动速度与环境光。USB带宽和计算机接收能力会影响可用流配置；深度误差必须注明距离和目标条件，不能用单个像素数代替。

## 官方资料

- [D435i 原厂资料入口](https://www.realsenseai.com/products/depth-camera-d435i/)
- [D435i 数据手册（官方 PDF）](https://www.realsenseai.com/wp-content/uploads/2022/04/Intel-RealSense-D400-Series-Datasheet-April-2022-v2.pdf)

- [D400系列数据手册Rev020，2025-08，第67页相机表、第75～76页表4-2](https://realsenseai.com/wp-content/uploads/2025/08/Intel-RealSense-D400-Series-Datasheet-August-2025.pdf)
- [Intel D435i独立规格页](https://www.intel.com/content/www/us/en/products/sku/190004/intel-realsense-depth-camera-d435i/specifications.html)
