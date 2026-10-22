---
title: "昆泰芯"
description: "昆泰芯 CONNTEK：泉州起步的磁与光编码器芯片厂，霍尔 KTH71/78 到 16 位、AMR KTM52/53 到 21 位、细分器 KTM5800 30 位、游标光学 KTO9512 24 位。"
wiki: true
wiki_type: "company"
wiki_rank: 1
seed_count: 84
lastmod: "2026-10-22"
official_url: "https://www.conntek.com.cn/"
related_models: ["KTM5900", "KTM5800", "KTM5200", "KTH78", "KTH7111", "KTO9512"]
related_companies: []
---

昆泰芯在这批公司里是唯一把磁与光两条编码器芯片路线放进同一份目录的一家：霍尔做绝对角，AMR 与 TMR 做高精度角，一颗细分器吃外部正余弦，一颗游标光学芯片吃码盘。读它的资料，重点不是单个位数，而是同一测量任务在四条路线上各自付什么代价——延时、温区、安装方式、要不要外部解算。

## 公司与品牌

官网署名昆泰芯微电子，英文 CONNTEK，公司介绍页标注“2016 since”。总部在福建泉州丰泽区华大街道体育街华创园 D410 室，研发中心分设苏州（工业园区唯新路 63 号）、上海（浦东盛夏路 608 号）、南京（雨花台雨花客厅）、杭州（滨江江虹路 459 号），运营中心在深圳南山留仙大道众冠时代广场。[公司介绍](https://www.conntek.com.cn/html/web/joinUs/index.html)

同一页面自述研发团队核心毕业于清华大学、荷兰代尔夫特理工等院校，曾在 NXP、Marvell、Qualcomm 任职；IP 覆盖 MEMS、霍尔磁传感、磁阻传感、高精密混合信号链处理、高精度传感器校准与超低功耗射频。对外提供的服务不只卖芯片，还包括磁场仿真、热学仿真、结构压力仿真与模组结构设计。

站点导航把产品分成五组：3D 霍尔芯片、编码器芯片、开关芯片、其他芯片、旋钮系列。编码器相关的型号全部落在前两组。[产品中心](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/index.html)

## 编码器相关产品线与公开规格

| 系列 | 路线与安装 | 公开分辨率 | 其他公开参数 |
| --- | --- | --- | --- |
| [KTH78xx](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html) | 霍尔绝对角，在轴与离轴 | 16 位 | INL ±0.35°（在轴）、±1° 左右（离轴），噪声 0.007–0.015°、系统延时 1 µs、SPI／SSI／ABZ 4–4096 步／UVW 1–8 对极／PWM、AEC-Q100、QFN16 3×3 或 SOP8、−40…150 °C、120000 rpm |
| [KTH71xx](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html) | 霍尔绝对角，带 ANLC 自动非线性校准 | 16 位 | 校准后在轴 ±0.1°、离轴 ±0.2°，SOP-8 4.9×6 mm、1 µs 更新、SPI 最高 10 Mbps、ABZ 1–4096 线、PWM 120 Hz–3.8 kHz、启动 1–100 ms 可调、120000 rpm |
| [KTM5200／5220](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM52XX/index.html) | AMR 在轴 | 21 位 | 校准后 INL ±0.015°（典型）、噪声 0.005°、输出延时 2–10 µs、SPI／ABZ 1–65536 线／UVW 1–64 对极／PWM、3–5.5 V、25 mA、TSSOP16、磁场 20–150 mT、60000 rpm |
| [KTM5300](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM53XX/index.html) | AMR 离轴，配垂直霍尔与算法 | 21 位 | 校准后 INL ±0.03°（典型）、QFN3×3-16L、60000 rpm、其余口径同 52 系列 |
| [KTM5800](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/absoluteangledivider/index.html) | 30 位绝对角度细分器，吃外部正余弦 | 单对极细分最高 18 位 | 最大 4096 对极输入、双 16 位 2 M SAR ADC、36 M SPI、ABZ 1–65536 线与 UVW 1–256 对极、INL ≤±0.025°、180000 rpm、40 mA、QFN32 5×5、80 M 主频 |
| [KTM5900／5910](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html) | TMR 磁编码器，在轴与离轴 | 24 位角度 | 有效位 16 bit、在轴 ±0.02°、离轴 ±0.05°、双 16 位 2 M SAR ADC、36 M SPI、±ABZ／±UVW／PWM、180000 rpm、QFN32 5×5、磁场 30–150 mT |
| [KTO9512](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/cursorabsoluteencoder/index.html) | 光学游标，3 码道相位阵列 | 单圈 24 位（Nonius 插值） | 26 mm 码盘、512/510/480 CPR、2 bit 格雷码扇区、6 对模拟差分输出、32-pin optoQFN 5×5×0.9 mm、9.5–15 mA、光谱 400–950 nm、−40…125 °C |

## 四条路线各自的取舍

霍尔路线（KTH78、KTH71）付的是精度：16 位、在轴最好到 ±0.1°，但它给的是最全的接口和最高的温区（KTH78 到 150 °C），还有 1 µs 级的刷新与内建磁场强弱报警，适合电机换相、步进闭环、车门与泵类这类要稳不要极致准的场合。

AMR 路线（KTM52、KTM53）付的是安装条件：器件工作在饱和区，公开写饱和磁场约 300 高斯，只响应平行芯片表面的场方向，所以对磁铁加工误差与安装距离不敏感，换来 21 位与 ±0.015°。代价是轴向安装要正对轴端，离轴版本还要加垂直霍尔与算法兜住。

TMR 与细分器路线（KTM59、KTM5800）付的是系统复杂度：KTM59 是 24 位角度但有效位写 16 bit，KTM5800 干脆只做解算、把敏感元件留给外部 AMR／TMR／光编／磁栅。后者的公开口径里最值得注意的是输入侧——一圈或一个绝对机械周期允许最多 12 bit（4096 线）多极对输入，模拟输入 20 mV–2 V 且推荐最大 1 V，这说明它对前端幅度是有要求的，不是随便接。

光学路线（KTO9512）是另一条赛道：26 mm 码盘、三条码道做游标、单圈 24 位，输出的是 6 对模拟差分而不是数字角，后级要自己插值。它和磁编的区别不在位数，而在码盘、对准容差与温漂的来源完全不同。

另有一支容易被漏掉的产品：3D 霍尔（KTH57xx、KTH55xx）。KTH5701 官方给的是三轴数字输出，XYZ 三轴 16 位、I2C 或 SPI 从机、XY 轴典型工作范围 ±130 mT、Z 轴 ±80 mT、工作频率 1000 Hz、QFN3×3-16L 与 DFN2×2.5-8L 两种封装、待机功耗 1.4 µA。它本身不做角度解算，官方定位是摇杆、旋钮与位移这类要拿原始磁场再由软件算运动信息的场合。看昆泰芯的目录时把这一支和编码器分开：前者卖的是“三个方向的场”，后者卖的是“一个角度”。

## 在编码器链上的位置

它在链上卖的是“敏感元件 + 解算 + 接口”这一段，买的是晶圆代工、封装测试与磁仿真工具。往下游看，它的客户是电机厂、编码器模组厂和整机厂；往上游看，它自己不建线，工艺能力靠代工伙伴。

能推断的是它想用一套接口语言覆盖多条路线（ABZ／UVW／PWM／SPI／SSI 在多个系列里反复出现，ABZ 线数与 UVW 极对数都可编程）；**不能推断**的是这些系列最终进了哪家整机——官网不公布客户，也不公布 BOM。

## 公开资料的边界

官网给到系列级的分辨率、INL 典型或最大值、噪声、延时、温区、封装与磁场范围，且多数参数标了“典型值”或“校准后”。**没有公开**：INL 的全温区最大值与温度曲线、重复性、长期漂移、EMC 与 ESD 等级、逐型号的启动时间默认值、报价与交期。方案级数字（如离轴 ±1°）必须连同磁铁与校准条件一起引用，不能单独摘出来做对比。

## 官方资料

- [昆泰芯官网](https://www.conntek.com.cn/)
- [产品中心总览](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/index.html)
- [公司介绍](https://www.conntek.com.cn/html/web/joinUs/index.html)
- [KTH78 系列高速高分辨率磁编码角度传感器](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [KTH71 系列 16 位自校准磁编码器](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html)
- [KTM52 系列在轴 AMR 角度编码器](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM52XX/index.html)
- [KTM53 系列离轴 AMR 角度编码器](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM53XX/index.html)
- [KTM5800 30 位绝对角度细分器](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/absoluteangledivider/index.html)
- [KTM59 系列 24 位 TMR 磁编码器](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html)
- [KTO95 系列游标绝对值光学编码器芯片](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/cursorabsoluteencoder/index.html)
