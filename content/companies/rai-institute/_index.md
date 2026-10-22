---
title: "RAI Institute"
wiki: true
wiki_type: "company"
wiki_rank: 217
lastmod: "2026-10-22"
description: "Marc Raibert 主持的机器人与 AI 研究机构，剑桥 Kendall Square 与苏黎世 Oerlikon 两处，五大方向里明确写自己在造传感器。"
wiki_category: "科研机构"
official_url: "https://rai-inst.com/about/"
---

RAI Institute 是**研究机构**这一层：它不卖机器人，也不卖器件，靠论文、博客和视频对外。对做编码器的人来说，它的用处不是采购入口，而是公开的硬件描述——机构自述在研究"给轮式、人形、四足机器人用的先进传感器"，这句话是它在整条链上唯一直接碰感知的地方。

## 两个园区：剑桥 Kendall Square 与苏黎世 Oerlikon

机构由 Marc Raibert 主持，职务写 Executive Director。Raibert 是波士顿动力的创始人，官网在团队段落里直接这么介绍。总部园区在麻省剑桥 Kendall Square，地址 145 Broadway, Cambridge, MA 02142；苏黎世办公室在 Oerlikon 火车站旁的机器人与 AI 聚集区。[机构介绍](https://rai-inst.com/about/)

研究分成五个方向：灵巧操作、面向控制的高级学习、面向物理交互的数据驱动 AI 模型、挑战性环境中的导航、机器人在社会中的伦理。第三个方向的自述值得抄下来——现有 AI 模型难以把学到的技能迁移到需要精确力控与紧公差的物理任务，所以要把数据驱动与"体现机器人物理性的原理模型"结合起来。[研究方向](https://rai-inst.com/research/)

## 五个方向里，哪一条真的碰角度反馈

| 方向 | 官方自述的关键句 | 与角度传感的关系 |
| --- | --- | --- |
| 灵巧操作 | 要超越以静态抓取为主的现状，做动态操作、装配、维修、搬运 | 手与臂的关节角是策略输入 |
| 高级学习控制 | 用强化学习做控制，靠组合自然动态行为完成长时序任务 | 控制频率与反馈质量决定可学动作的上限 |
| 物理交互的数据驱动模型 | 现有模型在精确力控与紧公差任务上迁移失败 | 力矩与位置的可观测性直接决定数据质量 |
| 挑战性环境导航 | 明确写"为轮式、人形、四足机器人造先进传感器" | 全机构唯一直接造传感器的地方 |
| 机器人与社会伦理 | 社会、法律、伦理语境 | 无直接关系 |

第四行的原话是 building advanced sensors that provide robots (including wheeled, humanoid, and quadruped designs) with a deep understanding of their surroundings。这是它公开承认自研传感的唯一出处，但没有说造的是哪种传感器，也没有给任何指标。

## 在编码器链上的位置

它买整机与执行器，产出论文、模型与人才。上游是机器人平台厂与执行器厂，下游没有商业客户，成果以开源仓库、论文、视频的形式外溢。选型权不在它手里：它用的机器是买来的或合作方提供的，关节里的角度反馈跟着平台走；它自己能定的是外挂传感器的安装位置与数据接口。

对供应商的实际含义是：这里没有采购口，只有曝光口。要进这个圈子，渠道是论文共著、开源仓库与展会，不是报价单。

## 公开资料的边界

官网没有公开：在用机器人平台的型号与数量、执行器来源、关节编码器类型与分辨率、采样率与同步方案、自研传感器的原理与指标、经费来源与规模。资源页按 blog / papers / videos 三类归档，具体硬件细节要到单篇论文里找，本页不填。

## 官方资料

- [RAI Institute 机构介绍](https://rai-inst.com/about/)
- [研究方向](https://rai-inst.com/research/)
- [领导团队](https://rai-inst.com/about/leadership-overview/)
- [资源总览（论文、博客、视频）](https://rai-inst.com/resources/)
- [新闻与媒体](https://rai-inst.com/news/)
- [招聘](https://rai-inst.com/careers/)
