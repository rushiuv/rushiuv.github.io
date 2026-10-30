---
title: SIN60系列
description: 非光学直线编码器，由读头和尺配合进行行程反馈。
wiki: true
wiki_type: model
wiki_rank: 261
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 锐鹰
wiki_category: 线性编码
catalog_vendor: 锐鹰
catalog_type: 线性编码
catalog_form: 编码模块
search_aliases:
- SIN60
- SIN60系列
official_url: https://www.reagles.cn/index/product_detail/content/10137.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

SIN60是与2mm栅距码尺配套的直线通信型增量编码模块。现有公开表对应系列配置，未展开完整订货号，不能把协议名称当成具体型号。

## 型号与核心异同

| 配置（非完整料号） | 目录能力 | 需核对的差异 |
| --- | --- | --- |
| RS485通信配置 | 产品技术表列出；5Mbps目录口径 | 完整料号、报文与更新时序 |
| BiSS支持配置 | 简介列支持BiSS | 具体接口版本与订货映射 |

## 共同条件与参数依据

- **形态**：直线编码模块，不是线性霍尔裸芯片
- **分辨率／重复定位**：技术表0.5µm／±0.75µm；栅尺精度另列±10µm/m，三者分开
- **安装间隙**：目录给出读头与尺0.3～0.9mm
- **栅距**：2mm
- **最高速度／加速度**：24m/s；400m/s²，按对应配置及测试条件
- **供电／电流**：DC5V±5%；120mA典型
- **工作温度**：−20～85°C
- **防护**：IP67，按安装及连接条件
- **附加信息**：读头集成原点、限位和霍尔信号，经通信输出

## 接口与安装

0.5µm分辨率、±0.75µm重复定位和±10µm/m栅尺精度分别描述步距、重复性和长度误差。三者不能选最小数字合称整机精度；长行程还要考虑尺与设备的热膨胀差。

## 动态与装配验证

0.6±0.3mm是读头到尺的目录间隙，机械验收还要覆盖全行程起伏和侧向偏移。24m/s、400m/s²与5Mbps也需在对应配置下验证，不应认为所有最大值可同时达到。

## 官方资料

- [SIN60系列 官方资料](https://www.reagles.cn/index/product_detail/content/10137.html)
