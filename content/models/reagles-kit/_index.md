---
title: "锐鹰KIT系列"
description: "同侧中空电感双编码器，以两个转子与读头构成紧凑反馈模块。"
wiki: true
wiki_type: "model"
wiki_rank: 259
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["锐鹰"]
wiki_category: "旋转编码模块"
catalog_vendor: "锐鹰"
catalog_type: "旋转编码模块"
catalog_form: "编码模块"
search_aliases: ["KIT"]
official_url: "https://www.reagles.cn/index/product_detail/content/10158.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 结构 | 非接触电感检测，官网称最薄小于8mm |
| 角度／通信 | 两端23bit，RS485、2.5Mbps |
| 重复定位 | 官网±10角秒，不能当扭矩精度 |
| 工况 | 表列≤6000rpm、−20～105°C；装配后仍需验证 |
| 双通道用途 | 单接口传送两端位置；采样同步与帧结构须另核对 |
| 最薄结构 | 官网描述小于8mm；具体尺寸按型号图 |

参数依据：[原厂产品页或对应资料](https://www.reagles.cn/index/product_detail/content/10158.html)。

## 产品功能与测量链

KIT采用同侧电感双编码器结构，激励与接收线圈感知两个转子的涡流变化。两个转子的相对安装和各自读头位置都参与最终测量，薄型化不能代替安装公差要求。

## 接入与配置

两端23bit输出、±10角秒重复定位和最薄小于8mm是不同类型的产品信息。具体厚度要以所选机械尺寸图为准，不能对所有KIT型号统一写8mm。

## 使用与验证

联调时按两路分别核对零点、方向、跨零和动态同步，再评价关节控制。RS485的2.5Mbps是线速，双位置实际刷新率还取决于帧长、轮询和内部测量时序。

## 官方资料

- [锐鹰KIT系列 官方资料](https://www.reagles.cn/index/product_detail/content/10158.html)
