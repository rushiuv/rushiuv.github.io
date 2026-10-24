---
title: "TMR3108"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 67
seed_count: 3
lastmod: "2026-10-24"
description: "TMR3108是多维科技早期17位高速TMR数字角度编码器，集成磁阻敏感元件、信号调理和数字角度处理。"
official_url: "https://www.dowaytech.com/TMR3108-TMR-Angle-Sensors.html"
related_companies: ["多维科技"]
datasheet_url: "https://www.dowaytech.com/en/res/202310/12/219e5842f1299a33.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tmr3108-datasheet-figure.png"
product_image_caption: "tmr3108 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.dowaytech.com/en/res/202310/12/219e5842f1299a33.pdf"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应技术 | TMR |
| 角度分辨率 | 17 位 |
| 角度接口 | SPI |
| 配置保存 | EEPROM，写入方式见 TMR3108 版本手册 |
| 理想数字码距 | 按17位全圈换算：360°/2^17 ≈ 0.00274658°；计算值，不是准确度保证 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/en/res/202310/12/219e5842f1299a33.pdf)。

## 工作方式与型号定位

TMR3108集成TMR、信号调理和17位数字角度处理，通过SPI读取位置并使用EEPROM保存配置。它与后续23位器件属于不同产品代际。

## 安装、接口与配置

EEPROM写入需按本型号手册核对电源、命令、完成状态和等待时间。不能把TMR3109的自校准流程或MT6835的保存等待时间直接搬到这颗器件。

## 校准与选型验证

比较新旧设计时，先核对供电、电平、引脚和命令兼容，再看码宽。整圈误差、低速噪声及动态响应需要在相同磁体与温度下比较，否则增加输出位数不足以证明系统性能提高。

## 官方资料

- [TMR3108 原厂资料入口](https://www.dowaytech.com/TMR3108-TMR-Angle-Sensors.html)
- [TMR3108 数据手册（官方 PDF）](https://www.dowaytech.com/en/res/202310/12/219e5842f1299a33.pdf)
