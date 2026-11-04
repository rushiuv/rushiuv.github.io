---
title: STM32系列
wiki: true
wiki_type: model
wiki_rank: 96
seed_count: 2
lastmod: '2026-10-30'
description: STM32 是 ST 的 32 位微控制器家族，可通过具备相应外设的成员接收增量脉冲、SPI 角度或模拟传感器信号。
official_url: https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html
related_companies:
- ST
wiki_category: 控制计算与外设采样
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
catalog_level: 系列
search_aliases:
- STM32系列
---

STM32是MCU家族，接收并处理编码器信号，不是位置传感器。当前页作为接入选型入口，未指定完整MCU料号，下表区分所需外设路径。

## 型号与核心异同

| 接入配置（非具体MCU型号） | 所需资源 | 具体成员需核对 |
| --- | --- | --- |
| 增量ABZ采集 | 支持编码器模式的定时器与引脚 | 计数位宽、滤波、捕获频率 |
| 串行绝对角度采集 | 相应SPI等串行外设 | 时序、DMA、数据帧及引脚映射 |
| 模拟正余弦采集 | ADC、采样同步与角度运算 | 同步能力、参考、带宽与计算资源 |

## 共同条件与参数依据

- **产品范围**：ST 的 32 位 MCU 家族
- **型号差异**：内核、存储、外设及封装随完整 STM32 料号

## 接口与安装

增量接口使用定时器编码器模式，绝对值编码器使用SPI等串行接口，模拟正余弦则需要ADC采样与角度解算。三种链路对引脚、时序和计算量的要求不同。

## 动态与装配验证

选具体料号时核对定时器位宽、输入滤波、最高捕获频率、ADC同步和DMA映射。控制程序还应处理计数器回绕、角度跨零和读取时间戳，避免只验证静止读数而遗漏高速丢边沿。

## 官方资料

- [STM32 原厂资料入口](https://www.st.com/en/microcontrollers-microprocessors/stm32-32-bit-arm-cortex-mcus.html)
