---
title: "TDK"
wiki: true
wiki_type: "company"
wiki_rank: 24
seed_count: 9
lastmod: "2026-10-22"
description: "TDK 是日本的电子元件集团，磁传感板块给两条角度路线：TDK-Micronas 的 3D 霍尔 HAL 37xy 家族测 BX/BY/BZ，另有从硬盘磁头下移的 TMR 角度传感器。"
official_url: "https://www.tdk.com/en/index.html"
wiki_category: "传感器与测量前端"
related_models: []
---

TDK 在编码器链上不是一个编码器厂，而是"磁传感芯片加无源件"的元件集团：角度传感器这一块有两条并行路线——TDK-Micronas 的 3D 霍尔（HAL 37xy 家族，能同时测 BX/BY/BZ 三个分量）和从硬盘磁头技术下移的 TMR 角度传感器。对做编码器的人，看它的意义在于这两条路线覆盖了"宽气隙穿轴测量"和"高精度小体积"两种需求。

## 元件集团里的传感板块，是多平台拼起来的

TDK 的品牌主张是 "In Everything, Better"，现任 CEO 为 Noboru Saito。官网产品中心的一个细节能说明它的传感业务是怎么组织的：按料号检索的范围覆盖 TDK、InvenSense、Micronas、Tronics 与 TDK-Lambda 五家——也就是惯性、磁传感、MEMS 与电源分属不同平台，统一在一个检索入口下。[TDK 官网](https://www.tdk.com/en/index.html)

官网产品中心的传感器分类把角度单列一类，并在其下分"霍尔角度（direct angle）""TMR 角度""角度传感器模组"三支；另有线性霍尔、齿轮转速（gear tooth）、霍尔开关、运动与惯性（加速度、陀螺、IMU）、电流、温度（NTC/PTC）、压力、液位、超声波等分类。这条结构说明它的角度传感不是孤立产品，而是挂在整个磁传感体系里。[产品中心站图](https://product.tdk.com/product_top_page/sitemap.xml)

## 两条角度路线：3D 霍尔测三分量，TMR 走磁头工艺

霍尔这一支的官方技术说明是：用立式霍尔片测芯片平面内的磁场分量（而不是垂直芯片表面的分量），由此得到成比例的角度或位置输出；这套方法在官方页里叫 "3D HAL technology from TDK-Micronas"。HAL 37xy 家族能测 BX、BY、BZ 三个分量，芯片内算出角度并转成输出信号，还带可编程的分段线性特性用于校正；HAC 37xy 在同族里加了集成电容以改善 EMC、面向无 PCB 应用；HAR 37xy 是双 die 版本，两片独立 die 叠在同一封装里，因此保证两片感受同一磁场位置、输出同步，属于真正的冗余。[霍尔角度传感器](https://product.tdk.com/en/products/sensor/angle/direct-angle/index.html)

TMR 这一支的官方说法是：把在硬盘磁头上有长期验证的 TMR（隧道磁阻）技术下移做传感器，卖点是高输出、抗噪声、角度精度好、温度特性平稳、封装小，便于车用；并写明已量产，用在电动助力转向（EPS）电机等要求精度与稳定的场合。[TMR 角度传感器](https://product.tdk.com/en/products/sensor/angle/tmr-angle/index.html)

| 系列/族 | 类型 | 公开关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [HAL 37xy](https://product.tdk.com/en/products/sensor/angle/direct-angle/index.html) | 3D 霍尔角度/位置传感器 | 测 BX/BY/BZ 三分量，芯片内算角度 | 支持宽气隙、角度与穿轴角度测量；输出特性可编程；非易失存储器可改主要参数 |
| [HAC 37xy](https://product.tdk.com/en/products/sensor/angle/direct-angle/index.html) | 3D 霍尔，集成电容版 | 与 HAL 37xy 同族 | 集成电容改善 EMC，面向无 PCB 装配 |
| [HAR 37xy](https://product.tdk.com/en/products/sensor/angle/direct-angle/index.html) | 3D 霍尔，双 die 版 | 两片独立 die 堆叠 | 单片封装内双 die 同步输出，构成真冗余 |
| [TMR 角度传感器](https://product.tdk.com/en/products/sensor/angle/tmr-angle/index.html) | TMR 角度传感器 | 页面未给位数与角秒值 | 高输出、抗噪声、温度特性平稳、小封装；已量产，用于 EPS 电机 |
| [角度传感器模组](https://product.tdk.com/en/products/sensor/angle/index.html) | 模组形态 | 页面未给数值 | 与芯片并列的一支，按模组交付 |
| [齿轮转速 / 线性霍尔 / 霍尔开关](https://product.tdk.com/product_top_page/sitemap.xml) | 磁传感其他分类 | 页面未给数值 | 分别面向转速、直线位置与开关量检测 |
| [运动与惯性（加速度/陀螺/IMU）](https://product.tdk.com/product_top_page/sitemap.xml) | 惯性器件 | 页面未给数值 | 由 InvenSense 平台承载，与角度传感互补 |

## 在编码器链上的位置

TDK 站的位置比单一芯片厂更上游：它同时做磁传感芯片、无源件（电容、电感、磁珠）与惯性器件，编码器厂从它这里可能一次买走敏感芯片和板上的被动件。所以"TDK 在这个编码器里"这句话，可能指角度芯片，也可能只指一颗电容——**具体是哪一颗，官网不公布客户 BOM，推不出来**。

两条角度路线的分工可以推：3D 霍尔靠测三个分量支持宽气隙与穿轴布置，适合机械公差大、要离轴的场合；TMR 靠高输出与低噪声拿精度，适合对精度和体积都紧的场合（官方举的例子就是 EPS 电机）。下游决策权在 Tier1、电机厂与编码器模组厂手里，安全相关的项目还要按功能安全等级再筛一遍。

## 官方资料

- [TDK 官网](https://www.tdk.com/en/index.html)
- [TDK 产品中心](https://product.tdk.com/en/index.html)
- [角度传感器总览（霍尔/TMR/模组三支）](https://product.tdk.com/en/products/sensor/angle/index.html)
- [霍尔角度传感器（HAL/HAC/HAR 37xy）](https://product.tdk.com/en/products/sensor/angle/direct-angle/index.html)
- [TMR 角度传感器](https://product.tdk.com/en/products/sensor/angle/tmr-angle/index.html)
- [传感器产品分类树（官方站图）](https://product.tdk.com/product_top_page/sitemap.xml)
- [按料号检索（覆盖 InvenSense、Micronas、Tronics 等）](https://product.tdk.com/en/search/part_no/)
