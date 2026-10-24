---
title: "KTO9512"
description: "KTO9512 是三通道相位阵游标光学编码器前端，读取匹配码盘，输出差分正余弦和分区信号，供后级细分与绝对位置解算。"
wiki: true
wiki_type: "model"
catalog_type: "光学编码"
catalog_form: "芯片"
wiki_rank: 17
seed_count: 12
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/cursorabsoluteencoder/index.html"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTO9512-D26-QN32%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTO9512 数据手册"
document_version: "公开手册封面日期 2025-08-14，10 个 PDF 页面"
model_card: true
product_image: "/images/wiki/kto9512.webp"
product_image_caption: "图片来源：昆泰芯官方产品页。"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTO9512-D26-QN32%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 器件类型 | 三通道相位阵游标光学编码前端 |
| 配套码盘 | 产品特点列直径26mm光栅码盘 |
| 扫描结构 | 3条模拟轨道+2条数字分区轨道，2位Gray码分区 |
| 位置能力 | 配后级三通道Nonius插值最高24位单圈表达，不是芯片直接数字角度输出 |
| 整体供电 | 4.1～5.5V；数字分区独立供电条件另列1.6～5.5V |
| 供电电流 | 整体表9.5～15mA；数字分区表典型1000µA，不能相加为统一工作点 |
| 跨阻增益 | 0.7～1.4MΩ，典型1.0MΩ |
| 截止频率 | −3dB典型400kHz |
| RMS输出噪声 | 电气表典型0.5mV，不直接等于角度噪声 |
| 光谱范围/峰值 | 400～950nm；峰值灵敏度波长典型680nm |
| 光电流输入 | 允许0～1120nA，按电气表 |
| 输出阻抗/启动 | 内部输出阻抗典型110Ω；上电稳定最大100µs |
| 温度/封装 | −40～125°C；optoQFN-32，5×5×0.9mm |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTO9512-D26-QN32%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 前端输出什么

KTO9512把匹配码盘的明暗信息转换为差分正余弦及分区信号。后级仍需完成同步采样、细分与游标解算，不能直接用SPI读取本芯片24位角度。24位是配套系统的表达能力，不是光电前端独立保证的准确度。

## 三通道与两位分区

三条模拟轨道用于Nonius关系，两条数字轨道提供分区信息以区分重复刻度。码盘轨道几何与芯片感光区需要匹配，不能用任意26mm码盘替换；直径相同并不意味着线数、相位和分区码一致。

## 光源和模拟采集

光谱响应、光电流及跨阻增益共同决定输出幅度。应按目标光源、反射材料和间隙检查信号裕量，避免削波或弱光噪声。400kHz模拟带宽不能直接换成机械最高转速，还需要轨道周期数。

## 电源与整机验收

整体工作需4.1～5.5V，低压数字分区条件不代表全部模拟通道也能在1.6V工作。验证需同时保存三通道SIN/COS和分区状态，检查整圈码值连续性、偏心、倾斜、温度及污染，不能只看单路正弦幅值。

## 多通道采样和整机启动

三条模拟轨道的每条均有正弦和余弦差分信号，接入后端时应核对各组极性与两位分区信息。多路ADC应采用相容时间基准；轮流采样还要检查通道切换后的建立时间和输入负载，避免运动中因采样时间差改变轨道相位关系。

若要求上电即用，必须覆盖光源稳定、模拟输出建立、分区判定和后端解算的全过程。前端100µs上电稳定参数不能当成整机已完成自检的时间。调试可先检查光电信号，再检查分区，最后核对整圈角度；位数增加无法补回弱光或错误轨道关系丢失的信息。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/cursorabsoluteencoder/index.html)
- [下载KTO9512 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTO9512-D26-QN32%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- 资料版本：公开手册封面日期 2025-08-14，10 个 PDF 页面
