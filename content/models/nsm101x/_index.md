---
title: "NSM101x系列"
description: "三线霍尔开关与锁存器系列，三款成员的触发逻辑不同。"
wiki: true
wiki_type: "model"
wiki_rank: 246
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["纳芯微"]
wiki_category: "磁开关"
catalog_vendor: "纳芯微"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["NSM1011","NSM1012","NSM1013"]
official_url: "https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf"
document_version: "官方公开 PDF，英文版 V1.0；核对：2026-10-24"
model_card: true
datasheet_url: "https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf"
datasheet_label: "NSM101x 官方数据手册（英文版 V1.0）"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 成员区别 | NSM1011单极、NSM1012全极、NSM1013锁存 |
| 供电 | 常规版2.7～28V；低功耗版3.1～28V，依具体版本 |
| 输出 | 开漏，需外部上拉 |
| 温度 | −40～150°C；阈值、极性、输出相位及封装须逐项选 |

参数来源：本页所列[原厂产品资料与手册](https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf)。

## 工作方式与型号定位

NSM1011、1012和1013分别对应单极、全极与锁存逻辑。它们都输出状态，但对磁体极性、移开以及反向磁场的响应不同，不能仅按阈值大小互换。

## 安装、接口与配置

开漏输出需要外部上拉，电阻值要兼顾电流、线缆电容和边沿速度。常规版与低功耗版的供电下限不同，最低电流和最高响应速度也应按所选版本同时核对。

## 校准与选型验证

测量动作点、释放点及磁滞时，应注明磁场方向和运动路径。锁存器的复位需要相反极性的条件，磁体移开不一定释放；验收还应包含上电状态、温度及最短事件持续时间。

资料版本：当前保留远端修复的原厂NSM101x英文V1.0下载入口；单极、全极和锁存逻辑仍须分别阅读对应成员，不能将锁存翻转条件扩展到全系列。

## 官方资料

- [NSM101x系列 官方资料](https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf)
