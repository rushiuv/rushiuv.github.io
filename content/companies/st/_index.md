---
title: "ST"
wiki: true
wiki_type: "company"
wiki_rank: 66
seed_count: 3
lastmod: "2026-10-22"
description: "意法半导体：1987 年成立、总部日内瓦近郊，STM32F407 等定时器带正交编码输入，编码器链上站在主控与驱动一侧而非敏感元件。"
official_url: "https://www.st.com/"
wiki_category: "芯片与信号链"
related_models: ["STM32"]
---

ST 在这条链上不在敏感元件那一头。它的位置是主控与驱动：MCU 的定时器直接吃正交编码信号，电机驱动与功率器件在编码器外围，MEMS 目录里是惯性、磁力计与测距，而不是旋转角度芯片。读它的资料最该看两处：产品页里那句"quadrature (incremental) encoder input"到底挂在哪些定时器上，以及传感器目录里有没有面向伺服的角度 IC。

## 1987 年两家国营半导体合出来的公司

STMicroelectronics NV，注册在荷兰，总部在瑞士 Plan-les-Ouates（日内瓦近郊）。1987 年由意大利 SGS Microelettronica 与法国 Thomson Semiconducteurs 合并成立，1994 年在巴黎与纽约上市，四年后在意大利挂牌。中文常叫"意法半导体"。产品面以 STM8/STM32 微控制器、模拟、功率与 MEMS 著称，公开记录里 2024 年员工数 49,602 人。上述沿革与人数取自维基百科 STMicroelectronics 条目（引用公司 2024 年 20-F 年报）；官网首页可核对现行产品分类。[官网](https://www.st.com/)；[维基条目](https://en.wikipedia.org/wiki/STMicroelectronics)

## 编码器接口在主控侧，定时器的正交输入就是入口

| 对象 | 类型 | 公开关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [STM32F407VG](https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html) | MCU | 产品页原文：定时器"each with up to 4 IC/OC/PWM or pulse counter and quadrature (incremental) encoder input" | Cortex-M4 带 FPU 与 DSP 指令，168 MHz，1 MB Flash，192 KB SRAM，3 个 12 位 ADC，最多 17 个定时器 |
| [STM32 系列目录](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html) | MCU 产品族 | 页面标题即 STM32 Microcontrollers (MCUs)，按 Cortex-M 核分系列 | 编码器接口的具体数量与分辨率随系列与封装变化，要按型号查 |
| [MEMS and Sensors 目录](https://www.st.com/en/mems-and-sensors.html) | 传感器 | 目录以 MEMS 惯性、磁力计、压力、温度与 ToF 为主 | 本次核对未在该目录查到面向旋转编码的专用角度 IC 系列条目 |
| [Motor drivers 目录](https://www.st.com/en/motor-drivers.html) | 驱动 | 站点设独立电机驱动目录 | 与编码器配套出现在同一套电机控制方案里，具体型号按目录查 |

要注意的是：正交编码输入解决的是"数脉冲"，不解决细分、校准与误差补偿。它把 A/B 两相的边沿交给硬件计数器，剩下的插值质量、噪声与温漂，仍在编码器那一侧决定。差分 A/B 进来要走比较器或专用输入，单端 ABZ 在长线上容易被电机噪声吃掉边沿，这一点在主控选型时就该定下来，而不是等做成板子再改。

## 在编码器链上的位置

ST 站在控制器这一侧：编码器整机厂把 STM32 当主控，整机厂拿它做闭环控制与通信。ST 自己不卖码盘、磁体、光电元件，也不做整机编码器。所以它提供的是接口与算力，而不是测量本身。能推理的是：客户需要正交计数、互补 PWM、多路 ADC 同步采样时，这条产品线够全，生态与例程也多；**不能推理的是某台编码器、某个关节模组里用了 ST 的哪颗料**——官网不公布客户设计与 BOM。

采购层面还有一条容易忽略的事：同一块编码器板上，主控与驱动往往同批报价，ST 在这两处都能供，代理商的议价逻辑就变成「打包」。这解释了为什么很多中小编码器厂的方案里，主控、栅极驱动与电源是一色的——不是因为它们必须同厂，而是因为打包更便宜。

因为不做角度芯片，官网上自然没有角秒级精度、INL 这类对外宣称；STM32 定时器在高计数率下的丢步边界也不在产品页上，要读参考手册的定时器章节。

## 官方资料

- [STMicroelectronics 官网](https://www.st.com/)
- [STM32 32-bit Arm Cortex MCUs 目录](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)
- [STM32F407VG 产品页（正交编码输入原文）](https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html)
- [MEMS and Sensors 目录](https://www.st.com/en/mems-and-sensors.html)
- [Motor drivers 目录](https://www.st.com/en/motor-drivers.html)
- [维基百科 STMicroelectronics（沿革与人数）](https://en.wikipedia.org/wiki/STMicroelectronics)
