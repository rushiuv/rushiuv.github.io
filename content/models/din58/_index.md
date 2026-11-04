---
title: DIN58系列
description: 感应式工业旋转编码器系列，按工业网络和机械接口选择配置。
wiki: true
wiki_type: model
wiki_rank: 264
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 锐鹰
wiki_category: 完整编码器
catalog_vendor: 锐鹰
catalog_type: 完整编码器
catalog_form: 完整编码器
search_aliases:
- DIN58
- DIN58系列
official_url: https://www.reagles.cn/index/product_detail/content/10142.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

DIN58是带机械安装结构的完整编码器系列。选型要区分通信和供电配置；技术表的RS485／CANopen参数不能直接覆盖目录中的所有协议。

## 型号与核心异同

| 目录配置（非完整料号） | 已有资料 | 仍需确认 |
| --- | --- | --- |
| RS485配置 | 当前技术表；2.5Mbps | 完整订货号、安装与误差条件 |
| CANopen配置 | 当前技术表；默认250kbps | 完整订货号及网络配置 |
| PROFINET配置 | 目录列出 | 成员技术表与完整料号 |
| EtherCAT配置 | 目录列出 | 成员技术表与完整料号 |
| SSI配置 | 目录列出 | 成员技术表与完整料号 |

## 共同条件与参数依据

- **绝对定位**：官网目录±40角秒；重复定位±7角秒，两者分开
- **防护**：官网目录IP65，须按连接器及安装条件确认
- **形态**：带机械安装结构的完整编码器，不是信号调理芯片
- **单圈／多圈码宽**：单圈18bit、多圈16bit，当前技术表配置
- **计圈结构**：机械多圈、无计圈电池，按系列说明
- **供电版本**：DC5V±5%或10～30V，按订货配置；不是同一输入连续覆盖
- **工作温度**：−40～85°C
- **环境湿度**：≤90%，无结露；官网注明40°C/21d条件

## 接口与安装

目录绝对定位±40角秒约为±0.01111°，重复定位±7角秒约为±0.00194°。两项分别描述准确程度与反复返回的一致性，不能合并成一个更好的精度值。

## 动态与装配验证

IP65依赖具体装配和连接器条件。验收除整圈误差外，还应检查轴连接、供电、协议更新及通信异常；网络周期不能直接当成编码器测量延迟。

## 官方资料

- [DIN58系列 官方资料](https://www.reagles.cn/index/product_detail/content/10142.html)
