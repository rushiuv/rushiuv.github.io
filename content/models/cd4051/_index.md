---
title: "CD4051"
wiki: true
wiki_type: "model"
wiki_rank: 115
seed_count: 1
lastmod: "2026-10-24"
description: "CD4051 在本站对应 TI CD4051B 八通道模拟多路复用器，用于在多个模拟输入之间选择通路。"
official_url: "https://www.ti.com/product/CD4051B"
datasheet_url: "https://www.ti.com/lit/ds/symlink/cd4051b.pdf"
datasheet_label: "官方数据手册"
wiki_category: "多路模拟扫描"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 本站对应版本 | TI CD4051B |
| 开关结构 | 8 选 1 模拟多路复用 |
| 控制 | 地址选择与禁止端 |
| 信号功能 | 切换模拟通路，不包含 ADC |
| 推荐供电范围 | 单电源3～20V；双电源±3～±10V，按CD4051B手册 |
| 模拟路径 | 双向；break-before-make切换 |
| 导通电阻 | 125Ω典型，VDD=15V；不能套用到低压条件 |
| 带宽 | 产品目录20MHz，具体测试条件见手册 |
| 工作温度 | −55～125°C，按订货等级 |
| 封装 | 16引脚SOIC、TSSOP、PDIP、SOP |

参数依据：[原厂产品页或对应资料](https://www.ti.com/product/CD4051B)。

## 产品功能与测量链

CD4051B将八路模拟信号中的一路连接到公共端，本身不采样、不存储，也不输出数字角度。用于多路传感采集时，它只是ADC前面的通路选择器。

## 接入与配置

地址切换后需给模拟节点建立时间。导通电阻、源阻抗、寄生电容和ADC采样电容共同决定误差，不能把数字选择信号翻转时刻当成模拟信号已稳定。

## 使用与验证

正余弦两路若轮流采集，会产生时间偏移；运动越快，相位误差越明显。信号电压还须落在所用电源配置允许的范围内，不能仅依据逻辑控制电平选择供电。

快速轮询时应检查上个通道的残留电荷，尤其关注高源阻抗输入；扫描整组通道所需时间也要计入测量延迟。

## 官方资料

- [CD4051 原厂资料入口](https://www.ti.com/product/CD4051B)
- [CD4051 数据手册（官方 PDF）](https://www.ti.com/lit/ds/symlink/cd4051b.pdf)
