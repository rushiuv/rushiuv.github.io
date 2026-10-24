---
title: KTD-S100B-1609-LP2A-BAQ
description: 这是POSITAL免电池多圈套件的一种明确订货配置。原厂系列说明Wiegand脉冲给断电计圈供能；正常位置接口仍有供电要求，不能把“免电池”理解成整条串行接口无需电源。
wiki: true
wiki_type: model
wiki_rank: 300
seed_count: 0
lastmod: '2026-10-24'
related_companies:
- POSITAL
wiki_category: 免电池多圈套件
catalog_vendor: POSITAL
catalog_type: 免电池多圈套件
catalog_form: 编码模块
search_aliases:
- KTD-S100B-1609-LP2A-BAQ
- posital ktd s100b 1609
official_url: https://www.posital.com/en/products/kit-encoders/KTD-S100B-1609-LP2A-BAQ/3440429
document_version: 原厂英/德文订货型号页，核对2026-10-24
model_card: true
product_image: images/wiki/global-posital-ktd-s100b-1609-20261024.webp
product_image_source: https://www.posital.com/en/products/kit-encoders/KTD-S100B-1609-LP2A-BAQ/3440429
product_image_caption: 原厂为该订货配置展示的产品图
---


## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 产品状态 | 页面生命周期列Lab Sample；不能按已量产可采购承诺介绍 |
| 单圈／多圈 | 此订货号单圈9bit、多圈16bit；不是25bit角度准确度 |
| 技术／接口 | TMR磁测量；SSI with Preset，RS422输出；页面列错误/警告位和寄存器诊断 |
| 接口周期 | ≥50µs；不等于所有内部测量都在该周期完成 |
| 供电／功耗 | 4.5～5.5VDC；57mA（5V），功耗≤0.3W |
| INL条件 | 页面列±0.0878°（≤12bit），室温校准后；该9bit成员仍需区分码宽与INL定义 |
| 环境／结构 | −40～105°C，IP30，轮毂式套件；整机EMC由集成方案确认 |

## 产品功能与测量链

这是POSITAL免电池多圈套件的一种明确订货配置。原厂系列说明Wiegand脉冲给断电计圈供能；正常位置接口仍有供电要求，不能把“免电池”理解成整条串行接口无需电源。

## 接入与验证

此型号页面明确是Lab Sample，不能作为既成量产替换推荐。恢复位置还应验证断电移动、反转、上电首帧、Preset和圈数边界。先读[免电池多圈的状态边界](/topics/guides/batteryless-multiturn/)，再将应用所需配置与量产供货状态向原厂逐项确认。

## 官方资料

- [英文订货型号页](https://www.posital.com/en/products/kit-encoders/KTD-S100B-1609-LP2A-BAQ/3440429)
- [德文Wiegand原理](https://www.posital.com/de/wiegand-sensors)
- [德文Kit产品族](https://www.posital.com/de/products/kit-encoders)
