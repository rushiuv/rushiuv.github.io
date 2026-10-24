---
title: "AM26C32"
wiki: true
wiki_type: "model"
wiki_rank: 76
seed_count: 2
lastmod: "2026-10-24"
description: "AM26C32 是 TI 四通道差分线路接收器，将线路差分信号转换为逻辑电平，可用于编码器接收端。"
official_url: "https://www.ti.com/product/AM26C32"
related_companies: ["TI"]
datasheet_url: "https://www.ti.com/lit/ds/symlink/am26c32.pdf"
datasheet_label: "官方数据手册"
wiki_category: "差分接收与位置数据"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 通道 | 4 路差分接收，0 路发送 |
| 供电 | 单 5 V |
| 共模输入范围 | ±7 V |
| 差分输入灵敏度 | ±200 mV |
| 传播延迟 | 17 ns 典型值 |
| 输入迟滞 | 60 mV 典型值 |
| 输出 | 三态，共用使能；输入开路时输出高电平 |
| 线路标准 | TIA/EIA-422-B、TIA/EIA-423-B、ITU V.10／V.11 |
| 信号速率 | 最高10Mbps，目录值；时序仍按所用负载与温度核对 |
| 工作电流 | 10mA典型；目录最大供电电流15mA，按订货等级 |
| 温度等级 | 目录覆盖−40～125°C；具体后缀需核对 |
| 封装 | 16引脚SOIC、TSSOP、SOP、SSOP与PDIP选项 |

参数依据：[原厂产品页或对应资料](https://www.ti.com/product/AM26C32)。

## 产品功能与测量链

AM26C32位于编码器链路接收端，将四组差分信号变为本地逻辑信号。它不生成位置，也不把普通模拟正余弦直接转换为角度。

## 接入与配置

单5V供电与±7V输入共模范围是不同指标。接入3.3V控制器前应核对输出电平兼容性；长线还要结合发送端、终端电阻和线缆阻抗设计。

## 使用与验证

17ns是传播延迟典型值，不能作为所有温度与负载下的最大延迟。输入开路的高电平行为也不能替代整条线路的断线诊断，短路和共模越界需另测。

恢复差分电平之后，主控仍须解析协议、校验并换算单位；接收器不能判断当前报文是否代表有效位置。

## 官方资料

- [AM26C32 原厂资料入口](https://www.ti.com/product/AM26C32)
- [AM26C32 数据手册（官方 PDF）](https://www.ti.com/lit/ds/symlink/am26c32.pdf)
