---
title: "MA735"
description: "采用小型UTQFN-14封装的MagAlpha角度芯片，提供ABZ及PWM输出。"
wiki: true
wiki_type: "model"
wiki_rank: 218
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA735"]
official_url: "https://www.monolithicpower.com/en/ma735.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 分辨率 | 9～13位，依配置 |
| 输出 | SPI、ABZ、PWM |
| 封装 | UTQFN-14 |
| 选型边界 | 带宽、噪声和有效分辨率不是独立最大值 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～125°C |
| 供电电流 | 参数表11.7 mA；特性摘要约12 mA，具体条件以手册为准 |
| 匀速延迟 | 官网参数表8 µs；不含主控传输调度 |
| 最高转速 | 0～60,000 rpm，按手册磁路与配置 |
| 工作磁场下限 | 40 mT，原厂参数表 |
| ABZ脉冲 | 每通道1～1024脉冲/圈；四倍频4～4096步/圈 |
| 滤波截止频率 | 23～6000 Hz，依配置；不能与最高有效分辨率无条件组合 |
| PWM | 14位位置表达；官网列970 Hz |
| 封装尺寸 | UTQFN-14，2 × 2 mm |
| 分辨率口径 | 9～13位为±3σ分辨率；14位PWM是输出码宽 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma735.html)。

## 工作方式与型号定位

MA735把角度检测、SPI、ABZ和PWM放进2×2mm的UTQFN-14封装，适合空间受限的反馈板。封装缩小并不取消磁体尺寸、敏感中心和布线去耦要求。

## 安装、接口与配置

9～13位±3σ分辨率与14位PWM码宽采用不同口径。前者和噪声、滤波有关，后者描述输出表达；不能因为PWM有14位就宣称传感器拥有14位有效角度精度。

## 校准与选型验证

每通道ABZ最多1024脉冲/圈，滤波截止频率23～6000Hz按配置选择。磁场至少40mT的条件要在最大气隙和装配偏差下检查，并将角度抖动、阶跃响应和增量边沿一起验证。

## 官方资料

- [MA735 官方资料](https://www.monolithicpower.com/en/ma735.html)
