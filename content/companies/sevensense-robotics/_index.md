---
title: "Sevensense Robotics"
wiki: true
wiki_type: "company"
wiki_rank: 219
lastmod: "2026-10-22"
description: "2018 年成立的苏黎世视觉 SLAM 公司，2024 年 1 月并入 ABB；Alphasense Position 支持 8 路相机、定位精度标称到 1 cm，整机零转轴。"
wiki_category: "导航与空间感知"
official_url: "https://www.sevensense.ai/company"
related_companies: ["ABB Robotics", "ABB"]
---

Sevensense 是一家**一根转轴都没有的定位公司**：它卖的是视觉 SLAM 盒子，装在别人的 AGV、AMR 和叉车上，输出位姿。正因为它自己不做运动，它对编码器的态度是"拿来用"——车辆的轮式里程计、底盘控制器的状态量，都是它融合的输入。这条路线上，轮速反馈的精度与时间戳质量会直接落进位姿输出，而它不是这些反馈的生产者。

## 2018 年苏黎世成立，2024 年 1 月并入 ABB

官网公司页写明：总部苏黎世，2018 年成立，2024 年 1 月被 ABB 收购，现在作为 ABB 内部的专门业务单元继续做机器人自主技术。产品线三条：Alphasense Autonomy（整机自主）、Alphasense Position（定位）、Alphasense Trackr（给人工驾驶的叉车与牵引车做实时定位的 RTLS）。[Sevensense 公司页](https://www.sevensense.ai/company)

应用面覆盖物料搬运、地面清洁、配送与巡检。这条覆盖面本身就是它的价值：同一套视觉 SLAM 卖给不同车辆厂，等于把"定位"从每家的自研项变成可采购件。

## Alphasense Position 的公开规格

官方产品页给的参数不多，但都是硬指标。

| 公开项 | 官方口径 | 备注 |
| --- | --- | --- |
| 方案形态 | 多相机、工业级、Visual-SLAM-in-a-box | 边缘 AI 盒子 |
| 定位精度 | 官方写 accurate down to 1 cm | 未给 RMS 定义与置信区间 |
| 相机路数 | 最多 8 路视频流实时处理 | 官方写 up to 8 camera streams |
| 两种配置 | 紧凑型 5 台已标定相机；扩展型相机可独立布置 | 外壳可选 |
| 部署条件 | 不需要反光板、信标或标记 | 与传统激光反光板方案对立 |
| 地图 | 车队内自动共享地图 | 支持多楼层、坡道、不平地面 |
| 输出 | 完整 3D 建图与位姿 | 可输出用于巡检的视觉数据 |

表格里"1 cm"是官方宣传口径，没写清是重复精度还是绝对精度、也没给置信区间——这种数字拿来做横向对比前必须先问定义。第二种配置（相机可独立布置）说明它的标定流程是产品的一部分：多相机外参标不好，1 cm 就无从谈起。[Alphasense Position](https://www.sevensense.ai/product/alphasense-position)

官网没有公开：融合算法里轮速与视觉的权重、支持的车速上限、输出频率与延时、时间同步方式、IMU 型号与指标、盒子算力平台、单套价格。

## 在编码器链上的位置

它买相机、算力模块与 IMU，做 SLAM 盒子，卖给车辆厂与系统集成商。它不买关节编码器，因为它没有关节；它依赖的是**轮式里程计**这一路外部输入。融合结构里，视觉给绝对位姿但有延迟与失效区间，轮速给高频短时增量，两者互补，所以轮速的刻度误差、量化步长和时间戳抖动，最后都会体现在位姿的短时误差上。

这条关系决定了一件事：想进这台车，不是找 Sevensense 谈一颗编码器，而是找车辆厂谈底盘测速方案；Sevensense 只定义输入接口与容差。

## 官方资料

- [Sevensense 公司页（历史与归属）](https://www.sevensense.ai/company)
- [Alphasense Position 产品页](https://www.sevensense.ai/product/alphasense-position)
- [Alphasense Autonomy 产品页](https://www.sevensense.ai/product/alphasense-autonomy)
- [Alphasense Trackr 产品页](https://www.sevensense.ai/product/alphasense-tracker)
- [ABB 收购 Sevensense 公告](https://new.abb.com/news/detail/111398/abb-acquires-sevensense-expanding-leadership-in-next-generation-ai-enabled-mobile-robotics)
