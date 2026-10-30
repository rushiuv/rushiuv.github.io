---
title: KIN60系列
wiki: true
wiki_type: model
catalog_type: 旋转编码模块
catalog_form: 编码模块
wiki_rank: 123
seed_count: 1
lastmod: '2026-10-30'
description: KIN60 是锐鹰中空绝对值旋转编码器系列，官网将其归为电感式编码器，包含不同位数及通信接口版本。
official_url: https://reagles.cn/en/index.php/index/product_detail/content/10133.html
related_companies:
- 锐鹰
datasheet_url: https://www.reagles.cn/uploads/Download/20231206/154034849925524.pdf
datasheet_label: 官方数据手册
wiki_category: 绝对位置编码器
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
product_image: /images/wiki/kin60-product.png
product_image_caption: KIN60 原厂手册产品／安装图（PDF 第 1 页）
product_image_source: https://www.reagles.cn/uploads/Download/20231206/154034849925524.pdf
catalog_level: 系列
search_aliases:
- KIN60系列
---

KIN60是电感式中空绝对值编码器系列。现有资料同时保留历史与当前规格书成员，先区分单圈／多圈和手册版本，再落实通信后缀。

## 型号与核心异同

| 目录型号／配置 | 圈数表达 | 资料口径 |
| --- | --- | --- |
| KIN60-17ST00 | 单圈17位配置 | 既有手册所列 |
| KIN60-23ST00 | 单圈23位配置 | 当前官网规格书V1.3 |
| KIN60-23BS20 | 单圈配置；23位口径需对应规格书 | 当前官网规格书V1.3 |
| KIN60-21SI00 | 单圈配置；位数按正式表 | 当前官网规格书V1.3 |
| KIN60-21BS20 | 按该历史配置核对 | 既有手册所列 |
| M16S23ST00 | 多圈16位＋单圈23位配置 | 当前官网规格书V1.2，保留原目录写法 |
| M16S23BS20 | 多圈16位＋单圈23位配置 | 当前官网规格书V1.2，保留原目录写法 |
| M16S19SI00 | 多圈16位＋单圈19位配置 | 当前官网规格书V1.2，保留原目录写法 |

## 共同条件与参数依据

- **产品形态**：中空绝对值编码器；单圈与多圈版本分别选型
- **原厂分类**：inductive 电感式
- **供电／电流**：5V±5%；150mA典型，官网技术表
- **通信速率选项**：RS485 2.5Mbps；SSI 2Mbps；BiSS 10Mbps；速率栏另列SPI 3Mbps，须按完整料号确认
- **工作温度**：−40～85°C
- **重复定位**：目录可达±3角秒，不能当绝对精度

## 接口与安装

简介提到RS485、SPI与BiSS，技术表通信栏列RS485、SSI、BiSS-C，速率栏又包含SPI。各栏目口径并非同一订货版本的完整承诺，选型应核对23ST00、23BS20及21SI00等实际料号。

## 动态与装配验证

目录重复定位可达±3角秒，表征反复回到同一位置的一致性。23位输出的数字刻度远小于该值，不能把码宽换算成绝对精度；还需在安装公差和温度条件下看整圈残差与读数噪声。

## 官方资料

- [KIN60 原厂资料入口](https://reagles.cn/en/index.php/index/product_detail/content/10133.html)
- [KIN60 数据手册（官方 PDF）](https://www.reagles.cn/uploads/Download/20231206/154034849925524.pdf)
