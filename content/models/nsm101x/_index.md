---
title: NSM101x系列
description: 三线霍尔开关与锁存器系列，三款成员的触发逻辑不同。
wiki: true
wiki_type: model
wiki_rank: 246
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 纳芯微
wiki_category: 磁开关
catalog_vendor: 纳芯微
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- NSM1011
- NSM1012
- NSM1013
- NSM101x系列
official_url: https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf
document_version: 官方公开 PDF，英文版 V1.0；核对：2026-10-24
model_card: true
datasheet_url: https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf
datasheet_label: NSM101x 官方数据手册（英文版 V1.0）
catalog_level: 系列
---

NSM101x的首要区别是磁检测逻辑。单极、全极和锁存对磁体移开及反向磁场的响应不同，不能仅按阈值大小替换。

## 型号与核心异同

| 具体型号 | 检测逻辑 | 输出 | 常规／低功耗供电 |
| --- | --- | --- | --- |
| NSM1011 | 单极 | 开漏 | 2.7～28V／3.1～28V，按具体版本 |
| NSM1012 | 全极 | 开漏 | 2.7～28V／3.1～28V，按具体版本 |
| NSM1013 | 锁存 | 开漏 | 2.7～28V／3.1～28V，按具体版本 |

## 共同条件与参数依据

- **温度**：−40～150°C；阈值、极性、输出相位及封装须逐项选

## 接入电路与配置

开漏输出需要外部上拉，电阻值要兼顾电流、线缆电容和边沿速度。常规版与低功耗版的供电下限不同，最低电流和最高响应速度也应按所选版本同时核对。

## 标定与应用验证

测量动作点、释放点及磁滞时，应注明磁场方向和运动路径。锁存器的复位需要相反极性的条件，磁体移开不一定释放；验收还应包含上电状态、温度及最短事件持续时间。

资料版本：当前保留远端修复的原厂NSM101x英文V1.0下载入口；单极、全极和锁存逻辑仍须分别阅读对应成员，不能将锁存翻转条件扩展到全系列。

## 官方资料

- [NSM101x系列 官方资料](https://www.novosns.com/en/datasheet/NSM1011-BNLCA-Q0STDR/NSM101x.pdf)
