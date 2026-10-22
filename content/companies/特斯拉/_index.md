---
title: "特斯拉"
description: "特斯拉：Optimus 第一代产线 2026 年在弗里蒙特安装、初期产出用于训练数据采集；Cortex 1／2 训练算力超 90／115 MW，编码器方案从未公开。"
wiki: true
wiki_type: "company"
wiki_rank: 15
seed_count: 13
lastmod: "2026-10-22"
official_url: "https://www.tesla.com/"
related_models: []
related_companies: []
---

特斯拉在这条链上是"整机 + 自研执行器"的一端，也是少数把产线状态写进定期材料的公司。对做位置反馈的人，它的价值不在产品页，而在 8-K 与季报：Optimus 走到哪一步、线建在哪、初期机器人拿去干什么，这些都能核。至于关节里用什么编码器、单编还是双编、谁供的货，官方从未公开，任何"特斯拉用了某方案"的说法都需要供应商侧的独立证据。

## 官方把车辆、机器人、推理硬件放在同一页

官网 AI & Robotics 页把三件事并列。FSD 芯片一节讲自研推理芯片的架构、功耗与验证流程；神经网络一节给了可核对的数字——一次完整的 FSD 网络构建包含 48 个网络、训练需 7 万 GPU 小时、每个时间步输出 1000 个张量；人形一节只讲目标：通用双足、可执行危险重复枯燥的任务，需要平衡、导航、感知与物理交互的软件栈。这是研发口径，不是产品规格，页面上没有任何关节、自由度或传感配置的参数。

## 2026 年第二季度：产线在装，机器先给训练用

2026 年 7 月 22 日的 8-K 季度更新写得具体：弗里蒙特工厂停掉 Model S 与 X 的产线后，开始安装 Optimus 第一代产线，预计当年内开始生产；初期下线的机器用于 Optimus Academy 做训练数据采集与功能开发，得州超级工厂的建设同期推进。同一份材料的产能表把 Optimus 在加州与得州都标为"建设中"。AI 训练算力：Cortex 1 超 90 MW、Cortex 2 超 115 MW，均标为在产。这几条是逐年可对照的硬信息，比二手转述稳。

## 在编码器链上的位置

它买什么：车辆侧的电机与电控是成熟量产体系，人形侧的执行器是自研方向，但电机、减速、位置反馈的来源从未公开。能推的是取舍——自研执行器意味着它对编码器的体积、抗磁干扰、成本有内部标准，供应商更可能被指定而非被选型；不能推的是具体料号、位数、接口与封装。反过来说，把特斯拉当"行业风向标"来证明某条技术路线，目前没有公开依据。

## 官方资料

- [AI & Robotics 官方页面](https://www.tesla.com/ai)
- [2026 年第二季度 8-K 季度更新（PDF，36 页）](https://ir.tesla.com/_flysystem/s3/sec/000162828026049213/tsla-20260722-gen.pdf)
- [Robotaxi 官方页面](https://www.tesla.com/robotaxi)
- [Master Plan Part 3 官方页面](https://www.tesla.com/master-plan-part-3)
- [能源业务官方页面](https://www.tesla.com/energy)
- [Master Plan Part 3 报告 PDF](https://www.tesla.com/ns_videos/Tesla-Master-Plan-Part-3.pdf)
