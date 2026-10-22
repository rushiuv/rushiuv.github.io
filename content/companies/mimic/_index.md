---
title: "mimic"
wiki: true
wiki_type: "company"
wiki_rank: 225
lastmod: "2026-10-22"
description: "苏黎世灵巧操作公司，mimic hand M1 用 15 个主动自由度覆盖 21 个关节，电机侧与关节侧双编码器把单向接触力分辨到 0.1 N。"
wiki_category: "机器人学习与灵巧操作"
official_url: "https://www.mimicrobotics.com/"
---

mimic 是本批次里对编码器最直接的一家：它把"电机侧一颗、关节侧一颗"的双编码器结构写进了官方技术博客，用来解释一只腱驱手怎么把接触力分辨到 0.1 牛。它的位置是**灵巧操作整机与手部模组**，不是芯片；但它对角度反馈的定义方式，比多数整机厂都写得更清楚。

## 苏黎世总部，旧金山设研究单元

官网 about 页写明团队 50 人以上，总部在苏黎世，另在旧金山设研究单元，人员来自 Google DeepMind、Tesla Optimus，以及 ETH Zurich、MIT、斯坦福的研究者。2025 年 11 月的种子轮 1600 万美元，由 Elaia 与 SpeedInvest 领投。技术上它自称发明了 Video-Action Models，用视频生成模型预测并执行机器人动作；2026 年 7 月又与 Black Forest Labs 合作发布 FLUX-mimic。[about 页](https://www.mimicrobotics.com/about)

## M1 手：15 个主动自由度、21 个关节、双编码器

2026 年 7 月 16 日的发布博客是这家公司公开信息最密的一页，把机械与传感都写到了具体数值。

| 公开项 | 官方口径 | 出处 |
| --- | --- | --- |
| 主动自由度 / 关节总数 | 15 个主动自由度，覆盖 21 个关节 | 发布博客 |
| 驱动方式 | 腱驱，电机移到前臂，腱全程走轴承与滑轮 | 发布博客 |
| 反向驱动扭矩 | 低于 0.05 N·m | 发布博客 |
| 力分辨 | 靠电机电流可感知 50 g 的重量 | 发布博客 |
| 角度反馈 | 全关节编码器；电机侧与关节侧的高速双编码器 | 发布博客 |
| 接触力分辨 | 双编码器差值把单向接触力分辨到 0.1 N | 发布博客 |
| 指尖触觉 | 独立指尖触觉传感器，给切向剪力与更高空间分辨率 | 发布博客 |
| 执行器来源 | 明确写用"行业已验证的现成执行器" | 发布博客 |

双编码器在这里不是冗余：电机侧给的是腱轮转过的量，关节侧给的是手指真正转到的角度，两者的差就是腱的伸长与传动柔度。官方把它当成测力的手段——回差与低摩擦的腱路被做成线性传动之后，这个差值才稳定到能换算成牛。[Solving Dexterity 发布博客](https://www.mimicrobotics.com/en/blog/solving-dexterity-a-full-stack-approach)

配套的 U1 外骨骼按 M1 的运动学做，人戴着手套采集的动作可以直接映射到手上。这条设计对角度传感点数的意义是翻倍：一个工位上一只 M1 加一套 U1，两边的关节角都要测。

## 在编码器链上的位置

它买现成执行器、自己做手与整机、卖工作单元与模型。上游是执行器厂和触觉传感器厂，下游是制造、包装分拣、物流的产线。手部这 21 个关节的角度反馈由 mimic 自己定义安装与接口——这是链上少数由整机厂直接决定"哪里放第二颗编码器、怎么把两路拼起来"的位置。

发布博客给的是"全关节编码器 + 双编码器"这种结构描述和力分辨的终点指标，中间的分辨率与带宽都没有。

## 官方资料

- [mimic 官网](https://www.mimicrobotics.com/)
- [技术页](https://www.mimicrobotics.com/technology)
- [关于页（团队与融资）](https://www.mimicrobotics.com/about)
- [Solving Dexterity: A Full-Stack Approach（M1 与 U1 发布）](https://www.mimicrobotics.com/en/blog/solving-dexterity-a-full-stack-approach)
- [Introducing FLUX-mimic](https://www.mimicrobotics.com/en/blog/introducing-flux-mimic)
- [Video-Action Models 技术博客](https://www.mimicrobotics.com/en/blog/video-action-models-are-video-model-backbones-the-future-of-vlas)
