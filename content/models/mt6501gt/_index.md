---
title: MT6501GT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 421
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6501GT 是MT6501汽车AMR角度系列的TSSOP16型号，提供与SOP8 CT不同的封装资源；模拟输出曲线和具体预设按完整订货号确认。
official_url: https://www.novosns.com/product/MT6501GT-ABD-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6501
- MT6501GT
- MT6501GT-ABD-R
- MT6501GT-ADD-R
- MT6501GT-ADDC-R
- MT6501GT-P1KB-R
- MT6501GT-PB1-R
- MT6501GT-PGQ1-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/c7e90e5222cb61b2.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/ABPwbOVGbocqAPxpD51c2RJbn8b.png
---

## 核心参数与配置

以下为官网目录中 **MT6501GT-ABD-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 汽车角度传感器 |
| 封装 | TSSOP16 |
| 目录等级 | Automotive |
| PWM输出 | Yes；官网目录标注，适用于上述订货配置 |
| Digital Interface | SPI；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | No；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | No；官网目录标注，适用于上述订货配置 |
| Angle Accuracy | <±1.5°；官网目录标注，适用于上述订货配置 |
| Analog Output Curve Programming | Any 4-point Programming；官网目录标注，适用于上述订货配置 |
| Redundant Package Option | Yes；官网目录标注，适用于上述订货配置 |
| Output Overvoltage Protection | 18V；官网目录标注，适用于上述订货配置 |
| ISO26262 | No；官网目录标注，适用于上述订货配置 |
| Automotive Qualification | Yes；官网目录标注，适用于上述订货配置 |
| Operating Temperature (℃) | -40~150；官网目录标注，适用于上述订货配置 |
| 目录供电 | 4.5~5.5；官网目录标注，适用于上述订货配置 |
| Magnetic Sensing Principle | AMR；官网目录标注，适用于上述订货配置 |

## TSSOP16成员独立核对引脚

系列参数相同不表示CT与GT接线相同。应按GT引脚表核对供电、编程与输出的组合，尤其在涉及系列冗余选项时逐项确认内部通道和外部连接，不从引脚数推断独立冗余。

## 曲线编程服务接收端需求

四点编程描述输出映射能力，接收端还需确定有效电压窗口、滤波和异常判据。对节气门或踏板等机构，应在全行程验证两端裕量及回程一致性，不能以一个角度点的输出正常判定完成。

## 车规标签与系统安全证据分开

官网汽车资格字段与ISO26262字段分别列示，不能以汽车应用定位推出系统安全等级。GT的具体OPN和温区、保护条件以对应手册为准，旧预设生命周期单独保留。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Not Recomended for New Designs | MT6501GT-ABD-R |
| Active | MT6501GT-ADD-R、MT6501GT-ADDC-R、MT6501GT-P1KB-R、MT6501GT-PB1-R、MT6501GT-PGQ1-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6501GT-ABD-R](https://www.novosns.com/product/MT6501GT-ABD-R) | TSSOP16；Automotive；Not Recomended for New Designs；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501GT-ADD-R](https://www.novosns.com/product/MT6501GT-ADD-R) | TSSOP16；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501GT-ADDC-R](https://www.novosns.com/product/MT6501GT-ADDC-R) | TSSOP16；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501GT-P1KB-R](https://www.novosns.com/product/MT6501GT-P1KB-R) | TSSOP16；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501GT-PB1-R](https://www.novosns.com/product/MT6501GT-PB1-R) | TSSOP16；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |
| [MT6501GT-PGQ1-R](https://www.novosns.com/product/MT6501GT-PGQ1-R) | TSSOP16；Automotive；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf) |

“Not Recommended for New Designs”表示该完整订货号不推荐用于新设计，不代表全部预设停产。请结合表内仍为Active的版本核对供应与配置。

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

同型号不同预设的生命周期可能不同，供货与新设计适用性按具体OPN查询。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6501GT-ABD-R)
- [DatasheetCN)MT6501_Rev.1.9.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/EXBnbYCABoa0IFxcmYhc5eC5nXf.pdf)
- [MT6501_Rev.1.9.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Mt9bb7hEvoTXOex3H3gcHjlwn0a.pdf)
- [汽车角度传感器目录](https://www.novosns.com/automotive-angle-sensor)
