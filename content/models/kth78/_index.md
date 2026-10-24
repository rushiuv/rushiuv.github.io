---
title: "KTH78系列"
linkTitle: "KTH78"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7801", "KTH7803", "KTH7812", "KTH7813", "KTH7814", "KTH7815", "KTH7816", "KTH7823"]
description: "KTH78 是 KTH78xx 霍尔角度编码器系列简称，覆盖 KTH7801、KTH7812、KTH7813、KTH7814、KTH7815、KTH7816、KTH7823 等成员。下列具体数值仅标注其对应型号。"
wiki: true
wiki_type: "model"
wiki_rank: 9
seed_count: 16
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7812 数据手册（系列代表型号）"
document_version: "KTH7812 官方公开手册，32 个 PDF 页面；其他成员以系列页同名手册为准"
model_card: true
product_image: "/images/wiki/kth78-diagram.webp"
product_image_caption: "图片来源：KTH7812 官方数据手册，第 5 个 PDF 页面，功能框图局部。本图仅代表 KTH7812。"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 系列范围 | KTH7801/7803、7812/7813/7814/7815/7816、7823等；成员页独立列参 |
| 检测方式 | 霍尔平面磁场方向，支持指定在轴/离轴磁路 |
| 编码格式 | N版本16位；C版本常为12位角度+4位CRC，按订货号 |
| KTH7812供电 | 3.3V模式3.0～3.6V；5V模式按对应电气表 |
| KTH7812噪声/INL | 0.015°（1σ）；±0.35°，具体条件见其手册 |
| KTH7812 ABZ/UVW | 4～4096步/圈；1～8对极 |
| KTH7812电流/启动 | 11.6mA@3.3V典型；1ms典型 |
| KTH7812磁场 | 30～150mT，典型60mT |
| KTH7812数据更新 | 1µs，不等于所有运动下测量链路无延时 |
| 温度分级 | 官网新表：7801/7803至150°C；781x至125°C；7823至105°C；不同表/手册另有冲突 |
| 封装 | QN16或SOP8，接口数量按成员与封装 |
| 资料冲突 | 官网两张选型表与部分型号手册存在噪声、接口、温度口径差异，本页不合成全系最佳值 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 系列页先解决哪三个问题

先确定应用等级，再确定引脚和输出组合，最后选择噪声与响应配置。KTH78不是每个型号都具备全部接口的统一芯片。汽车、工业与消费成员的温度上限和默认滤波等条件，应进入正式订货资料。

## 位数与CRC如何区分

N和C后缀涉及数据表达。12位角度加4位CRC占16位帧，但只有12位位置内容，不能写成16位角度分辨率。SPI、SSI、ABZ和PWM也可能有各自的码宽或更新行为。

## QFN与SOP8不是只缩封装

SOP8引脚少，通常保留PWM和SPI等组合，不能沿用QN16的全部增量输出。测试脚连接要求也应以具体引脚表为准。设计替换时需重新核对原理图、软件模式和输出电气条件。

## 怎样使用本页参数

上表以明确标注的KTH7812作代表，其他成员通过各自页查核心表。官网同时保留新旧两套表，噪声、温度和7815接口并不完全一致；应以适用正式手册和原厂确认收敛，不能挑每一栏最优值拼成一款器件。

## 官方资料

- [官方产品介绍](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [下载KTH7812 数据手册（系列代表型号）（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- 资料版本：KTH7812 官方公开手册，32 个 PDF 页面；其他成员以系列页同名手册为准
