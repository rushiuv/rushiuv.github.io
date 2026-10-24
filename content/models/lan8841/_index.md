---
title: "LAN8841"
wiki: true
wiki_type: "model"
wiki_rank: 130
seed_count: 1
lastmod: "2026-10-24"
description: "LAN8841是Microchip以太网物理层器件，位于数字MAC与线缆之间。"
official_url: "https://www.microchip.com/en-us/product/LAN8841"
wiki_category: "以太网物理层与时间"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 器件类别 | 千兆以太网 PHY |
| 网络功能 | 以太网物理层收发 |
| 同步相关功能 | 硬件时间戳 |
| 以太网速率 | 10/100/1000Mbps，10BASE-T/100BASE-TX/1000BASE-T |
| 主控接口 | GMII/MII，另可选RGMII模式；接口与引脚按手册 |
| 时间同步 | IEEE1588v2/PTP硬件支持，含报文时间戳 |
| 管理接口 | MDC/MDIO用于PHY寄存器配置，非上层运动控制通信 |

参数依据：[原厂产品页或对应资料](https://www.microchip.com/en-us/development-tool/EV19G28A)。

## 产品功能与测量链

LAN8841是以太网PHY，把主控MAC的数据转换为网线上的物理层信号，适合构成工业传感节点的网络链路。它不直接计算轴角度，也不承担上层运动控制协议的全部功能。

## 接入与配置

使用时先核对MAC接口、时钟、供电域、网络变压器与连接器，再看时间戳和网络同步需求。以太网标称线速反映链路能力，不能直接当成位置测量更新率。

## 使用与验证

与编码器联合设计需建立采样时刻到网络报文的时间关系，并验证丢包、重连和链路降速行为。本页保留LAN8841原厂入口，尚未核实的封装后缀、电源轨和时钟条件不从其他LAN88xx型号填入。

## 官方资料

- [LAN8841 原厂资料入口](https://www.microchip.com/en-us/product/LAN8841)

- [EVB-LAN8841官方说明：PHY、MAC与PTP功能](https://www.microchip.com/en-us/development-tool/EV19G28A)
