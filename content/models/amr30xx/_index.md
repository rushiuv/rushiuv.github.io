---
title: "AMR30xx模拟角度系列"
description: "多维的AMR模拟角度产品组，与TMR数字编码器使用不同信号处理链。"
wiki: true
wiki_type: "model"
wiki_rank: 230
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "模拟角度"
catalog_vendor: "多维科技"
catalog_type: "模拟角度"
catalog_form: "芯片"
search_aliases: ["AMR3001","AMR3003","AMR3008","AMR3013"]
official_url: "https://www.dowaytech.com/sensor/angle_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 成员 | AMR3001、AMR3003、AMR3008、AMR3013 |
| 输出形式 | 官网列入模拟角度类，不直接输出SPI角度码 |
| 解算边界 | AMR方向周期与机械360°绝对角应分别核对，不从系列名推断消歧能力 |
| 选型 | 按具体桥路、磁场及封装手册选择 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/angle_sensors.html)。

## 工作方式与型号定位

AMR30xx覆盖AMR3001、AMR3003、AMR3008与AMR3013模拟角度器件。桥路把磁场方向转换为电压，系统还需要模拟前端、ADC和角度计算；它不直接提供可由SPI读取的绝对角度码。

## 安装、接口与配置

AMR的原生方向周期与机械360°唯一位置是两个问题。需要整圈上电绝对位置时，应确认具体成员和系统是否含极性消歧，而不是在软件里将180°输出简单乘二。桥路供电、共模和差分幅度应一并匹配后端ADC。

## 校准与选型验证

比较成员时先按桥阻、工作磁场和输出形式筛选，再检查温漂与噪声。样机应保存原始SIN/COS轨迹，分别观察偏置、幅差和正交误差；调成圆形后仍需独立角度参考检查整圈残差。

## 官方资料

- [AMR30xx模拟角度系列 官方资料](https://www.dowaytech.com/sensor/angle_sensors.html)
