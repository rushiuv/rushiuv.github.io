---
title: "AKM"
wiki: true
wiki_type: "company"
wiki_rank: 112
seed_count: 1
lastmod: "2026-10-22"
description: "AKM（旭化成微电子）是东京的混合信号芯片厂，角度传感器以霍尔加信号处理为主，AK7440 官方标 ±20 角秒、AK7455 为 14 位、±0.1° 且支持离轴。"
official_url: "https://www.akm.com/"
wiki_category: "传感器与测量前端"
related_models: []
---

AKM 在编码器链上属于"磁传感前端"这一层：卖的是霍尔与磁阻敏感元件加信号处理的芯片，不是编码器整机。它对做编码器的人最有参考价值的是两条路线同时存在——用霍尔做角度但把误差校正做进芯片（AK7440 标 ±20 角秒），以及用 14 位分辨率换离轴安装自由度（AK7455 标 ±0.1°）。

## 从旭化成的 IC 合资公司做到独立法人

AKM 全名 Asahi Kasei Microdevices Corporation，总部在东京千代田区有乐町 1-1-2 日比谷三井大厦。官网沿革写得直接：1983 年旭化成与美国 AMI 以 50:50 合资设立 Asahi Microsystems，由此进入 IC 业务；此后在美国圣何塞设 AKM Semiconductor Inc.，在中国上海设本地子公司。[公司概况](https://www.akm.com/global/en/about-us/company-profile/)

它在集团里的定位是"混合信号器件"：产品线从磁传感器（霍尔、三轴磁、角度、半导体磁阻元件、电子罗盘）到电流传感器、气体传感器、音频器件与 DSP，再到毫米波雷达、蓝牙低功耗、能量收集。对编码器读者有用的只有前两块，但这条宽度说明了它的能力结构——敏感元件与模拟前端、ADC、DSP 在同一个体系里，所以它做角度传感时天然带补偿算法。

## 角度传感产品线：霍尔为底，误差校正做进芯片

官网把角度传感器单独成节，产品页给两条主张：可在恶劣环境使用；即使安装有偏心也能保持高精度，并且内置角度误差校正功能；同时支持空心轴电机的离轴（off-axis）安装，绝对角度检测免去回零动作。下表数值取自官方产品介绍页。[旋转角度传感器](https://www.akm.com/global/en/products/rotation-angle-sensor/)

| 系列 | 类型 | 公开分辨率/精度 | 其他公开参数 |
| --- | --- | --- | --- |
| [AK7440](https://www.akm.com/global/en/products/rotation-angle-sensor/) | 霍尔角度传感器，面向 40 mm 法兰电机 | 角度精度 ±20 角秒 | 内置修正安装导致角度误差的算法，按 40 mm 法兰电机优化 |
| [AK7455](https://www.akm.com/global/en/products/rotation-angle-sensor/) | 霍尔角度传感器，轴端（shaft-end）与离轴两用 | 14 位，精度 ±0.1° | 官方卖点是"简单结构即达 ±0.1°"，可离轴安装 |
| [AK7455B](https://www.akm.com/global/en/products/rotation-angle-sensor/) | 离轴版本 | 14 位 | 与 AK7455 同族，定位离轴安装 |
| [半导体磁阻元件（SMR）](https://www.akm.com/global/en/) | 磁阻敏感元件 | 页面未给位数 | 与霍尔并列的另一条敏感层，按元件形态供货 |
| [霍尔 / 三轴磁 / 电子罗盘](https://www.akm.com/global/en/) | 磁传感芯片 | 页面未给位数 | 用于位置、开合角度与地磁定向，属同一磁传感板块 |

两条路线在同一个产品页上并排，本身就说明了一件事：**精度是靠校正算法换来的，不是靠敏感元件天生更准**。AK7440 用"±20 角秒"打 40 mm 法兰电机，代价是绑定法兰尺寸与磁路；AK7455 用"14 位、±0.1°"换离轴安装的自由度。选型时这两条不能只比数字，还要看磁体尺寸与偏心预算。

官网角度传感器页给的是产品定位与精度主张（±20 角秒、14 位、±0.1°），并明确写了"内置校正算法""支持离轴"。另外要注意口径：±20 角秒是 AK7440 在指定法兰与磁体条件下的官方主张，不等于全温区保证值；±0.1° 与 14 位分别对应精度与分辨率，不能互相换算。

## 在编码器链上的位置

AKM 是芯片厂，位置在编码器厂的上游：它卖敏感元件加前端，编码器厂拿去做成带壳体、轴承、现场总线的成品。所以看到"某编码器用 AKM"这种说法，只有在对方公开声明时才算数；**不能从 AKM 的产品目录反推某家编码器的 BOM**，也不能从编码器型号推断里面是 AKM。

它自己公开的边界也很清楚：不做码盘、不做整机、不做现场总线。下游决策权在两类客户手里——电机厂（把角度芯片直接贴到电机端，按法兰与磁体设计）与编码器厂（把芯片做成模块）。它在这条链上的对手是同做霍尔角度方案的 Melexis、TDK-Micronas、Allegro，以及做磁阻的 Sensitec、多维科技一类。

## 官方资料

- [AKM 官网](https://www.akm.com/global/en/)
- [旋转角度传感器产品页](https://www.akm.com/global/en/products/rotation-angle-sensor/)
- [AKM 与其他厂商的差异说明](https://www.akm.com/global/en/products/rotation-angle-sensor/what-makes-akm-different/)
- [角度检测技术教程（含角度误差与离轴配置）](https://www.akm.com/global/en/products/rotation-angle-sensor/tutorial/)
- [公司概况与沿革](https://www.akm.com/global/en/about-us/company-profile/)
- [AKM 新闻](https://www.akm.com/global/en/about-us/news/)
