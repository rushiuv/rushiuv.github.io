---
title: "KTH7801"
description: "KTH7801是KTH78霍尔角度系列成员；接口和编码格式按具体封装及后缀区分。"
wiki: true
wiki_type: "model"
wiki_rank: 209
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "数字角度"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7801"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth78"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7801%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7801 官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 编码 | N：16位；C：12位角度+4位CRC，按后缀 |
| 输出配置 | 官网QN16：SSI/PWM/SPI/ABZ；SOP8：PWM/SPI |
| 工作供电 | 手册3.3V模式3.0～3.6V；5V模式4.5～5.5V，分别使用 |
| 磁场条件 | 关键表30～150mT，典型60mT |
| 典型工作电流 | 11.6mA@3.3V；5V表另核对 |
| 启动时间 | 典型1ms，关键表 |
| 数据更新/表列延时 | 1µs；匀速补偿与加减速响应不能混用 |
| INL | 手册关键表±0.35°，按安装和校准条件 |
| 温度漂移 | 手册关键表0.002°/°C，保留原测试口径 |
| 最高转速 | 手册关键表120000rpm，不能与任意滤波设置拼接 |
| 噪声 | 手册及官网对应行0.015°（1σ） |
| 工作温度 | 官网新表−40～150°C；官网另一表−40～125°C，须按完整订货号确认 |
| 封装 | QFN-16L或SOP-8，接口受引脚约束 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7801%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 车规成员如何选版本

KTH7801的完整料号包含电源兼容项、角度/CRC格式及封装。需要16位纯角度还是带CRC的数据帧，应从控制器需求出发选择，不能在软件里把CRC低位当作角度继续运算。

## 高温能力的资料冲突

官网新选型表将7801列为−40～150°C，另一张旧表列到125°C。页面保留两种口径，不把其中较高上限自动当成所有7801订货号的保证。量产前应取得适用手册与等级确认。

## 安装与校准

在轴与离轴都需要规定磁场条件。线性幅值调整修正信号链的一部分，不能将任意磁体偏心或磁化不均自动消除。比较整圈误差时应保持相同磁体、气隙、滤波和校准状态。

## 控制接口验收

QN16与SOP8的输出组合不同，替换时先核对引脚。绝对值读数用于位置初始化，ABZ用于增量计数；最高转速还受接收端边沿频率和滤波配置限制，不能单凭120000rpm标注决定可用系统速度。

## 官方资料

- [KTH7801 官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

- [KTH7801 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7801%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
