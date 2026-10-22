---
title: "Allegro"
wiki: true
wiki_type: "company"
wiki_rank: 26
seed_count: 8
lastmod: "2026-10-22"
description: "Allegro MicroSystems 是做磁传感与功率 IC 的美国芯片厂，角度传感器以 CVH 立式霍尔为底，A1333 在 900 G 下标 12 位有效分辨率、AAS33001 在 300 G 下标 12.5 位。"
official_url: "https://www.allegromicro.com/"
wiki_category: "传感器与测量前端"
related_models: []
---

Allegro 在编码器链上是磁传感前端加功率驱动的芯片厂，位置在编码器厂与电机厂的上游。它的角度传感器有一个别家少见的底层结构：CVH（环形立式霍尔）用一圈立式霍尔片旋转扫描磁场矢量，单个敏感点就能测 360°，因此对气隙和偏心不像传统正交霍尔桥那样敏感。读它的资料，先看这个结构，再看它把诊断做到哪一级。

## 三十多年历史，卖的是传感加功率两半

官网自述 1990 年起做传感与功率半导体，1990 年至今超过 30 年；自我定位是"磁传感领域第一"，并给了一组规模口径：约 1,900 项专利、产品组合超过 1,500 个器件、每年出货约 20 亿颗、客户超过 15,000 家，几乎覆盖所有主要整车厂；商业模式是无晶圆厂的轻资产。[关于 Allegro](https://www.allegromicro.com/en/about-allegro)

技术史上它点了几件"第一家"：斩波稳定（chopper stabilization）、离子注入商业化、1 MHz 电流传感器的表面贴装 IC。这些说法是公司自述，但方向可核——斩波稳定确实是霍尔传感器的标配技术路线。市场结构上它服务汽车、工业、消费三块，重点应用写成 xEV 电驱、ADAS 安全系统、AI 数据中心、机器人与能源基础设施。[我们做什么](https://www.allegromicro.com/en/about-allegro/what-we-do)

## 角度传感器产品线：CVH 为底，诊断和安全做到芯片级

官网把位置传感器分成一维线性、二维电机位置、三维多轴三组；角度传感器属于二维那一组，主力是 A13xx 与 AAS33xxx 两条命名。下表数值取自各型号页的公开参数。[二维电机位置传感器](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d)

| 型号 | 类型 | 公开分辨率/精度 | 其他公开参数 |
| --- | --- | --- | --- |
| [A1333](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d/a1333) | 0–360° 非接触角度传感器，带诊断 | 900 G 磁场下 12 位有效分辨率 | CVH 单通道、UVW/ABI/SPI/PWM 四种输出、SPI 10 MHz、4 位 CRC、ECC、片上 EEPROM、4.0~16.5 V、−40…+150 °C、堆叠双 die 版本 |
| [AAS33001](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d/aas33001) | 0–360° 角度传感器，安全型 | 300 G 磁场下 12.5 位有效分辨率（更高场强可更高） | CVH、32 段线性化、按 ISO 26262 SEooC 开发、3.7~18 V（绝对最大 28 V）、−40…+150 °C |
| [A1335](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d/a1335) | 0–360° 非接触角度传感器 | 12 位、刷新率 32 µs | CVH 支持轴上与离轴、I2C/SPI/SENT 三种数字接口、片上谐波与分段线性化、EEPROM 带 ECC |
| [一维线性霍尔（A13xx 线性族）](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/linear-sensors-1d) | 线性位置传感 | 页面按型号分档 | 面向行程与位置检测，与角度族共用工艺平台 |
| [三维多轴（A31301 等）](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/multi-axis-linear-and-angle-sensors-3d) | 3D 磁场传感 | 页面按型号分档 | 可测三轴分量，用于摇杆、折叠角与离轴场合 |

A1333 这一页最能看出它的打法：把"诊断"当卖点写在前排——逻辑内建自检（LBIST）、信号通路诊断、看门狗、SPI 上 4 位 CRC、单比特纠错加双比特检错；同时给堆叠双 die 版本，用来改善两颗 die 之间的匹配，官方明确说这比并排双 die 更能抗磁体偏心。目标应用列的是电动助力转向、电液、变速箱、座舱电机、机油泵——都是对功能安全和温区要求最硬的地方。

## 在编码器链上的位置

它在链条上是"敏感元件 + 模拟前端 + 诊断"的提供者：编码器厂买去做模块与整机，电机厂直接把芯片贴到电机端。所以能推的是它对精度、温区、诊断覆盖与成本的取舍；**不能推的是任何编码器整机的内部选型**——官网不公布客户 BOM。

决策权分两处：汽车项目由 Tier1 与主机厂按 ISO 26262 等级与 AEC-Q100 要求倒推型号；工业与机器人项目由编码器厂或关节设计方按接口（ABI/UVW/SPI/PWM）、磁体尺寸与气隙预算选。它在这条链上的对手是 TDK-Micronas（3D HAL）、Melexis、AKM（霍尔角度）、Sensitec 与多维科技（磁阻路线）。

## 公开资料的边界

型号页给分辨率、磁场条件、供电、温区、输出格式、诊断项与安全开发方法；**没有公开**的是逐型号的 INL 曲线、噪声密度、带宽与输出延时、温漂系数、气隙公差窗口、磁体尺寸建议的完整表格，也没有报价与交期。要拿到这些必须下 datasheet 与安全手册（safety manual）。

一处容易误读：所有角度分辨率都绑定了磁场强度（900 G 下的 12 位、300 G 下的 12.5 位），换磁体或换气隙数字就变；所以"12 位"不是无条件指标。

## 官方资料

- [Allegro 官网](https://www.allegromicro.com/en)
- [关于 Allegro（规模、专利、商业模式）](https://www.allegromicro.com/en/about-allegro)
- [业务与市场结构](https://www.allegromicro.com/en/about-allegro/what-we-do)
- [二维电机位置传感器目录](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d)
- [A1333 型号页](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d/a1333)
- [AAS33001 型号页](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d/aas33001)
- [A1335 型号页](https://www.allegromicro.com/en/products/sense/linear-and-angular-position/motor-position-sensors-2d/a1335)
- [角度误差来源技术文档](https://www.allegromicro.com/en/design-support/design-and-development/angle-error-contributions)
