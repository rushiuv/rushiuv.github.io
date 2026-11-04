---
title: MT6901QB
wiki: true
wiki_type: model
model_card: true
wiki_rank: 410
lastmod: '2026-10-30'
catalog_type: 电涡流角度
catalog_form: 芯片
wiki_category: 电涡流角度
description: MT6901QB 是QFN32封装的电涡流感应双码道游标角度编码器，系统由定子PCB、激励/接收线圈与转子结构共同构成，不属于磁体式AMR或Hall传感器。
official_url: https://www.novosns.com/product/MT6901QB-STD
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6901
- MT6901QB
- MT6901QB-STD
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
product_image: /images/wiki/novosns/5018253ad18ae2e7.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/JNVsb8r5AosZ30xKUSJcuG3cn9f.png
series_parent: mt6901
---

## 核心参数与配置

以下为官网目录中 **MT6901QB-STD** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | 电涡流感应游标编码器 |
| 目录类别 | 工业编码器 |
| 封装 | QFN32 |
| 目录等级 | Industrial |
| 数字接口 | 4-wire SPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 21bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 12bit；官网目录标注，适用于上述订货配置 |
| UVW增量输出 | 1~16pole pairs programmable；官网目录标注，适用于上述订货配置 |
| ABZ增量输出 | 1~16384lines programmable；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <12,000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 10us；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## 传感器包括定转子PCB几何

官网明确基于电涡流感应，定子上有激励、接收线圈和芯片，转子上有对应线圈。板层、线圈几何、气隙及转子材料都参与位置测量，不能只选一颗芯片就沿用磁编码器的磁体安装方式。

## 双码道提供游标位置关系

游标绝对位置来自两个码道信号的组合，粗位置与周期内角度需协调。应验证全圈唯一性、码道过渡和上电状态，再看细分码宽；21bit目录字段不单独证明线圈系统的有效精度。

## 完整手册与设计条件

官网目录与产品详情暂无独立数据手册PDF；引脚设计、寄存器配置和线圈实现需使用对应版本的完整手册。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6901QB-STD](https://www.novosns.com/product/MT6901QB-STD) | QFN32；Industrial；Active；官网当前未列可核验PDF |

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

官网目录与产品详情暂无该型号公开数据手册下载项。

这些OPN的目录参数相同，寄存器预设、包装和其他功能仍应按完整订货号确认。

官网暂无此型号PDF下载入口，详细电参数与时序请向原厂索取对应版本。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6901QB-STD)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
