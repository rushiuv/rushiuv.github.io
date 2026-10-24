---
title: "TMR3109"
description: "集成TMR与23位信号处理ASIC，支持对轴、离轴及客户端自校准。"
wiki: true
wiki_type: "model"
wiki_rank: 229
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "数字角度"
catalog_vendor: "多维科技"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["TMR3109"]
official_url: "https://www.dowaytech.com/TMR3109-TMR-Angle-Sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度／接口 | 360°；23位绝对位置，三线／四线SPI |
| 电源／封装 | 3.3～5V；SOP-8 |
| 校准 | 支持客户端自校准，安装误差须按校准条件验证 |
| 精度口径 | 网页表格±0.5°，特性区小于±0.05°；未明确统一条件，不合并成保证值 |
| 工作磁场 | 200～800 Gs（20～80 mT），原厂产品表 |
| 典型工作电流 | 10 mA，原厂特性摘要 |
| 最高转速 | 40,000 rpm；依手册工作条件 |
| 角度输出延迟 | 原厂特性列<2 µs；不能替代阶跃响应 |
| 温度 | −40～125°C，对应手册选型表 |
| Auto校准运行条件 | 300～3000 rpm恒速；推荐600 rpm，等待3～5 s；按V1.0.1校准章节 |
| 多点校准 | 64点，使用外部角度参考获得误差；与Auto校准分开 |
| 理想数字码距 | 按23位全圈换算：360°/2^23 ≈ 0.00004292°；计算值，不是准确度保证 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR3109-TMR-Angle-Sensors.html)。

## 工作方式与型号定位

TMR3109将TMR敏感结构与23位角度处理集成，SOP8主要通过三线或四线SPI读取绝对位置。与TMR3110相比，不能把后者的ABZ、UVW和PWM一起算进本型号。

## 安装、接口与配置

Auto校准依赖按手册提供的恒速旋转，推荐600rpm，建议窗口300～3000rpm，等待3～5秒。校准结果进入EEPROM；操作结束还应冷启动并用参考角验证，不把完成标志等同于最终精度合格。

## 校准与选型验证

对轴Auto校准、离轴Auto及64点外部参考校准属于不同条件。官网表格±0.5°与特性小于±0.05°不得合并成无条件保证。磁场20～80mT及全温误差也应与装配方式一起记录。

## 官方资料

- [TMR3109 官方资料](https://www.dowaytech.com/TMR3109-TMR-Angle-Sensors.html)
