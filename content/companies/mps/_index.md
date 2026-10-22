---
title: "MPS"
wiki: true
wiki_type: "company"
wiki_rank: 49
seed_count: 4
lastmod: "2026-10-22"
description: "MPS（芯源系统）：主业电源，MagAlpha 磁角度线 MA600 给 12~15 位、INL <0.6°、校准后 <0.1°。"
official_url: "https://www.monolithicpower.com/en/products/sensors.html"
wiki_category: "芯片与信号链"
related_models: ["MA600"]
---

MPS 的主业是电源管理，磁角度传感是它挂在 MagAlpha 名下的一条产品线。在编码器链上它是"TMR / 霍尔角度芯片 + ABZ、UVW 输出"的芯片厂，位置在模组厂上游一格。读它的资料要抓两点：INL 有两个数（出厂 <0.6°、用户 32 点校准后 <0.1°），以及 [MA600](/models/ma600/) 已经进入"仅供既有客户"状态、新设计要看 [MA600A](/models/ma600a/)。

## 公司与品牌

Monolithic Power Systems（MPS），中文常称芯源系统。官网与产品页可见其以电源转换与模拟芯片为主，磁角度传感属于传感器产品线（MaGAlpha / MagAlpha 系列，评估套件叫 EVKT-MagAlpha 与 MagAlpha Evaluation App）。据维基百科条目，公司 1997 年由 Michael Hsing 创立，Michael Hsing 现任 CEO，总部在美国佛罗里达州 West Palm Beach。

公司的产品结构决定了这条线的定位：角度传感器不是它的主营，评估工具与文档风格也沿用电源产品那一套（datasheet 用 documentview 路径、评估板单独编号）。[MPS 公司条目](https://en.wikipedia.org/wiki/Monolithic_Power_Systems)

## 角度传感器产品线与公开规格

MagAlpha 系列的共同点：端轴或侧轴安装、径向充磁圆柱磁铁、片上 NVM 存零位与 ABZ/UVW/PWM 配置、SPI 与 SSI 读数。差别在位数、封装与温度档。

| 系列 | 类型 | 公开分辨率/精度 | 其他公开参数 |
| --- | --- | --- | --- |
| MA600 | TMR 磁角度传感器（数字输出） | 12~15 位可配、INL <0.6°，32 点用户校准后 <0.1° | 10~100 mT、12 kHz@12.5 位、标称无延时、SPI / SSI、ABZ 1~4096、UVW、PWM、QFN-16 3×3 mm、3.3 V、−40~125 °C |
| MA600A | 同上（现役推荐型号） | 12~15 位、INL <0.6°（校准后 <0.1°） | 与 MA600 同族特性，官网对 MA600 标注"继续为既有客户供货"并推荐新设计改用 MA600A |
| [MA702](https://www.monolithicpower.com/en/ma702.html) | 数字角度传感器 | 12 位 | ABZ 1~256、PWM、SPI / SSI、最小磁场 30 mT、QFN-16 3×3 mm、0~60000 rpm、−40~125 °C |
| [MA710](https://www.monolithicpower.com/en/ma710.html) | 数字角度传感器 | 12 位 | ABZ、PWM 12 位、QFN-16 3×3 mm、−40~125 °C |
| [MA735](/models/ma735/) | 数字角度传感器 | 9~13 位 | ABZ 与 PWM、UTQFN-14 超小封装 |
| [MAQ473](/models/maq473/) | 车规角度传感器 | 14 位 | ABZ 与 PWM、−40~150 °C、QFN-16 3×3 mm |

MA600 那两个数字要分开读：**<0.6° 是出厂校准后的 INL**，**<0.1° 是客户用片上 32 点查找表做系统校准之后的结果**——后者依赖客户的工装与磁铁一致性，不是买来就有的指标。另外"无延时"是官方特性栏的说法，对应的具体数值在 datasheet 里，本页不替它换算成 µs。MA600 产品页

MPS 在文档侧还有一件对选型更有用的东西：官网把"分辨率不等于精度"这件事单独写成两篇技术文章。一篇讲磁编分辨率与光编分辨率的可比性问题，指出把两者的"位数"直接对照会误导；另一篇讲精度与分辨率的关系，拆开 INL、噪声与有效位数。做跨品牌对比时，这两篇比产品页更能防止拿错口径。

官网给位数与 INL，不给重复性、温漂、长期稳定性、抗外磁场强度、气隙公差与磁铁偏心容差；"无延时"没有在特性栏给出 µs 数；12 kHz@12.5 位是带宽与分辨率的组合点，其他分辨率下的带宽要查曲线。MA702 给的 60000 rpm 是电子学允许的转速上限，不是精度保证范围。

## 在编码器链上的位置

MPS 卖芯片加评估板（例如 TBMA600-Q-LT-00A 测试板，配合 EVKT-MagAlpha-MagDiff 通信套件与 MagAlpha 评估 App）。客户是电机驱动厂、机器人与编码器模组厂，它的 ABZ / UVW 输出让下游能直接替掉增量光编或霍尔换相，这是它在这一层最实际的卖点。

不能推断的：TMR 敏感膜与晶圆来源（官网只讲结构与封装）、客户名单，以及某家关节客户是否用了 MA 系列。MA600 到 MA600A 的换代是公开的，但两者电学差异官网只给特性栏，不给对照表。

## 官方资料

- MA600 产品页
- MA600A 产品页
- [MA702 产品页](https://www.monolithicpower.com/en/ma702.html)
- [MA710 产品页](https://www.monolithicpower.com/en/ma710.html)
- MA735 产品页
- MAQ473 车规产品页
- [技术文章：磁角度传感器的分辨率怎么理解](https://www.monolithicpower.com/en/learning/resources/magnetic-angle-sensors-resolution-explained)
- [技术文章：磁角度传感器的精度与分辨率](https://www.monolithicpower.com/en/learning/resources/understanding-accuracy-and-resolution-for-magnetic-angle-sensors)
- [MPS 公司条目（沿革）](https://en.wikipedia.org/wiki/Monolithic_Power_Systems)
