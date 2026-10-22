---
title: "Disney Research"
wiki: true
wiki_type: "company"
wiki_rank: 207
lastmod: "2026-10-22"
description: "迪士尼的洛杉矶研究机构，机器人研究方向公开的是机构设计与控制方法：Olaf 把两条不对称腿藏在泡沫裙下、臂嘴眼用球面与平面连杆，执行器与反馈全部外购。"
wiki_category: "科研机构"
official_url: "https://la.disneyresearch.com/research/"
---

Disney Research 站在"科研机构"这一层，而且是一个特殊位置：它不卖机器人、不卖器件，发表的是机构设计与控制方法；机器人上的执行器与关节模组是外购成品，反馈元件随模组进来，论文里一个字都不提。对做编码器的人，它的价值在于看清这类研究的验收标准——**角度"够用"的定义是策略能跑起来、噪声能压下去、执行器不烧，而不是绝对精度**。

## 组织与研究方法：学术与产业各占一半

Disney Research 洛杉矶站点自述"结合学术界与产业界"，做基础研究也做应用驱动研究，成果公开发表并参与全球研究社区；研究领域分三块：机器人、人工智能与机器学习、沉浸式技术。地点策略是刻意与高校同城，官网点名与加州理工（Caltech）合作，另有学术顾问与实习项目。[研究页](https://la.disneyresearch.com/research/)

成果发表在同行评审期刊与 RSS、SIGGRAPH 这类会议。机器人方向最近的一批论文集中在角色机器人与物理动画：Olaf 把动画角色做成实体、CoCo-InEKF 做动态接触丰富的状态估计、ReActor 做物理感知的动作重定向、Walk Like This 做风格化行走。[论文目录](https://la.disneyresearch.com/publication/)

## Olaf 这篇把"机构塞进角色"的代价写透了

2026 年 5 月发表在 IEEE Robotics and Automation Letters 的 Olaf 论文，是这批工作里对机构约束讲得最具体的：

| 部位 | 公开做法 |
| --- | --- |
| 腿 | 两条不对称的腿藏在软泡沫裙下，制造"脚沿身体移动"的错觉 |
| 臂、嘴、眼 | 用球形连杆与平面连杆，把执行器塞进角色体腔内 |
| 头与颈 | 大头部由细颈里的小执行器驱动，过热风险被服装放大，因此把温度值作为策略的额外输入 |
| 控制 | 强化学习，以动画参考引导；额外奖励用来压低落脚冲击噪声 |

这四条说明的事很朴素：角色机器人的难点不是测量精度，而是**在体积、重量与散热的三重挤压下把机构做出来**。细颈里塞小执行器、再加服装保温，热就成了硬约束，官方做法是让控制策略读温度并在边界内运行。[Olaf 论文页](https://la.disneyresearch.com/publication/olaf-bringing-an-animated-character-to-life-in-the-physical-world/)

## 在编码器链上的位置

它是机构设计方与控制算法方，执行器是成品件——论文原文说"把执行器塞进角色体内"，说明采购的是现成执行器或关节模组，角度反馈随之进来。**所以它不选编码器，编码器的选型权在模组厂手里。**

不能推的部分：论文不写用哪家的执行器与关节模组、不写反馈是光电还是磁、不写多少位、不写装在电机侧还是关节侧。这类研究真正关心的指标是落脚冲击噪声、执行器温度与行走成功率，公开材料里没有关节角分辨率这一项。

公开页面给的是研究领域、论文标题、作者、摘要与发表刊物。**没有公开**：机器人整机的自由度与关节数、执行器型号与扭矩、反馈元件规格、控制频率、整机成本。要拿到细节只能读论文与补充材料，公司层面的 BOM 与采购信息不对外。

## 官方资料

- [Disney Research 研究页](https://la.disneyresearch.com/research/)
- [论文目录](https://la.disneyresearch.com/publication/)
- [Olaf：把动画角色做成实体](https://la.disneyresearch.com/publication/olaf-bringing-an-animated-character-to-life-in-the-physical-world/)
- [CoCo-InEKF：接触协方差学习的状态估计](https://la.disneyresearch.com/publication/coco-inekf-state-estimation-with-learned-contact-covariances-in-dynamic-contact-rich-scenarios/)
- [ReActor：物理感知动作重定向](https://la.disneyresearch.com/publication/reactor-reinforcement-learning-for-physics-aware-motion-retargeting/)
- [Walk Like This：风格化行走](https://la.disneyresearch.com/publication/walk-like-this-stylized-locomotion-for-physics-based-characters-through-example-driven-diffusion/)
