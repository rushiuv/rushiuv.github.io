---
title: "MA600A"
description: "MPS用于新设计的高精度磁角度器件，是MA600官网给出的后续选择。"
wiki: true
wiki_type: "model"
wiki_rank: 222
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA600A"]
official_url: "https://www.monolithicpower.com/en/ma600a.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 分辨率 | 12～15位可配置 |
| 校准 | 32点校准表 |
| INL | 出厂小于0.6°；用户校准可小于0.1°，须满足相应手册条件 |
| 资料版本 | 官方数据手册Rev.1.0，2025-06-05 |
| 技术 | 集成TMR |
| 工作磁场 | 10～100 mT |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 静态电流 | 7.5 mA（IAVDD + IDVDD） |
| 温度／封装 | −40～125°C；QFN-16，3 × 3 mm |
| 绝对位置接口 | SPI、SSI；SPI支持多器件菊链 |
| 增量／换向 | ABZ每通道1～4096脉冲/圈，另有UVW |
| PWM频率 | 250 Hz或1000 Hz，按配置 |
| 带宽条件示例 | 12.5位分辨率时12 kHz；原厂给出的配置示例 |
| 动态口径 | 原厂称No Latency；接口传输和主控运算另计 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma600a.html)。

## 工作方式与型号定位

MA600A集成TMR测量、数字角度处理及32点用户校准表，面向高带宽位置控制。出厂INL小于0.6°与用户校准后可小于0.1°应分别阅读，后者依赖最终装配与校准质量。

## 安装、接口与配置

12～15位分辨率和滤波带宽需要成组选择。原厂举出12.5位时12kHz带宽的工作例子；产品表最高截止频率不能与15位分辨率机械拼在一起。标为无延时也不表示SPI事务和主控处理不消耗时间。

## 校准与选型验证

SPI支持菊链顺序读取多颗器件，SSI用于串行角度输出；ABZ、UVW和PWM按所用引脚设置。32点校准完成后，应在独立角度、正反转及温度点检验残差，并重新上电核对配置保持。

## 官方资料

- [MA600A 官方资料](https://www.monolithicpower.com/en/ma600a.html)
