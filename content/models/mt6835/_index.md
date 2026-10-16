---
title: "MT6835"
wiki: true
wiki_type: "model"
wiki_rank: 21
seed_count: 10
lastmod: "2026-10-16"
description: "MT6835 是麦歌恩 21 位 AMR 磁角度编码器，集成磁敏元件、自校准与多种位置输出，面向伺服和闭环步进反馈。"
official_url: "https://www.magntek.com.cn/"
related_companies: ["麦歌恩"]
datasheet_url: "https://www.magntek.com.cn/upload/pdf/202312/MT6835_Rev.1.3_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mt6835-datasheet-figure.jpg"
product_image_caption: "mt6835 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.magntek.com.cn/upload/pdf/202312/MT6835_Rev.1.3_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
---

## 核心性能

- **角度分辨率** 21 位，0～360°
- **绝对值输出** 四线 SPI、12 位 PWM
- **增量 ABZ** 1～16,384 脉冲／圈，最高 65,536 步／圈
- **换向 UVW** 1～16 对极可编程
- **最高转速** 120,000 rpm，见 Rev.1.3 适用条件
- **校准** 客户端自动非线性校准，INL 典型 ±0.07°，按第 9 章条件
- **系统延时** 匀速下典型 10 µs；BW=5 阶跃响应典型 100 µs
- **温度／封装** −40～125°C，TSSOP-16

## 官方资料

- [MT6835 原厂资料入口](https://www.magntek.com.cn/)
- [MT6835 数据手册（官方 PDF）](https://www.magntek.com.cn/upload/pdf/202312/MT6835_Rev.1.3_%E4%B8%AD%E6%96%87%E7%89%88.pdf)
- 参数出处：Rev.1.3，第 1、3、6～7 页；延时按电气表匀速条件。
