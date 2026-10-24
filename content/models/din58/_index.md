---
title: "DIN58系列"
description: "感应式工业旋转编码器系列，按工业网络和机械接口选择配置。"
wiki: true
wiki_type: "model"
wiki_rank: 264
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["锐鹰"]
wiki_category: "完整编码器"
catalog_vendor: "锐鹰"
catalog_type: "完整编码器"
catalog_form: "完整编码器"
search_aliases: ["DIN58"]
official_url: "https://www.reagles.cn/index/product_detail/content/10142.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 绝对定位 | 官网目录±40角秒；重复定位±7角秒，两者分开 |
| 协议区别 | 目录列CANopen、PROFINET、EtherCAT、SSI；当前技术表为RS485／CANopen配置，订货时逐项确认 |
| 防护 | 官网目录IP65，须按连接器及安装条件确认 |
| 形态 | 带机械安装结构的完整编码器，不是信号调理芯片 |
| 单圈／多圈码宽 | 单圈18bit、多圈16bit，当前技术表配置 |
| 计圈结构 | 机械多圈、无计圈电池，按系列说明 |
| 技术表接口 | RS485、CANopen；RS485 2.5Mbps，CANopen默认250kbps |
| 供电版本 | DC5V±5%或10～30V，按订货配置；不是同一输入连续覆盖 |
| 工作温度 | −40～85°C |
| 环境湿度 | ≤90%，无结露；官网注明40°C/21d条件 |

参数依据：[原厂产品页或对应资料](https://www.reagles.cn/index/product_detail/content/10142.html)。

## 产品功能与测量链

DIN58是带工业机械接口的感应式旋转编码器，选型应同时确定轴型、连接器和通信协议。CANopen、PROFINET、EtherCAT与SSI属于不同订货配置。

## 接入与配置

目录绝对定位±40角秒约为±0.01111°，重复定位±7角秒约为±0.00194°。两项分别描述准确程度与反复返回的一致性，不能合并成一个更好的精度值。

## 使用与验证

IP65依赖具体装配和连接器条件。验收除整圈误差外，还应检查轴连接、供电、协议更新及通信异常；网络周期不能直接当成编码器测量延迟。

## 官方资料

- [DIN58系列 官方资料](https://www.reagles.cn/index/product_detail/content/10142.html)
