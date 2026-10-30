---
title: NSM350x系列
wiki: true
wiki_type: model
catalog_type: 数字角度
catalog_form: 芯片
wiki_rank: 91
seed_count: 2
lastmod: '2026-10-30'
description: NSM350x 是纳芯微双码道霍尔游标磁编码器系列，面向中空或离轴绝对角度测量。
official_url: https://www.novosns.com/product/NSM3502-IND-Q1QWAR
related_companies:
- 纳芯微
wiki_category: 双码道与绝对位置
document_version: 公开资料核对：2026-10-16；文件版本见下载件
model_card: true
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/AgawbuVmLoE8A2xS2CpcwMzonPf.pdf
datasheet_label: NSM3502数据手册（PDF）
catalog_level: 系列
---

NSM350x采用双码道Hall阵列与游标关系取得中空／离轴绝对位置。目前本地目录资料可确认NSM3502的IND与STD两种完整订货配置，不能把它们当成后缀可随意删除的同一版本。

## 已确认型号与核心异同

| 完整订货号 | 目录封装／等级 | 核心输出 | 尚未展开的差异 |
| --- | --- | --- | --- |
| NSM3502-IND-Q1QWAR | QFN48；Industrial | 22bit；4-wire SPI；12bit PWM | IND预设与适用配置需核对 |
| NSM3502-STD-Q1QWAR | QFN48；Industrial | 目录所列参数相同 | STD预设与适用配置需核对 |


## 先配磁环，再配输出

NSM3502介绍中的主码道对应2mm极距，两个码道的几何及周期关系需一起匹配。细分位数高只说明位置表达，不能证明偏心和气隙变化下的组合消歧一定正确。

代表IND配置目录列ABZ 1～65536lines可编程、UVW 1～64对极可编程、转速＜24000rpm、匀速传播延迟5µs、−40～125°C及3.3～5.0V供电；这些是目录条件，不能将所有最大输出能力与最高速度无条件组合。

## IND和STD怎样落实到设计

现有目录字段未显示差别，不证明寄存器预设、校准、封装内设置或资格完全一致。完整OPN、磁环参数和配置文件应一起确定，样机检查整圈连续性、跨零和上电绝对位置。

更多完整订货行与原厂链接见[NSM3502型号页](/models/nsm3502/)。其他NSM350x成员的规格需以各自原厂资料为准。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://www.novosns.com/product/NSM3502-IND-Q1QWAR)
- [NSM3502数据手册（PDF）](https://wwwapi.novosns.com/dms/userfiles/docs/AgawbuVmLoE8A2xS2CpcwMzonPf.pdf)
