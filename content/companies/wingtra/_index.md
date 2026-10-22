---
title: "Wingtra"
wiki: true
wiki_type: "company"
wiki_rank: 223
lastmod: "2026-10-22"
description: "苏黎世 Wingtra AG 的尾座式测绘无人机，WingtraRAY 靠两副桨垂直起降、巡航 22 m/s，单架次覆盖 550 公顷、PPK 绝对精度 3 cm。"
wiki_category: "无人机与空中作业"
official_url: "https://wingtra.com/"
---

Wingtra 做的是**测绘整机**，构型是尾座式垂直起降固定翼：竖直立在尾撑上，靠两副桨直接起飞，转平后当固定翼巡航。这种构型的可动件极少——垂直起降与过渡全靠两副桨的推力向量，巡航靠舵面，没有云台倾转机构。对做角度传感的人来说，它是一台"轴上几乎没有位置反馈"的整机，值多少颗取决于舵面数量，而官方不公布这个数。

## 苏黎世 Giesshübelstrasse，美国另设点

官网页脚给的法律实体与地址是 Wingtra AG, Giesshübelstrasse 40, 8045 Zurich, Switzerland，另在美國劳德代尔堡设办公室。产品线两代：现役主力 WingtraRAY，上一代 WingtraOne GEN II。业务不止卖飞机——它还卖差分改正（WingtraGROUND、Trimble 方案）、载荷（RGB、LiDAR、多光谱）、以及 WingtraCARE 服务包与培训。[Wingtra 官网](https://wingtra.com/)

## WingtraRAY 的公开规格

官方产品页把关键数放在首屏，这套数字在同级别里属于"一次飞一大片"的定位。

| 公开项 | 官方口径 | 备注 |
| --- | --- | --- |
| 构型 | 尾座式 VTOL，靠两副桨垂直起降 | VTOL 说明页 |
| 巡航速度 | 最高 22 m/s | 产品页 |
| 单架次覆盖 | 550 公顷（1360 英亩） | 产品页 |
| 绝对精度 | PPK 下 3 cm（RMS x, y, z） | 产品页 |
| 续航 | 最长 59 分钟 | 产品页 |
| 通信/改正 | 支持 PPK、网络 RTK 改正；与 Trimble 方案并存 | 产品目录 |
| 安全 | 降落伞自动或手动触发；NDAA、Blue UAS、Green UAS 认证 | 产品页 |
| 合规 | 欧盟 Open 类；STS-02 标准场景下可做 BVLOS | 产品页 |
| 载荷 | RGB、LiDAR、多光谱（含 MicaSense RedEdge-P） | 载荷目录 |

两副桨这个数字很重要：它是全机唯一的推力源，垂直起降、悬停、过渡、巡航全程都用这两副。也就是说，桨的转速环与两路电调是整机的核心执行链，而这类电调按行业惯例用无感 FOC，不引入转子位置传感器。[WingtraRAY 产品页](https://wingtra.com/wingtraray/) [VTOL 工作原理](https://wingtra.com/vtol-drone/)

## 在编码器链上的位置

它买电机、电调、舵机、IMU、GNSS 板卡与相机，自己做整机、飞控与航线软件，卖给测绘、矿业、建筑、环保与农业用户。上游是航模级电机电调与惯导供应商，下游是测绘服务商。

链上真正带"角度"的只有两处：舵面舵机与（如果有）云台。舵机里的位置反馈是舵机厂的内置件，整机厂通常只选舵机型号，不选里面的芯片。所以这台机器对独立编码器件的需求接近于零；它的精度预算几乎全部花在 GNSS/PPK 与惯导上——3 cm 是 PPK 后处理的绝对精度，不是机体姿态精度。

## 公开资料的边界

官网没有公开：舵面数量与舵机型号、机体材料与翼展、空机重量与最大起飞重量、飞控主控与 IMU 型号、姿态估计输出频率、电机与电调型号、链路协议。产品页只给上表这些结果级数字，Technical Specification 的详细表要询价或进支持知识库。本页不推测舵面数，也不把"四可动件"当成公开事实。

## 官方资料

- [Wingtra 官网](https://wingtra.com/)
- [WingtraRAY 产品页](https://wingtra.com/wingtraray/)
- [VTOL 工作原理（尾座式与两副桨）](https://wingtra.com/vtol-drone/)
- [WingtraOne GEN II 产品页](https://wingtra.com/wingtraone-gen-ii-drone/)
- [LiDAR 测绘方案](https://wingtra.com/lidar-drone/)
- [Wingtra 软件](https://wingtra.com/software/)
