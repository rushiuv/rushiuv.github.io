---
title: "MT6701"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 62
seed_count: 3
lastmod: "2026-10-24"
description: "MT6701是麦歌恩基于差分霍尔的磁角度传感器，面向旋钮、机器人和电机反馈等应用。"
official_url: "https://www.magntek.com.cn/"
related_companies: ["麦歌恩"]
datasheet_url: "https://www.magntek.com.cn/upload/pdf/202312/MT6701_Rev.1.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mt6701-datasheet-figure.jpg"
product_image_caption: "mt6701 原厂手册插图（PDF 第 1 页）"
product_image_source: "https://www.magntek.com.cn/upload/pdf/202312/MT6701_Rev.1.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感知技术 | 差分霍尔 |
| 角度分辨率 | 14 位 |
| 绝对值读取 | SSI |
| 封装选件 | I²C、模拟量、PWM 或增量输出依引脚版本 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |
| 推荐供电 | 3.0～5.5 V，典型3.3～5.0 V；EEPROM烧写要求VDD>4.5 V |
| 工作电流 | 典型10 mA，最大14 mA |
| 最高转速 | 55,000 rpm |
| 延迟口径 | 概述<5 µs；电气表为匀速典型5 µs，二者分别保留 |
| INL | 典型±1.0°，最大±1.5°；具体安装和温度按手册注释 |
| ABZ | 1～1024脉冲/圈，四倍频最多4096步/圈 |
| UVW | 1～16对极，可编程 |
| 模拟量／PWM | 12位位置表达；PWM典型994.4/497.2 Hz，可编程 |
| 工作温度／封装 | −40～125°C；SOP8或QFN3×3-16L |
| 上电准备时间 | 最大32 ms，电源上升<10 µs条件 |

参数来源：本页所列[原厂产品资料与手册](https://www.magntek.com.cn/upload/pdf/202312/MT6701_Rev.1.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf)。

资料定位：MT6701 Rev.1.8（2022-12）第1、7页；参数中的典型/最大和上电斜率按原表保留。

## 工作方式与型号定位

MT6701采用差分霍尔检测磁体方向，提供14位绝对角度。SSI读取用于绝对位置，I²C、模拟、PWM或增量功能应按封装与输出版本确认。

## 安装、接口与配置

引脚数量限制实际可同时使用的输出。选型时应先确定控制器需要上电位置、计数还是模拟接口，再核对完整料号；不能把所有封装的接口汇总成每颗器件共有能力。

## 校准与选型验证

磁体偏心、倾斜和气隙需要在目标机械结构下测试。14位码距约0.02197°只表示数字刻度，准确度和静止噪声应另测；SSI时钟也不能直接当作内部角度更新频率。

## 官方资料

- [MT6701 原厂资料入口](https://www.magntek.com.cn/)
- [MT6701 数据手册（官方 PDF）](https://www.magntek.com.cn/upload/pdf/202312/MT6701_Rev.1.8_%E4%B8%AD%E6%96%87%E7%89%88.pdf)
