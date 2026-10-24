---
title: SMD-01B
description: SMD-01B把光源和光检测/模拟处理封在一起，以反射码尺的相对运动形成模拟周期信号。它连接的是光学前端与外部细分链，不是开机即给全行程绝对位置的完整编码器。
wiki: true
wiki_type: model
wiki_rank: 300
seed_count: 0
lastmod: '2026-10-24'
related_companies:
- 精工NPC
wiki_category: 光学反射编码
catalog_vendor: 精工NPC
catalog_type: 光学反射编码
catalog_form: 芯片
search_aliases:
- SMD-01B
- smd 01b
official_url: https://www.npc.co.jp/products/438
document_version: 日文DE220185-J002，2024.04，第1/3/4页
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 形态 | LED与OEIC同封装的反射式增量光编码器IC，需配码尺 |
| 信号 | 模拟A/B及反相信号；20µm信号周期，不是20µm整机精度 |
| 供电 | SWV=H时3.13～5.25V；其它配置按推荐条件表，不笼统写所有模式可3.3V |
| 速度／温度 | 推荐条件0～2m/s、−20～60°C |
| 电流 | 12.2mA典型：5V、27°C、SWL1=H且SWL2=H；亮度设置会改变电流 |
| 封装 | HCOB14，5.3×4.3×1.68mm；完整公差另见尺寸图 |
| 细分边界 | 手册首页5µm由20µm周期与A/B构成；更细分辨率依赖外部插值，不自动提高准确度 |

## 产品功能与测量链

SMD-01B把光源和光检测/模拟处理封在一起，以反射码尺的相对运动形成模拟周期信号。它连接的是光学前端与外部细分链，不是开机即给全行程绝对位置的完整编码器。

## 接入与验证

先核码尺反射/非反射条件、安装间距与SWV/SWL设置，再保存A/B原始波形。2m/s除以20µm得到100kHz周期率，只是单位换算；可用精度仍由幅相、噪声、插值与安装共同验证。对应[光学信号链](/topics/guides/optical-signal-chain/)及[直线电机](/applications/linear-motor/)。

## 官方资料

- [日文产品页](https://www.npc.co.jp/products/438)
- [日文数据手册DE220185-J002](https://www.npc.co.jp/filecontents/file/1121/file/)
- [日文应用笔记ANJ240010-J001](https://www.npc.co.jp/filecontents/file/1150/file/)
