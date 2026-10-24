---
title: "MT6826S"
description: "AMR磁角度编码器，提供15位绝对角度及可编程增量输出。"
wiki: true
wiki_type: "model"
wiki_rank: 241
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["麦歌恩","纳芯微"]
wiki_category: "数字角度"
catalog_vendor: "麦歌恩"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MT6826S"]
official_url: "https://www.magntek.com.cn/upload/pdf/202404/MT6826S_Datasheet_Rev.1.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
document_version: "官方公开PDF，核对：2026-10-18；版本见下文"
model_card: true
datasheet_url: "https://www.magntek.com.cn/upload/pdf/202404/MT6826S_Datasheet_Rev.1.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
datasheet_label: "官方公开PDF"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度编码 | 0～360°，15位绝对角度 |
| 输出 | 四线SPI、ABZ、UVW、PWM |
| ABZ | 1～4096线可编程，线数不等于绝对精度 |
| 校准 | 支持客户端自校准，精度提升依原厂流程与磁路条件 |
| 手册 | Rev.1.1，2024年1月 |
| 理想数字码距 | 按15位全圈换算：360°/2^15 ≈ 0.01098633°；计算值，不是准确度保证 |
| 推荐供电 | 3.0～5.5 V，典型3.3～5.0 V |
| 工作电流 | 典型22 mA，最大28 mA；电气表默认4.5～5.5V、−40～125°C |
| 最高转速 | 120,000 rpm |
| 匀速延迟／阶跃 | 典型10 µs匀速延迟；BW=5时100 µs典型阶跃响应；概述2～10 µs另依配置 |
| 出厂INL | 25°C无偏心典型±0.5°；规定全温/最大气隙/偏心条件最大±1.0° |
| 用户校准INL口径 | 概述<±0.07°；第9页电气表典型±0.1°，条件口径不同，不合并 |
| 瞬态噪声 | 典型0.0015° RMS；25°C、ABZ模式、BW=5 |
| PWM／UVW | PWM12位；UVW1～16对极 |
| 工作温度 | −40～125°C |

参数来源：本页所列[原厂产品资料与手册](https://www.magntek.com.cn/upload/pdf/202404/MT6826S_Datasheet_Rev.1.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf)。

资料定位：MT6826S Rev.1.1（2024-01）第1、8～9页；正常工作磁场行误写MT6835，故未据该行给本型号确定场强保证。

## 工作方式与型号定位

MT6826S是15位AMR角度编码器，四线SPI提供绝对角度，ABZ、UVW和PWM服务计数、换相及占空比采集。完整输出组合仍由引脚及配置决定。

## 安装、接口与配置

ABZ的1～4096线可编程，四倍频计数为4～16384步。这与32768个绝对角度码是两种表达，主控不能把线数、边沿数和角度位宽混在一个换算式里。

## 校准与选型验证

客户端自校准应在手册指定磁路和运动条件下进行。校准后的准确度要单独与参考角比较，并在重新上电后核对结果保存；本页依据Rev.1.1，不从MT6835借用21位、转速或校准圈数。

## 官方资料

- [MT6826S 官方资料](https://www.magntek.com.cn/upload/pdf/202404/MT6826S_Datasheet_Rev.1.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf)
