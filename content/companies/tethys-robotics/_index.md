---
title: "Tethys Robotics"
wiki: true
wiki_type: "company"
wiki_rank: 220
lastmod: "2026-10-22"
description: "苏黎世 Schlieren 的 ETH 衍生公司，Tethys ONE 水下机器人 2024 年发布，能在 3.5 节水流中自主保持位置做定点检查。"
wiki_category: "水下与海事机器人"
official_url: "https://www.tethys-robotics.ch/"
---

Tethys Robotics 做的是**水下整机**：一台紧凑型水下机器人，卖点在"能在急流里定住"。这条卖点对推进与反馈的含义很直接——能抗 3.5 节水流做定点作业，靠的不是更强的推进器，而是闭环控制，而闭环里最贵的那一环是"我现在在哪、朝哪、有没有被冲走"。它公开的正好是能力，不公开的正好是这套反馈。

## ETH 衍生，Schlieren 落地

法律主体 Tethys Robotics AG，地址 Zürcherstrasse 39d, 8952 Schlieren，瑞士。官网自述是苏黎世联邦理工（ETH Zurich）的衍生公司（ETH Spin-off），强调"长期研究积累"。[公司使命页](https://www.tethys-robotics.ch/company/our-mission)

里程碑给了两条硬信息：2023 年拿到 Wyss Zurich 转化中心、Bridge PoC、InnoBooster（Gebert Rüf 基金会）与 Venture Kick 的支持；2024 年发布重新设计的 Tethys ONE 并全球接单，官方写它在 3.5 节水流中可自主保持位置，能在浑浊水域做定点作业，适配海上任务。

## 公开的能力清单

| 公开项 | 官方口径 | 备注 |
| --- | --- | --- |
| 抗流能力 | 3.5 节水流中自主保持位置 | 2024 年发布口径 |
| 部署时间 | 5 分钟内可下水 | 产品页 |
| 弱能见度 | 零能见度条件下做高分辨率建图 | 产品页 |
| 载荷 | 支持多种任务载荷 | 未列型号 |
| 应用 | 油气、海上风电、水电、核电、电缆与通信、土木、公共安全、港口、海洋科研 | 官网应用目录 |
| 交付形态 | 整机 + 作业服务 | 官网 |

"零能见度建图"这一条决定了它必须靠声学而不是光学：官方没说用哪种声呐，也没给频率与量程，只能确认它把"看不清也能画图"写成了产品能力。[产品页](https://www.tethys-robotics.ch/product)

## 在编码器链上的位置

它买推进器、驱动、声呐、惯导与水深计，自己做整机与自主控制，卖给海上能源与公共安全客户。这条链上的角度反馈分两种：推进器里的那一路只服务于换相与转速环，按行业惯例不对外提供位置信息，供应商也不会为它单独加编码器；真正需要"角度"的是机械臂、云台这类可动件，如果整机上装了，那颗编码器的采购口在臂的供应商那里，不在 Schlieren。

前一种最容易被误判：看到一台水下机器人，很容易以为"推进器多，编码器就多"。实际相反——推进器越多，越倾向于用无感 FOC，因为穿压力壳出线越少越好。

## 官方资料

- [Tethys Robotics 官网](https://www.tethys-robotics.ch/)
- [产品页（Tethys ONE 能力）](https://www.tethys-robotics.ch/product)
- [公司使命与里程碑](https://www.tethys-robotics.ch/company/our-mission)
- [应用目录](https://www.tethys-robotics.ch/applications)
- [新闻](https://www.tethys-robotics.ch/news)
