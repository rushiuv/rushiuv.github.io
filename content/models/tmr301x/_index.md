---
title: "TMR3014～3017系列"
description: "覆盖差分与单端输出的TMR模拟角度器件，需按型号选后端采集方式。"
wiki: true
wiki_type: "model"
wiki_rank: 227
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "模拟角度"
catalog_vendor: "多维科技"
catalog_type: "模拟角度"
catalog_form: "芯片"
search_aliases: ["TMR3014","TMR3015","TMR3016","TMR3017"]
official_url: "https://www.dowaytech.com/sensor/angle_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 输出区别 | 3014／3016为差分；3015／3017为单端 |
| 桥阻区别 | 3014目录1kΩ，3016为2.5kΩ，3017为200kΩ |
| TMR3015 | 目录列3～5.5V，DFN4／SOT23-5 |
| 测量链 | 模拟角度相关信号仍需ADC及角度计算 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/angle_sensors.html)。

## 工作方式与型号定位

TMR3014和3016为差分输出，3015与3017为单端输出，后端电路不能只按系列名共用。桥阻和供电条件也要随成员核对。

## 安装、接口与配置

差分采样需要关注两端共模，单端采样则要关注地与参考噪声。1kΩ、2.5kΩ及200kΩ桥阻反映不同负载和功耗条件，不能只按最小电流选择而忽略采集阻抗。

## 校准与选型验证

SIN/COS要在相同时间基准下采样，经过偏置、幅差和正交校正后计算角度。整机验证仍需参考角度，校正后的圆轨迹只能说明部分电气失配被处理，不能证明磁体误差已消除。

## 官方资料

- [TMR3014～3017系列 官方资料](https://www.dowaytech.com/sensor/angle_sensors.html)
