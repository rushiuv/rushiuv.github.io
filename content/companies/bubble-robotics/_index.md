---
title: "Bubble Robotics"
wiki: true
wiki_type: "company"
wiki_rank: 206
lastmod: "2026-10-22"
description: "把水面驻留母船 BubbleDock 与现成 ROV/AUV 平台组合成常驻式海上监测系统：续航 6 个月以上、巡航 6 节、下潜 300 米，官方写毫米级数据精度。"
wiki_category: "水下与海事机器人"
official_url: "https://www.bubble-robotics.com/"
---

Bubble Robotics 站在"水下与海事机器人"这一层，但它卖的不是机器，是常驻海上的监测服务：一座能自己发电、自己抛锚定位、自己布放回收水下机器人的水面母船（BubbleDock），加若干台集成现成 ROV/AUV 平台的水下作业机（BubbleBot）。对做角度测量的人，这是链条里最"少转轴"的一类客户——水下推进器按行业惯例不给位置反馈，全机真正有明确角位移过程的是布放回收那一段，而这一段官方只写"自主"，不写机构。

## 公司与品牌

官网结构是四页：首页、技术、关于、案例。产品命名统一用 Bubble 前缀：BubbleDock 是驻留母船，官方叫"resident mothership"；BubbleBot 是水下作业机，明确写"集成成熟的 ROV 与 AUV 平台"，也支持两种形态分别使用。业务定位三句话：无船、无船员、无人下潜。[首页](https://www.bubble-robotics.com/)

## 公开规格：续航、航速、深度、精度

| 对象 | 公开指标 | 其他公开参数 |
| --- | --- | --- |
| [BubbleDock](https://www.bubble-robotics.com/technology) | 续航 6 个月以上，单次充电航程约 60 km，六个月潜在里程 1,800 km 以上 | 混合可再生发电实现能源自给；自主抛锚与定点保持；自扶正结构，生存海况到 7 级；巡航 6 节 |
| [BubbleDock](https://www.bubble-robotics.com/technology) | 操作能力 | 自主布放、回收、再充电与数据卸载 BubbleBots；同时支持 ROV 与 AUV |
| [BubbleBot](https://www.bubble-robotics.com/technology) | 集成现成 ROV/AUV 平台 | 自主布放回收；多月至数月的无人水下作业；自研边缘自主与岸基遥控 |
| [BubbleBot](https://www.bubble-robotics.com/technology) | 耐流 2 节，下潜 300 m | 模块化传感：视觉、声学、无损检测、环境传感 |
| 数据 | 官方称毫米级影像与多模态数据精度 | 支持相机、声呐、多波束、侧扫、水听器、eDNA 等载荷 |

以上全部取自技术页与首页。注意"毫米级"是官方对**数据精度**的表述，指影像与量测结果，不是平台定位或姿态精度。[技术页](https://www.bubble-robotics.com/technology)

公开页面给的是续航、航速、航程、海况等级、耐流、下潜深度、载荷类型与数据精度口径。**没有公开**：整机尺寸与重量、推进与布放机构的构型与轴数、电机与反馈型式、姿态与定位精度（只有"毫米级数据"这一句）、母船定点保持的控制方式、单套系统的价格与租期。

## 在编码器链上的位置

这台系统的采购结构很清楚：**水下机器人本身是外购平台**（官方原文"集成成熟的 ROV 与 AUV 平台"），所以推进器、舵机、机械臂上的任何角度反馈随平台一起买进来，选型权在平台厂，不在 Bubble。它自己做的是母船、能量系统、自主软件与数据链路。

整机里唯一由它自己定义、且带明确角位移过程的动作是"自主布放、回收与再充电"——把水下机器人从母船放下与收回。这一段必然有绞车、滑轨或机械臂一类的机构，但**官方没有说明用哪种机构、几根轴、如何测位**，所以不能推断这里有编码器，更不能推断型号。水下推进器按行业惯例用无位置反馈的直流无刷方案，这条也只是行业惯例，不是本公司的公开声明。

## 官方资料

- [Bubble Robotics 首页](https://www.bubble-robotics.com/)
- [技术页（BubbleDock 与 BubbleBot 规格）](https://www.bubble-robotics.com/technology)
- [关于页](https://www.bubble-robotics.com/about)
