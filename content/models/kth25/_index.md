---
title: KTH25系列
description: 高压双极锁存霍尔系列，适合转子磁极切换与位置事件检测。
wiki: true
wiki_type: model
wiki_rank: 204
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 磁开关
catalog_vendor: 昆泰芯
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- KTH2502
- KTH25系列
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/automotiveHvdlHallEffectSensor/index.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

KTH25采用双极锁存逻辑。目录列QA、QB、QC磁阈值档，完整型号还需包含温度与封装；不能把档位当成独立基础型号。

## 型号与核心异同

| 阈值档（非完整料号） | 动作／释放场 | 共同输出 | 选型区别 |
| --- | --- | --- | --- |
| QA | 15／−15Gs | 开漏 | 低门限；正负方向按封装确认 |
| QB | 30／−30Gs | 开漏 | 中间门限；正负方向按封装确认 |
| QC | 60／−60Gs | 开漏 | 较高门限；正负方向按封装确认 |

## 共同条件与参数依据

- **目录供电**：2.7～36V；官网介绍另有32V上限，正式设计按具体手册
- **目录电流**：2.7mA
- **目录频率**：30kHz
- **输出**：开漏；官网介绍列最大30mA灌电流，需对应负载条件
- **温度**：−40～125°C
- **封装**：SOT-23-3L、TO-92S，磁极性按具体图示

## 锁存与接近开关的区别

KTH25使用相反极性的磁场完成动作和释放，适合交替磁极经过的转子位置检测。磁体只靠近后又移远，未必满足反向释放条件，因此不能按普通全极接近开关的逻辑使用。

## 高压输入与输出负载

供电上限、输出耐压和输出灌电流是不同约束。开漏端需要按负载电压和电流设计上拉，输出低电平功耗还会随负载增加。官网介绍与选型表的32V/36V差异不能选较大值直接承诺全系列。

## 封装会改变磁极定义

同一个磁场向量，从不同封装标注的敏感面观察会得到不同极性约定。PCB布局和磁体极性需以该完整订货号的封装图为准，不能因为都叫SOT-23就默认引脚与磁极方向一致。

## 验收方式

用正负磁场扫完整迟滞回线，分别记录动作、释放及输出电平。机构测试应覆盖最高转速下的磁极驻留时间、负载电流和温升；目录30kHz不直接等于允许电机机械转速。

## 官方资料

- [KTH25系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/automotiveHvdlHallEffectSensor/index.html)
