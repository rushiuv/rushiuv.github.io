---
title: "ABB Robotics"
wiki: true
wiki_type: "company"
wiki_rank: 200
lastmod: "2026-10-22"
description: "ABB 的机器人业务：大型六轴 IRB 6700 系列 150~310 kg、位姿重复性 0.03 mm，OmniCore 控制器路径精度低至 0.6 mm，官网不公开各轴编码器型式与分辨率。"
wiki_category: "工业机器人与自动化"
official_url: "https://www.abb.com/global/en/areas/robotics"
related_companies: ["ABB", "Sevensense Robotics"]
---

ABB Robotics 站在**整机应用**这一层，而且是这一层里选型权最集中的一类：伺服电机、齿轮单元、控制器和运动学都在集团内部闭环，关节上的反馈由它自己定，集成商和终端用户都碰不到。对做编码器的人，它的公开资料是一个明确的负样本——官网给到 TCP 位姿重复性与路径精度为止，再往下的单轴角分辨率、编码器型式、装在电机侧还是关节侧，一个字都没有。

## 集团里机器人在哪一块

ABB 集团官方自述：全球员工约 110,000 人，历史超过 140 年，2025 年营收 332.20 亿美元，研发投入 13.18 亿美元，业务分 Electrification、Motion、Automation 三个领域。[集团概况](https://global.abb/group/en/about)；[About ABB](https://www.abb.com/global/en/company/about)

机器人归在 Automation 之下，与控制器、软件、应用单元一起卖。这个结构对器件侧的含义很直接：**机器人部门的关节执行器在集团内部就有来源**。ABB 自己在卖 Motor and Gear Units，官方写这些单元"已经用在 ABB 自家的 positioner 和机器人上"，现在打包卖给系统集成商做外部轴（第七轴、变位机）。也就是说，外部轴制造商拿到的是电机加减速机加反馈的成套件，不是散件。[Motor and Gear Units](https://www.abb.com/global/en/areas/robotics/products/equipment/motor-and-gear-units)

## 公开指标停在 TCP 这一层

官网产品结构是六类本体加控制器：六轴、协作、Delta、SCARA、喷涂、码垛，另有移动机器人。下表只抄本次能打开的产品页原口径。

| 对象 | 形态 | 公开数值 | 其他公开参数 |
| --- | --- | --- | --- |
| [IRB 6730](https://www.abb.com/global/en/areas/robotics/products/robots/articulated-robots/large-robots/irb-6730) | 六轴大型，含多个变型 | 负载最高 270 kg，臂展最高 3.10 m | 位姿重复性 0.03 mm、路径重复性 0.08 mm |
| [IRB 6710~6740](https://www.abb.com/global/en/areas/robotics/products/robots/articulated-robots/large-robots/irb-6730) | 同代四个型号 | 负载 150~310 kg，臂展 2.5~3.2 m | 官方称合计 22 个变型 |
| [OmniCore](https://www.abb.com/global/en/areas/robotics/products/controllers/omnicore) | 机器人控制器平台 | 路径精度低至 0.6 mm | 多机同时运行、速度最高 1600 mm/s |
| [Motor and Gear Units](https://www.abb.com/global/en/areas/robotics/products/equipment/motor-and-gear-units) | 外部轴用电机＋齿轮成套件 | 页面未列扭矩与转速 | 官方称已用于自家 positioner 与机器人 |

三个数要分开读：0.03 mm 是**位姿重复性**（回到同一点的能力），0.08 mm 是**路径重复性**（走同一条轨迹的能力），0.6 mm 是控制器在 1600 mm/s 下的**路径精度**。三者定义不同，互相不能替代，也都不等于绝对精度。

## 在编码器链上的位置

它是链条最上游的整机厂：采购伺服电机、减速机与角度反馈，做成六轴臂，卖给集成商与产线。决策权落在 ABB 的关节设计与采购部门，集成商买不到单独的编码器选型权——连第七轴都按整套电机单元买。对器件厂，这一层现实的进入路径是先成为电机或关节模组的供应商，而不是直接向 ABB 机器人报编码器。

一个常见的错误换算要写清楚：0.03 mm 在 3.1 m 臂展上折合末端角约 0.00055°，但这个数字里同时含减速机回差、臂体刚度、热漂移与标定残差，官方不做分解。**因此不能由重复性反推关节角分辨率，也不能据此判断它用旋变、光电还是磁，单圈还是多圈。**官网不公布各轴反馈型式，也不公布编码器供应商，任何"ABB 用某家芯片"的说法都缺公开依据。

公开页面给的是负载、臂展、重复性、循环时间、控制器精度档位。**没有公开**的是：各轴反馈元件型式与位数、反馈装在电机侧还是关节侧、伺服环周期、关节角分辨率、编码器供应商与料号。这些只在维护手册、备件目录和内部规格书里，不在对外网页上。

## 官方资料

- [ABB Robotics 总览](https://www.abb.com/global/en/areas/robotics)
- [机器人产品目录](https://www.abb.com/global/en/areas/robotics/products)
- [六轴机器人分类页](https://www.abb.com/global/en/areas/robotics/products/robots/articulated-robots)
- [IRB 6730 产品页](https://www.abb.com/global/en/areas/robotics/products/robots/articulated-robots/large-robots/irb-6730)
- [控制器分类页](https://www.abb.com/global/en/areas/robotics/products/controllers)
- [OmniCore 控制平台](https://www.abb.com/global/en/areas/robotics/products/controllers/omnicore)
- [Motor and Gear Units](https://www.abb.com/global/en/areas/robotics/products/equipment/motor-and-gear-units)
- [About ABB](https://www.abb.com/global/en/company/about)
- [ABB 集团概况](https://global.abb/group/en/about)
