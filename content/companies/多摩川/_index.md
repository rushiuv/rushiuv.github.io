---
title: "多摩川"
wiki: true
wiki_type: "company"
wiki_rank: 27
seed_count: 8
lastmod: "2026-10-22"
description: "多摩川精机是 1938 年创立于日本饭田的旋变与编码器厂，多圈编码器以 23 位单圈+16 位多圈为主力，并有无电池型号与 Smartsyn 无刷旋变。"
official_url: "https://www.tamagawa-seiki.com/"
wiki_category: "位置测量与编码器"
related_models: []
---

多摩川精机在编码器链上同时占两个位置：旋转变压器的老牌供应商，和伺服电机内置编码器的供应商。对做选型的人，它最有参考价值的是两条并行的事实——同一台伺服既可以配无刷旋变 Smartsyn，也可以配 23 位单圈加 16 位多圈的绝对编码器，两条路线的取舍在官网产品表里能横向看到。

## 1938 年在长野饭田创立，编码器只是伺服元件的一支

公司 1938 年 3 月 3 日设立，资本金 1 亿日元，总部与第一工厂在长野县饭田市小谷 1879，另有第二工厂与松川、八户（青森）等多处厂区。2025 年 11 月 21 日口径：单体员工 665 人、合并 2,680 人；单体销售额 481 亿日元、合并 822 亿日元。董事长兼 CEO 萩本保男，社长松尾忠则。[公司概况](https://www.tamagawa-seiki.com/company/about/)

官网自述的"主要业务"里，伺服元件是成组出现的：编码器、旋转变压器、角速度传感器、陀螺、交流伺服电机与驱动器、步进电机与驱动器、自整角机、LVDT，另有 IMU、自动控制设备与生物试剂。这条结构说明它不是在卖单个传感器，而是在卖"伺服反馈的一整套选项"——这也是它在中国伺服电机配套市场里长期占位的原因。

## 编码器与旋变两条线的公开规格

绝对编码器（多圈）产品表给的是"每圈位数 + 多圈位数"两段式口径，输出码统一为纯二进制，供电 DC+5 V±5%，输出形式为线驱动。下表数值来自官方产品表，属系列口径，逐型号差异要看对应型号行。[多圈绝对编码器](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/)；[单圈绝对编码器](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-singleturn/)

| 系列/型号 | 类型 | 公开分辨率 | 其他公开参数 |
| --- | --- | --- | --- |
| [TS5723N140 / N143](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/) | 多圈绝对，SA35，Ø35 mm | 23 位/圈 + 16 位多圈 | 轴 Ø6 mm、8,000 rpm、−10…+105 °C、50 mA 典型（电池备份时 30 µA）、转动惯量 0.17×10⁻⁶ kg·m² |
| [TS5966N1 / N20](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/) | 多圈绝对，无电池型，SA35 | 23 位/圈 + 16 位多圈 | 轴 Ø5 mm、8,000 rpm、−10…+105 °C、55 mA 典型、免电池 |
| [TS5667N120](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/) | 多圈绝对，SA35 | 17 位/圈 + 16 位多圈 | 轴 Ø6 mm、6,000 rpm、−10…+85 °C、90 mA 典型（电池模式 100 µA）、起动转矩 5.9×10⁻³ N·m |
| [TS5702N40](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/) | 多圈绝对，SA35 | 23 位/圈 + 16 位多圈 | 轴 Ø8 mm、125 mA 典型（电池模式 65 µA） |
| [TS5667N420](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/) | 多圈绝对，SA48 | 27 位/圈 + 16 位多圈 | 外径 Ø46 mm、60 mA 典型（电池模式 100 µA） |
| [TS5720N8□10](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/) | 多圈绝对，SA48 | 17~25 位/圈（按型号）+ 16 位多圈 | 外径 Ø48 mm、50 mA 典型（电池模式 30 µA） |
| [TS5668N20](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-singleturn/) | 单圈绝对，SA35 | 17 位 | 轴 Ø6 mm、6,000 rpm、110 mA 最大 |
| [TS5710N40 / TS5711N40](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-singleturn/) | 单圈绝对，SA35 | 23 位 | 轴 Ø6 mm / Ø8 mm、150 mA 典型、起动转矩 5.9×10⁻³ N·m |
| [Smartsyn 无刷旋变](https://www.tamagawa-seiki.com/products/resolver-synchro/brushless-resolver-smartsyn/) | 无刷旋转变压器 | 模拟量（旋变，不按位数计） | 机座号 06/08/10/15/21/34，最高转速 30,000/40,000/10,000/10,000/10,000/6,000 rpm；空心轴款 21 号 5,000 rpm；振动 20 G、冲击 100 G |

多圈是怎么记的，官方原理页写得很直白：码盘从圆心向外排同心圆狭缝，用二进制码串表示每圈 2 的幂次，多圈型另外记住"转过多少圈"。无电池型号（TS5966 系列）在官网有单独的白皮书 PDF 入口，属于"断电后仍能记圈"的路线，与需要外接电池备份的型号并列。

旋变一侧的差别在原理而不在位数：Smartsyn 无刷旋变不用电刷也不含光学件，官方用"免维护、抗噪声、可长距离传输、耐振动冲击"作为卖点，并注明标准品是 1X（一个电周期对一圈机械转角），2X 以上多极需定制。

## 在编码器链上的位置

多摩川自己设计并制造敏感与解算部分，是典型的"垂直整合型"整机厂：既做旋变的绕组与结构，也做编码器的光学码盘、光电元件与解算电路，还做伺服电机与驱动器。因此**看它的型号能推出它对精度、体积、温度与成本的取舍，不能推出它的光电元件或解算 ASIC 由谁代工**——官网不公布供应链。

决策权在伺服电机厂与机床/机器人整机厂：编码器型号与电机端结构、法兰、轴径绑定，一旦选定电机平台，替换要动机械接口。旋变与编码器的选择则是系统级取舍——旋变耐温耐振、接口简单但需要外部 R/D 解码；绝对编码器上电即知位置、分辨率高但涉及电池或储能元件。

## 公开资料的边界

官网产品表给位数、轴径、转速、温度、电流、转动惯量、起动转矩、质量这些机械与电气参数，给得比多数厂商细。**没有公开**的是精度（±角秒）、重复性、细分误差曲线、输出延时、接口时序细节与报价交期；这些要下具体型号的规格书。多圈编码器的电池寿命、无电池型号的储能元件耐久性也不在公开页。

本页不写"多摩川精度优于某家"这类判断——官网没有公开可比的精度数字，任何这类结论都缺依据。

## 官方资料

- [多摩川精机官网](https://www.tamagawa-seiki.com/)
- [公司概况（沿革、资本、员工、销售额）](https://www.tamagawa-seiki.com/company/about/)
- [多圈绝对编码器产品表](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-multiturn/)
- [单圈绝对编码器产品表](https://www.tamagawa-seiki.com/products/rotaryencoder/absolute-singleturn/)
- [Smartsyn 无刷旋变](https://www.tamagawa-seiki.com/products/resolver-synchro/brushless-resolver-smartsyn/)
- [旋变/自整角机产品总览](https://www.tamagawa-seiki.com/products/resolver-synchro/)
