---
title: "英飞凌"
description: "英飞凌 Infineon：XENSIV 磁位置传感器覆盖霍尔、AMR、GMR、TMR 四种原理，角度系列从 TLE5012B 的 1.0° 到 TLE5109A16D 的 0.5°。"
wiki: true
wiki_type: "company"
wiki_rank: 10
seed_count: 16
lastmod: "2026-10-22"
official_url: "https://www.infineon.com/"
related_models: ["AS5047P"]
related_companies: ["ams OSRAM"]
---

英飞凌在编码器链上是“四种磁阻原理全都自己做”的那一层：霍尔、AMR、GMR、TMR 各有角度产品线，且多数型号同时给单 die 与双 die 两个版本。读它的资料，最该看的是官方选型指南里那张把原理、die 配置、输出形式、精度与功能安全等级并排的表——它把“同一颗芯片怎么做到 ASIL D”这件事讲得比多数厂商清楚。

## 公司与品牌

英文名 Infineon Technologies，磁位置传感归在 XENSIV 品牌下。官方选型指南开篇写得很直白：所有磁传感技术都在自有产线上制造，因此客户可以在霍尔、各向异性磁阻（AMR）、巨磁阻（GMR）与隧穿磁阻（TMR）之间挑最合适的一种。指南同时把安全等级写到具体型号：ISO 26262 的 SEooC 最高到 ASIL D，抗杂散场指标按 ISO 11452-1 口径描述。[XENSIV 磁位置传感器选型指南](https://www.infineon.com/assets/row/public/documents/24/66/infineon-xensiv-magnetic-position-sensors-productselectionguide-en.pdf)

目录里另有大量开关与锁存器（TLx496x 系列官方标工作电流 1.6 mA）与线性 TMR 器件（TLI55910 量程 ±35 mT、灵敏度 5 mV/V/mT；TLI55950 带放大输出，灵敏度到 85.5 mV/mT）。这些不直接做角度，但在同一份选型资料里，读的时候要分清“测场强”和“测场方向”。

## 角度产品线与公开规格

下表数值全部来自官方选型指南的角度传感器对照表，精度是该表给出的角度误差口径。

| 系列 | 原理与 die 配置 | 输出形式 | 公开角度误差 | 其他公开参数 |
| --- | --- | --- | --- | --- |
| [TLE5012B(D)／TLI5012B](/models/tle5012b/) | GMR，单 die 与双 die | SSC(SPI) 角度 + sin/cos，另给 PWM／IIF／SPC／HSM | 1.0°（双 die）／1.9°（TLI5012B） | 工业版按 JEDEC JESD47，车规版 ISO 26262-ready，DSO-8 与 TDSO-16 |
| TLE5009／TLE5009A16D | GMR，单 die／双 die | 模拟 sin/cos | 0.9° | ISO 26262-ready，DSO-8／TDSO-16 |
| TLE5014 C16／P16／S16／SP16(D) | GMR，单 die 与双 die | SPC／PWM／SENT／SPI | 1.0° | 单 die 到 ASIL C，双 die 到 ASIL D，TDSO-16 |
| TLE5501 | TMR，单 die | 模拟 sin/cos | 1.0° | 磁场 20–100 mT、输出至 0.37 V/V 可直连 MCU、约 2 mA、AEC-Q100 grade 0（−40…150 °C）、DSO-8 |
| [TLE5502](/models/tle5502/)(D) | TMR，单 die 与双 die | 模拟 sin/cos | 0.8° | 单封装最多 4 路 ASIL-D 传感器、QFN-16 3×3 mm |
| TLE5109A16D | AMR，双 die | 模拟 sin/cos | 0.5° | 带温漂补偿，TDSO-16 |
| TLE5309D | AMR + GMR 双 die | 模拟 sin/cos | AMR 0.5°／GMR 0.9° | 两种原理同封装，TDSO-16 |
| TLx49012 | 霍尔，单 die | SPI | 0.8° | 最高 16 位、30000 rpm、25000 rad/s²、对轴与离轴、VSON-8 |

TLE5012B 的独立手册把细节写得更细：15 位绝对角表示（分辨率 0.01°）、接口上给 16 位 sin/cos、开启自动校准后全寿命与全温区最大角度误差 1.0°、双向 SSC 到 8 Mbit/s、0.25 µm CMOS、结温 −40…150 °C、ESD 大于 4 kV，带 CRC 与上电自检。TLE5012B 数据手册

官网给的是选型表口径的角度误差、接口、封装与安全等级，以及单颗器件手册里的分辨率与电气参数。选型表里的 0.5°／0.8°／1.0° 是最大误差口径，和“典型值”不可混用。另外，某些具体订购号在产品页上标为“not for new design”，那是单条目的状态，不能扩大成整个系列停产，也不能忽略后继续推荐。

## 四条原理在同一张表里的读法

精度档位是按原理排的：AMR 双 die 0.5°、TMR 双 die 0.8°、GMR 双 die 1.0°、霍尔 0.8° 但位数与速度上限不同。这说明“换原理”主要换的是误差来源，不是简单换一个更好的数字。

die 配置是另一个独立维度。同一个型号的单 die 与双 die 版本精度可以不同（TLE5012B 1.0° 与 TLI5012B 1.9°），安全等级也不同（单 die 到 ASIL C，双 die 到 ASIL D）。选型时把“型号 + 后缀 + die 数”当一个整体看，只写前三段字符会选错。

输出形式分两类：一类内部算好角度直接给数字（SSC、SPI、SPC、SENT、PWM），一类只给模拟 sin/cos，把插值与误差预算留给后端 ADC。TMR 系列偏后者，理由是它的输出幅度大、温漂低，可以不放大直接进 MCU。

## 在编码器链上的位置

英飞凌卖的是敏感元件与解算，买的是自己的晶圆产能（官方口径是四种原理都自产）。下游是电机厂、转向系统、机器人关节与编码器模组厂。

官方选型指南把目标应用写成“人形机器人、移动机器人、灵巧手、伺服电机、高端无人机、高端云台”，这是它自己对角度产品落点的表述，属于官方宣称，不等于这些行业里它的份额。

**不能推断**的是具体编码器整机厂用了它哪颗裸片——官网不公布 BOM。能推断的只有它对安全等级与输出形式的取舍。

## 官方资料

- [英飞凌官网](https://www.infineon.com/)
- [XENSIV 磁位置传感器选型指南（PDF）](https://www.infineon.com/assets/row/public/documents/24/66/infineon-xensiv-magnetic-position-sensors-productselectionguide-en.pdf)
- [磁位置传感器产品门类](https://www.infineon.com/cms/en/product/sensor/magnetic-sensors/magnetic-position-sensors/)
- TLE5012B-E5000 产品页
- TLE5012B 数据手册（PDF）
