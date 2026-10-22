---
title: "Hexagon Robotics"
wiki: true
wiki_type: "company"
wiki_rank: 214
lastmod: "2026-10-22"
description: "海克斯康（Hexagon）旗下机器人都门，AEON 人形整机公开 34 个自由度、165 cm / 60 kg、轮式底盘，执行器由舍弗勒供给。"
wiki_category: "人形机器人与关节"
official_url: "https://robotics.hexagon.com/"
---

Hexagon Robotics 站在**整机应用**这一层：它不做编码器，也不做关节里的敏感元件，而是把执行器、传感器和自有测量技术装进一台叫 AEON 的人形机器人里，卖给工厂和物流现场。对做编码器的人，它值得读的地方有两个：一是 34 个自由度这个数直接等于单机的关节轴数量级；二是它把执行器公开交给舍弗勒供给，等于把关节内的角度反馈选择权也一并交了出去。

## 从测量集团里长出来的机器人都门

AEON 于 2025 年 6 月 17 日在 Hexagon 的 Hexagon LIVE Global 活动上发布，归在此前已宣布的 Robotics 事业部之下，公告发自斯德哥尔摩。集团自述的底子是测量技术、定位方案与现实捕获，机器人业务把这套东西当成"空间智能"来卖。首发阶段公开的两家试点客户是舍弗勒（Schaeffler）与皮拉图斯（Pilatus），应用写明是操作、机床上下料、零件检测与现实捕获。[发布公告](https://robotics.hexagon.com/hexagon-launches-aeon-a-humanoid-built-for-industry/)

## AEON 的公开规格：34 个自由度、轮式移动

官方产品页给了一张 spec sheet，全部数字只有七项，没有一项涉及关节内部结构。

| 公开项 | 官方数值 | 备注 |
| --- | --- | --- |
| 全身自由度 | 34 | 产品页 spec sheet |
| 身高 / 重量 | 165 cm / 60 kg | 产品页 |
| 最高速度 | 2.4 m/s | 产品页 |
| 负载 | 短期 15 kg，持续搬运 8 kg | 产品页 |
| 续航 | 单次充电 5 h，自主换电 1 min | 产品页 |
| 移动方式 | 轮式底盘 | 2026-04-22 公告写 wheel-based locomotion |
| 执行器来源 | 舍弗勒提供高精度执行器 | 2026-04-22 公告 |
| 部署规模 | 舍弗勒计划 2032 年前部署不少于 1000 台 | 2026-04-22 公告 |

2026 年 4 月 22 日的舍弗勒公告是这批资料里信息量最大的一份：它在试点复盘里写明 AEON 用"自有传感器组加轮式移动"完成多机床工位的上下料与检测，并把舍弗勒的高精度执行器写进供应关系，同时给出七年 1000 台的部署计划。[舍弗勒部署公告](https://robotics.hexagon.com/hexagon-robotics-and-schaeffler-deploy-a-fleet-of-aeon-humanoids/)

spec sheet 只有上表七项，产品页结尾指向 Contact us。舍弗勒公告也只写到"高精度执行器"，没有给扭矩、转速或反馈接口。

## 34 个自由度，但关节里的反馈跟着执行器走

34 个自由度意味着单机 34 个受控轴，其中相当一部分落在轮式底盘与双臂上。这里有一个公开的分界线：**执行器由舍弗勒供给**，那么关节模组内部的角度敏感元件，最可能是随模组一起进来的，而不是 Hexagon 自己选一颗芯片装上——但这只是从供应关系推的合理路径，官网没有一句话说关节里用的是哪种编码器。

反过来，能确认留在 Hexagon 手里的是融合层：公告反复强调 sensor fusion 与 spatial intelligence，产品页也把"多模态传感器组"写成卖点。轮式底盘的速度反馈、IMU、视觉与激光的位姿融合，这套东西是它自己的。

## 在编码器链上的位置

它买执行器、买传感器件，卖整机与产线数据。上游是执行器与模组供应商（舍弗勒已在公告里点名），下游是汽车、航空、制造、仓储的产线。决策权被切成两半：关节内的单圈角度反馈大概率跟着执行器供应商的既有方案；底盘轮速与整机位姿融合则由 Hexagon 定义。判断一个编码器方案能不能进这台机器，先要问清是打进舍弗勒的执行器，还是打进 Hexagon 的底盘与传感板，这两条路的门槛完全不同。

## 官方资料

- [Hexagon Robotics 官网](https://robotics.hexagon.com/)
- [AEON 产品页与 spec sheet](https://robotics.hexagon.com/product/)
- [机器人都门介绍与团队](https://robotics.hexagon.com/about/)
- [AEON 发布公告（2025-06-17）](https://robotics.hexagon.com/hexagon-launches-aeon-a-humanoid-built-for-industry/)
- [与舍弗勒的千台部署公告（2026-04-22）](https://robotics.hexagon.com/hexagon-robotics-and-schaeffler-deploy-a-fleet-of-aeon-humanoids/)
- [新闻与故事列表](https://robotics.hexagon.com/news/)
