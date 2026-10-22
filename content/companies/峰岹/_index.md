---
title: "峰岹"
wiki: true
wiki_type: "company"
wiki_rank: 158
seed_count: 1
lastmod: "2026-10-22"
description: "峰岹科技（Fortior）：2010 年创办的深圳电机驱动芯片厂，SR3511N 是 10~16 位可调的旋变数字转换器，配套自研双磁式旋变走无绕组路线。"
official_url: "https://www.fortiortech.com/"
wiki_category: "芯片与信号链"
related_models: ["SR3511N"]
---

峰岹（Fortior）本来是被当作"电机驱动芯片厂"读的：MCU、ASIC、IPM、HVIC 一整套围着无刷电机转。但 SR3511N 与它配套的双磁式旋变，把这家公司推到了位置反馈的解算侧——RDC 负责把旋变的正余弦解成角度，双磁式旋变则把"旋变"从绕线结构搬到更薄、更便宜的载体上。所以读它要看两页：SENSOR 产品线讲它怎么测转子位置，SR3511N 的发布稿讲它怎么解算。

## 2010 年在深圳起家，A 股与港股两地上市

峰岹科技（Fortior Technology），2010 年成立，总部深圳，官网自述专注电机驱动 IC 技术与电机技术咨询，产品用于工业设备、运动控制、电动工具、消费电子、AI 与机器人、IT 与通信。投资者关系入口指向 SSE 的 688279（科创板），2025 年又在港交所主板上市（1304.HK）；2023 年拿到 ISO 26262 功能安全认证，同年上海子公司入选国家级专精特新"小巨人"；2025 年与三花控股合资做无芯电机技术。中文常叫"峰岹"，英文 Fortior。[公司简介](https://www.fortiortech.com/en/about/index)；[发展历程](https://www.fortiortech.com/en/about/history)

## 旋变解码是它的入口，SENSOR 是它的位置来源

| 系列 | 类型 | 公开分辨率/关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [SR3511N](https://www.fortiortech.com/en/news/detail/40) | 旋变数字转换器（RDC） | 官方原文：10 到 16 位分辨率可调，驱动旋变并读取角度与速度 | 自动带宽调节、实时相位校正（官方称可补超过 90° 的相位延迟）、插值校正与误差消除；面向工业伺服、电驱、机器人关节 |
| [双磁式旋变](https://www.fortiortech.com/en/news/detail/40) | 无绕组磁旋变 | 官方原文：绝对或增量两种检测模式、双通道角度检测、超低延时 | 官方称"业界最薄最紧凑"；抗杂散磁场；与 SR3511N 配套成方案 |
| [SENSOR 产品线](https://www.fortiortech.com/en/product/sensor) | 转子位置与电流检测 | 官方定位：为电机控制系统精确检测转子位置与电流信号 | 主打高性能、低功耗、低成本；具体料号在站点的产品选择器里，页面文本没有给出型号表 |
| [MCU 产品线](https://www.fortiortech.com/en/product/mcu) | 双核电机控制器 | 集成高速电机控制引擎与 8051 核，片内含预驱、LDO、运放、比较器、高速 ADC、乘除法器 | 支持 CRC、SPI、I2C、UART、定时器、PWM；面向方波、SVPWM 与 FOC |

要点在 SR3511N 的定位：它不是角度传感器，而是"驱动旋变 + 解算正余弦"的那颗片子。传统做法靠固定带宽设定分辨率与跟踪速率，官方称 SR3511 改成按实时工况自动选带宽；相位校正则针对旋变激励与接收之间的延迟，官方写可补任意大小、包括超过 90° 的相位差。这些是宣传口径，页面没给测试条件与误差曲线。

## 在编码器链上的位置

峰岹在链上是"驱动 + 解算"的一层：往上买晶圆代工与封装，往下卖 MCU、驱动与 RDC，客户是电机厂、伺服厂与机器人关节厂。它不卖磁场敏感的角度芯片（那是 SENSOR 线的方向，但公开料号未列），也不做整机编码器。双磁式旋变的打法值得注意：旋变本来是绕线结构，贵且厚；把它做成磁的、薄的，等于用"旋变的接口习惯 + 磁的成本"去替换光电编码器，这条路和纯磁角度芯片是竞争关系。

能推理的是它对系统成本的取舍——用一颗 RDC 加一对廉价的磁旋变，换掉贵的光编；**不能推理的是 SR3511N 的角度精度、跟踪速率上限、延时与温漂**，这些官方页面都没写，也不能由"10~16 位可调"推出角秒级性能。

## 公开资料的边界

能核对的只有产品线定位与发布稿里的功能描述：分辨率档位、自动带宽、相位校正、插值校正、双磁式旋变的绝对/增量两种模式。**未公开**的是：SR3511N 的 INL 与角秒级精度、最大跟踪速率、群延时、工作温度范围、封装；双磁式旋变的极对数、气隙容差、精度与成本；SENSOR 线的具体料号与规格。这些都藏在需要注册下载的文档与产品选择器里。报价与交期不公开。

## 官方资料

- [Fortior 官网](https://www.fortiortech.com/)
- [公司简介 Who We Are](https://www.fortiortech.com/en/about/index)
- [发展历程（含 2025 港股上市）](https://www.fortiortech.com/en/about/history)
- [SR3511N 与双磁式旋变发布稿](https://www.fortiortech.com/en/news/detail/40)
- [SENSOR 产品线](https://www.fortiortech.com/en/product/sensor)
- [MCU 产品线](https://www.fortiortech.com/en/product/mcu)
- [投资者关系](https://www.fortiortech.com/en/investor)
