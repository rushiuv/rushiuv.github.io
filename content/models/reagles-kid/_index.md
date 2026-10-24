---
title: "锐鹰KID系列"
description: "异侧中空双编码器，集成双读头并通过单接口传输两路位置。"
wiki: true
wiki_type: "model"
wiki_rank: 258
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["锐鹰"]
wiki_category: "旋转编码模块"
catalog_vendor: "锐鹰"
catalog_type: "旋转编码模块"
catalog_form: "编码模块"
search_aliases: ["KID"]
official_url: "https://www.reagles.cn/index/product_detail/content/10159.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 结构 | 异侧双编码器模块，面向机器人关节 |
| 输出码宽 | 23bit；官网另列有效分辨率大于17bit，两种口径分开 |
| 通信 | RS485，2.5Mbps |
| 重复定位 | 技术表电机端≤±10角秒、减速机端≤±8角秒；不等于绝对精度 |
| 最高主轴转速 | ≤6000rpm，官网技术表 |
| 工作温度 | −20～105°C |
| 有效分辨率 | 目录>17bit；与23bit输出码宽分开 |

参数依据：[原厂产品页或对应资料](https://www.reagles.cn/index/product_detail/content/10159.html)。

## 产品功能与测量链

KID将两路读头布置在关节异侧，通过单个通信接口传递电机端与减速机端的位置。它可以减少连接器，但两个位置字段的时间关系仍需按协议确认。

## 接入与配置

23bit是输出码宽，官网同时列有效分辨率大于17bit。电机端≤±10角秒、减速机端≤±8角秒是重复定位项目，不应改写成两端绝对精度或扭矩精度。

## 使用与验证

装配时应分别记录两端机械零点、方向和减速比。用角差估算弹性扭转时，还需辨识回差、摩擦和结构刚度；接口共用也不能据此认定已提供同步扭矩输出。

## 官方资料

- [锐鹰KID系列 官方资料](https://www.reagles.cn/index/product_detail/content/10159.html)
