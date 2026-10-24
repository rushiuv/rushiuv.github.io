---
title: "TMR3110"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 146
seed_count: 1
lastmod: "2026-10-24"
description: "TMR3110是多维科技的23位TMR磁性角度编码器，集成磁阻传感与数字处理，用于对轴及离轴绝对位置检测。"
official_url: "https://www.dowaytech.com/TMR3110-TMR-Angle-Sensors.html"
related_companies: ["多维科技"]
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tmr3110-official.jpg"
product_image_caption: "TMR3110 原厂产品／封装图"
product_image_source: "https://www.dowaytech.com/TMR3110-TMR-Angle-Sensors.html"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应技术 | TMR |
| 绝对角度分辨率 | 23 位 |
| 安装方式 | 对轴与离轴 |
| 数字输出 | SPI，具体接口组合按 TMR3110 订货版本 |
| 工作磁场 | 200～800 Gs（20～80 mT），原厂产品表 |
| 典型工作电流 | 10 mA，原厂特性摘要 |
| 最高转速 | 40,000 rpm；依手册工作条件 |
| 角度输出延迟 | 原厂特性列<2 µs；不能替代阶跃响应 |
| 温度 | −40～125°C，对应手册选型表 |
| Auto校准运行条件 | 300～3000 rpm恒速；推荐600 rpm，等待3～5 s；按V1.0.1校准章节 |
| 多点校准 | 64点，使用外部角度参考获得误差；与Auto校准分开 |
| 供电范围 | 3.3～5 V |
| 封装 | TSSOP-16 |
| ABZ | 1～4096线/圈；四倍频最高16384步/圈 |
| UVW | 1～32对极仿真 |
| PWM | 12位，频率4档可配置 |
| 精度条件 | 官网表格±0.5°；特性与校准章节另列更低数值，按校准/安装/温度分别阅读 |
| 理想数字码距 | 按23位全圈换算：360°/2^23 ≈ 0.00004292°；计算值，不是准确度保证 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR3110-TMR-Angle-Sensors.html)。

## 工作方式与型号定位

TMR3110提供23位SPI绝对角度，并增加ABZ、UVW和12位PWM。TSSOP16引脚允许的输出组合仍需按配置确认，不能仅依据系列功能总表布线。

## 安装、接口与配置

ABZ最高4096线对应四倍频16384步，UVW最多32对极用于换向仿真。串行角度与脉冲计数采用不同分辨率，控制器应各自换算并在跨零时检查一致性。

## 校准与选型验证

自校准要按原厂恒速条件执行，不能把任意运动当校准输入。出厂、Auto及外部64点表补偿的精度应分开；单次校准完成后，应检查温度、气隙与断电重启，特别核对EEPROM实际保存。

## 官方资料

- [TMR3110 原厂资料入口](https://www.dowaytech.com/TMR3110-TMR-Angle-Sensors.html)
