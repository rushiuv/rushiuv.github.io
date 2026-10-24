---
title: "KMZ60"
wiki: true
wiki_type: "model"
catalog_type: "模拟角度"
catalog_form: "芯片"
wiki_rank: 124
seed_count: 1
lastmod: "2026-10-24"
description: "KMZ60是NXP历史磁角度传感器件，提供与磁场方向有关的正余弦模拟信息。"
official_url: "https://www.nxp.com/products/KMZ60"
related_companies: ["NXP"]
wiki_category: "模拟角度信号与外部解算"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 敏感技术 | 磁阻角度检测 |
| 输出 | 模拟正余弦信号 |
| 处理边界 | 需外部采样与角度计算 |
| 尚待补齐的核心参数 | 现行产品页未给出完整历史料号的推荐供电、电流、磁场与精度条件。 |

参数来源：本页所列[原厂产品资料与手册](https://www.nxp.com/products/KMZ60)。

## 工作方式与型号定位

KMZ60提供与磁场方向相关的模拟正余弦信息。它属于需要外部采样解算的磁角度前端，不能按内部带数字角度处理的编码器接入。

## 安装、接口与配置

放大器与ADC需匹配信号共模、差分摆幅和供电条件。两路采样时间不一致会在运动时转化为相位误差，因此应把采集同步和模拟滤波一起设计。

## 校准与选型验证

角度解算前先校正零偏、幅值及正交误差，再对照机械参考检查周期残差。当前资料入口属于历史产品资料，完整订货后缀和适用手册需另核，不能移植其他NXP磁传感器的保证参数。

## 官方资料

- [KMZ60 原厂资料入口](https://www.nxp.com/products/KMZ60)
