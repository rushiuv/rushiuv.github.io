---
title: "MA302"
description: "MPS MagAlpha 12位磁角度芯片，兼有SPI绝对角度、ABZ增量和UVW换相信号，支持在轴及离轴布置。"
wiki: true
wiki_type: "model"
wiki_rank: 200
model_card: true
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "磁角度测量"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA302"]
official_url: "https://www.monolithicpower.com/en/ma302.html"
document_version: "官方产品页，核对：2026-10-18"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 绝对角度 | 12位，通过SPI读取；分辨率不等于系统精度 |
| 增量／换相 | ABZ每通道1～256脉冲／圈；UVW支持1～8对极仿真 |
| 安装 | 支持轴端与离轴；离轴性能依磁路与配置确认 |
| 供电／封装 | 3.0～3.6V，QFN-16（3×3mm） |
| 工作温度 | −40～125°C |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 供电电流 | 参数表11.7 mA；特性摘要约12 mA，具体条件以手册为准 |
| 匀速延迟 | 官网参数表8 µs；不含主控传输调度 |
| 最高转速 | 0～60,000 rpm，按手册磁路与配置 |
| 工作磁场下限 | 30 mT，原厂参数表 |
| 角度刷新 | 1 MHz；不等于位置带宽或接口时钟 |
| 滤波截止频率 | 官网参数表390 Hz |
| 理想数字码距 | 按12位全圈换算：360°/2^12 ≈ 0.08789062°；计算值，不是准确度保证 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma302.html)。

## 工作方式与型号定位

MA302将12位绝对角度、ABZ增量和UVW换向集成在同一器件。它适合既要启动位置又要脉冲反馈的控制器，SPI与增量口的职责应明确分开。

## 安装、接口与配置

ABZ每通道1～256脉冲/圈，四倍频计数对应4～1024步；UVW仿真的1～8对极应与电机电角度匹配。修改线数或方向后，控制器的角度换算和Z相解释也要同步更新。

## 校准与选型验证

轴端和离轴安装均受磁路条件约束。产品页给出30mT最低工作磁场，不能把可诊断的弱磁状态当成仍满足精度。8µs延迟、390Hz截止频率及1MHz刷新是不同指标，应分别用于动态预算。

## 官方资料

- [MA302 官方产品页与数据手册入口](https://www.monolithicpower.com/en/ma302.html)
