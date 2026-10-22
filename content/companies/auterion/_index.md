---
title: "Auterion"
wiki: true
wiki_type: "company"
wiki_rank: 204
lastmod: "2026-10-22"
description: "做自主系统软件栈的公司，卖 AuterionOS 与三合一 Skynode X（FMUv6x，跑 PX4/MAVLink），接口表只到直连电调与 GPS，平台侧没有任何角度反馈输入通道。"
wiki_category: "自主系统软件与平台"
official_url: "https://auterion.com/"
---

Auterion 站在"自主系统软件与平台"这一层：它卖飞控操作系统、集成计算模块和云端的机队管理，不造机体、不造电机，也不采购编码器。对做角度测量的人，这是一个结构性负样本——无人机与地面车的姿态由 IMU、磁力计与 GNSS 融合给出，**转子位置在电调内部闭环、不回传平台**，所以它的接口表里连一个角度反馈通道都没有。

## 三件套：操作系统、集成模块、云端

Auterion 的产品结构是"一个 OS 加一个硬件模块加一个云"。AuterionOS 跑在载具上、负责连接整支机队，官方定位是厂商无关、基于开放标准、支持现场持续部署；Skynode X 把飞控、任务计算机与 LTE 三合一，用 FMUv6x 这一代飞控硬件，基于 PX4 与 MAVLink，官方标注 NDAA 合规；Auterion Suite 负责飞行日志上云、机队管理与 OTA；Auterion Mission Control 用一个界面管所有机型。[首页](https://auterion.com/)；[Skynode](https://auterion.com/product/skynode/)

2026 年的重心已经明显偏向防务：Nemyx 做集群自主，Nemyx VLS 是把多家厂商的商用无人机、攻击机与拦截机统一发射的模块化发射器，Long Range One Way Attack 官方称打到 1,000 英里。[Nemyx](https://auterion.com/product/nemyx/)；[Long Range](https://auterion.com/product/long-range/)

## Skynode 的接口清单里没有位置反馈

官方对 Skynode X 的接口描述是：可直接接电调（ESC）、GPS、各类传感器、深度相机与 FPV 相机；支持多旋翼、固定翼、VTOL，也支持地面车与无人艇；载荷走 Pixhawk Payload Bus 标准；要算力就外挂 AI Node，里面是 NVIDIA Jetson Xavier NX。[Skynode](https://auterion.com/product/skynode/)

这段话的工程含义很明确：**平台出去的是控制指令与遥测，回来的是姿态与位置估计，中间没有"关节角"这一项**。飞行器的姿态来自 IMU 融合加磁力计与 GNSS 校正；旋翼的转子位置在电调里闭环，最多以转速或电流形式作为遥测出现。这不是缺陷，是这一类架构的分工——编码器如果存在，它在电调与云台里，不在飞控平台上。

## 在编码器链上的位置

它买的是计算模块、飞控板上的 IMU 与磁力计、GNSS 模组，以及整机厂提供的机体与执行机构；它卖的是软件栈、接口标准、认证与合规。**器件选型权落在飞控板设计方与整机厂，Auterion 定的是接口、实时性与认证预算**。

不能推的部分：Skynode 用哪家的 IMU 或磁力计、电调用什么换相反馈、云台用什么角度传感器，官网一律不披露；也不能由"NDAA 合规""FMUv6x"反推任何传感指标。云台与光电吊舱是这条链上真正带角度闭环的部件，但它属于载荷厂，不在 Auterion 的公开资料范围内。

公开页面给的是平台组成、支持的载具类型、合规状态与合作伙伴名单。**没有公开**：控制环频率与端到端延时、IMU 型号与噪声、磁力计型号、电调协议细节、任何角度反馈元件的规格、单机价格与交付。

## 官方资料

- [Auterion 首页](https://auterion.com/)
- [公司页](https://auterion.com/company/)
- [Skynode X 产品页](https://auterion.com/product/skynode/)
- [AuterionOS](https://auterion.com/product/auterionos/)
- [Auterion Suite](https://auterion.com/product/auterion-suite/)
- [Nemyx 集群自主](https://auterion.com/product/nemyx/)
- [Long Range One Way Attack](https://auterion.com/product/long-range/)
- [合作伙伴页](https://auterion.com/partners/)
