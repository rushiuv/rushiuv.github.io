---
title: "ADI"
wiki: true
wiki_type: "company"
wiki_rank: 25
seed_count: 8
lastmod: "2026-10-22"
description: "ADI（亚德诺）：ADMT4000 做 46 圈真上电多圈、角度精度 ±0.25°，AD2S1210 是 16 位旋变数字转换器。"
official_url: "https://www.analog.com/en/products/admt4000.html"
wiki_category: "芯片与信号链"
related_models: ["ADMT4000"]
---

ADI 在编码器链上占两格：一格是把多圈与角度做进一颗的磁传感（ADMT4000），一格是旋变路线（AD2S1210 / AD2S83 旋变数字转换器、AD2S99 激励振荡器、ADA4571 AMR 角度前端）。前者回答"掉电后圈数怎么记住"，后者回答"不用光学码盘怎么把角度读出来、怎么给出激励"。读 ADI 的资料，价值几乎全在数据手册：器件级指标写得比任何系列页都细。

## 公司与品牌

Analog Devices, Inc.（ADI），中文常称亚德诺半导体，总部在美国马萨诸塞州 Wilmington（One Analog Way, Wilmington, MA 01887，见数据手册版权页）。本次取到的官方页面只有公司概览与六份数据手册正文，成立年份与并购年表未出现在取到的内容里，本页不逐年罗列，也不引用未核对的数字。

本页只覆盖与位置测量直接相关的几条产品线：磁多圈、旋变数字转换、AMR 角度前端与旋变激励。ADI 的转换器、电源、接口、射频等大类与编码器链关系较远，不在此展开。

## 角度与多圈产品线的公开规格

六个型号代表三条技术路线：GMR 计圈加 AMR 测角、旋变数字转换、AMR 模拟前端。参数全部取自各自数据手册的规格表或首页特性栏。

| 型号 | 类型 | 公开指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [ADMT4000](https://www.analog.com/media/en/technical-documentation/data-sheets/ADMT4000.pdf) | 真上电多圈磁传感（GMR 计圈 + GMR 象限 + AMR 测角） | 0~46 圈、角度精度 ±0.25° | SPI（VDRIVE 1.7~5 V）、结温 −40~150 °C、绝对范围 0~16560°、12 位 SAR ADC、片上 1/2/3 次谐波校准、24 引脚封装 |
| [AD2S1210](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S1210.pdf) | 旋变数字转换器（R/D） | 10/12/14/16 位可选、角精度 ±2.5′+1 LSB（B/D 级）、最大跟踪 3125 rps | 内置可编程正弦激励、输入 3.15 Vpp ±27%、2~20 kHz、II 型伺服环、可编程故障阈值、编码器仿真输出 |
| [AD2S83](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S83.pdf) | 可变分辨率旋变数字转换器 | 10/12/14/16 位由用户设定、10 位时最大跟踪 1040 rps（约 62400 rpm） | 参考频率 0~20 kHz、44 引脚 PLCC、并行三态输出可配 8/16 位总线、模拟速度输出、带宽与跟踪率由外部阻容决定 |
| [AD2S1205](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S1205.pdf) | 12 位 R/D（含参考振荡器） | 12 位、精度 ±11 角分、最大跟踪 1250 rps | 并行与串行数据口、内置参考振荡器、II 型跟踪环、故障检测与编码器仿真输出 |
| [AD2S99](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S99.pdf) | 可编程正弦激励振荡器 | 激励频率 2 / 5 / 10 / 20 kHz 可选 | 同步参考输出（3 Vpp 方波）与失信号指示、20 引脚 PLCC、−40~85 °C、可驱动旋变与 LVDT/RVDT |
| [ADA4571](https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4571.pdf) | AMR 角度传感器 + 仪表放大器 | 180° 测量范围、最大角误差 0.5°（单点校准后 ±0.7°）、动态误差 ±0.1~0.5° | 双惠斯通电桥互成 45°、增益 G=40、2.7~5.5 V、−40~150 °C、SOIC-8、磁场旋转频率上限 50000 rpm |

ADMT4000 的多圈机制要单独说：手册写明它靠一条铁磁纳米线做的螺旋，磁畴壁沿螺旋传播，GMR 叠层测出局部电阻变化来定位畴壁，从而解码转数。它既不是齿轮也不是电池，掉电时物理状态还在。但手册同时写明一条硬边界——**只有 0~46 圈区间里"真上电"能力成立**，掉电期间转过这个范围，上电后角度可能错且 FAULT 位不一定置起；AMR 推算出的 −9~54 圈只用于系统校准，不应作为正常工作范围。

旋变那一路的组合关系也值得记清：AD2S99 负责给旋变提供激励与同步参考，AD2S83 或 AD2S1210 负责把 sin/cos 解成数字角，ADA4571 则是完全不同的路线——AMR 桥直接测磁场方向，输出模拟 sin/cos 交给下游 ADC。同一个系统里用哪一条，取决于电机端装的是旋变、磁铁还是光学码盘。[ADMT4000 数据手册](https://www.analog.com/media/en/technical-documentation/data-sheets/ADMT4000.pdf)

## 在编码器链上的位置

ADI 卖芯片，客户是编码器厂、伺服驱动厂与汽车 Tier1。几个型号的用法不同：ADMT4000 要配外部磁铁并解决同轴，输出直接是绝对多圈位置；ADA4571 只给模拟 sin/cos，后面必须接 ADC 或插值器，它在链条里更靠前端；AD2S1210 与 AD2S83 的对偶是旋变——用它们做系统时，电机端的"传感器"其实是旋变而不是编码器。

不能推断的：ADI 是否给某家整机编码器厂供货（官网不公布客户）、ADMT4000 的 GMR 螺旋膜在哪条工艺线上做（手册只讲结构不讲代工）；也不要把 46 圈当成所有多圈需求的解——超过这个范围就要另想方案。

## 公开资料的边界

手册给的是器件级指标，不是整机指标：ADMT4000 的 ±0.25°、ADA4571 的 0.5°、AD2S1210 的 ±2.5′、AD2S1205 的 ±11′ 都不含装配偏心、磁铁不均匀、线圈不对称带来的误差。分辨率与精度必须分开看：ADMT4000 用 12 位 SAR ADC，手册没给等效角度分辨率；ADA4571 是模拟输出，位数由下游 ADC 决定。

没有公开的：报价、交期、样片与评估板政策；ADMT4000 的长期漂移与温漂曲线要给整段手册；各型号的抗外磁场指标需查对应章节，本页不填未取到的数字。

## 官方资料

- [公司概览](https://www.analog.com/en/about-adi.html)
- [ADMT4000 数据手册（真上电多圈）](https://www.analog.com/media/en/technical-documentation/data-sheets/ADMT4000.pdf)
- [AD2S1210 数据手册（16 位旋变数字转换）](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S1210.pdf)
- [AD2S83 数据手册（可变分辨率 R/D）](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S83.pdf)
- [AD2S1205 数据手册（12 位 R/D 含振荡器）](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S1205.pdf)
- [AD2S99 数据手册（可编程激励振荡器）](https://www.analog.com/media/en/technical-documentation/data-sheets/AD2S99.pdf)
- [ADA4571 数据手册（AMR 角度）](https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4571.pdf)
