---
title: "iC-MA3"
description: "带增益调节的霍尔角度前端，向后端提供正余弦模拟信号。"
wiki: true
wiki_type: "model"
wiki_rank: 249
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["iC-Haus"]
wiki_category: "模拟角度"
catalog_vendor: "iC-Haus"
catalog_type: "模拟角度"
catalog_form: "芯片"
search_aliases: ["iC-MA3"]
official_url: "https://www.ichauschina.com/products/enc_mag.htm"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 输出 | 模拟正余弦，非SPI绝对角度码 |
| 电源 | 3.0～5.5V |
| 信号链 | 四霍尔阵列、自动增益及失磁提示 |
| 资料范围 | 采用官方中文产品摘要，完整规格以原厂授权手册为准 |
| 最高转速 | 公开产品摘要列60000rpm，需匹配输出带宽 |
| 输出配置 | 差分正余弦，或单端信号并带参考和增益信息 |
| 可选项 | 引脚选择输出电平、功耗模式与带宽 |
| 监控 | 数字失磁提示及模拟增益信号，供磁场强度监测 |

参数依据：[原厂产品页或对应资料](https://www.ichauschina.com/products/enc_mag.htm)。

## 产品功能与测量链

iC-MA3提供经过增益调节的模拟正余弦信号，后级仍要完成采样与角度计算。自动增益用于调节信号幅度，不能直接视为整机角度非线性校准。

## 接入与配置

3.0～5.5V是器件供电条件，后端ADC还需匹配输出共模与摆幅。若使用差分输入，应同时检查两臂电压，不仅看两臂相减后的波形。

## 使用与验证

失磁提示与可用角度范围需按手册验证。量产评估应保存最小磁场下的幅度、相位和噪声，避免把增益拉高后的噪声增加误认成ADC分辨率不足。

## 官方资料

- [iC-MA3 官方资料](https://www.ichauschina.com/products/enc_mag.htm)
