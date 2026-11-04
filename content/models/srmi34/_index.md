---
title: SRMI34系列
description: 分体式磁电增量编码器，用于电机位置与速度脉冲反馈。
wiki: true
wiki_type: model
wiki_rank: 263
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 锐鹰
wiki_category: 旋转编码模块
catalog_vendor: 锐鹰
catalog_type: 旋转编码模块
catalog_form: 编码模块
search_aliases:
- SRMI34
- SRMI34系列
official_url: https://www.reagles.cn/index/product_detail/content/10117.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

SRMI34是34mm分体式增量编码模块。两种目录线数会改变输出频率，选型时必须把线数、转速与接收器计数能力一起核算。

## 型号与核心异同

| 目录配置（非完整料号） | 线数 | 四倍频计数（计算值） | 共同输出 |
| --- | --- | --- | --- |
| 2500C/T配置 | 2500周期／圈 | 10000步／圈 | 26C31差分线驱动 |
| 1024C/T配置 | 1024周期／圈 | 4096步／圈 | 26C31差分线驱动 |

## 共同条件与参数依据

- **形态**：薄型分体模块，需要配套转动磁体与安装条件
- **资料范围**：官网产品页及资料中心列有SRMI34规格书V1.1
- **外径**：34mm，分体式结构
- **转速／响应频率**：≤7200rpm；输出响应频率<250kHz，按所选线数核对
- **电源／电流**：5V±5%；50mA典型
- **工作温度**：−40～85°C
- **环境边界**：90%RH、无结露；由电机后壳防护
- **输出逻辑**：26C31线驱动；官网列VOH≥2.4V、VOL≤0.5V，负载条件依规格书

## 接口与安装

26C31线驱动适合差分接收，接线需成对布置并匹配接收端。单端直接读取一根差分线会改变抗扰和电平条件，不能照抄为标准连接。

## 动态与装配验证

官网给出的≤7200rpm与输出响应频率＜250kHz应和所选线数一同检查。上电后需要原点或其他参考恢复绝对位置；测试须同时观察A/B相位、Z相和反转时的计数一致性。

## 官方资料

- [SRMI34系列 官方资料](https://www.reagles.cn/index/product_detail/content/10117.html)
- [官方补充资料1](https://www.reagles.cn/index/specification.html)
