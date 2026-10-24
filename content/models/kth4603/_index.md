---
title: "KTH4603系列"
description: "XYZ三轴全极霍尔开关，用于多方向磁体接近检测，而非三轴场强采样。"
wiki: true
wiki_type: "model"
wiki_rank: 207
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "磁开关"
catalog_vendor: "昆泰芯"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["KTH4603"]
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心性能

### 产品介绍

XYZ三轴全极霍尔开关，用于多方向磁体接近检测，而非三轴场强采样。

本页只写入能够由 KTH4603系列 当前官方入口、下载件或站内已核对来源支持的内容。资料口径为“官方公开产品页或目录，核对：2026-10-18”。系列名、相近料号和不同后缀的参数不自动并入本型号；典型值、可配置上限与保证范围也分别理解。

### 核心参数

- **检测量** 三轴磁场触发的开关事件
- **版本** AA-STx目录2.5Hz；AB-STx目录5Hz
- **电源／输出** 2.25～5.5V，开漏
- **温度／封装** −40～125°C；SOT23-3／SOT23-6按型号选

### 接口与输出

KTH4603系列 与主控或驱动器的连接应以完整订货号、引脚表和时序章节为准。下面保留官方公开页已经确认的输出与编码信息；没有列出的接口不据系列习惯补写。

- **版本** AA-STx目录2.5Hz；AB-STx目录5Hz
- **电源／输出** 2.25～5.5V，开漏

### 工作原理

KTH4603系列 把磁场变化转换成离散状态，而不是连续角度值。其工作链路是：磁敏单元检测目标磁体产生的场，比较与迟滞电路判定阈值，输出级再给出逻辑状态；任一极性的磁场达到动作阈值即可改变开关状态，释放阈值决定返回。动作点、释放点、采样频率和输出拓扑必须按具体版本理解。

### 典型应用与使用条件

XYZ三轴全极霍尔开关，用于多方向磁体接近检测，而非三轴场强采样。

把 KTH4603系列 放入样机前，至少应核对：目标磁极与运动方向、动作／释放阈值及迟滞、采样频率与最高运动速度、输出上拉、灌电流和上电状态。典型应用只是选型入口，不等于原厂对任意整机结构的性能承诺；最终应在目标装配和控制周期下保留可复现的原始数据。

本页只写入能够由 KTH4603系列 当前官方入口、下载件或站内已核对来源支持的内容。资料口径为“官方公开产品页或目录，核对：2026-10-18”。系列名、相近料号和不同后缀的参数不自动并入本型号；典型值、可配置上限与保证范围也分别理解。

## 官方资料

- [KTH4603系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html)
