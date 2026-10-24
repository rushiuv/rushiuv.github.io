---
title: "MA782"
description: "小型低功耗角度芯片，保留SPI读数及角度变化唤醒能力。"
wiki: true
wiki_type: "model"
wiki_rank: 221
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA782"]
official_url: "https://www.monolithicpower.com/en/products/ma782.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度编码 | 8～12位 |
| 接口／封装 | SPI；QFN-14（2×2mm） |
| 供电 | 3.3V标称 |
| 功耗条件 | 空闲低于0.5µA，活动状态约10mA；两者不是同一工作点 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～125°C |
| 状态电流 | 空闲<0.5 µA；活动10 mA，按工作占空比求平均 |
| 磁场下限 | 30 mT |
| 配置延迟范围 | 官网表4～16,000 µs，依配置 |
| 截止频率范围 | 官网表5～160,000 Hz，依配置 |
| 封装 | QFN-14，2 × 2 mm |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/products/ma782.html)。

## 工作方式与型号定位

MA782保留低功耗周期采集和角度变化唤醒，并采用2×2mm封装。它可在轴端或离轴检测永磁体方向，SPI用于角度与配置访问。

## 安装、接口与配置

空闲低于0.5µA和活动10mA要按占空比合成平均电流。缩短唤醒间隔有利于捕捉运动，但会提高平均功耗；8～12位分辨率和滤波窗也需要随应用选择。

## 校准与选型验证

磁场检测阈值与角度变化阈值解决不同问题。样机应测试磁体移动、快速转动和小角抖动时的唤醒行为，冷启动后检查零点、工作周期与阈值是否恢复，不把唤醒标志直接解释成已得到最新角度。

## 官方资料

- [MA782 官方资料](https://www.monolithicpower.com/en/products/ma782.html)
