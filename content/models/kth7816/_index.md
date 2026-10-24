---
title: "KTH7816"
description: "KTH7816是KTH78霍尔角度系列成员；接口和编码格式按具体封装及后缀区分。"
wiki: true
wiki_type: "model"
wiki_rank: 213
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "数字角度"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7816"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth78"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7816%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7816 官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 编码格式 | N：16位；C：12位角度+4位CRC，按封装后缀 |
| QN16输出 | 官网N-QN16：SSI、PWM、SPI、ABZ |
| SOP8输出 | PWM、SPI；N/C版本数据格式不同 |
| 工作供电 | 手册3.3V模式3.0～3.6V；5V模式4.5～5.5V，分别使用 |
| 磁场条件 | 关键表30～150mT，典型60mT |
| 典型工作电流 | 11.6mA@3.3V；5V表另核对 |
| 启动时间 | 典型1ms，关键表 |
| 数据更新/表列延时 | 1µs；匀速补偿与加减速响应不能混用 |
| INL | 手册关键表±0.35°，按安装和校准条件 |
| 温度漂移 | 手册关键表0.002°/°C，保留原测试口径 |
| 最高转速 | 手册关键表120000rpm，不能与任意滤波设置拼接 |
| 噪声 | 0.015°（1σ），PDF关键表 |
| 温度 | −40～125°C |
| 封装 | QFN-16L或SOP8 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7816%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 7816怎样在两种封装中选

QN16目录列SSI、PWM、SPI与ABZ，SOP8则主要保留PWM与SPI。选择封装前先确定主控需要哪一种位置输入，避免缩小封装之后才发现所需增量输出没有引脚。

## N与C的解析方式

16位纯角度与12位角度加4位CRC在软件中使用不同解码方式。帧长度相同也不能使用同一缩放系数；CRC应先校验，再按有效角度位数换算。

## 磁场与动态表现

有效磁场需覆盖全圈、最大气隙与最高温的最弱点。1µs刷新、滤波响应与输出传输分别决定数据新鲜程度；匀速延时补偿不能被写成快速反转时也没有误差。

## 接入验收

按实际封装确认测试脚和未用脚要求，记录零点、方向、ABZ计数口径与PWM模式。测试上电首次读数、跨零连续性、正反转和参数保存；不要只以SPI通信正常判定整个编码器反馈链已通过。

## 官方资料

- [KTH7816 官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

- [KTH7816 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7816%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
