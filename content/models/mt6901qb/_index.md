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

## 公开资料缺口直接保留

官网本次目录与代表详情没有提供数据手册PDF，不能创建一个猜测地址。当前可记录目录参数与系统描述，正式画图、寄存器配置和线圈设计仍需取得对应版本手册。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6901QB-STD](https://www.novosns.com/product/MT6901QB-STD) | QFN32；Industrial；Active；官网当前未列可核验PDF |

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

官方当前目录及代表详情的数据手册字段为空；不制造PDF链接。

目录已列参数在这些OPN间未显示不同，不代表寄存器预设、包装或未列功能完全相同。

官网目前没有提供此型号的PDF链接，参数暂以公开产品页和目录为界，不生成下载地址。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6901QB-STD)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
