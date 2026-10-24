---
title: "MAQ473"
description: "车规MagAlpha角度芯片，提供ABZ及PWM，按配置折衷分辨率与带宽。"
wiki: true
wiki_type: "model"
wiki_rank: 223
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MAQ473"]
official_url: "https://www.monolithicpower.com/en/maq473.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 分辨率 | 9～14位，依配置 |
| 输出 | SPI、ABZ、PWM |
| 产品定位 | 汽车磁角度传感器 |
| 认证边界 | 车规器件不自动使整机满足功能安全要求 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～150°C |
| 滤波截止频率 | 23～6000 Hz，依配置；不能与最高有效分辨率无条件组合 |
| PWM | 14位位置表达；官网列970 Hz |
| 工作电流 | 12 mA，官网列值 |
| 工作磁场 | 官网列30～60 mT |
| 匀速延迟 | 8 µs |
| ABZ | 每通道1～1024脉冲/圈；四倍频最多4096步/圈 |
| 封装 | QFN-16，3 × 3 mm，带可润湿侧翼 |
| 器件资格 | AEC-Q100 Grade 1 |
| SPI校验 | 带奇偶校验；不等于整机功能安全诊断 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/maq473.html)。

## 工作方式与型号定位

MAQ473为车规角度器件，提供SPI、ABZ与PWM，分辨率随滤波从9位到14位变化。它的150°C工作温度与普通工业级MagAlpha成员应分别对照。

## 安装、接口与配置

SPI带奇偶校验，可发现相应传输错误，但不能覆盖磁体松动和全部硬件故障。AEC-Q100 Grade1描述器件资格，整机功能安全仍需系统架构和诊断证据。

## 校准与选型验证

每通道1～1024脉冲/圈ABZ与14位PWM的接入方式不同。应在目标温度、磁路和所选23～6000Hz滤波档下验证准确度与动态响应，并检查上电有效时间、报文错误及控制器失效处理。

## 官方资料

- [MAQ473 官方资料](https://www.monolithicpower.com/en/maq473.html)
