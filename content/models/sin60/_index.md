---
title: "SIN60系列"
description: "非光学直线编码器，由读头和尺配合进行行程反馈。"
wiki: true
wiki_type: "model"
wiki_rank: 261
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["锐鹰"]
wiki_category: "线性编码"
catalog_vendor: "锐鹰"
catalog_type: "线性编码"
catalog_form: "编码模块"
search_aliases: ["SIN60"]
official_url: "https://www.reagles.cn/index/product_detail/content/10137.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 形态 | 直线编码模块，不是线性霍尔裸芯片 |
| 分辨率／重复定位 | 技术表0.5µm／±0.75µm；栅尺精度另列±10µm/m，三者分开 |
| 安装间隙 | 目录给出读头与尺0.3～0.9mm |
| 通信／电源 | RS485、支持BiSS，5Mbps；DC5V±5% |
| 栅距 | 2mm |
| 最高速度／加速度 | 24m/s；400m/s²，按对应配置及测试条件 |
| 供电／电流 | DC5V±5%；120mA典型 |
| 工作温度 | −20～85°C |
| 防护 | IP67，按安装及连接条件 |
| 附加信息 | 读头集成原点、限位和霍尔信号，经通信输出 |

参数依据：[原厂产品页或对应资料](https://www.reagles.cn/index/product_detail/content/10137.html)。

## 产品功能与测量链

SIN60是与码尺配套的直线通信型增量编码器，面向高速往复及频繁换向运动。读头集成的原点、限位和霍尔信息可通过通信输出，零点恢复仍要遵循增量系统的流程。

## 接入与配置

0.5µm分辨率、±0.75µm重复定位和±10µm/m栅尺精度分别描述步距、重复性和长度误差。三者不能选最小数字合称整机精度；长行程还要考虑尺与设备的热膨胀差。

## 使用与验证

0.6±0.3mm是读头到尺的目录间隙，机械验收还要覆盖全行程起伏和侧向偏移。24m/s、400m/s²与5Mbps也需在对应配置下验证，不应认为所有最大值可同时达到。

## 官方资料

- [SIN60系列 官方资料](https://www.reagles.cn/index/product_detail/content/10137.html)
