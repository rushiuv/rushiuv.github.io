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

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 检测方式 | XYZ三轴全极霍尔开关，输出事件状态 |
| 供电 | 2.25～5.5V |
| AA-STx版本 | 2.5Hz；5.5µA（3.3V），官网目录 |
| AB-STx版本 | 5.0Hz；8.0µA（3.3V），官网目录 |
| 动作/释放阈值 | ±25Gs/±15Gs，官网目录 |
| 输出 | 开漏 |
| 工作温度 | −40～125°C |
| 封装 | SOT-23-3L或SOT-23-6L，依具体版本 |

参数依据：[原厂产品与型号选型表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html)。

## 三轴开关不是三轴磁通计

KTH4603用于多方向磁体接近事件，三个方向参与开关判断。它不通过I²C或SPI输出XYZ连续场强，也不能仅凭三轴名称推导出三维位置或姿态。

## 慢采样决定事件速度

目录2.5Hz和5Hz对应约400ms和200ms采样周期。该换算表明它适合慢变化、低功耗的状态检测；若磁体短时间掠过，需要单独验证捕获，不把慢采样版本放进高速齿轮测速。

## 开漏输出怎样接

输出上拉电压、电阻和控制器输入电平要匹配，待机电流还需算入外部上拉的消耗。SOT-23-3L与6L的引脚和敏感方向必须按该版本图示确定。

## 验收重点

至少沿目标机构的全部接近方向扫磁体，记录动作与释放位置。测试最大气隙、磁体极性、全温以及冷启动状态，避免只在一个方向验证后把三轴能力理解为所有方向距离相同。

## 官方资料

- [KTH4603系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html)
