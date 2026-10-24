---
title: "VCE2755"
description: "集成AMR与ASIC的18位编码器，提供360°绝对角度及多种位置输出。"
wiki: true
wiki_type: "model"
wiki_rank: 238
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["圣邦微"]
wiki_category: "数字角度"
catalog_vendor: "圣邦微"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["VCE2755"]
official_url: "https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf"
document_version: "官方公开PDF，核对：2026-10-18；版本见下文"
model_card: true
datasheet_url: "https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf"
datasheet_label: "官方公开PDF"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度编码 | 18位，0～360° |
| 输出 | SPI、SSI、ABZ、UVW、PWM，具体引脚组合依封装和订货配置 |
| 供电／温度 | 3.0～5.5V，−40～125°C |
| 动态指标 | 手册标注延时小于2µs、最高18000rpm；系统按相应条件验证 |
| 资料版本 | 2026年1月Rev.A.3，30页 |
| 理想数字码距 | 按18位全圈换算：360°/2^18 ≈ 0.00137329°；计算值，不是准确度保证 |
| INL | 全温±0.3°，工作磁场>300 Gs（30 mT）条件 |
| 有效分辨率口径 | 电气表14位有效角度、0.022°最小分辨率；18位为输出字宽，不混同 |
| 工作电流 | 典型10 mA |
| 瞬态噪声 | 25°C典型0.01° RMS，随滤波带宽配置调整 |
| ABZ | 1～1024脉冲/圈，可配置 |
| 启动时间 | 典型16 ms |
| 封装选择 | SOIC8；TQFN3×3-16JL，输出组合按引脚复用 |

参数来源：本页所列[原厂产品资料与手册](https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf)。

资料定位：VCE2755 Rev.A.3（2026-01）第1、5页及第7页接线图；18位码宽与14位有效角度口径分开。

## 工作方式与型号定位

VCE2755把AMR敏感结构与处理ASIC集成，提供18位360°绝对角度及多种位置输出。它与仅有180°模拟桥的VCE1715在系统职责上不同。

## 安装、接口与配置

SPI、SSI、ABZ、UVW及PWM需要按封装和引脚复用选择，不能认为全部输出都能无条件同时使用。增量脉冲与绝对角度的设置要和控制器位置单位对齐。

## 校准与选型验证

Rev.A.3给出小于2µs延时和18000rpm最高转速，应用应在相应条件下验证。静态准确度、噪声及高速跟踪分别检查；温度与供电范围内的功能正常，也不自动代表每个配置都达到相同误差。

## 官方资料

- [VCE2755 官方资料](https://www.sg-micro.com/rect/assets/db119b16-8eeb-40df-8fd5-74e92fd603fd/VCE2755.pdf)
