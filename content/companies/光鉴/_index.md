---
title: "光鉴"
wiki: true
wiki_type: "company"
wiki_rank: 153
seed_count: 1
lastmod: "2026-10-22"
description: "光鉴科技（Deptrum）：2018 年成立的深圳 3D 视觉模组厂，Nebula sToF 相机深度分辨率 248×180@10fps、Libra 3000 双目 AI 相机 640×540@30fps，整条产品线没有转轴、不输出角度。"
official_url: "https://www.deptrum.com/site/index"
wiki_category: "光学感知与空间测量"
related_models: []
---

光鉴科技做的是**固定在壳体里的 3D 深度相机模组**，站在"外部空间感知"这一层，不在关节位置反馈这条链上：它给机器人一个"前面有什么、离多远"的点云，不给"第几轴转角多少"。模组里没有电机、没有转轴、没有编码器，所以谈它"用谁家的位置反馈"从一开始就是伪问题；该看的是深度分辨率、帧率、出图延迟与接口，以及这些指标在哪个距离段成立。

## 公司与品牌

公司全称光鉴科技，品牌 DEPTRUM，2018 年成立，官网列深圳（福田区滨河大道中洲湾西座）、上海（浦东新区金港路 121 号）、重庆（两江新区仙桃数据谷 B11）三处地址，自述全球累计申请专利超 1000 项、产品落地二十多个国家和地区、核心研发团队 100 人以上。[公司介绍](https://www.deptrum.com/zh/about.html)

创始人兼 CEO 朱力、首席科学家吕方璐均为清华电子系本科、伯克利博士，师从 VCSEL 领域开创者之一 Connie Chang-Hasnain；CTO 汪博为清华本科、斯坦福博士，曾在 ZOOX 负责自动驾驶深度学习平台。官网记的技术节点是 2019 年前后做出消费级超表面结构光芯片，2020–2022 年随微信刷脸支付规模化，2023 年后转入机器人与具身智能。[公司介绍](https://www.deptrum.com/zh/about.html)

这层背景的实际含义：它的差异化在光学与算法（超表面、散斑结构光、双目神经网络深度估计），不在机电执行，因此不像整机厂那样成为角度传感器的采购方。

## 产品线：六个系列全是固定模组，参数表里没有角度输出

下表数值抄自各产品页参数表，同系列不同型号差别很大，属"视型号"口径。

| 系列 | 类型 | 公开深度规格 | 其他公开参数 |
| --- | --- | --- | --- |
| [Nebula 280](https://www.deptrum.com/zh/product-nebula.html) | sToF，3D 避障 + SLAM | 3 cm–10 m，≥248×180@10 fps，mToF ≤3 mm@3–25 cm，sToF ≤1%@70 cm–8 m | FOV H98°×V60°，功耗 <0.6 W，34.5×15.35×8.35 mm，MIPI，主从同步 |
| [Nebula 411](https://www.deptrum.com/zh/product-nebula.html) | sToF + mToF + RGB | 3 cm–8 m，mToF <5 mm@3–30 cm，sToF ≤1%@60 cm–8 m | RGB 800×600，≤1.7 W，66.6×30.2×21.3 mm，USB 2.0 Wafer |
| [Libra 1000](https://www.deptrum.com/zh/product-libra.html) | 被动双目 AI，操作感知 | 0.1–5 m，深度 640×540@30 fps，<1 mm@4–20 cm | RGB 1280×1080@30 fps，基线 20 mm，FOV H91°×V78°，6 轴 IMU，Fakra GMSL 2.0 |
| [Libra 3000](https://www.deptrum.com/zh/product-libra.html) | 被动双目 AI，空间感知 | 深度 640×540@30 fps，<1%@10 cm–1 m、<1.5%@1–2 m、<2%@2–5 m | 基线 65 mm，FOV H115°×V99°，6 轴 IMU，GMSL 2.0 或 USB 2.0 Type-C |
| [Aurora 900 / 910](https://www.deptrum.com/zh/product-aurora-900.html) | 散斑结构光刷脸 | 0.3–1 m，±3 mm@0.5 m、±4 mm@0.8 m、±7 mm@1 m | RGB/IR/Depth 硬件同步且像素级对齐，3–100000 Lux，61×18×13.5 mm，USB 2.0 |
| [Veinshine / HandPass](https://www.deptrum.com/zh/products.html) | 掌静脉模组 / 刷掌终端 | 产品页未给深度分辨率 | 面向刷掌支付与身份核验，与 Nebula、Aurora 分属不同业务线 |

三处值得单独记：**Nebula 的深度输出只有 248×180@10 fps 一档**，是避障用的数据率，不是测量用的；**Libra 把算力写进产品定位**，深度图计算平台标 Orin NX/AGX；**Aurora 是 0.3–1 m 近距离精度**，与 Nebula 的 3 cm 近场属两套光学设计，放在一起比"精度"没有意义。

## 在编码器链上的位置

它是这条链的**上游互补件**：整机厂同一个 BOM 里既买关节编码器（测自身姿态）也买深度相机（测外部环境），两笔钱互不替代。关节角度必须来自电机侧或输出侧编码器，深度相机补不上——它给的是机体坐标下的点云，误差来自标定、时延与特征匹配，不来自码盘。

能推的是需求结构：把深度模组做到 31 mm 级、功耗压到 0.8 W 以下，说明客户群是消费级移动机器人与扫地机，这类客户对成本敏感、角度需求落在电机换相与轮速上，不是高精度关节。**不能推**的是它内部用哪家图像传感器、激光器或处理芯片——官网只给模组级参数，不公布 BOM。

官网新闻有一条跨界信号：2026-08-24 光鉴与松延动力达成合作，Nebula 页面也挂了追觅、松延动力两条应用案例入口。人形机器人本体有关节、要编码器（见 `/companies/松延动力/`），光鉴在合作里给的是头部或躯干视觉，不是关节反馈，两边采购口不重叠。

## 公开资料的边界

官网给到模组级深度精度、FOV、帧率、功耗、尺寸与接口，**没有公开**深度标定的重复性、温漂、单帧时延分布、MTBF，也没有价格与交期。做精度预算要拿对应型号的规格书与标定报告，官网只留"咨询产品与样品 / 规格书与资料"两个入口。

本页不把官网"毫米级""行业首个"当可核对数字——那是官方表述，不是测试条件。跨公司比较至少要对齐量程段与照度，否则 Nebula 的 3 cm 近场会被拿去和 Aurora 的 0.5 m 人脸精度并排。

## 官方资料

- [光鉴科技官网](https://www.deptrum.com/site/index)
- [公司介绍（成立年份、团队、技术节点）](https://www.deptrum.com/zh/about.html)
- [产品中心（六类产品分类）](https://www.deptrum.com/zh/products.html)
- [Nebula 系列 sToF 深度相机（五型号参数表）](https://www.deptrum.com/zh/product-nebula.html)
- [Libra 1000 & 3000 双目 AI 深度相机](https://www.deptrum.com/zh/product-libra.html)
- [Aurora 900 系列 3D 结构光刷脸深度相机](https://www.deptrum.com/zh/product-aurora-900.html)
