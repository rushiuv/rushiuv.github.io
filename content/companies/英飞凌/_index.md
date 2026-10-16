---
title: "英飞凌"
description: "Infineon 英飞凌：Hall、AMR、GMR、TMR 角度传感器及其接口，并承接原 ams 非光学传感器业务。"
wiki: true
wiki_type: "company"
wiki_rank: 10
seed_count: 16
lastmod: "2026-10-16"
official_url: "https://www.infineon.com/"
related_models: ["AS5047P"]
related_companies: ["ams OSRAM"]
---

## 公司与品牌

英飞凌英文名称为 Infineon Technologies。位置感知产品在其 XENSIV 传感器体系中占有一部分，官方磁位置选型资料同时涵盖 Hall、AMR、GMR 和 TMR 技术，面向汽车、工业与消费场景。不同物理原理、封装和输出方式组成了较宽的角度传感产品范围。

2026 年 7 月，英飞凌承接 ams OSRAM 的非光学模拟／混合信号传感器业务。AS5047P 等历史型号现在有英飞凌产品页，相关 PDF 也附有归属说明。阅读旧文章时，应同时辨认历史品牌与当前提供者。

## 相关业务与技术路线

TLE5012B 是数字 GMR 角度路线的代表。官方介绍说明，它通过集成磁阻元件测得正弦与余弦分量，在内部计算磁场方向，并通过 SSC 等接口输出。不同后缀涉及接口预配置，因此完整料号对硬件与软件都重要。[TLE5012B-E5000 产品页](https://www.infineon.com/part/TLE5012B-E5000)

TLE5501 等 TMR 角度器件采用模拟正余弦输出，为外部采样和计算提供输入。相对于直接读取数字角度，系统设计需要更多关注后端 ADC、输入共模、采样同步和模拟布线。两种路线应比较整条测量链的资源与误差。

新增的原 ams 磁角度产品则保留熟悉的 AS 型号。AS5047P 以在轴霍尔测量、DAEC 动态补偿和多种输出服务电机控制。业务整合扩大了目录，但不使不同系列变成统一寄存器或引脚的产品。

## 产品系列与代表型号

| 方向 | 代表型号 | 需要核对的差异 |
| --- | --- | --- |
| 数字 GMR 角度 | TLE5012B | SSC 与其他输出、后缀预配置 |
| 模拟 TMR 角度 | TLE5501 | 正余弦输出、后端采样与安全资料 |
| 历史 ams 在轴霍尔 | AS5047P | 14 位绝对角度、ABI／UVW／PWM |
| 评估工具 | Sensor 2GO 等 | 芯片版本、软件、通信协议 |
| 磁位置选型 | XENSIV 官方选型指南 | 原理、封装、温度与产品状态 |

产品页中的状态值得单独检查。例如本次查阅的 TLE5012B-E5000 页面标为“not for new design”。这属于该具体条目的当前状态，不应扩大成整个 TLE5012 系列停产，也不应被忽略后继续默认推荐给新设计。

## 官方资料

- [英飞凌官网](https://www.infineon.com/)
- [XENSIV 磁位置传感器选型指南](https://www.infineon.com/assets/row/public/documents/24/66/infineon-xensiv-magnetic-position-sensors-productselectionguide-en.pdf)
- [TLE5012B-E5000 官方产品页](https://www.infineon.com/part/TLE5012B-E5000)
- [TLE5012B 官方数据手册](https://www.infineon.com/dgdl/Infineon-TLE5012B_Exxxx-DataSheet-v02_01-EN.pdf?fileId=db3a304334fac4c601350f31c43c433f)
- [AS5047P 官方产品页](https://www.infineon.com/part/AS5047P)
