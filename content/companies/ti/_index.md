---
title: "TI"
description: "Texas Instruments 德州仪器：磁位置、模拟信号链与电机控制器件，代表方向包括 3D 霍尔和 AMR 角度感应。"
wiki: true
wiki_type: "company"
wiki_rank: 7
seed_count: 19
lastmod: "2026-10-16"
official_url: "https://www.ti.com/"
related_models: []
related_companies: []
---

## 公司与品牌

TI 是 Texas Instruments 的简称，中文为德州仪器。其产品覆盖模拟与嵌入式处理，位置反馈系统中常见的相关环节包括磁传感器、放大与采样、接口、电源和电机控制。读者在一套编码器原理图中见到 TI 器件时，应先确认它负责感应、调理、通信还是供电。[公司介绍](https://www.ti.com/about-ti.html)

TI 的磁传感目录同时列有开关、锁存器、线性磁场与角度器件。分类对应输出物理量和使用方式，不能把所有霍尔芯片都直接当作旋转编码器。

## 相关业务与技术路线

3D 霍尔路线的代表是 TMAG5170。它通过 SPI 提供三轴磁场相关数据，片内还设有角度计算功能，可用两个磁轴的测量值计算角度。由此既能读取磁场，也可以围绕旋转磁体构造位置检测系统。[TMAG5170 官方资料](https://www.ti.com/product/TMAG5170)

AMR 路线中，TI 当前目录列出 TMAG6180-Q1 等角度器件。它以模拟正余弦信号服务后端采样，和直接给出数字角度的方案在系统分工上不同。设计者需要把 MCU 的 ADC、采样同步和角度计算成本纳入比较。

TI 同时提供评估模块和图形工具。TMAG5170UEVM 可读写配置、查看并保存磁场、温度、角度与幅值数据。这类工具有利于先观察磁路轨迹，再决定是否需要调整磁体和安装位置，而非直接从单个角度读数判断整个结构。

## 产品系列与代表方向

| 方向 | 代表对象 | 主要阅读问题 |
| --- | --- | --- |
| 三轴霍尔 | TMAG5170 | 量程、轴组合、采样顺序、角度计算 |
| AMR 角度 | TMAG6180-Q1 | 模拟正余弦、磁场条件与后端采样 |
| 磁开关／锁存 | TI magnetic sensors 目录 | 触发与释放阈值、磁极和功耗 |
| 评估平台 | TMAG5170UEVM | 配置、测量数据与机械样件验证 |
| 系统器件 | 模拟／接口／电源产品线 | 按编码器完整电气架构选择 |

代表型号用于说明产品路线，表中不会将各器件的最高性能拼成一颗虚构的“TI 编码器”。实际选型应进入单独型号页及手册。

## 官方资料

- [TI 公司介绍](https://www.ti.com/about-ti.html)
- [磁传感器产品目录](https://www.ti.com/product-category/sensors/magnetic/overview.html)
- [TMAG5170 官方产品页](https://www.ti.com/product/TMAG5170)
- [TMAG5170 官方数据手册](https://www.ti.com/lit/ds/symlink/tmag5170.pdf)
- [TMAG5170UEVM 评估模块](https://www.ti.com/tool/TMAG5170UEVM)
