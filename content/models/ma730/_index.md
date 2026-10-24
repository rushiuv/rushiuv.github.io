---
title: "MA730"
description: "14位MagAlpha磁角度芯片，以SPI、ABZ和PWM连接控制器。"
wiki: true
wiki_type: "model"
wiki_rank: 215
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA730"]
official_url: "https://www.monolithicpower.com/en/ma730.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度编码 | 14位绝对角度 |
| 输出 | SPI、ABZ、PWM |
| 安装 | 轴端及离轴，依原厂应用条件 |
| 选型边界 | 14位输出码宽不等于14位绝对精度 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～125°C |
| 供电电流 | 参数表11.7 mA；特性摘要约12 mA，具体条件以手册为准 |
| 匀速延迟 | 官网参数表8 µs；不含主控传输调度 |
| 最高转速 | 0～60,000 rpm，按手册磁路与配置 |
| 工作磁场下限 | 40 mT，原厂参数表 |
| ABZ脉冲 | 每通道1～1024脉冲/圈；四倍频4～4096步/圈 |
| PWM | 14位位置表达；官网列970 Hz |
| 角度刷新 | 1 MHz；不等于位置带宽或接口时钟 |
| 封装 | QFN-16，3 × 3 mm |
| 滤波截止频率 | 官网参数表23 Hz |
| 串行接口补充 | 现行官网参数表同时列SPI、SSI；接法与版本按手册确认 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma730.html)。

## 工作方式与型号定位

MA730提供14位绝对角度、ABZ和PWM，既可接数字角度采集，也可接传统计数器。产品页的接口表还列SSI，正式设计应以所选版本手册确认接法。

## 安装、接口与配置

ABZ每通道1～1024脉冲/圈，四倍频最多4096步，不能把它等同于14位串行角度。970Hz PWM约每1.03ms一个周期，高频轮询不会让PWM产生更快的独立位置更新。

## 校准与选型验证

原厂列出1MHz刷新、23Hz截止频率与8µs延迟，三者描述不同环节。高速应用应实际测量滤波响应，磁体则需保持规定工作磁场；支持离轴安装不等于任意磁环和偏置都具有同一误差。

## 官方资料

- [MA730 官方资料](https://www.monolithicpower.com/en/ma730.html)
