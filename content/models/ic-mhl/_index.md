---
title: "iC-MHL系列"
description: "用于磁栅或离轴磁环的12位霍尔编码器系列，按磁极宽度选择成员。"
wiki: true
wiki_type: "model"
wiki_rank: 251
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["iC-Haus"]
wiki_category: "线性编码"
catalog_vendor: "iC-Haus"
catalog_type: "线性编码"
catalog_form: "芯片"
search_aliases: ["iC-MHL100","iC-MHL200"]
official_url: "https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf"
document_version: "官方公开PDF，核对：2026-10-18；版本见下文"
model_card: true
datasheet_url: "https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf"
datasheet_label: "官方公开PDF"
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 磁栅匹配 | MHL100单极宽1mm、周期2mm；MHL200单极宽2mm、周期4mm |
| 细分 | 每磁周期最多4096步；对应约0.5µm／1µm |
| 输出 | ABZ及BiSS-C等，依成员配置 |
| 速度条件 | 全分辨率下MHL100为4m/s、MHL200为8m/s；不是整尺绝对精度 |
| AB频率 | 最高2MHz；边沿数按正交解码另算 |
| 增量／换相电气 | RS422兼容，输出驱动及转换速率可配置 |
| UVW | 每磁周期1倍或2倍换相 |
| 配置存储 | OTP zapping ROM，非无限次可擦写存储 |
| 工作温度 | −40～125°C，公开factsheet |
| 错误监测 | NERR开漏输出，含失磁或频率错误；错误码可经BiSS读取 |

参数依据：[原厂产品页或对应资料](https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf)。

## 产品功能与测量链

iC-MHL面向磁栅或离轴磁环，MHL100与MHL200对应不同磁极宽。单极宽1mm和2mm分别构成2mm、4mm磁周期，读头不能任意互换。

## 接入与配置

每周期4096步换算约0.488µm与0.977µm，只说明输出步距。整尺精度还受磁栅节距误差、安装姿态和温度影响。

## 使用与验证

全分辨率下4m/s与8m/s分别对应两种成员条件。接口计数能力必须覆盖运动频率，并检查方向、索引和丢磁状态；局部周期位置也不自动变成全行程绝对位置。

## 官方资料

- [iC-MHL系列 官方资料](https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf)
