---
title: "ENX 22 EMT"
wiki: true
wiki_type: "model"
catalog_type: "完整编码器"
catalog_form: "完整编码器"
wiki_rank: 118
seed_count: 1
lastmod: "2026-10-24"
description: "ENX 22 EMT 是 maxon 的多圈绝对编码器，用于与电机配套的位置反馈。"
official_url: "https://www.maxongroup.com/"
related_companies: ["maxon"]
datasheet_url: "https://www.maxongroup.com/medias/sys_master/root/9257532456990/enx-emt-en-04-2024.pdf"
datasheet_label: "官网文档入口"
wiki_category: "多圈与断电位置"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 位置类型 | 多圈绝对位置 |
| 产品形态 | 与 maxon 电机配套的编码器 |
| 订货范围 | 机械接口、通信接口及适配电机随完整订货号确定 |
| 单圈分辨率 | 17bit，131072步/圈，maxon目录 |
| 多圈范围 | 16bit，65536圈，maxon目录 |
| 通信版本 | BiSS-C或SSI，按订货号选择 |
| SSI速率 | 最高1000kbit/s，EPOS4配置说明 |
| SSI帧前导 | 8个leading special bits，随后16bit多圈和17bit单圈，MSB先发 |
| 温度／重量 | 目录−40～105°C；25g，依配套版本 |

参数依据：[原厂产品页或对应资料](https://www.maxongroup.com/medias/sys_master/root/9416689156126/Brosch-IDX-70-BLDC-Motor-0525-EN.pdf)。

## 产品功能与测量链

ENX 22 EMT用于与maxon电机配套的多圈绝对位置反馈。编码器机械连接、电机组合和通信版本共同决定最终可用的反馈形式。

## 接入与配置

多圈位置包含单圈角度与圈数，不能只比较合计位数。需明确断电计圈方式、允许范围、重新上电行为以及控制器如何解释多圈字。

## 使用与验证

订货前核对适配电机、轴连接和安装尺寸，不能把同直径编码器视为通用附件。实际验收应包含正反转跨零、无电源运动和上电位置恢复。

### SSI接入EPOS4

原厂说明要求保留8个前导特殊位，再处理16位多圈及17位单圈；SSI速率不得高于1Mbit/s。EPOS4位置字段长度有限时，应按原厂配置说明选择处理位数，而不是直接截掉多圈字段。降低处理位数属于控制器配置，不能据此改写编码器自身17位规格。

## 官方资料

- [ENX 22 EMT 原厂资料入口](https://www.maxongroup.com/)
- [官网文档入口（官方入口）](https://www.maxongroup.com/medias/sys_master/root/9257532456990/enx-emt-en-04-2024.pdf)

- [maxon ENX 22 EMT目录](https://www.maxongroup.com/medias/sys_master/root/9416689156126/Brosch-IDX-70-BLDC-Motor-0525-EN.pdf)
- [maxon EMT的SSI与EPOS4配置说明](https://support.maxongroup.com/hc/en-us/articles/4406420812434-EPOS4-SSI-configuration-of-maxon-s-EMT-multi-turn-encoder)
