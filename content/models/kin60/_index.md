---
title: "KIN60"
wiki: true
wiki_type: "model"
catalog_type: "旋转编码模块"
catalog_form: "编码模块"
wiki_rank: 123
seed_count: 1
lastmod: "2026-10-24"
description: "KIN60 是锐鹰中空绝对值旋转编码器系列，官网将其归为电感式编码器，包含不同位数及通信接口版本。"
official_url: "https://reagles.cn/en/index.php/index/product_detail/content/10133.html"
related_companies: ["锐鹰"]
datasheet_url: "https://www.reagles.cn/uploads/Download/20231206/154034849925524.pdf"
datasheet_label: "官方数据手册"
wiki_category: "绝对位置编码器"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kin60-product.png"
product_image_caption: "KIN60 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.reagles.cn/uploads/Download/20231206/154034849925524.pdf"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 产品形态 | 中空绝对值编码器；单圈与多圈版本分别选型 |
| 原厂分类 | inductive 电感式 |
| 版本 | 既有手册列17ST00、23ST00、21BS20；当前官网成员见下列规格书行 |
| 通信 | RS485 或 BiSS，按订货后缀区分 |
| 单圈／多圈位数 | 技术表单圈17～23bit、多圈16bit，实际单圈/多圈版本分别选 |
| 供电／电流 | 5V±5%；150mA典型，官网技术表 |
| 通信速率选项 | RS485 2.5Mbps；SSI 2Mbps；BiSS 10Mbps；速率栏另列SPI 3Mbps，须按完整料号确认 |
| 工作温度 | −40～85°C |
| 重复定位 | 目录可达±3角秒，不能当绝对精度 |
| 单圈规格书成员 | KIN60-23ST00、23BS20、21SI00等，当前官网列规格书V1.3 |
| 多圈规格书成员 | M16S23ST00、M16S23BS20、M16S19SI00等，当前官网列规格书V1.2 |

参数依据：[原厂产品页或对应资料](https://reagles.cn/en/index.php/index/product_detail/content/10133.html)。

## 产品功能与测量链

KIN60采用电感式中空感应结构，为直驱、机器人与机床提供旋转位置反馈。公开目录给出单圈与多圈版本，具体通信后缀和位宽应以所选规格书为准。

## 接入与配置

简介提到RS485、SPI与BiSS，技术表通信栏列RS485、SSI、BiSS-C，速率栏又包含SPI。各栏目口径并非同一订货版本的完整承诺，选型应核对23ST00、23BS20及21SI00等实际料号。

## 使用与验证

目录重复定位可达±3角秒，表征反复回到同一位置的一致性。23位输出的数字刻度远小于该值，不能把码宽换算成绝对精度；还需在安装公差和温度条件下看整圈残差与读数噪声。

## 官方资料

- [KIN60 原厂资料入口](https://reagles.cn/en/index.php/index/product_detail/content/10133.html)
- [KIN60 数据手册（官方 PDF）](https://www.reagles.cn/uploads/Download/20231206/154034849925524.pdf)
