---
title: iC-MHL系列
description: 用于磁栅或离轴磁环的12位霍尔编码器系列，按磁极宽度选择成员。
wiki: true
wiki_type: model
wiki_rank: 251
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- iC-Haus
wiki_category: 线性编码
catalog_vendor: iC-Haus
catalog_type: 线性编码
catalog_form: 芯片
search_aliases:
- iC-MHL100
- iC-MHL200
- iC-MHL系列
official_url: https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf
document_version: 官方公开PDF，核对：2026-10-18；版本见下文
model_card: true
datasheet_url: https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf
datasheet_label: 官方公开PDF
catalog_level: 系列
---

iC-MHL读头与磁栅极距配套。MHL100和MHL200采用不同磁周期，因此相同细分步数对应不同线性步距和速度条件。

## 型号与核心异同

| 具体型号 | 单极宽／磁周期 | 每周期4096步时步距 | 全分辨率速度 |
| --- | --- | --- | --- |
| iC-MHL100 | 1mm／2mm | 约0.488µm，按周期换算 | 4m/s |
| iC-MHL200 | 2mm／4mm | 约0.977µm，按周期换算 | 8m/s |

## 共同条件与参数依据

- **输出**：ABZ及BiSS-C等，依成员配置
- **AB频率**：最高2MHz；边沿数按正交解码另算
- **增量／换相电气**：RS422兼容，输出驱动及转换速率可配置
- **UVW**：每磁周期1倍或2倍换相
- **配置存储**：OTP zapping ROM，非无限次可擦写存储
- **工作温度**：−40～125°C，公开factsheet
- **错误监测**：NERR开漏输出，含失磁或频率错误；错误码可经BiSS读取

## 接口与安装

每周期4096步换算约0.488µm与0.977µm，只说明输出步距。整尺精度还受磁栅节距误差、安装姿态和温度影响。

## 动态与装配验证

全分辨率下4m/s与8m/s分别对应两种成员条件。接口计数能力必须覆盖运动频率，并检查方向、索引和丢磁状态；局部周期位置也不自动变成全行程绝对位置。

## 官方资料

- [iC-MHL系列 官方资料](https://www.ichaus.de/wp-content/uploads/MHL_factsheet_rev4.pdf)
