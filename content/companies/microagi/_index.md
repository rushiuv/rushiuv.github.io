---
title: "microagi"
wiki: true
wiki_type: "company"
wiki_rank: 224
lastmod: "2026-10-22"
description: "慕尼黑起家的机器人部署与数据公司，2026 年 7 月拿到 5500 万美元种子轮；不造机器人，整机按任务挑最好的厂商买。"
wiki_category: "机器人学习与灵巧操作"
official_url: "https://www.microagi.ai/"
---

microagi 是这条链上少见的**零转轴公司**：它不造机器人，也不训练一颗编码器，做的是把工厂里的手工活录成训练数据、再把别人家的机器人部署回产线。对做编码器的人来说，它的价值不在产品，而在它公开写明的两条边界——不做遥操作、整机从"造得最好的厂商"买——这两句话直接决定了它的采集端和执行端各有多少个角度传感点。

## 慕尼黑、苏黎世、伦敦、伊斯坦布尔四地

官网自述是"data research and deployment lab"，办公室在慕尼黑、苏黎世、伦敦、伊斯坦布尔。2026 年 7 月 16 日的种子轮公告给了更硬的背景：公司由前一级方程式工程师创办，来自红牛车队与梅赛德斯-AMG 马石油车队，成立约十个月后完成 5500 万美元种子轮，由 Hummingbird 领投，Northzone、LocalGlobe、Village Global、redalpine 参投；公告称这是德国历史上最大的种子轮。创始人与 CEO 是 Bercan Kilic。[种子轮公告](https://www.microagi.ai/articles/seed)

产品有两条：Atlas 是部署模型，把机器人放进客户现有产线；shift 是数据采集产品，把"活到底怎么干"录成可训练的数据（独立站点 joinshift.com）。

## 两条产品线各自公开了什么

| 环节 | 公开做法 | 与角度反馈的关系 |
| --- | --- | --- |
| 采集（shift / Atlas 第一层） | 把专用采集硬件搬进车间，录真实任务、边角案例与老师傅手上的经验 | 官网明确写"no teleoperation"，即不靠人远程操作机器人去采 |
| 训练（Atlas 第二层） | 在客户数据上训练基础模型，并按任务、物体、环境微调 | 不锁单一模型或实验室 |
| 部署（Atlas 第三层） | 人形、机械臂、移动平台都行，"从造得最好的那家买" | 整机随厂商进来，执行端的编码器不由 microagi 选 |

第三行是关键：官网原话是 deploy the robot that fits your task, whether a humanoid, an arm or a mobile system, from whichever manufacturer builds it best。这句话把它自己钉在集成与数据层，执行器的选择权留在整机厂手里。[Atlas 产品页](https://www.microagi.ai/atlas)

种子轮公告只给融资与市场数字（欧洲制造业占全球 15%、中国 30%，2024 年中国装机 29.5 万台、欧洲 8.5 万台），没有硬件参数。

## 在编码器链上的位置

它买整机、买采集硬件，卖的是部署服务与数据资产。上游是宇树、优必选这类整机厂与各类采集设备商，下游是欧洲的工业巨头。选型权在链条的上一层：机器人厂定执行器，执行器厂定编码器，microagi 只负责把这些机器跑起来并记录发生的事。

对编码器真正相关的一点是时间戳——采集数据要和产线节拍、视觉帧、机器人状态对齐，才谈得上训练。但它公开的只有"不中断产线、不做遥操作"，没有任何关于同步精度、采样率、时钟源的说明。

## 官方资料

- [microagi 官网](https://www.microagi.ai/)
- [Atlas 部署模型](https://www.microagi.ai/atlas)
- [5000 万美元级种子轮公告（2026-07-16）](https://www.microagi.ai/articles/seed)
- [shift 数据采集产品](https://joinshift.com/)
- [benchmarks 目录](https://www.microagi.ai/benchmarks)
- [newsroom](https://www.microagi.ai/newsroom)
