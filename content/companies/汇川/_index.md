---
title: "汇川"
wiki: true
wiki_type: "company"
wiki_rank: 31
seed_count: 7
lastmod: "2026-11-05"
description: "汇川技术（Inovance，300124.SZ）2003 年成立、2010 年创业板上市，伺服电机与驱动器成套卖；编码器在它这里是电机内置件加驱动器接口，2011 年收购长春汇通建传感器件平台。"
official_url: "https://www.inovance.com/"
wiki_category: "驱动、控制与系统配套"
related_models: ["IS620N", "SV660ND"]
---

汇川站在“驱动器 + 伺服电机 + 系统”这一层。它的编码器相关性落在三段：一段在伺服电机内部，反馈件随电机订货型号一起定；一段在驱动器侧，机床或产线要接的外部编码器按驱动器支持的协议走；第三段是它单列在官网的 EA 系列编码器整机。所以读汇川的公开资料，能拿到的不是“某颗编码器用了谁的方案”，而是“一个国产驱动平台把哪些反馈形态当成标准配置”。本页只写能从官网读到的部分，规格级数字不猜。

## 2003 年起家于变频器，靠并购补齐传感件与机床

官网里程碑给出的主线很清楚：2003 年成立，2010 年 9 月登陆创业板，代码 300124；2011 年苏州基地投产，同年收购长春汇通，官方英文表述为 establishment of “transducer technologies and product platforms”，即传感器件技术与产品平台；2015 年收购江苏经纬进入轨道交通；2016 年成立苏州汇川联合动力；2017 年在苏州开建智能制造中心，同年提出“一轴一网一生态”；2018 年收购德国 PA，2019 年收购 BST，2021 年收购北京 EKSYS 与 MOOXEE，2023 年收购韩国 SBC Linear。官网把当前业务归为四块：工业自动化与数字化、新能源汽车动力系统、智能机器人、数字能源。[公司概况与里程碑](https://www.inovance.com/global/about/index.html)

对做反馈件的人来说，这条并购线里只有 2011 年那一笔与编码器直接相关：做出编码器需要的“传感元件 + 解算 + 产品平台”三项能力，官网用 transducer 这个词概括，但没有展开是光电、磁还是电感。其余几笔分别补机床（PA）、电梯与能源（BST）、系统集成（EKSYS）。

## 编码器在汇川这里是电机内置件、驱动器接口、关节模组与单列整机

| 系列 / 产品 | 形态 | 与编码器的关系（官网口径） | 其他公开参数 |
| --- | --- | --- | --- |
| [IR-U4/U6/U8/U13/U18 协作机器人](https://www.inovance.com/portal/product/details?productId=751) | 整机 | 关节角度随关节伺服系统一起进来，官网未公布各关节编码器配置 | 负载 4/6/8/13/18 kg；臂长 625/915/780/1301/1046 mm |
| [伺服电机（产品选型工具单列类目）](https://www.inovance.com/selector/) | 电机 | 编码器作为电机附件随订货型号确定 | 选型工具按产品分类筛选，伺服电机为独立入口 |
| [EA47 系列整体式锥轴编码器](https://www.inovance.com/product/details?productId=679) | 编码器整机 | 官网单列产品页，面向伺服电机 | 锥轴 φ9、锥度 1:10；单圈 23 位、多圈 16 位；磁多圈；双向异步串行 |
| [EA58 系列总线编码器](https://www.inovance.com/product/details?productId=514) | 编码器整机 | 官网单列产品页，CANopen 协议 | 外径 58 mm；单圈 13 位、多圈 12 位 |
| [EA84 系列双核功能安全编码器](https://www.inovance.com/portal/product/details?productId=852) | 编码器整机 | 官网单列产品页，配伺服实现 SIL3 | 26 bit 光编码器；IP67；双 MCU；支持 SS1/SS2/SLS/SBC/SDI/SOS/SSM |
| [工业自动化标准品（伺服、变频、PLC、触摸屏）](https://www.inovance.com/global/product/overview.html) | 驱动器与控制 | 驱动器侧的编码器接口能力属技术手册内容，公开总览页不列 | 总览页只写品类，具体型号落在下级页 |
| [长春汇通（2011 年并购）](https://www.inovance.com/global/about/index.html) | 传感器件平台 | 官方称 transducer technologies and product platforms，未披露具体产品形态 | 并购年份 2011，纳入工业自动化板块 |

表里能确认的是：汇川的编码器有两条交付路径。一条是随伺服电机订货的内置件，不给单独型号；另一条是 EA 系列这样在官网单列产品页、可单独采购的整机，从 13 位的 CANopen 总线型到 26 位带功能安全的型号都有公开参数页。协作机器人的负载与臂长是官网产品页原文数字，但它们说明不了关节里装了什么——一台 18 kg 负载的六轴，关节输出侧要的是上电即绝对的角度，电机侧要的是换相用的电角度，这两种需求在采购单上是两个条目，官网都不公开。

## 谁决定编码器：电机选型在前，驱动器协议在后

采购一台汇川伺服时，编码器先被电机型号锁死，再被驱动器支持的外部反馈类型约束一次。前一步的决策权在伺服电机厂的电机设计（轴端结构、安装深度、线束走向），后一步的决策权在整机厂的电气工程师——他要接光栅尺、第三方旋转编码器或旧设备遗留的反馈件时，看的是驱动器手册里的接口表，不是电机样本。

一家同时做变频器、伺服、PLC 与机器人的公司，会把编码器接口的覆盖面当成机型分档的手段，高配机型多给几种协议，低配机型只留一种。内部用谁的裸片则是另一层：长春汇通做的是哪一类传感件、伺服电机里的编码器是自制还是外购、驱动器的解算由 MCU 还是专用芯片完成，公开页只到型号与接口，不写 BOM 与供应链。

## 官方资料

- [汇川技术官网（中文）](https://www.inovance.com/)
- [汇川技术全球站（英文）](https://www.inovance.com/global)
- [公司概况与 2003–2024 里程碑](https://www.inovance.com/global/about/index.html)
- [产品中心总览](https://www.inovance.com/global/product/overview.html)
- [IR-U 系列协作机器人产品页](https://www.inovance.com/portal/product/details?productId=751)
- [EA47 系列整体式锥轴编码器](https://www.inovance.com/product/details?productId=679)
- [EA58 系列 CANopen 总线编码器](https://www.inovance.com/product/details?productId=514)
- [EA84 系列双核功能安全编码器](https://www.inovance.com/portal/product/details?productId=852)
- [产品选型工具入口](https://www.inovance.com/selector/)
