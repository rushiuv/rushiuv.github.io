---
title: "nRF52832"
wiki: true
wiki_type: "model"
wiki_rank: 136
seed_count: 1
lastmod: "2026-10-24"
description: "nRF52832是Nordic Semiconductor的蓝牙低功耗SoC，将微控制器与无线电集成，可用于无线传感节点、外设和交互设备。"
official_url: "https://www.nordicsemi.com/Products/nRF52832"
datasheet_url: "https://docs.nordicsemi.com/r/bundle/ps_nrf52832/page/nrf52832_ps.html"
datasheet_label: "官网文档入口"
wiki_category: "控制计算与外设采样"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 处理器 | Arm Cortex-M4 |
| 无线 | Bluetooth Low Energy SoC |
| 集成 | 微控制器与无线电 |
| 订货差异 | Flash、RAM 与封装随具体料号 |
| 主频／内核 | 64MHz Arm Cortex-M4，带FPU |
| 存储版本 | QFAA/CIAA：512kB Flash、64kB RAM；QFAB：256kB Flash、32kB RAM |
| 工作电压 | 1.7～3.6V |
| 无线速率 | Bluetooth LE 1Mbps、2Mbps，依协议与配置 |
| ADC | 12bit、200ksps，8个可配置通道 |
| 数字外设 | QDEC、SPI、TWI/I²C、UART、PWM、PPI及EasyDMA，资源与实例按手册 |
| 低功耗条件 | 3V System OFF约0.3µA；全64kB RAM保持时约0.7µA，不能当连续采集电流 |

参数依据：[原厂产品页或对应资料](https://docs.nordicsemi.com/r/bundle/ps_nrf52832/page/nrf52832_ps.html?contentId=96Da0Nf4VS5ePLinBRUs8g)。

## 产品功能与测量链

nRF52832把64MHz Cortex-M4F与2.4GHz无线电结合，可接入传感器并发送测量数据。它是采集和通信节点，不自带可直接替代外部磁编码器的位置测量功能。

## 接入与配置

QFAA与CIAA为512kB Flash/64kB RAM，QFAB为256kB/32kB。无线协议栈也占用存储和运行时间，选型应按实际固件资源核算，而非只比较处理器主频。

## 使用与验证

GPIO、电源与模拟输入须按手册电平接入。QDEC、SPI和ADC对应不同传感信号，不能互相替换；无线发包周期、重传与主控采样周期也应分别记录，保证测量时间戳可追溯。

## 官方资料

- [nRF52832 原厂资料入口](https://www.nordicsemi.com/Products/nRF52832)
- [官网文档入口（官方入口）](https://docs.nordicsemi.com/r/bundle/ps_nrf52832/page/nrf52832_ps.html)

- [nRF52832 Product Specification：Key features、Memory、Ordering information](https://docs.nordicsemi.com/r/bundle/ps_nrf52832/page/nrf52832_ps.html?contentId=96Da0Nf4VS5ePLinBRUs8g)
