---
title: "MT6816"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 63
seed_count: 3
lastmod: "2026-10-24"
description: "MT6816是麦歌恩的AMR磁角度编码器，通过磁阻桥和信号处理ASIC完成0～360°测量，面向闭环步进和伺服等场景。"
official_url: "https://www.magntek.com.cn/136/105"
related_companies: ["麦歌恩"]
datasheet_url: "https://www.magntek.com.cn/upload/pdf/202312/MT6816_Rev.2.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/mt6816-product.png"
product_image_caption: "MT6816 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.magntek.com.cn/upload/pdf/202312/MT6816_Rev.2.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感知技术 | AMR |
| 角度分辨率 | 14 位 |
| 绝对值接口 | 三线／四线 SPI |
| 位置输出 | ABZ、UVW、PWM |
| 封装 | SOP8 |
| 延时 | 官网介绍小于 2 µs，需对应手册运行条件 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |
| 最高转速 | 25,000 rpm |
| ABZ | 1～1024脉冲/圈，四倍频最多4096步/圈 |
| 工作温度 | −40～125°C |
| PWM频率 | 971.1/485.6 Hz，可编程，容差±8% |

参数来源：本页所列[原厂产品资料与手册](https://www.magntek.com.cn/upload/pdf/202312/MT6816_Rev.2.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf)。

资料定位：MT6816 Rev.2.1（2022-12）第1、8页。

## 工作方式与型号定位

MT6816集成AMR桥路与角度处理，输出0～360°位置，适用于闭环步进等反馈链。14位绝对角度与增量、换向及PWM输出各有不同的接入方式。

## 安装、接口与配置

SOP8封装下应特别核对引脚复用，SPI三线与四线方式也要区分数据方向和时序。接口名称相同不表示可套用其他磁编码器的命令格式。

## 校准与选型验证

官网小于2µs的延时须对应原厂运行条件，不能用来代替整条闭环延迟。校验应包含全圈误差、静止噪声、加减速响应及ABZ方向，机械装配变更后复查原校准的适用性。

## 官方资料

- [MT6816 原厂资料入口](https://www.magntek.com.cn/136/105)
- [MT6816 数据手册（官方 PDF）](https://www.magntek.com.cn/upload/pdf/202312/MT6816_Rev.2.1_%E4%B8%AD%E6%96%87%E7%89%88.pdf)
