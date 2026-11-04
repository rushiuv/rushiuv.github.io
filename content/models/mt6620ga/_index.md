---
title: MT6620GA
wiki: true
wiki_type: model
model_card: true
wiki_rank: 400
lastmod: '2026-10-30'
catalog_type: 磁栅位置与角度
catalog_form: 芯片
wiki_category: 磁栅位置与角度
description: MT6620GA 是TSSOP24封装的离轴磁栅/磁环读头，基于固定极距Hall阵列感知周期磁场，适合多极旋转与线性位置链路。
official_url: https://www.novosns.com/product/MT6620GA-ACH-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6620
- MT6620GA
- MT6620GA-ACH-R
- MT6620GA-AKT-R
- MT6620GA-STD-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Ksm5bgqAnoaChwx3v5Yc50Qpn2b.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/e289152f5761c653.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/EWtpbqabtoN8Ljx1J6qcsJmknHd.png
series_parent: mt6620
---

## 核心参数与配置

以下为官网目录中 **MT6620GA-ACH-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 霍尔角度/位置编码器 |
| 目录类别 | 工业编码器 |
| 封装 | TSSOP24 |
| 目录等级 | Industrial |
| 数字接口 | SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 16bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~63pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~2500ines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <192,000/N；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 5us；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 固定极距决定磁尺和磁环

官网说明内置阵列面向2mm极距。磁环直径、极对数和读头半径必须与该空间周期配合，磁尺则要核对极距和移动方向；不能把任意多极环放到上方就沿用同一位置比例。

## 周期内角度与全行程位置分开

读头先由正余弦信号解析电气周期。单周期细分不独自识别跨过了多少个磁极，上电唯一位置还需要系统说明极号、参考或其他粗位置来源；目录16bit不能改写成任意磁环的全圈绝对精度。

## 最高转速必须带上磁极数

目录转速字段使用含N的表达式，说明机械速度和磁极事件频率有关。应按实际磁环、输出线数与接收器带宽换算脉冲密度，再验证高速往返和参考建立，不直接复制一个脱离N的最高转速。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6620GA-ACH-R](https://www.novosns.com/product/MT6620GA-ACH-R) | TSSOP24；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Ksm5bgqAnoaChwx3v5Yc50Qpn2b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Rb6dbaacgobq1RxO5EBcLEcYnJg.pdf) |
| [MT6620GA-AKT-R](https://www.novosns.com/product/MT6620GA-AKT-R) | TSSOP24；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Ksm5bgqAnoaChwx3v5Yc50Qpn2b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Rb6dbaacgobq1RxO5EBcLEcYnJg.pdf) |
| [MT6620GA-STD-R](https://www.novosns.com/product/MT6620GA-STD-R) | TSSOP24；Industrial；Active；[中文手册](https://wwwapi.novosns.com/dms/userfiles/docs/Ksm5bgqAnoaChwx3v5Yc50Qpn2b.pdf) · [英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Rb6dbaacgobq1RxO5EBcLEcYnJg.pdf) |

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

这些OPN的目录参数相同，寄存器预设、包装和其他功能仍应按完整订货号确认。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6620GA-ACH-R)
- [MT6620_Rev.1.0_CN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Ksm5bgqAnoaChwx3v5Yc50Qpn2b.pdf)
- [MT6620_Rev.1.0_EN.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Rb6dbaacgobq1RxO5EBcLEcYnJg.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
