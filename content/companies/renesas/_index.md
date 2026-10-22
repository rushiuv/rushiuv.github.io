---
title: "Renesas"
wiki: true
wiki_type: "company"
wiki_rank: 23
seed_count: 9
lastmod: "2026-10-22"
description: "瑞萨电子：东京的嵌入式半导体厂，电感式位置传感器 IPS2550（车规 ASIL-C(D)、600 krpm 电气转速）与 IPS2200 以 PCB 线圈加金属靶输出正余弦。"
official_url: "https://www.renesas.com/"
wiki_category: "芯片与信号链"
related_models: []
---

瑞萨在这条链上卖的是"感应芯片加线圈设计工具"，不卖磁体、也不卖码盘：它把客户自制的 PCB 印刷线圈与一片金属靶之间的涡流变化，解成一对正余弦或增量脉冲。读它的资料最该看两处：电感式位置传感器分类页讲清了端轴、侧轴、直线与弧形四种装法怎么选线圈，IPS2550 与 IPS2200 的参数页则给出车规等级、电气转速与传播延迟这三档硬指标。

## 从两条半导体业务线合出来的公司

Renesas Electronics Corporation，总部东京，官网自述"嵌入式半导体方案商"，团队超过 21,000 人、分布在 30 多个国家。法律沿革是两条线合并：2002 年 11 月 NEC 把半导体业务拆出为 NEC Electronics；2003 年 4 月日立与三菱电机的非 DRAM 半导体业务合成 Renesas Technology；两家 2009 年 9 月宣布合并，2010 年 4 月 1 日以 NEC Electronics 为存续公司改名瑞萨电子。此后靠并购补产品面，公开记录里包括 Intersil、IDT、Dialog 与 Altium。中文常叫"瑞萨"或"瑞萨电子"。沿革与并购清单取自维基百科 Renesas Electronics 条目（该条目引用官网 Corporate Outline），员工数采用官网 About 页原话。[官网 About](https://www.renesas.com/en/about)；[维基条目](https://en.wikipedia.org/wiki/Renesas_Electronics)

## 电感式位置传感器只有两颗公开在售，靠线圈工具补差异

下表数值全部抄自系列页原文，是"这一族大概在什么档位"，不是选型保证：输出电压口径、延迟与带宽的对应关系还要看 datasheet。

| 系列 | 类型 | 公开关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [IPS2550](https://www.renesas.com/en/products/ips2550) | 电感式，车规 | 正余弦输出（单端或差分）；电气转速上限 600,000 rpm；传播延迟 <5 µs | AEC-Q100 Grade 0；ISO 26262 到 ASIL-C (D) single；−40…+160 °C；3.3 V 或 5 V ±10%；I²C 编程；16-TSSOP 带散热焊盘；片内 AGC |
| [IPS2200](https://www.renesas.com/en/products/ips2200) | 电感式，工业 | 正余弦输出（单端或差分）；电气转速上限 250,000 rpm；传播延迟可编程 <10 µs | −40…+125 °C；3.3 V 或 5 V ±10%；AB 增量脉冲输出；I²C 或 SPI 编程；16-TSSOP；官网标注 Obsolete |
| [IPS 分类页](https://www.renesas.com/en/products/sensor-products/inductive-position-sensors) | 技术方向整体 | 官方称线圈与靶的极对数配合下可达 up to 0.01° | 端轴 on-axis、侧轴与穿轴 off-axis、直线与弧形；绝对或增量；提供线圈优化工具 |

三条必须分开看：芯片本身只给正余弦或增量脉冲，机械角由后端 ADC 加解算完成；"0.01°"是分类页对整条技术路线的宣传上限，原文是 up to，随线圈、靶与极对数变化，不是任何一颗料的保证值；IPS2200 页面已标 Obsolete，新设计要先确认替代型号。

## 在编码器链上的位置

Renesas 卖芯片外加一个线圈仿真工具（Inductive Position Sensor Coil Optimizer，可下载 Gerber 供打样），买的是 PCB 与金属靶，而这两样由客户自己做。所以它在链上属于"把机械公差换成设计规则"的一层：接收线圈图形决定谐波预算，靶的扇区形状决定线性度，芯片只负责激励稳定、增益与相位可调。这也解释了它为什么要把 AGC 和增益/偏移补偿做进片内——不做，客户光靠线圈调不出可用信号。

能推理的是它对成本与可靠性的取舍：去掉磁体、去掉码盘与光源，换来抗杂散磁场和更低的物料成本，代价是必须有一块精度可控的 PCB 与一片空间够的靶。**不能推理的是哪家电机厂、机器人厂或 Tier1 在设计里用了它**——官网不公布设计导入，也不公布 BOM。

## 公开资料的边界

官网系列页给的是上限值：转速、传播延迟、温度范围、车规与功能安全等级、封装。**没有公开**逐颗的 INL 或角秒级精度、噪声密度、延迟与带宽的对应曲线、不同线圈-靶组合下的实测误差分布；这些要下 datasheet 与应用笔记。完整型号表放在 JS 渲染的产品树里，本次只取到 IPS2200 与 IPS2550 两颗（其中一颗已标 Obsolete），其余型号名不在此页出现。报价与交期不公开。跨品牌比精度时，先把"芯片输出位数""整机 INL""重复性"三件事对齐，再谈数字。

## 官方资料

- [Renesas 官网](https://www.renesas.com/)
- [About Renesas](https://www.renesas.com/en/about)
- [Corporate Outline / Who We Are](https://www.renesas.com/en/about/profile/who-we-are)
- [电感式位置传感器分类页](https://www.renesas.com/en/products/sensor-products/inductive-position-sensors)
- [IPS2550 产品页](https://www.renesas.com/en/products/ips2550)
- [IPS2200 产品页](https://www.renesas.com/en/products/ips2200)
- [维基百科 Renesas Electronics（沿革与并购）](https://en.wikipedia.org/wiki/Renesas_Electronics)
- [东京证券交易所 Prime 市场股本信息](https://www.renesas.com/about/investor-relations/stock/basic)
