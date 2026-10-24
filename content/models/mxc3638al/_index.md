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

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 感知结构 | 三轴电容加速度计 |
| 量程 | ±2／4／8／12／16 g |
| 数字接口 | I²C、SPI |
| FIFO | 32 样本 |
| 功能 | 运动检测与唤醒 |
| 封装 | 2 × 2 mm |
| 输出位数 | 产品页列 8／10／12 位配置；新闻所述 16 bit 未作统一口径 |
| 采样率 | 14～1300样本/秒，依工作模式 |
| 低功耗条件 | Sniff 0.4µA（6Hz）；Wake 0.9µA（25Hz），模式不同不可并用 |
| 接口速率 | I²C最高1MHz；SPI最高8MHz |
| 工作温度 | −40～85°C |
| 封装尺寸 | 2.0×2.0×0.94mm，12引脚 |
| 噪声 | 官网列低至2.3mg RMS，须结合对应模式与带宽 |
| 认证 | AEC-Q100 Class 3，依原厂产品页 |

参数依据：[原厂产品页或对应资料](https://www.memsic.com/cn/capacitive-accelerometer-85)。

## 产品功能与测量链

MXC3638AL通过三轴电容结构测量加速度，提供FIFO、运动检测和唤醒。量程、分辨率与采样率需要一起配置；扩大g量程会改变每个输出码对应的加速度。

## 接入与配置

32样本FIFO用于暂存测量数据，减少主控唤醒次数；深度不等于32字节。主控读取周期应按三轴格式、输出速率和水位中断设计，避免覆盖未读数据。

## 使用与验证

0.4µA Sniff（6Hz）与0.9µA Wake（25Hz）属于特定低功耗模式，不能当作1300样本/秒连续工作电流。车辆钥匙应用还应检查唤醒误触发、漏触发和温度下的静止噪声。

## 官方资料

- [MXC3638AL 原厂资料入口](https://www.memsic.com/cn/capacitive-accelerometer-85)
- [MXC3638AL 数据手册（官方 PDF）](https://www.memsic.com/Public/Uploads/uploadfile/files/20220119/MXC3638ALDatasheet.pdf)
