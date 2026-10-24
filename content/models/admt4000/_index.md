---
title: "ADMT4000"
wiki: true
wiki_type: "model"
wiki_rank: 75
seed_count: 2
lastmod: "2026-10-24"
description: "ADMT4000 是 ADI 的无电源多圈磁位置传感器，断电期间仍能记录磁场旋转圈数，上电后通过 SPI 读出多圈绝对位置。"
official_url: "https://www.analog.com/en/products/admt4000.html"
related_companies: ["ADI"]
wiki_category: "多圈与断电位置"
document_version: "ADMT4000 Rev.C，2026-07；本次核对2026-10-24"
model_card: true
datasheet_url: "https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf"
datasheet_label: "ADMT4000 数据手册 Rev.C"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 计圈方式 | 器件无电源时仍记录外部磁场转数 |
| 多圈范围 | 46 圈 |
| 测量更新率 | 100 kSPS |
| 角度精度 | 典型±0.25°；理想磁系统、25mT；完整范围见下列条件 |
| 工作磁场 | 16～31 mT |
| 芯片供电 | 3.3V芯片供电；SPI逻辑电平1.7～5V，按Rev.C |
| 结温范围 | −40～150°C |
| 封装 | TSSOP-24；内置温度传感器 |
| 角度精度条件 | Rev.C表1：理想磁系统、25mT时典型±0.25°，最小/最大列为−0.90°/+0.90°；不把典型值当全条件保证 |
| 角度噪声 | 25°C、25mT：IIR关闭0.25° RMS、开启0.03° RMS，按Rev.C表1 |
| SPI逻辑电平 | Rev.C特性页列1.7～5V，与芯片3.3V供电分开 |

参数依据：[原厂产品页或对应资料](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)。

## 产品功能与测量链

ADMT4000的重点是断电期间仍记录磁体转过的圈数。它解决的是多圈位置保持，单圈方向检测、圈数边界和上电后的数字读数仍需一起验证。

## 接入与配置

46圈是可表达的多圈范围，不能理解为无限计圈。磁体安装须使敏感点的工作场落入16～31mT；断电计圈功能也不能脱离磁场条件单独保证。

## 使用与验证

测试应覆盖无电源正反转、范围边缘往返及上电读取的一致性。100kSPS是测量更新率，不能直接当作SPI每次事务都拿到独立新样本的保证。

## 版本与待核项目

本次按原厂Rev.C（2026年7月）重读表1，纠正把典型±0.25°当成完整精度范围的读法；SPI电平下限由旧卡的1.8V更新为当前手册的1.7V。磁场窗口也带温度系数，不应把25°C磁场条件无条件扩展到全温。

## 官方资料

- [ADMT4000 原厂资料入口](https://www.analog.com/en/products/admt4000.html)
- [官网文档入口（官方入口）](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)
- [ADMT4000 数据手册 Rev.C（官方 PDF）](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)
