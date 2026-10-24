---
title: "KTH7813"
description: "KTH7813是KTH78霍尔角度系列成员；接口和编码格式按具体封装及后缀区分。"
wiki: true
wiki_type: "model"
wiki_rank: 211
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "数字角度"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7813"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth78"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7813%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7813 官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位绝对角度 |
| 输出 | SPI、ABZ、UVW，官网QN16对应行 |
| 工作供电 | 公开PDF5V关键表：4.5～5.5V；3.3V模式另核对 |
| 典型工作电流 | 13.6mA@5V，公开PDF关键表 |
| 磁场条件 | PDF30～150mT、典型60mT；官网另一表列15～150mT，保留差异 |
| 噪声口径 | 官网新表0.004°（1σ）；下载PDF关键表0.015°，不能当成同一条件 |
| 启动/延时 | PDF典型1ms启动、表列1µs延时 |
| INL/温漂 | PDF±0.35°、0.002°/°C，按对应条件 |
| 最高转速 | PDF120000rpm，适用配置另核对 |
| 温度/封装 | 官网−40～125°C；QFN-16L |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7813%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 与7812比较要先统一表

KTH7813在官网新选型表中以低噪声与7812区分，但下载手册的关键表仍列0.015°。本页将两种口径同时列出，不能从新表拿最低噪声、再从旧手册拿另一带宽，拼成一个未经确认的工作点。

## 输出用途与配置

SPI用于绝对位置和配置，ABZ提供增量计数，UVW提供换相状态。正式设计应依据7813自己的引脚和寄存器，不以接口名称相同证明与7812全部兼容。

## 磁路条件的区别

官网表和PDF对工作磁场下限还有15mT与30mT差异。最低场强将影响噪声和信号质量，设计气隙前应先确认所用版本；不能把读得到角度当成已满足最低场强条件。

## 验证重点

在相同磁体、供电和滤波下记录静止噪声、整圈误差与动态响应，再核对全温及装配偏移。若以低噪声作为选型理由，验收报告需注明其来自哪份资料、什么配置，以及实物测试结果。

## 官方资料

- [KTH7813 官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

- [KTH7813 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7813%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
