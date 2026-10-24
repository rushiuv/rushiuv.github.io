---
title: "iC-MA"
description: "可级联的8位霍尔角度器件，支持多种模拟或数字输出模式。"
wiki: true
wiki_type: "model"
wiki_rank: 248
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["iC-Haus"]
wiki_category: "数字角度"
catalog_vendor: "iC-Haus"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["iC-MA"]
official_url: "https://www.ichaus.de/product/ic-ma/"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 角度细分 | 每周期最多256步 |
| 感应结构 | 四霍尔阵列及差分检测 |
| 配置 | 引脚选择工作模式，可级联读取多轴 |
| 输出边界 | 模拟模式与数字模式按配置选择，不是所有输出同时启用 |
| 可选位置数 | 360°内64、128或256个位置，模式依引脚设置 |
| 最高转速 | 公开产品摘要列60000rpm，依其工作条件 |
| 监控 | 弱磁故障信号；不等于系统级全故障诊断 |

参数依据：[原厂产品页或对应资料](https://www.ichauschina.com/products/enc_mag.htm)。

## 产品功能与测量链

iC-MA使用四霍尔阵列及差分检测，提供每周期最多256步的角度表达。工作模式由引脚配置决定，模拟与数字输出不能不加区分地同时列成固定功能。

## 接入与配置

级联用于多轴连接时，需计算整条链的传输长度与刷新时间。256步是一个信号周期内的细分数，是否对应机械一圈取决于磁体与安装结构。

## 使用与验证

接入前按模式核对引脚、电气输出与采样方式。安装测试应检查整周期连续性及过零行为，并区分数字量化和磁场几何引起的误差。

## 官方资料

- [iC-MA 官方资料](https://www.ichaus.de/product/ic-ma/)

- [iC-Haus中文产品摘要：本型号分节](https://www.ichauschina.com/products/enc_mag.htm)
