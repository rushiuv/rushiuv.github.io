---
title: "Melexis"
description: "迈来芯：磁性 Triaxis 位置传感器与电感位置接口芯片，覆盖模拟正余弦及数字角度输出。"
wiki: true
wiki_type: "company"
wiki_rank: 5
seed_count: 24
lastmod: "2026-10-16"
official_url: "https://www.melexis.com/"
related_models: []
related_companies: []
---

## 公司与品牌

Melexis 中文常称迈来芯，其位置传感产品同时覆盖磁感应与电感测量。对于电机和机器人读者，值得区分的是两类产品：输出模拟正余弦信号的 resolver 器件，以及在芯片内计算位置并提供数字接口的编码器或接口芯片。

官网产品描述较明确地给出各型号的测量对象、输出与应用条件。理解品牌时，沿着具体产品的信号流阅读，比将所有器件统一理解成“磁编码器”更准确。MLX90380 和 MLX90520 就分别体现了两种差异明显的系统分工。

## 相关业务与技术路线

Triaxis 是 Melexis 的磁位置技术品牌。MLX90380 采用该技术，检测磁场相关分量并输出模拟正弦和余弦，面向无刷电机等需要快速位置反馈的场景。可选择的磁场轴组合为不同安装方式提供空间，输出仍需要后端采集和角度计算。[MLX90380 产品页](https://www.melexis.com/en/product/MLX90380/Preprogrammed-Magnetic-Resolver)

电感路线的 MLX90520 则配合发射线圈、目标件和两组接收线圈工作。片内激励产生电磁场，目标件的位置改变接收信号，模拟前端、ADC 与 DSP 将其转换为位置数据。它支持两路同步读取，也可结合通道信息计算游标角度。[MLX90520 产品页](https://www.melexis.com/en/product/MLX90520/22-bit-Inductive-position-sensor-dual-input)

两类器件的机械配套不同：磁方案需要匹配磁体，电感方案需要设计线圈和导电目标件。后者可以利用 PCB 形成感应结构，适合围绕中空空间设计，但实际性能依赖线圈、气隙、目标几何和信号处理配置。

## 产品系列与代表型号

| 方向 | 代表型号 | 主要系统分工 |
| --- | --- | --- |
| 磁性 resolver | MLX90380 | 磁感应后输出模拟正余弦 |
| 紧凑磁性 resolver | MLX90381 | 作为磁位置产品线的另一个成员查阅 |
| 数字磁位置 | MLX90382 等 | 按具体型号确认角度计算与输出 |
| 电感编码接口 | MLX90520 | 双输入采集、片内位置处理、SPI／SSI |
| 开发工具 | 对应 EVB、编程器和设计资料 | 验证磁路或线圈与器件配置 |

MLX90520 官方页给出 22 位分辨率和片内游标角度计算。这里的位数描述数据表达能力，不能直接用于推导某种直径、某种线圈下的整机精度。通道电角误差与机械角误差也需要结合刻度周期理解。

## 官方资料

- [MLX90380 产品页与资料下载](https://www.melexis.com/en/product/MLX90380/Preprogrammed-Magnetic-Resolver)
- [MLX90380 官方数据手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90380-datasheet-melexis.pdf)
- [MLX90520 产品页与资料下载](https://www.melexis.com/en/product/MLX90520/22-bit-Inductive-position-sensor-dual-input)
- [MLX90520 官方数据手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf)
