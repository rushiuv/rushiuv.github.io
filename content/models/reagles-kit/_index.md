---
title: KIT系列
description: 同侧中空电感双编码器，以两个转子与读头构成紧凑反馈模块。
wiki: true
wiki_type: model
wiki_rank: 259
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 锐鹰
wiki_category: 旋转编码模块
catalog_vendor: 锐鹰
catalog_type: 旋转编码模块
catalog_form: 编码模块
search_aliases:
- KIT
- KIT系列
official_url: https://www.reagles.cn/index/product_detail/content/10158.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

锐鹰KIT是同侧电感双编码器系列。两端位置通过单接口传送，当前资料未展开完整订货成员和逐成员差异。

## 型号与核心异同

| 通道（非独立型号） | 输出 | 通信 | 尚需核对 |
| --- | --- | --- | --- |
| 第一端位置 | 23bit | RS485，2.5Mbps | 采样同步、字段与零点 |
| 第二端位置 | 23bit | 同一接口 | 采样同步、字段与零点 |

## 共同条件与参数依据

- **结构**：非接触电感检测，官网称最薄小于8mm
- **重复定位**：官网±10角秒，不能当扭矩精度
- **工况**：表列≤6000rpm、−20～105°C；装配后仍需验证
- **双通道用途**：单接口传送两端位置；采样同步与帧结构须另核对
- **最薄结构**：官网描述小于8mm；具体尺寸按型号图

## 接口与安装

两端23bit输出、±10角秒重复定位和最薄小于8mm是不同类型的产品信息。具体厚度要以所选机械尺寸图为准，不能对所有KIT型号统一写8mm。

## 动态与装配验证

联调时按两路分别核对零点、方向、跨零和动态同步，再评价关节控制。RS485的2.5Mbps是线速，双位置实际刷新率还取决于帧长、轮询和内部测量时序。

## 官方资料

- [锐鹰KIT系列 官方资料](https://www.reagles.cn/index/product_detail/content/10158.html)
