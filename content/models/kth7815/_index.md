---
title: "KTH7815"
series_parent: "kth78"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 127
seed_count: 1
lastmod: "2026-10-24"
description: "KTH7815是KTH78系列的16位工业霍尔角度器件。公开资料存在不同接口口径，须以具体订货号和适用手册确认。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth7815-datasheet-figure.jpg"
product_image_caption: "KTH7815 手册中的 KTH78 系列磁体布置示意，输出与精度依具体型号"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位，按实际后缀/帧格式确认 |
| 官网新表输出 | QN16和SOP8对应行均列PWM、SPI |
| 下载PDF QN16引脚 | SPI、ABZ及反相ABZ；与官网新表存在冲突 |
| 下载PDF SOP8引脚 | PWM、SPI；不能沿用QN16增量输出 |
| 工作供电 | 手册3.3V模式3.0～3.6V；5V模式4.5～5.5V，分别使用 |
| 磁场条件 | 关键表30～150mT，典型60mT |
| 典型工作电流 | 11.6mA@3.3V；5V表另核对 |
| 启动时间 | 典型1ms，关键表 |
| 数据更新/表列延时 | 1µs；匀速补偿与加减速响应不能混用 |
| INL | 手册关键表±0.35°，按安装和校准条件 |
| 温度漂移 | 手册关键表0.002°/°C，保留原测试口径 |
| 最高转速 | 手册关键表120000rpm，不能与任意滤波设置拼接 |
| 噪声差异 | 官网新表0.059°、旧表0.24°；下载PDF关键表0.015°，三种条件未统一 |
| 磁场差异 | PDF30～150mT；官网另一表15～150mT |
| 温度/封装 | −40～125°C；QFN-16L、SOP8，按订货号 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 先处理接口冲突再画电路

KTH7815官网新表将QN16与SOP8都列为PWM/SPI，而下载PDF的QN16引脚表列有ABZ及反相信号。这里保留原始差异，不能把所有接口并成同一订货版本同时具备。正式设计需要原厂确认适用料号与手册。

## 噪声不能挑最小数字

同页两张表和下载PDF分别出现0.059°、0.24°与0.015°。这些数值未在同一配置和带宽条件下统一，本页不据此作优劣排名。若项目依靠高带宽或低噪声，必须先锁定配置并用实物核对。

## 封装连接需要分别处理

SOP8与QN16的接口和测试脚连接要求不同。替换封装不仅是焊盘变化，控制器连接、模式和可用输出也需要重查。不能把QN16的增量用途直接移到SOP8。

## 样机验证顺序

先确认丝印、完整订货号、引脚与报文，再测磁场范围、静止噪声和阶跃响应。完成这一步后再测全圈误差与温漂；在资料版本尚未收敛前，不对外承诺组合后的“最佳性能”。

## 官方资料

- [KTH7815 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [KTH7815 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7815%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- [系列资料中的接口版本提示](https://conntek.github.io/products/encoder/kth78)
