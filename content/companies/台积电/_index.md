---
title: "台积电"
wiki: true
wiki_type: "company"
wiki_rank: 154
seed_count: 1
lastmod: "2026-10-22"
description: "台积电以新竹为总部，逻辑节点从 0.18µm 排到 N2（2025 年四季度量产），特色工艺另列 MEMS、CIS、eNVM 与 BCD。"
official_url: "https://www.tsmc.com/"
wiki_category: "制造工艺与产业分工"
related_models: []
---

台积电在编码器链上不出现，它出现的地方是所有用先进节点芯片的产品——机器人主控 SoC、视觉处理、AI 加速。它的公开资料分两层：逻辑节点的年表式叙述（谁先量产、哪一年）与特色工艺的类别清单。读它最该注意的是这两层的时间点，而不是"最先进"这个形容词。

## 公司与品牌

总部与企业研发在台湾新竹科学园区，官网把总部与 Fab 12A 写在同一地址（新竹市力行六路 8 号）。12 英寸厂分布在新竹（Fab 12B、Fab 20）、台南（Fab 14A/14B、Fab 18A/18B）、台中（Fab 15A/15B）、高雄（Fab 22）、南京（Fab 16）、日本熊本（JASM）、美国凤凰城（TSMC Arizona）；8 英寸厂在新竹（Fab 3、Fab 5）与台南（Fab 6、Fab 8）。官网定位写作 Dedicated IC Foundry。[厂区清单](https://www.tsmc.com/english/aboutTSMC/TSMC_Fabs)

## 逻辑节点有明确年表，特色工艺按类别列

官网逻辑工艺页按节点逐条给"首次量产/首次试产"的年份，这是可核对的骨架：

| 节点 | 官网写的时间与定位 |
| --- | --- |
| [N2](https://www.tsmc.com/english/dedicatedFoundry/technology/logic) | 第一代纳米片晶体管，2025 年四季度按计划进入量产 |
| N3 | 2022 年首个把 3nm FinFET 推进量产的代工厂 |
| N5 | 2020 年首个量产 5nm FinFET |
| N7 | 2018 年首个量产 7nm FinFET |
| 16nm | 2013 年首个进入 16nm FinFET 风险试产，2014 年交付首个全功能客户产品 |
| 28nm | 2011 年首个提供 28nm 通用工艺；22ULP 由 28nm 派生 |
| 40/65/90nm | 分别在 2008、2005、2004 年量产或试产，90nm 首次用浸没式光刻 |
| 0.13µm | 业界首个 low-k 铜互连 SoC 工艺；另有 0.18µm 成熟节点 |

A12、A14、A16 三条则是纳米片加背面供电的后续路线，官网分别写作第二代背面供电、下一代 full-node PPA、以及纳米片加背面供电的组合。特色工艺一侧，官网列 MEMS、CIS、eNVM、MS/RF、Analog、高压、BCD 与 ULP，并写明 2011 年推出业界首个 Sensor SoC 工艺。[特色工艺](https://www.tsmc.com/english/dedicatedFoundry/technology/specialty)

## 在编码器链上的位置

角度与位置芯片几乎不需要先进节点：够用的是 MS/RF、Analog、BCD、eNVM 这几类，做片上光电的光学编码器才可能碰 CIS。所以"某颗编码器芯片用台积电"这句话，推理价值很低——真正能推的是它对模拟精度、温漂、非易失存储的选择，而不是节点先进程度。先进节点影响的是机器人主控与算力板：那里决定一台设备能跑多大模型、能接几路相机。

节点页给相对提升（同功耗性能、密度改进）与时间点，不给晶圆价格、产能分配、良率与客户名单；特色工艺页给类别与能力描述，不给各平台的电压档位表与 IP 成熟度。

## 官方资料

- [TSMC 英文官网](https://www.tsmc.com/english)
- [逻辑工艺节点年表](https://www.tsmc.com/english/dedicatedFoundry/technology/logic)
- [特色工艺（MEMS、CIS、eNVM、BCD 等）](https://www.tsmc.com/english/dedicatedFoundry/technology/specialty)
- [厂区清单](https://www.tsmc.com/english/aboutTSMC/TSMC_Fabs)
