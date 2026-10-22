---
title: "Flexion Robotics"
wiki: true
wiki_type: "company"
wiki_rank: 211
lastmod: "2026-10-22"
description: "做人形机器人自主软件栈的苏黎世团队：从指令到控制、从操作到行走，靠仿真与强化学习做跨硬件泛化，创始团队来自 ETH 与 NVIDIA 的 Isaac Gym/Isaac Lab。"
wiki_category: "机器人学习与灵巧操作"
official_url: "https://flexion.ai/"
---

Flexion 站在"机器人学习与灵巧操作"这一层，卖的是人形机器人的自主软件栈，不卖机器人也不卖关节。对做角度测量的人，它属于"不采购器件、但直接消耗器件输出"的一类：它读的是整机 API 给的关节状态，**角度质量在它这里只体现为状态估计与控制能不能收敛**，因此它提出的要求是频率、噪声与时间戳一致性，而不是分辨率位数。

## 团队：ETH 与 NVIDIA 的组合

公开的创始团队写得很具体：CEO Nikita Rudin，ETH 苏黎世博士，方向是机器人深度强化学习，曾在 NVIDIA 做研究科学家；CTO David Höller，强化学习博士，十余年机器人学习与仿真经验，在 NVIDIA 期间参与搭建 Isaac Gym 与 Isaac Lab；感知负责人 Julian Nubert，ETH 博士，曾在 Meta Reality Labs、NASA JPL、AWS 与马普所短期研究；硬件负责人 Fabian Tischhauser，长期做机器人硬件平台；联合创始人里还有 ETH 机器人系统教授、RAI Institute 苏黎世分部主任 Marco Hutter，以顾问身份参与。[团队页](https://flexion.ai/about)

这支队伍的构成解释了公司路线：仿真与强化学习的工程经验压过机构经验，所以产品从软件切入。

## 公开的东西：产品定位与三篇研究

官方产品描述是"从指令到控制、从操作到行走，跨任意硬件与任务的人形自主栈"，靠仿真与强化学习把能力迁移到真实世界，尽量减少人工介入。[首页](https://flexion.ai/)

公开的研究节奏有三个节点：2025 年 11 月 Flexion Reflect v0（走向可泛化的机器人自主）、2026 年 6 月 Reflect v1.0（走向长时序自主作业）、2026 年 7 月与 Niantic Spatial、NVIDIA 合作做人形机器人的 Sim2Real 收口。[新闻页](https://flexion.ai/news)

## 在编码器链上的位置

它不买编码器：软件跑在别人的整机上，关节状态通过整机接口拿到。**能推的是它对上游的隐含要求**——跨硬件泛化意味着它必须容忍不同整机的关节反馈频率与噪声差异，所以它的策略设计天然偏向"用鲁棒性吃掉器件差异"；这一点与整机厂追求单机指标最优是两种不同的工程哲学。

不能推的部分：它自己不做机构、不做关节，官网也没有任何器件级参数；不能因为它有硬件负责人就推断它会自研关节，也不能推断它用哪家整机。

## 公开资料的边界

公开页面给的是团队背景、产品定位、研究节点与合作方。**没有公开**：它支持哪些整机型号、关节状态的读取频率与接口、策略推理的算力平台与时延、控制频率、任何精度指标、商业模式与价格。要判断它的真实能力只能读研究文章与演示，本页不填没有来源的数字。

## 官方资料

- [Flexion Robotics 首页](https://flexion.ai/)
- [团队页（创始团队背景）](https://flexion.ai/about)
- [新闻与研究页](https://flexion.ai/news)
- [招聘页](https://flexion.ai/careers)
