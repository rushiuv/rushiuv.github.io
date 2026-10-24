---
title: "VCS2381／2382／2383"
description: "二维全极AMR开关组，以不同磁阈值区分，输出都是开关状态。"
wiki: true
wiki_type: "model"
wiki_rank: 239
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["圣邦微"]
wiki_category: "磁开关"
catalog_vendor: "圣邦微"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["VCS2381","VCS2382","VCS2383"]
official_url: "https://www.sg-micro.com/product/VCS2381"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应／输出 | 平面二维全极感应，推挽输出 |
| 阈值区别 | 2381：±7／±5Gs；2382：±15／±12Gs；2383：±10／±8Gs（动作／释放） |
| 电源／采样 | 2～5.5V，15Hz，典型0.2µA |
| 封装／温度 | SOT23-3，−40～125°C |

参数来源：本页所列[原厂产品资料与手册](https://www.sg-micro.com/product/VCS2381)。

## 工作方式与型号定位

VCS2381、2382与2383是二维全极AMR磁开关，输出为推挽状态。它们检测的是磁场跨过动作/释放阈值，不提供连续角度或位移值。

## 安装、接口与配置

±7/±5Gs、±15/±12Gs与±10/±8Gs分别是各成员动作/释放口径。符号代表极性范围，磁滞窗口用于抑制临界反复切换，不能把两个数理解成连续线性量程。

## 校准与选型验证

15Hz采样意味着事件捕捉受采样时序限制，典型0.2µA不能与高速持续检测拼成一个条件。选型应检查磁体全公差、敏感方向、最短事件和上电状态，并在温度下复测阈值。

## 官方资料

- [VCS2381／2382／2383 官方资料](https://www.sg-micro.com/product/VCS2381)
