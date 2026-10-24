---
title: "新板读不通，先把供电引脚分清"
description: "把电源输入、内部稳压去耦和接口电源分别实测，再进入帧时序排查。"
date: "2026-10-24"
lastmod: "2026-10-24"
layout: "engineering-single"
engineering_entry: true
plan_id: "E01"
guide_group: "接入与诊断"
weight: 10
related_basics: ["interfaces", "spi-ssi"]
related_model_slugs: ["admt4000"]
related_guides: ["mixed-voltage-backpower", "position-validity-state", "calibration-data-integrity"]
related_applications: ["servo-motor", "robot-joint"]
keywords: ["首次上电", "供电域", "接口不通"]
---

新板第一次读不通，先留一张逐脚电压记录。电源连接器上有3.3V，只能证明连接器处有电，不能证明芯片每个供电域已建立。

## 一个器件，三种电源脚用途

[ADMT4000 Rev.C手册](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)的引脚表把VDD列为主电源输入，VDRIVE列为逻辑电源输入，DV18列为内部1.8V稳压器的去耦端。DV18按指定方式接电容，不能因名字带电压就把它接到外部电源。

把实际封装脚号写进记录，按以下顺序核对：

| 要查什么 | 怎么量、何时停下 |
| --- | --- |
| 供电是否到脚 | 测芯片电源脚对本地GND的直流值；异常时断电查网表、焊接和连通性 |
| 上电是否完整 | 同屏抓VDD、VDRIVE与启动状态；检查斜坡、跌落和电源先后，不只量稳态 |
| IO归哪个电源域 | 核主机输出幅值、从机门限与掉电状态；不兼容时先处理电平转换 |
| 启动是否完成 | 留下启动状态及第一笔有效读数时间；未就绪时不把读回全零当角度 |

断电连通性检查不能代替带电测量：一根高阻连接可能在空载时读到正常电压，开始转换后才下陷。示波器探头参考点要落在器件附近，并记录限流设置、固件版本和复位脚状态。

## 把“电气通过”变成退出条件

假设新板在连接器测得3.30V、芯片脚仅2.85V，这是**人为设定的排障例子**。下一步是同时量连接器与引脚，观察启动电流期间的压差，再定位连接路径；此时改SPI时钟相位不会消除这0.45V压差。限值仍取该器件推荐工作条件，不能用例子的数值替代。

四项核对通过后，再抓片选、时钟与数据，按手册确认模式和读序。若主机已上电、传感器尚断电，还要检查[混压与反供电](/wiki/engineering/mixed-voltage-backpower/)；[TI的双电源转换器资料](https://www.ti.com/product/SN74LVC1T45)说明了接口电源隔离为何需要单独规定。曾正常运行后突然失效的板，还应另查损伤与负载变化，不能套用“首次接线有误”这个结论。
