---
title: "KTH3105"
series_parent: "kth31"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 125
seed_count: 1
lastmod: "2026-10-24"
description: "KTH3105属于昆泰芯比例式线性霍尔相关产品，传感链将磁通密度变化转换为模拟电压，可用于位置或磁场检测。"
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html"
related_companies: ["昆泰芯"]
wiki_category: "线性磁场与位移映射"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH31 系列官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 感应类型 | 比例式线性霍尔 |
| 供电 | 3.0～5.5V |
| 典型灵敏度 | 3.30mV/Gs@3.3V；5.0mV/Gs@5V，官网KTH3105行 |
| 目录场强范围 | ±420Gs@3.3V；±450Gs@5V |
| 典型电流 | 4.5mA@3.3V；5.4mA@5V，系列目录 |
| 输出 | 磁场相关模拟电压 |
| 工作温度 | −40～125°C |
| 封装 | SOT-23、TO-92S、DFN1616，按订货号 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 相对3101改变了什么

KTH3105的5V典型灵敏度为5.0mV/Gs，约为3101的3.33倍。该比值来自官网同条件数值的换算，说明相同磁场变化得到更大电压变化，不代表整机位置精度提高3.33倍。

## 提高灵敏度要同时看量程

3105的目录磁场范围比3101窄。磁体靠得过近或行程端部场强过大时，输出会接近可用摆幅边界。选择ADC增益前，应先测整个行程及最强磁体组合。

## 电压如何变成位置

传感器输出首先对应磁场，再通过磁路标定换成毫米或摇杆位置。零场电压、灵敏度、磁体形状和安装姿态都会进入换算；不能只用一个线性霍尔斜率假设机械行程也是线性。

## 验证与替换

确认ADC输入负载和参考电压，并测全温零点、端点、迟滞及重复性。替换不同灵敏度成员时需更新标定系数和量程判断，原有软件阈值不能因为引脚相似而沿用。

## 单路输出的可观测范围

同一模拟电压会同时受到磁体距离、姿态与背景场影响。只有先限定机构运动自由度并标定磁路，才能把读数解释成目标行程。比较不同模拟链的噪声时，应把电压噪声换算到相同磁场灵敏度，并使用相同测量带宽。

## 官方资料

- [KTH3105 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html)

- [KTH31系列官方手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
