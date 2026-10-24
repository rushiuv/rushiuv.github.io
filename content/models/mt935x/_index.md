---
title: "MT935x系列"
description: "带可控休眠的低压线性霍尔系列，正常工作时输出与磁场成比例的电压。"
wiki: true
wiki_type: "model"
wiki_rank: 245
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["麦歌恩","纳芯微"]
wiki_category: "线性磁场"
catalog_vendor: "麦歌恩"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["MT935X"]
official_url: "https://www.magntek.com.cn/136/95"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 供电 | 1.7～3.6V |
| 模式 | SLEEP引脚控制正常和休眠 |
| 电流条件 | 官方发布页约2mA工作、50µA休眠 |
| 休眠边界 | 休眠时输出高阻且不响应磁场，不能视为持续测量 |

参数来源：本页所列[原厂产品资料与手册](https://www.magntek.com.cn/136/95)。

## 工作方式与型号定位

MT935x用于低压模拟磁场检测，SLEEP脚把正常测量与休眠分开。休眠时输出高阻且不响应磁场，不能同时按低休眠电流和连续测量来计算系统性能。

## 安装、接口与配置

供电1.7～3.6V适合低压节点，但ADC输入、上拉与关断顺序仍要检查。休眠输出高阻时，采样节点可受泄漏或保持电荷影响，主控应避免把该电压解释成有效位置。

## 校准与选型验证

唤醒后需要等待信号稳定，再采集磁场相关电压。功耗评估应加入唤醒和测量时间；位置应用还需测试不同气隙、温度与运动速度下的输出映射，而不是只测静止工作电流。

## 官方资料

- [MT935x系列 官方资料](https://www.magntek.com.cn/136/95)
