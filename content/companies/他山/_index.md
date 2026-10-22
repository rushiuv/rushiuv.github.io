---
title: "他山"
wiki: true
wiki_type: "company"
wiki_rank: 150
seed_count: 1
lastmod: "2026-10-22"
description: "他山科技做电容式触觉感知芯片，Ruby 为 SNN 架构的模数混合触觉芯片，TS-F-A 触觉单元法向力分辨 0.01 N、切向 0.25 N。"
wiki_category: "触觉与接触状态"
official_url: "https://www.tashantec.com/"
related_models: []
---

他山科技（Tashan Technology）是**触觉感知芯片**这一层：它测的是接触力与接近，不是角度。放在编码器话题里，它的意义是边界参照——同一批做机器人感知的芯片公司里，触觉走的是电容/电场路线，输出的是三维力与距离，与磁、光的角度测量没有共用信号链，也没有共用客户决策口。

## 三颗芯片分成三个市场

官网技术页把产品按市场切成三颗，每颗都给了明确的应用面。

| 芯片 | 官方定位 | 公开特性 | 目标场景 |
| --- | --- | --- | --- |
| Ruby | 自述为全球首颗模数混合 AI 触觉处理芯片，也是首颗基于脉冲神经网络（SNN）产业化的类脑芯片 | 分布式协同架构，支持高精度感知、超低延迟、低功耗、多传感协同 | 灵巧手、机器人皮肤、工业控制、AI 研究 |
| Red Crystal | 车规触觉芯片 | AEC-Q100 认证，支持 CAN 2.0B 与 CAN FD；自有模拟路由分布式架构，可多芯片协同 | 座椅、中控、门板等 HMI；SBR 占座检测；HOD 方向盘离手检测；雨量与光照 |
| Rainstone | 消费级 AI 触觉芯片 | 高精度混合信号 MCU 路线 | 液位检测、触摸/非接触交互、编码识别 |

"全球首颗"这类表述是官方自我定位，本页照抄并标注来源，不当成第三方结论。[技术页](https://www.tashantec.com/technology)

## 机器人侧的公开参数

产品页给的触觉单元 TS-F-A 是全站少见的硬指标：独立感知单元、三维力触觉、IIC 通信；法向力量测分辨率 0.01 N，切向力 0.25 N，非接触（接近感知）距离不小于 1 cm。围绕这颗单元还有四类系统件：TS-ES 电子皮肤（面向多自由度机械臂的 360° 碰撞避免，接触与非接触两种方式）、TS-V 视触觉融合训练平台、TS-VT 视触觉数据采集平台、触觉仿真平台（在 MuJoCo 与 NVIDIA Isaac Sim 上开源）。另有一台 TS-R 服务机器人，官网写是与云迹的移动平台结合做抓取力度自适应与递送演示。[产品页](https://www.tashantec.com/robot)

首页给的四组能力口径是：高精度测量、30 种以上材质识别、1000 N 安全过载、R-SpiNNaker 类脑芯片架构。官网另称全球已有 200 家以上合作方。

## 在编码器链上的位置

它自己设计芯片、外协流片，卖芯片与模组给灵巧手厂、机器人厂、汽车 Tier 1 与家电厂。位置在"感知芯片"这一层，与磁角度芯片厂商是邻居但不是对手：电容触觉解决"碰到了没有、用了多大力、什么材质"，角度编码器解决"转到哪、转多快"。

对做机器人关节的人来说，两者会在同一个指尖或同一个腕部相遇，但接口与验收完全不同：触觉是低频、事件驱动、带材质语义；角度是高频、连续、要求温度与长期稳定性。

## 官方资料

- [他山科技官网](https://www.tashantec.com/)
- [技术页（Ruby、Red Crystal、Rainstone 三颗芯片）](https://www.tashantec.com/technology)
- [产品页（TS-F-A 触觉单元与系统件）](https://www.tashantec.com/robot)
- [触觉仿真平台 MuJoCo 开源仓库](https://github.com/TashanTec/TactiSim)
- [触觉仿真平台 Isaac Sim 开源仓库](https://github.com/TashanTec/Tashan-Isaac-Sim)
