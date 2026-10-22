---
title: "NXP"
wiki: true
wiki_type: "company"
wiki_rank: 92
seed_count: 2
lastmod: "2026-10-22"
description: "NXP（恩智浦）：2006 年从飞利浦分拆，AMR 角度传感器 KMZ60 给静态场 ±0.1°、磁场转速 0~25000 转每分。"
official_url: "https://www.nxp.com/company/about-nxp:ABOUT-NXP"
wiki_category: "芯片与信号链"
related_models: ["KMZ60"]
---

NXP 在编码器链上的位置是"车规磁角度前端 + 汽车控制器与接口"。它的 AMR 角度传感器 KMZ 系列曾是 BLDC 换相与 EPS 转角测量里的常见件，但 KMZ60 在官网已标注 Archived（停产/归档），这条信息对选型比任何参数都重要——参数再好，料号生命周期结束了就得换方案。

## 公司与品牌

NXP Semiconductors N.V.（中文常称恩智浦），2006 年从飞利浦分拆成立，总部在荷兰埃因霍温 High Tech Campus，2010 年在纳斯达克上市，代码 NXPI。维基百科条目给出的规模：约 34000 名员工、业务覆盖 30 多个国家、2024 年营收 126.1 亿美元；NXP 官网公司页自述"Present in 30+ countries"。NFC 是 NXP 与索尼共同发明的技术。

公司名 NXP 是 Next eXPerience 的缩写。产品结构上，汽车（MCU、驱动、接口、雷达）与工业物联网是两条主线，传感器只是其中一块，磁角度传感更只是这一块里的一条老产品线。[NXP 公司条目](https://en.wikipedia.org/wiki/NXP_Semiconductors)

## 角度传感产品线与公开规格

公开可核对的 AMR 角度型号在官网是 KMZ60，数据手册 Rev.2（2014-02-07）。它的架构是"一颗封装里两片 die"：AMR 角度传感片 + 仪表放大片。

| 型号 | 类型 | 公开指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [KMZ60](https://www.nxp.com/products/KMZ60) | AMR 角度传感器 + 集成仪表放大器 | 静态场角误差 ±0.1°、磁场旋转频率 0~25000 r/min、外部磁场 ≥25 kA/m | VCC 2.7~5.5 V、cos/sin 双通道模拟输出 + 温度参考输出、幅值温补可开关、Power-down 模式、Tamb −40~150 °C、SO8（SOT96-1，4.9×3.9×1.75 mm）、车规认证 |

三点要看清。**它输出的是模拟 sin/cos 加温度参考，不是数字角**：后面的 ADC 与角度解算在客户自己的 MCU 里，这也是它与现代集成式磁编芯片最大的差别。**±0.1° 是静态场条件下的角误差**，手册同时给的是 25 kA/m 的外部磁场下限——磁场弱了或磁铁远了，这个数不成立。**料号状态是 Archived**：官网产品页明确标注，替代方案需向 NXP 确认。[KMZ60 产品页](https://www.nxp.com/products/KMZ60)；[数据手册](https://www.nxp.com/docs/en/data-sheet/KMZ60.pdf)

手册框图里还有几件客户画板时必须对上的事：cos 与 sin 两路各走两级增益约 6 与 7 的缓冲，输出以 VCC/2 为共模；片上带断线检测与温度传感器，幅值温补可由 TCC_EN 脚开关；输出串阻 50~150 Ω、外部负载不低于 5 kΩ、外部去耦电容不低于 100 nF。这些不是选型参数，但决定了第二颗料能不能直接替上去。

与现在流行的集成式磁编相比，KMZ60 把解算留在客户的 MCU 里：好处是滤波、标定节拍与故障判据都能自己定，便于过安全评审；坏处是分辨率、延时与温漂都压在自己的 ADC 与算法上，芯片手册给不了整机指标。

手册给的是器件级指标：±0.1°（静态场）、25 kA/m 最小外部场、0~25000 r/min 磁场旋转频率、−40~150 °C 环境温度。它不含磁铁偏心、安装倾斜与 ADC 量化带来的误差，整机精度必须自己算。

## 在编码器链上的位置

NXP 在这个位置卖的是"前端 + 车规资质 + 汽车前装渠道"：KMZ60 面向 BLDC 转子位置检测、EPS 转角、雨刮位置与一般非接触角测量；客户是电机驱动厂、Tier1 与整车电子供应商。它不卖编码器整机，也不卖码盘与磁铁。

能推的是系统分工：用 KMZ60 的方案里，角度解算与标定落在客户的 MCU 上，NXP 的贡献是"干净的双通道 sin/cos + 温度信号 + 车规认证"。不能推断的：这颗料现在还有多少在产（Archived 状态说明官方已不做主推）、替代型号是哪一个（官网未在本页给出）、以及任何客户的 BOM。

## 官方资料

- [NXP 公司概况](https://www.nxp.com/company/about-nxp:ABOUT-NXP)
- [KMZ60 产品页（英文）](https://www.nxp.com/products/KMZ60)
- [KMZ60 产品页（中文）](https://www.nxp.com.cn/products/KMZ60)
- [KMZ60 数据手册](https://www.nxp.com/docs/en/data-sheet/KMZ60.pdf)
- [SOT96-1 封装图](https://www.nxp.com/docs/en/package-information/SOT96-1.pdf)
- [NXP 公司条目（沿革与规模）](https://en.wikipedia.org/wiki/NXP_Semiconductors)
