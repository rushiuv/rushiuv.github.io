---
title: "Sensitec"
wiki: true
wiki_type: "company"
wiki_rank: 65
seed_count: 3
lastmod: "2026-10-22"
description: "Sensitec 是德国 Wetzlar 的磁阻传感器厂，1999 年成立，AA700 系列 AMR 角度芯片做 180° 绝对角度、灵敏度 2.35 mV/度，AL700 系列按磁极距分档。"
official_url: "https://www.sensitec.com/"
wiki_category: "传感器与测量前端"
related_models: []
---

Sensitec 在编码器链上是"磁阻敏感元件"这一层：卖 AMR、TMR、GMR 芯片与配套的磁环、磁栅、编码器模组，不做带壳整机编码器。它对做选型的人最有价值的一点常被忽略——AMR 角度芯片测的是 180° 绝对角度，不是 360°，因为桥信号是磁场的两倍频，方向要靠外部或芯片侧逻辑另判。

## 1999 年在 Lahnau 起家，只做磁阻一条技术线

公司全名 Sensitec GmbH，地址 Schanzenfeldstr. 2, 35578 Wetzlar，电话 +49 6441 5291 0。官网"数字、数据、事实"页写：1999 年在 Wetzlar 近郊的 Lahnau 成立，目标是做面向工业与汽车批量应用的磁阻传感器；现在在 Wetzlar 与 Mainz 两地设点，产品线只围绕磁阻展开。[公司数据页](https://www.sensitec.com/en/about-sensitec/numbers-data-facts/)

它自称全球磁阻传感器技术的领先者，并把"MR-Sensors made in Germany"当成品牌标签。产品结构分三块：传感器芯片（AMR、TMR、GMR）、编码与磁性件（编码器元件、编码器模组、磁极环、线性磁栅）、电流传感器（含无芯与车用）。这条结构说明它不是通用传感器厂，而是把一种物理效应做到晶圆与磁路两端。

## 芯片线：角度、磁极距、弱场三条分支

AMR 角度芯片是 AA700 家族，用两套互成 45° 的惠斯通电桥，旋转磁场给出相位差 90° 的正弦与余弦，但频率是磁场的两倍——所以官方标注的角度量程是"180° 绝对"。三颗型号的定位不同：AA745 为离轴布置优化且有车规认证；AA746 为"大工作距离与低场强"优化；AA747 为轴端测量优化，两套桥是分开的，且也有车规认证。全系带自家 PerfectWave 技术，卖点是谐波低。下表数值来自官方 AMR 芯片页。[AMR 传感器芯片](https://www.sensitec.com/en/products-and-solutions/sensorchips/amr-sensoren/)

| 系列 | 类型 | 公开关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [AA745 / AA746 / AA747](https://www.sensitec.com/en/products-and-solutions/sensorchips/amr-sensoren/) | AMR 角度芯片（FreePitch，自由磁极距） | 180° 绝对角度、灵敏度 2.35 mV/度 | 信号幅度 65 mV @5 V、磁场范围 5~25 kA/m、−40…+125/+150 °C、裸片与 SO8/SIL6/LGA6 封装 |
| [AL795 / AL798 / AL796 / AL797 / AL794 / AL780](https://www.sensitec.com/en/products-and-solutions/sensorchips/amr-sensoren/) | AMR 磁极距固定芯片（FixPitch） | 测量不确定度 3~25 µm | 适配磁极距 0.5 / 1.0 / 2.0 / 2.5 / 2.5（高阻）/ 5.0 mm、信号幅度 60 mV @5 V、磁场 25 kA/m、−40…+125 °C |
| [AFF755 / AFF756](https://www.sensitec.com/en/products-and-solutions/sensorchips/amr-sensoren/) | AMR 弱场传感器（带翻转线圈） | 可测地磁级弱场（小于 20 µG 或 2 nT） | 灵敏度最高 75 mV/mT、线性场范围到 ±800 A/m、失调最大 ±5 mV、翻转电流到 ±400 mA、−40…+125 °C |
| [TMR / GMR 传感器](https://www.sensitec.com/en/) | 磁阻芯片另两条分支 | 页面未给逐型号数值 | 与 AMR 并列的产品分类，按芯片形态供货 |
| [编码器元件与模组、磁极环、线性磁栅](https://www.sensitec.com/en/) | 磁性件与模组 | 页面未给逐型号数值 | 与芯片配套销售，决定气隙与磁极距 |

三支的差别值得记住：AA700 是"自由磁极距"方案，靠磁体直径与气隙设计拿精度；AL700 是"固定磁极距"方案，必须配对应极距的磁栅或磁环，换栅距就得换型号；AFF700 是弱场测量，跟角度无关。这三条是不同生意，不能互相替代。

## 在编码器链上的位置

Sensitec 是纯上游：卖裸片与封装芯片、卖磁路件，不卖带轴承与现场总线的成品。所以看到"某编码器用 AMR"能推的是它对温漂、气隙与成本的取舍；**不能推它具体用 Sensitec 的哪颗片子**，除非对方公开声明——官网不公布客户 BOM。

它的位置决定了它的信息价值在"物理层"：把 AMR 的 180° 特性、两倍频、PerfectWave 的低谐波、FixPitch 对极距的绑定讲清楚，这些是整机厂在选磁体与栅距时必须先算清楚的前提。下游决策权在编码器模组厂与磁环供应商手里：磁极距、气隙与充磁质量一旦定下，芯片型号就被锁死。

## 公开资料的边界

芯片页给灵敏度、信号幅度、磁场范围、温度、封装、测量不确定度（AL700 是 3~25 µm）、角度量程（180° 绝对）。**没有公开**的是角度误差的具体数值（±度）、重复性、带宽、输出延时、噪声密度与温漂曲线，也没有报价与交期；这些要下 datasheet。TMR 与 GMR 两条线在本页只有分类，没有逐型号数值。

另有一处必须注意：180° 绝对角度不等于 360° 绝对编码，做整圈绝对位置时要么加方向判据，要么用两套错位布置，这一点在选型早期就要算进去。

## 官方资料

- [Sensitec 官网](https://www.sensitec.com/en/)
- [公司数字与事实（1999 年成立、Wetzlar/Mainz）](https://www.sensitec.com/en/about-sensitec/numbers-data-facts/)
- [AMR 传感器芯片（AA700/AL700/AFF700）](https://www.sensitec.com/en/products-and-solutions/sensorchips/amr-sensoren/)
- [传感器芯片总览](https://www.sensitec.com/en/products-and-solutions/sensorchips/)
- [磁阻传感技术说明](https://www.sensitec.com/en/about-sensitec/mr-sensorentechnologie/)
- [电流传感器](https://www.sensitec.com/en/products-and-solutions/current-sensors/)
