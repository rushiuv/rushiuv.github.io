---
title: "TMR3111"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 34
seed_count: 6
lastmod: "2026-10-24"
description: "TMR3111是多维科技集成TMR敏感元件和23位信号处理ASIC的磁编码器，兼容对轴与离轴应用，提供数字绝对角度与增量脉冲。"
official_url: "https://www.dowaytech.com/TMR3111-TMR-Angle-Sensors.html"
related_companies: ["多维科技"]
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tmr3111-official.jpg"
product_image_caption: "TMR3111 原厂产品／封装图"
product_image_source: "https://www.dowaytech.com/TMR3111-TMR-Angle-Sensors.html"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应技术 | TMR，支持对轴与离轴 |
| 绝对值接口 | 23 位 SPI |
| PWM | 12 位 |
| ABZ | 最高 4096 线 |
| 供电 | 3～5 V |
| 封装 | DFN-10L，3 × 3 mm |
| 工作磁场 | 200～800 Gs（20～80 mT），原厂产品表 |
| 典型工作电流 | 10 mA，原厂特性摘要 |
| 最高转速 | 40,000 rpm；依手册工作条件 |
| 角度输出延迟 | 原厂特性列<2 µs；不能替代阶跃响应 |
| 温度 | −40～125°C，对应手册选型表 |
| Auto校准运行条件 | 300～3000 rpm恒速；推荐600 rpm，等待3～5 s；按V1.0.1校准章节 |
| 多点校准 | 64点，使用外部角度参考获得误差；与Auto校准分开 |
| 输出组合 | SPI、ABZ、PWM；不含TMR3110的UVW |
| 供电／电流 | 3～5 V；典型10 mA |
| 封装尺寸 | DFN10L，3 × 3 × 0.75 mm |
| 精度条件 | 官网表格±0.5°；对轴Auto校准±0.05°条件不可直接扩展到离轴及全温 |
| 理想数字码距 | 按23位全圈换算：360°/2^23 ≈ 0.00004292°；计算值，不是准确度保证 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR3111-TMR-Angle-Sensors.html)。

## 工作方式与型号定位

TMR3111在3×3mm DFN10封装中提供23位SPI、ABZ与12位PWM，适合紧凑反馈板。它没有TMR3110的UVW输出，比较时应按实际接口需要选择。

## 安装、接口与配置

最高4096线ABZ对应四倍频16384步，不能把23位SPI字宽当成增量线数。Z相宽度、初相位及方向可配置，控制器归零和位置换算应与实际设置一致。

## 校准与选型验证

Auto校准推荐恒速600rpm、3～5秒，对轴与离轴的结果要分开；离轴更高精度需结合外部参考校准。官网±0.5°与小于±0.05°属于不同资料口径，不能不带校准、温度和安装条件直接宣称精度。

## 官方资料

- [TMR3111 原厂资料入口](https://www.dowaytech.com/TMR3111-TMR-Angle-Sensors.html)

TMR3111 官网简表列 ±0.5°，特性区列小于 ±0.05°，应按上表分别查看校准前后、在轴/离轴与温度条件，不合并成无条件精度。
