---
title: "KTH7803"
description: "KTH7803是KTH78霍尔角度系列成员；接口和编码格式按具体封装及后缀区分。"
wiki: true
wiki_type: "model"
wiki_rank: 210
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "数字角度"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7803"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth78"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位，官网N-QN16版本 |
| 输出 | SSI、PWM、SPI、ABZ，官网对应完整型号行 |
| 工作供电 | 3.0～5.5V，官网目录 |
| 工作电流 | 目录11.6mA，条件以正式电气表为准 |
| 噪声 | 官网新表0.004°（1σ），不是全温绝对精度 |
| 启动/刷新 | 官网典型1ms启动；1MHz角度刷新 |
| 磁路 | 官网列支持离轴；系列磁场范围30～150mT，成员手册待核 |
| 温度 | 官网新表−40～150°C |
| 封装 | QFN-16L |
| 证据层级 | 本页新增数值来自型号选型行；未取得独立7803正式手册，不套用7801全部保证值 |

参数依据：[原厂产品与型号选型表](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)。

## 7803的比较重点

官网将KTH7803与7801分列，并为7803给出更低的噪声数字。噪声是静止输出波动的统计量，不能据0.004°直接声称绝对精度或温漂也优于同系列其他成员。

## 接口按完整型号确认

当前目录可直接核对的型号为QN16版本。SSI、PWM、SPI和ABZ的复用与同时工作关系仍需对应引脚表，不因系列中存在SOP8就自动构造7803的SOP8订货版本。

## 低噪声需要带宽条件

低噪声与滤波配置有关。应用若要求快速转动或反转，应同时确认阶跃响应、匀速补偿和内部刷新，不能用1MHz刷新率推导1MHz位置带宽。

## 正式设计前的资料缺口

仍需独立手册收敛具体供电模式、接口时序、ABZ设置、磁场及温度保证条件。当前可用于方案筛选；与7801直接替换前，要逐项复核引脚、协议和工作等级。

## 官方资料

- [KTH7803 官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
