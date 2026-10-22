---
title: "ANYbotics"
wiki: true
wiki_type: "company"
wiki_rank: 113
lastmod: "2026-10-22"
description: "苏黎世 ETH 2016 年衍生公司，ANYmal 四足巡检机 IP67、0.75 m/s、单次 2 km，载 10 kg；官网规格只到整机级，不给关节数与编码器型式。"
wiki_category: "移动机器人与巡检"
official_url: "https://www.anybotics.com/"
---

ANYbotics 是"移动机器人与巡检"这一层里关节密度最高的一类整机厂：四足行走，每台机器十几个电机轴同时在力矩环里工作。但它对外只发表整机级指标——速度、续航、载荷、防护等级、传感器清单——关节数、单关节扭矩、反馈装在电机侧还是关节侧，一个字都没有。对做编码器的人，这是典型的"用量大、门槛在规格书之外"的客户：官网能确认它的应用边界，确认不了器件口径。

## 从 ETH 衍生公司长成巡检服务商

官方自述 2016 年从苏黎世联邦理工（ETH Zurich）衍生成立，2017 年实现首批销售，投资方包括 Walden Catalyst、NPG Capital、Bessemer Venture Partners、Aramco Ventures、Swisscom Ventures，早期客户与共创方提到 Petronas、Shell、BASF。[About](https://www.anybotics.com/about-us/)

卖的东西已经从机器人变成"巡检结果"：官网首页给的运营数字是每月分析 120,000 次以上巡检、监测 1,000 个以上工业资产；配套软件叫 Shift，负责排任务、看趋势、把发现转成工单。[首页](https://www.anybotics.com/)；[ANYmal](https://www.anybotics.com/robotics/anymal/)

## 公开规格全在整机这一级

| 项目 | 公开数值 |
| --- | --- |
| 形态 | 四足，官方页面未给关节数与自由度 |
| 防护 | IP67，防尘防水，全天气作业 |
| 行走速度 | 0.75 m/s |
| 续航与里程 | 90 min 续航，单次充电走 2 km |
| 充电 | 100 min 充到 70%，3 h 充满 |
| 载荷 | 标配云台载荷之外可再加 10 kg |
| 感知 | 360° 激光雷达、6 个深度相机、2 个遥操作相机 |
| 计算 | 2 颗第八代 Intel i7 六核 |
| 云台行程 | 垂直 ±90°、水平 ±165° |
| 热像 | −40~550 °C |
| 超声麦克风 | 0~384 kHz |
| 认证 | CE、FCC、Anatel；ANYmal X 另有 ATEX/IECEx，最高 Zone 1 IIB |

以上全部取自 ANYmal 产品页与规格页。[ANYmal 产品页](https://www.anybotics.com/robotics/anymal/)；[规格页](https://www.anybotics.com/anymal-specifications-sheet/)；[ANYmal X](https://www.anybotics.com/robotics/anymal-x/)

公开页面给的是整机规格与安全认证清单。ANYmal X 的防爆认证按 Zone 1 IIB 写是官方口径，但防爆对电机与反馈的温升、爬电距离的具体要求，官网没有展开。

## 在编码器链上的位置

四足是所有机器人形态里单位整机的角度通道最多的之一，两条腿一组要在力矩环里做阻抗控制，反馈的时间一致性和分辨率直接决定落脚稳不稳。但 ANYbotics 不外卖执行器：官网早年的 ANYdrive 独立产品页现在重定向回首页，说明执行器已经收回自用、不再作为商品对外。这意味着两件事——**选型权完整地留在苏黎世总部**；外部拿不到任何关节级参数，只能拿到整机指标。

不能推的部分要写明：关节数量、单关节峰值扭矩、反馈元件是旋变还是磁编、位数多少、装在电机侧还是关节侧、控制环周期，官网全部不公开。同样不能由"0.75 m/s""2 km"这类整机数字反推任何关节规格。

## 官方资料

- [ANYbotics 首页](https://www.anybotics.com/)
- [公司介绍](https://www.anybotics.com/about-us/)
- [ANYmal 产品页](https://www.anybotics.com/robotics/anymal/)
- [ANYmal X 防爆版](https://www.anybotics.com/robotics/anymal-x/)
- [机器人能力页](https://www.anybotics.com/robotics/robot-capabilities/)
- [ANYmal 规格页](https://www.anybotics.com/anymal-specifications-sheet/)
- [巡检自动化方案页](https://www.anybotics.com/robotics/automate-inspection/)
