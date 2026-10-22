---
title: "萝博派对"
wiki: true
wiki_type: "company"
wiki_rank: 236
lastmod: "2026-10-22"
description: "上海萝博派对（RoboParty）2025 年 2 月成立，四个月做出 ROBOTO_ORIGIN 人形原型并开源结构、电气、训练与部署全流程，RP Hand 灵巧手提供 Linux CAN-FD 加 ROS 2 接口。"
wiki_category: "人形机器人与关节"
official_url: "https://roboparty.com/"
---

萝博派对是开源人形这一档里少见的"全流程开源"：结构、电气、训练、部署都放到 GitHub 上，连灵巧手的驱动接口也公开成 SDK。对做位置反馈的人，这种公司的价值不在整机指标，而在接口——CAN-FD、ROS 2、关节描述文件都摆在明面上，谁都能看到它的关节里挂了几个自由度、用什么协议读位置，这在闭源整机厂那里看不到。

## 2025 年 2 月成立，四个月做完原型

上海萝博派对科技有限公司，英文名 RoboParty。官方 GitHub 组织首页的自述：2025 年 2 月 21 日成立，同年 4 月开始正式做人形机器人，四个月完成原型 ROBOTO_ORIGIN，并且把全研发流程、全部结构、电气、训练与部署都开源了。官网页脚备案为 沪ICP备 2025121706 号-1，公网安备 31011502403804 号；站点首页挂着 AGIBOT World Challenge 2026 的 Reasoning to Action 第三名。

## 三个开源项目与公开接口

| 项目 | 类型 | 公开指标 | 其他公开信息 |
| --- | --- | --- | --- |
| [RP1（roboto_01）](https://github.com/Roboparty) | 全开源人形平台 | 尚未公开自由度与关节参数 | 结构、电气、训练、部署全流程开源 |
| [Party_OS](https://github.com/Roboparty) | 人形系统与开放研发底座 | 仓库 181 星、16 分支 | GPL-3.0；含运动控制、感知交互、全身协调、操作与智能体 |
| [RP Hand（roboparty_dexhand）](https://github.com/Roboparty) | 灵巧手 SDK | 未公开关节数与分辨率 | Linux CAN-FD 接口，提供 C++ 与 Python 绑定及 ROS 2 封装 |
| [RPO 框架](https://github.com/Roboparty) | 全栈开源框架 | 未公开版本号 | 含硬件驱动、运动控制、算法模块与应用开发 |

## 在编码器链上的位置

公开的接口是 CAN-FD，这意味着关节控制器与手部模块之间走的是总线式数字链路，位置值以报文形式传输，编码器本身很可能在关节控制板本地完成解算——但官方没有写明是磁、光还是电感，也没给位数。能推的是：开源做法让第三方能直接读到关节描述文件与驱动代码，从而知道它期望的反馈格式（报文、单位、更新率）；不能推的是硬件选型。对做芯片的人，这类客户的门槛不在精度指标，而在"你的方案能不能被社区复现"。

## 公开资料的边界

没有产品规格书、没有关节参数表、没有售价。开源仓库给的是代码与描述文件，不给器件的品牌与型号；官网是脚本渲染，抓不到正文。因此本页只写已核实的成立时间、开源范围、仓库规模与接口类型，不写自由度、扭矩、精度。

## 官方资料

- [RoboParty 官网](https://roboparty.com/)
- [RoboParty 官方 GitHub 组织（71 个公开仓库，首页自述成立时间与 ROBOTO_ORIGIN 开源范围）](https://github.com/Roboparty)
