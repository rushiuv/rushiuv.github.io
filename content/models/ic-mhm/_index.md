---
title: "iC-MHM"
description: "支持外部多圈数据接入的霍尔单圈角度编码器，分辨率与最高跟踪速度需折衷。"
wiki: true
wiki_type: "model"
wiki_rank: 252
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["iC-Haus"]
wiki_category: "数字角度"
catalog_vendor: "iC-Haus"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["iC-MHM"]
official_url: "https://www.ichauschina.com/products/enc_mag.htm"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 单圈 | 最高14位；更高转速可用较低分辨率配置 |
| 接口 | BiSS／SSI、SPI模式，按配置 |
| 多圈边界 | 可处理外部多圈数据，不等于芯片断电后自行计圈 |
| 信号链 | 增益监控及可选精校准 |
| 分辨率与转速 | 14bit最高10000rpm；12bit最高80000rpm，分别为公开摘要配置 |
| 模拟输出 | 差分SIN/COS，1Vpp驱动100Ω，按相应电气条件 |
| 串行物理层 | 集成RS422收发，5V条件最高10Mbit/s；更高速率需满足LVDS条件 |
| 多圈数据范围 | 外部多圈数据处理最高32bit，不等于自身断电计圈 |
| 配置来源 | 外部EEPROM，经I²C加载且带CRC保护，按版本配置 |

参数依据：[原厂产品页或对应资料](https://www.ichauschina.com/products/enc_mag.htm)。

## 产品功能与测量链

iC-MHM提供单圈角度，并可接收外部多圈信息。多圈数据接入属于系统组合功能，芯片本身不因此获得无电源计圈能力。

## 接入与配置

最高14位与最高跟踪速度存在配置折衷。选定分辨率后，需要连同磁体、滤波和接口时序核对动态能力，不能把不同档位的最大值合成一个工作点。

## 使用与验证

使用BiSS/SSI或SPI模式时应确认输出字结构、状态位和多圈字段。验收要覆盖外部圈数与单圈过零的同步，防止出现整圈跳变而角度小数部分仍正常。

## 官方资料

- [iC-MHM 官方资料](https://www.ichauschina.com/products/enc_mag.htm)
