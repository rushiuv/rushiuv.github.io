---
title: "RLS"
wiki: true
wiki_type: "company"
wiki_rank: 43
seed_count: 5
lastmod: "2026-10-22"
description: "RLS 是斯洛文尼亚的磁性编码器厂、Renishaw 持股 50% 的关联公司，同时卖 AksIM 系列读头与 OnAxis 磁传感芯片，口径从 8 位芯片到 21 位大环。"
official_url: "https://www.rls.si/eng/"
wiki_category: "位置测量与编码器"
related_models: []
---

RLS 是编码器链上少见的"芯片与读头同一屋檐下"：它既卖 OnAxis 系列磁角度芯片（8~13 位），也卖 AksIM、Orbis、RM 这些读头与成套编码器（最高 21 位）。读它的资料最有价值的不是分辨率表，而是它公开承认的技术边界——哪些参数是环与读头一起决定的，哪些要靠系统级标定。

## 斯洛文尼亚起家，Renishaw 持股一半

公司全名 RLS Merilna tehnika d. o. o.，1989 年 12 月在卢布尔雅那成立，RLS 三个字母取自 "Rotary and Linear Motion Sensors"。官网自述 2000 年起把方向收紧到磁性编码器与元件，现在总部在 Komenda 的 Žeje 工业区（Pod vrbami 2, SI-1218 Komenda）。[公司信息](https://www.rls.si/eng/about-us)

股权关系它写得很直接：RLS 是 Renishaw 的关联公司，Renishaw 持有 50% 股份，并通过自己的全球网络销售 RLS 的磁性编码器；反向地，RLS 负责 Renishaw 产品在斯洛文尼亚、克罗地亚、波黑、塞尔维亚、北马其顿的销售。同页还写了一段对做传感器的人有用的历史：它早年与高校合作开发了"测量正上方直径充磁磁体转角"的集成霍尔 ASIC——这就是后来 OnAxis 芯片线的来源。2020 年 10 月 RLS 加入 Mag-ID 联盟，任务之一是验证 TMR 阵列做磁条码与磁栅读取的可行性，项目由欧盟 Horizon 2020 资助（协议号 870017）。

## 磁编码器产品线的公开规格

官网把产品按"磁环 + 读头"的离轴（off-axis）与通轴（through-hole）两类组织。下表数值来自绝对式模块页与芯片页，是族级口径；同一族里分辨率与环径的组合要看具体订货号。[绝对式模块目录](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular)；[磁传感芯片](https://www.rls.si/eng/products/components/ic-am)

| 系列 | 类型 | 公开分辨率/精度 | 其他公开参数 |
| --- | --- | --- | --- |
| [AksIM-2](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 离轴绝对式读头模块 | 最高 20 位 | 环外径 29/39/49/53/64/80 mm、最高 10,000 rpm、典型 130 mA（最大 150 mA） |
| [AksIM-2 Redundant](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 双通道绝对式 | 最高 20 位 | 双路 135 mA、BiSS-C 与 RS422 |
| [AksIM-4](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 离轴绝对式 | 最高 20 位，系统精度 ±0.005° | −40…+105 °C |
| [AksIM-4 Big Rings](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 大直径离轴绝对式 | 20 位与 21 位 | 环外径 115 mm、150 mm、−40…+105 °C |
| [AksIM-4 Dual Concentric](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 同心双编码（输入+输出） | 各 19 位，系统精度 ±0.006° | −40…+105 °C |
| [AksIM-4 HIPERFACE DSL](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 离轴绝对式，DSL 接口 | 最高 20 位，系统精度 ±0.005° | 环外径 53 mm、80 mm、−40…+105 °C |
| [Orbis](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 通轴磁编码模块 | 最高 14 位 | ABZ、BiSS-C、PWM、sin/cos、SPI、SSI、UART、UVW 八种输出 |
| [RTB20](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 20 mm 圆形模块 | 最高 18 位 | 最高 30,000 rpm、−40…+105 °C（受连接器限制） |
| [RM08](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular) | 8 mm 微型 | 最高 12 位，精度 ±0.3° | 最高 30,000 rpm |
| [AM8192B / AM4096](https://www.rls.si/eng/products/components/ic-am) | OnAxis 磁角度芯片 | 13 位 / 12 位（可编程） | 8~13 位（128~8192 CPR）、SSI/并行/增量/sin-cos/线性电压输出、内置 EEPROM |

芯片线上还有 AM256（8 位）与 AM512B（9 位）。官网对芯片的定位写得明确：OnAxis 用于 360° 非接触角度测量，内置 EEPROM 以便现场改参数；公司同时提供芯片倒装与 COB 组装服务，也就是把裸片直接做到客户板上。

## 在编码器链上的位置

RLS 同时占两个位置：芯片端卖磁传感 IC，整机端卖读头与成套编码器，中间还自己做磁环与磁栅。这条结构决定了它的公开话术：**系统精度（±0.005°、±0.006°）只在完整编码器上给，芯片页只给位数与输出格式**，因为误差里包含磁环充磁、偏心与安装气隙，单颗芯片负责不了。

它买什么，官网只在联盟项目里间接透露：Mag-ID 的活是验证 TMR 阵列与"基于霍尔阵列 ASIC 的磁相机"读磁条码，说明它在评估 TMR 这条新敏感层，但**没有公开任何一款量产读头用的是谁的 TMR 裸片**，也不能反过来把它的 20 位读头当作某家 TMR 芯片的出货证据。下游决策权在电机厂与机器人关节设计方：环径与通轴孔径一旦定下，读头型号基本被锁死。

## 公开资料的边界

官网给的是族级参数：分辨率上限、环径、转速、供电电流、工作温度、接口清单，以及部分系列的系统精度（±0.005°/±0.006°/±0.3°）。**没有公开**的是逐型号的重复性、温度系数曲线、输出延时与抖动、气隙公差窗口，也没有报价与交期。芯片页不写 INL、噪声密度、带宽这类模拟指标，要拿 datasheet 才有。

本页因此不写"RLS 精度优于某家"这类结论；比较时先确认对方给的是芯片级 INL 还是系统级 ±度。

## 官方资料

- [RLS 官网](https://www.rls.si/eng/)
- [公司与股权信息（Renishaw 50%）](https://www.rls.si/eng/about-us)
- [绝对式旋转磁编码器目录](https://www.rls.si/eng/products/rotary-magnetic-encoders/absolute-encoders/modular)
- [OnAxis 磁传感芯片](https://www.rls.si/eng/products/components/ic-am)
- [增量式旋转磁编码器目录](https://www.rls.si/eng/products/rotary-magnetic-encoders/incremental-encoders)
- [直线磁编码器目录](https://www.rls.si/eng/products/linear-magnetic-encoders)
- [编码器手册](https://www.rls.si/eng/encoder-handbook)
