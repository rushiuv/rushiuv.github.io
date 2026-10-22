---
title: "Duatic"
wiki: true
wiki_type: "company"
wiki_rank: 208
lastmod: "2026-10-22"
description: "苏黎世 Duatic AG 做准直驱关节模组与整臂：DynaArm 9.2 kg、连续负载 6 kg、臂展 0.99 m、关节力矩精度 ±0.5 Nm，官方称其 DynaDrive Baboon 已替换 ANYmal 髋膝上的 ANYdrive。"
wiki_category: "人形机器人与关节"
official_url: "https://www.duatic.com/"
---

Duatic 站在"关节模组加整臂"这一层，是这条链上离编码器选型权最近的一类公司：它自己设计准直驱关节（DynaDrive 系列），再组装成臂（DynaArm）、上身（DuaTorso）、底盘（DuaRover）和双手机器人（DXTR）。关节里的角度反馈由它定，整机厂买了模组就等于交出了选型权。它官网还公开写了一句极有价值的话：DynaDrive Baboon 已替换 ANYmal 髋与膝上的 ANYdrive——**模组换掉，模组里的编码器跟着换**。

## 公司与品牌

法律主体 Duatic AG，地址 Affolternstrasse 42, 8050 Zürich，官网自述技术"developed from ETH Zurich research"。[关于我们](https://www.duatic.com/about-us)

产品分两层。模组层是 DynaDrive 系列，官方在首页点名三个型号：Baboon 用于腿式机器人的髋与膝，Armadillo 用于 ANYexo V2 康复外骨骼的腕部驱动，Coyote 用于轮式驱动。整机层四个：DynaArm 单臂、DuaTorso 双臂上身、DuaRover 自主底盘、DXTR 双臂移动操作机。[首页](https://www.duatic.com/)

## 公开规格：DynaArm 与 DXTR

| 对象 | 公开指标 | 其他公开参数 |
| --- | --- | --- |
| [DynaArm](https://www.duatic.com/dynaarm) | 连续负载 6 kg，10 秒峰值 15 kg，自重 9.2 kg，臂展 0.990 m | 末端速度 10 m/s；48 V DC；IP66；关节力矩精度 ±0.5 Nm |
| [DynaArm](https://www.duatic.com/dynaarm) | 控制与集成 | ROS 2 原生、开放 API、全状态回读、重力补偿、无外部控制箱、瑞士制造 |
| [DXTR](https://www.duatic.com/dxtr) | 双臂合计举 30 kg，底盘顶部承载 200 kg | 在既有地面布局上作业，不改货架、不加安全围栏、不设固定拣选站 |
| [DuaTorso](https://www.duatic.com/duatorso) | 双臂上身，自带视觉 | 可装到自有平台上 |
| [DuaRover](https://www.duatic.com/duarover) | 自主移动底盘 | 面向既有仓库布局导航 |

值得单独拎出来的一条是"关节力矩精度 ±0.5 Nm"。它没有说力矩怎么得到：准直驱臂常见的做法是用电流与减速比估算，而不是在关节里再放一颗力矩传感器。这条属于工程惯例，官方页面没有明说。

## 在编码器链上的位置

准直驱（quasi-direct drive）意味着低减速比、高带宽、可反驱，代价是**同样的角度误差在关节输出端放大的倍数小、但力矩环对角度噪声更敏感**。这类结构通常要在关节里同时读电机侧与输出侧，才能把减速机的回差与柔性从控制里扣掉——具体它读几路、读什么，官网不写。

真正可用的公开线索是那句"Baboon 替换了 ANYmal 髋膝上的 ANYdrive"。它证明的是商业模式：**整机厂换代时换的是整个模组，编码器随模组走**。所以对器件厂，Duatic 这种客户的价值是"一次进模组、跟着模组进多个整机"；反过来，被替换掉的那颗编码器不会单独被保住。

不能推的部分：DynaArm 与 DynaDrive 各用几路反馈、光电还是磁、多少位、精度指标；官方只给 ±0.5 Nm 这一条力矩精度，没有角度精度。

## 官方资料

- [Duatic 首页](https://www.duatic.com/)
- [关于我们（ETH 研究来源、苏黎世地址）](https://www.duatic.com/about-us)
- [DynaArm 产品页](https://www.duatic.com/dynaarm)
- [DXTR 双臂移动操作机](https://www.duatic.com/dxtr)
- [DuaTorso 双臂上身](https://www.duatic.com/duatorso)
- [DuaRover 移动底盘](https://www.duatic.com/duarover)
