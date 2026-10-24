---
title: "PNH3348"
wiki: true
wiki_type: "model"
catalog_type: "光学编码"
catalog_form: "芯片"
wiki_rank: 93
seed_count: 2
lastmod: "2026-10-24"
description: "PNH3348 对应 iC-Haus 的 iC-PNH3348 三通道相位阵光学编码前端，配合匹配码盘与后级细分器使用。"
official_url: "https://www.ichauschina.com/PNH_factsheet_CN"
related_companies: ["iC-Haus"]
datasheet_url: "https://www.ichauschina.com/PNH_factsheet_CN"
datasheet_label: "官方数据手册"
wiki_category: "光学读头与码盘"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/pnh3348-datasheet-figure.png"
product_image_caption: "iC-PNH3348 原厂资料中的光学应用与产品图"
product_image_source: "https://www.ichauschina.com/PNH_factsheet_CN"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 前端结构 | 三通道相位阵 |
| 输出 | 模拟正余弦及辅助码道 |
| 绝对位置 | 与匹配码盘、后级插值处理配套 |
| 光源 | EncoderBlue 相关版本，按具体芯片版本匹配 LED |

参数依据：[原厂产品页或对应资料](https://www.ichauschina.com/PNH_factsheet_CN)。

## 产品功能与测量链

iC-PNH3348是三通道相位阵光学前端，通过匹配码盘产生模拟正余弦及辅助信息，后级再进行细分和绝对位置组合。它本身并非可直接读取SPI绝对角度的完整编码器。

## 接入与配置

多通道的采样位置与码盘轨道几何需成套设计。蓝光光源、反射层、安装高度和码盘直径都会改变信号质量，不能仅按芯片封装大小选择码盘。

## 使用与验证

调试要分别观察各通道幅值、直流偏置、相位及跨圈关系，再接后端细分器。系列宣传中的整机位数不能自动归为前端本身的有效精度；缺少完整条件的性能数值不填入保证规格。

## 版本与待核项目

当前公开factsheet支持前端定位与信号结构；需要按实际光学几何取得完整电气条件。发光驱动、供电、响应频率和输出负载尚不能仅从三通道名称推算。

## 官方资料

- [PNH3348 原厂资料入口](https://www.ichauschina.com/PNH_factsheet_CN)
- [PNH3348 数据手册（官方 PDF）](https://www.ichauschina.com/PNH_factsheet_CN)
