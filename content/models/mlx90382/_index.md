---
title: "MLX90382"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 90
seed_count: 2
lastmod: "2026-10-24"
description: "MLX90382 是 Melexis 的 16 位 Triaxis 霍尔绝对角度编码器，支持在轴和离轴安装，提供 SPI／SSI／PWM 及差分增量输出。"
official_url: "https://www.melexis.com/en/product/mlx90382/triaxis-magnetic-high-speed-encoder"
related_companies: ["Melexis"]
datasheet_url: "https://www.melexis.com/-/media/files/documents/datasheets/mlx90382-datasheet-melexis.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mlx90382-application.png"
product_image_caption: "MLX90382 在轴／离轴电机安装示意；来源为该型号原厂宣传页"
product_image_source: "https://media.melexis.com/-/media/files/documents/product-flyers/mlx90382-product-flyer-melexis.pdf"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应原理 | Triaxis 霍尔，支持在轴与离轴 |
| 绝对角度分辨率 | 16 位 |
| 绝对值输出 | SPI、SSI、PWM |
| 增量／换向 | ABI、UVW，单端与差分选项 |
| 同步 | SPI 支持多器件同步读取 |
| 封装结构 | 单 die 与双 die 选项 |
| 供电模式 | 3.3V±5%（VDD与VDD3V3短接）；5V±10%，按第9～10页 |
| 供电电流口径 | 第9～10页表列IMC 10 mA、抗杂散场模式11 mA，均不含输出接口负载 |
| 工作温度 | −40～150°C；标称精度条件通常−40～125°C，另有受限性能条件 |
| 电角转速 | 最高200,000 e-rpm；按手册速度/加速度与带宽条件 |
| 处理延迟 | 启用延时补偿时−333～+333 ns；关闭时6 µs；均不含输出接口，第12页 |
| 中场磁路 | XY平面上限70 mT；BNORM下限10 mT，标称精度条件≥30 mT；XZ/YZ按IMC换算 |
| 高场磁路 | XY平面上限120 mT；BNORM下限40 mT，标称精度条件≥60 mT；XZ/YZ按IMC换算 |
| 标称内禀线性误差 | EoL前：XY±0.5°；XZ/YZ±1°；−40～125°C、≤50krpm及标称场条件 |
| 标称角度噪声 | 旋转模式典型0.025° RMS（DSP_LFC_HI=0）或0.035°（=3）；第16页条件 |
| 校准分层 | 运行中I/Q增益与正交校准；另有16点外部误差线性化表 |
| 封装 | 单die QFN24；双die TSSOP16/TSSOP16-EP |

参数来源：本页所列[原厂产品资料与手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90382-datasheet-melexis.pdf)。

资料定位：MLX90382 Rev.1.0（2025-11-17）第9～16页、第6.6节；标称精度是EoL校准前且限定磁场/温度/速度，不是最终整机误差。

## 工作方式与型号定位

MLX90382把Triaxis前端、ADC、角度处理和多种输出集成在一起，可读取绝对位置并用于高速运动。16位角度码和接口状态应分别解析，不能把报文长度直接当作角度分辨率。

## 安装、接口与配置

片上自校准在运行中跟踪I/Q相对灵敏度和正交失配；16点线性化表则需要最终装配后的角度误差数据。两者修正对象不同，不能写成芯片自动获得整圈机械真值。

## 校准与选型验证

SPI多器件同步读取有助于统一采集时刻，仍需核对数据锁存和传输时序。单die和双die封装按具体料号选择；最终验证应区分校准前后、在轴离轴及温度条件，并检查增量和串行输出的一致性。

## 官方资料

- [MLX90382 原厂资料入口](https://www.melexis.com/en/product/mlx90382/triaxis-magnetic-high-speed-encoder)
- [MLX90382 数据手册（官方 PDF）](https://www.melexis.com/-/media/files/documents/datasheets/mlx90382-datasheet-melexis.pdf)
