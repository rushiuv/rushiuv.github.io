---
title: "舍弗勒"
wiki: true
wiki_type: "company"
wiki_rank: 108
seed_count: 2
lastmod: "2026-10-22"
description: "舍弗勒（Schaeffler）是德国运动技术集团，四个事业部覆盖电驱、动力总成与底盘、汽车后市场、轴承与工业；它供关节里被测量的机械那一侧，编码器不在其产品目录。"
official_url: "https://www.schaeffler.com/"
wiki_category: "机械传动与精密驱动"
related_models: []
---

舍弗勒站在机械传动与精密驱动这一层：轴承、直线与传动部件、机电一体化模组。**编码器不在它的产品目录里**，它在关节与执行机构里的角色是把“被测量的那一侧”做出来——轴、轴承、减速与导向结构。所以读它的资料，能得到的不是编码器规格，而是一个关节在机械侧留下了多少误差预算；这部分误差不会因为换了更高分辨率的编码器而消失。

## 四个事业部里没有编码器这一格

官网导航给出的事业部结构是四条线：E-Mobility（电驱）、Powertrain & Chassis（动力总成与底盘）、Vehicle Lifetime Solutions（车辆全生命周期方案）、Bearings & Industrial Solutions（轴承与工业方案）。集团页的自我描述是八十年来一直在运动技术领域推动突破性发明与开发，产品页的表述是从基础部件延伸到完整系统方案。[集团与事业部结构](https://www.schaeffler.com/en/divisions-products/)

这个结构本身就是一条信息：四条线分别对应电驱、动力总成、售后与工业轴承，没有一条是传感与测量。也就是说，在舍弗勒的公开产品体系里，找不到编码器这个独立品类页；它能提供的与反馈相关的东西，是承载编码器的机械界面——轴承内外圈、轴端、法兰，以及决定角度传递精度的减速与导向件。[轴承与工业方案](https://www.schaeffler.com/en/divisions-products/industrial/)

| 公开条目 | 层级 | 与编码器的关系 | 公开信息 |
| --- | --- | --- | --- |
| Bearings & Industrial Solutions | 事业部 | 提供承载与被测量的机械界面，轴承与导向精度进角度读数 | 事业部名称与归口公开 |
| E-Mobility | 事业部 | 电驱系统，反馈随电机与传动配置确定 | 同上 |
| Powertrain & Chassis | 事业部 | 动力总成与底盘，不含测量器件 | 同上 |
| Vehicle Lifetime Solutions | 事业部 | 售后与全生命周期服务，不涉及器件开发 | 同上 |
| 电机到减速器到输出法兰 | 工程结构 | 编码器测其中一根轴，游隙与背隙直接进读数 | 属工程判断，非厂商参数 |

## 关节里它供的是被测量的一端，编码器精度补偿不了机械回差

一个关节的执行链是电机、减速器、输出法兰三段，编码器通常测其中某一根轴的角度。这条链上有两处机械误差会直接进到角度读数里：轴承游隙让轴在受力时产生微小位移，减速器的背隙让输入端与输出端之间出现一个不随指令变化的死区。这两项属于机械件的公开属性（在样本里查游隙与背隙），但**不会被写进任何一份编码器规格书**。

这条判断对采购的实际含义是：用更高的编码器分辨率去追一个由回差决定的定位误差，方向是错的；反过来，若机械侧已经把回差压到很小，编码器的分辨率与重复性才会成为瓶颈。这是工程推理，不是舍弗勒的官方结论，本节不引用任何未经核实的整机指标。**能推的是它在链条上的位置，不能推的是它给某个具体关节模组配了什么反馈件**：官网公开层没有这条信息。

## 官方资料

- [舍弗勒集团官网](https://www.schaeffler.com/en/)
- [事业部与产品结构（四条事业部线）](https://www.schaeffler.com/en/divisions-products/)
- [轴承与工业方案（Bearings & Industrial Solutions）](https://www.schaeffler.com/en/divisions-products/industrial/)
- [产品总览入口](https://www.schaeffler.com/en/divisions-products/products/)
- [集团历史](https://www.schaeffler.com/en/group/history/)
