---
title: EAM1010系列
wiki: true
wiki_type: model
catalog_type: 其他既有型号
catalog_form: 既有产品（待细分）
wiki_rank: 117
seed_count: 1
lastmod: '2026-10-30'
description: EAM1010是湖南天羿领航的MEMS加速度计系列，官网列为在售惯性产品。
official_url: https://www.enavigate.cn/ypsq.html
wiki_category: 加速度与惯性测量
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
catalog_level: 系列
search_aliases:
- EAM1010系列
---

EAM1010是测量敏感轴比力的MEMS加速度计系列。官网量程覆盖并非单颗可切换范围；现有资料尚未列出逐成员完整后缀。

## 型号与核心异同

| 成员资料状态 | 系列覆盖 | 选型前必须补齐 |
| --- | --- | --- |
| 完整后缀尚未取得 | ±0.5～±30g，分别对应不同成员 | 轴数、输出、供电、噪声、带宽及封装 |

## 共同条件与参数依据

- **器件类别**：MEMS 加速度计系列
- **测量用途**：惯性与运动检测

## 接口与安装

±0.5g至±30g表示系列成员覆盖不同量程，不能视为每个成员都可软件切换。低量程和大量程版本需分别核对噪声、带宽与过载条件。

## 动态与装配验证

选型要先明确测振、倾角还是惯性导航用途，再核对轴数、供电及输出。标定需包含零偏、比例因子与安装方向；温度测试也要区分零偏漂移和随机噪声。

将加速度积分为速度与位置时，零偏会随时间积累，短时低噪声表现不能代替长期零偏、温度与安装应力验证。

## 官方资料

- [EAM1010 原厂资料入口](https://www.enavigate.cn/ypsq.html)
