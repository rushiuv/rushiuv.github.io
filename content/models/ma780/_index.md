---
title: "MA780"
description: "带角度变化唤醒检测的低功耗磁角度芯片，适合间歇读数。"
wiki: true
wiki_type: "model"
wiki_rank: 220
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA780"]
official_url: "https://www.monolithicpower.com/en/ma780.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度编码 | 8～12位，依配置 |
| 低功耗功能 | 角度变化检测可触发唤醒 |
| 模式区别 | 睡眠或周期唤醒电流不能当连续高速工作电流 |
| 测量对象 | 永磁体方向变化，不是触点式机械编码器 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～125°C |
| 状态电流 | 空闲<0.5 µA；活动10 mA，按工作占空比求平均 |
| 磁场下限 | 30 mT |
| 配置延迟范围 | 官网表4～16,000 µs，依配置 |
| 截止频率范围 | 官网表5～160,000 Hz，依配置 |
| 封装 | QFN-16，3 × 3 mm |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma780.html)。

## 工作方式与型号定位

MA780通过周期性工作降低平均功耗，同时检测角度变化以唤醒系统。空闲低于0.5µA与活动10mA是不同状态，不能把空闲电流当作持续读角度的功耗。

## 安装、接口与配置

工作周期由内部时钟或外部控制器协调，滤波窗影响8～12位分辨率。产品表4～16000µs延迟和5～160000Hz截止频率覆盖不同配置，需和唤醒周期一起理解。

## 校准与选型验证

适用于电池节点和间歇位置监测时，应验证最短事件能否在采样窗口内被捕捉，以及唤醒到首次有效角度的时序。功耗预算还要加主控、SPI与系统唤醒时间，而不只计算传感器空闲档。

## 官方资料

- [MA780 官方资料](https://www.monolithicpower.com/en/ma780.html)
