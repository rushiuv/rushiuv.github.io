---
title: "KTH7812"
series_parent: "kth78"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 84
seed_count: 2
lastmod: "2026-10-24"
description: "KTH7812是昆泰芯KTH78系列的工业类霍尔角度传感器，支持磁体在轴或离轴应用。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
related_companies: ["昆泰芯"]
related_models: ["KTH78", "KTH7823", "KTH7815"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth7812-datasheet-figure.jpg"
product_image_caption: "kth7812 原厂手册插图（PDF 第 4 页）"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 角度编码 | 16位绝对角度 |
| 输出 | 四线SPI、ABZ、UVW，依配置 |
| ABZ/UVW | 4～4096步/圈；1～8对极 |
| 工作供电 | 手册3.3V模式3.0～3.6V；5V模式4.5～5.5V，分别使用 |
| 磁场条件 | 关键表30～150mT，典型60mT |
| 典型工作电流 | 11.6mA（3.3V）；5V表另核对 |
| 启动时间 | 典型1ms，关键表 |
| 数据更新/表列延时 | 1µs；匀速补偿与加减速响应不能混用 |
| INL | 手册关键表±0.35°，按安装和校准条件 |
| 温度漂移 | 手册关键表0.002°/°C，保留原测试口径 |
| 最高转速 | 手册关键表120000rpm，不能与任意滤波设置拼接 |
| 噪声 | 关键表0.015°（1σ） |
| 温度 | −40～125°C |
| 封装 | QFN-16L；其他订货形式按适用手册 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 工业反馈中的三条输出链

SPI适合读取绝对角度和配置；ABZ向计数器提供相对位移；UVW提供电机换向状态。三者的方向和零点要共同对齐。4096步/圈是四倍频后计数口径，不能再错误乘四当成16384步。

## 1µs不等于没有动态误差

手册给出数据更新及延时补偿相关说明，控制器仍需考虑滤波、SPI事务和采样时刻。匀速补偿后的相位误差，与快速加减速时的跟踪误差应分别测试，不能从刷新周期直接推出可用闭环带宽。

## 磁体与增益配置

芯片测的是磁场方向。磁体偏心、倾斜和离轴场形状都会进入输出角度；幅值调整只能处理对应信号失配，不能代替整圈安装误差验收。气隙选择应使全圈场强位于规定区间。

## 上电与参数保存

记录完整订货号、默认ABZ线数以及方向设置。修改零点或其他参数后，按手册确认写入和重新上电回读。验证至少包含整圈正反转误差、Z相位置、弱磁报警与最高工作速度的边沿完整性。

## 官方资料

- [KTH7812 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [KTH7812 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
