---
title: MT6813CT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 403
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6813CT 是AMR绝对角度系列的SOP8成员，目录侧重I²C、三线/四线SPI与PWM读取，适合先确定更新节拍再安排控制输入。
official_url: https://www.novosns.com/product/MT6813CT-LAC-R
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6813
- MT6813CT
- MT6813CT-LAC-R
- MT6813CT-PAD-R
- MT6813CT-PBD-R
- MT6813CT-PCD-R
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/b48c45076127e433.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/XXBSbBZIOoqVo2x1VAhcWmfcnrg.png
---

## 核心参数与配置

以下为官网目录中 **MT6813CT-LAC-R** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 工业编码器 |
| 封装 | SOP8 |
| 目录等级 | Industrial |
| 数字接口 | I²C/3wire SPI/4-wireSPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 9~12bit；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <6000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 100μs~400μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## AMR感应与安装方向对应

官网说明感知平行芯片表面的旋转磁场。磁体方向、芯片朝向和场强条件应按该原理布置，不能把适用于另一类Hall读头的安装图直接套用。

## 串行输出优先于增量接口假设

目录对ABZ、UVW没有列出有效配置，不能因同品牌其他编码器有换向功能就补到本型号。三线SPI还涉及数据线换向，主控必须按具体时序处理输入输出，不能只把四线连接少接一根。

## 动态行为按延时配置检验

目录给出随条件变化的延时区间，应按最终配置评估运动中的角度滞后。静态码值稳定与控制环响应是不同指标；SOP8版本的预设状态也需逐OPN核对。

## 订货版本之间的差别

### 生命周期状态

| 目录标注 | 适用完整订货号 |
| --- | --- |
| Active | MT6813CT-LAC-R、MT6813CT-PAD-R、MT6813CT-PCD-R |
| Not Recomended for New Designs | MT6813CT-PBD-R |

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6813CT-LAC-R](https://www.novosns.com/product/MT6813CT-LAC-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf) |
| [MT6813CT-PAD-R](https://www.novosns.com/product/MT6813CT-PAD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf) |
| [MT6813CT-PBD-R](https://www.novosns.com/product/MT6813CT-PBD-R) | SOP8；Industrial；Not Recomended for New Designs；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf) |
| [MT6813CT-PCD-R](https://www.novosns.com/product/MT6813CT-PCD-R) | SOP8；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf) |

“Not Recommended for New Designs”表示该完整订货号不推荐用于新设计，不代表本页全部成员停产。请结合表内仍为Active的版本核对供应与配置。

## 资料边界

MT保留首连字符前完整字母，包装/预设尾缀记录在full_order_codes。

同一归一型号不同OPN生命周期不同；逐条保留，不能整体标Active。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6813CT-LAC-R)
- [DatasheetEN)MT6813_Rev.3.1.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
