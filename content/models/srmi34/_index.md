---
title: "SRMI34系列"
description: "分体式磁电增量编码器，用于电机位置与速度脉冲反馈。"
wiki: true
wiki_type: "model"
wiki_rank: 263
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["锐鹰"]
wiki_category: "旋转编码模块"
catalog_vendor: "锐鹰"
catalog_type: "旋转编码模块"
catalog_form: "编码模块"
search_aliases: ["SRMI34"]
official_url: "https://www.reagles.cn/index/product_detail/content/10117.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 编码方式 | 增量型，不等于上电即得单圈绝对位置 |
| 形态 | 薄型分体模块，需要配套转动磁体与安装条件 |
| 输出配置 | 技术表2500C/T或1024C/T；26C31线驱动，5V±5% |
| 资料范围 | 官网产品页及资料中心列有SRMI34规格书V1.1 |
| 外径 | 34mm，分体式结构 |
| 转速／响应频率 | ≤7200rpm；输出响应频率<250kHz，按所选线数核对 |
| 电源／电流 | 5V±5%；50mA典型 |
| 工作温度 | −40～85°C |
| 环境边界 | 90%RH、无结露；由电机后壳防护 |
| 输出逻辑 | 26C31线驱动；官网列VOH≥2.4V、VOL≤0.5V，负载条件依规格书 |

参数依据：[原厂产品页或对应资料](https://www.reagles.cn/index/product_detail/content/10117.html)。

## 产品功能与测量链

SRMI34是分体式增量编码器，输出正交脉冲供驱动器计数。2500C/T与1024C/T是不同配置；四倍频计数分别对应10000和4096步/圈，不能将线数直接当绝对角度位数。

## 接入与配置

26C31线驱动适合差分接收，接线需成对布置并匹配接收端。单端直接读取一根差分线会改变抗扰和电平条件，不能照抄为标准连接。

## 使用与验证

官网给出的≤7200rpm与输出响应频率＜250kHz应和所选线数一同检查。上电后需要原点或其他参考恢复绝对位置；测试须同时观察A/B相位、Z相和反转时的计数一致性。

## 官方资料

- [SRMI34系列 官方资料](https://www.reagles.cn/index/product_detail/content/10117.html)
- [官方补充资料1](https://www.reagles.cn/index/specification.html)
