---
title: "TMR1102／1148／1162"
description: "单极TMR位置开关器件组，连续感测和占空比采样版本需分开选择。"
wiki: true
wiki_type: "model"
wiki_rank: 235
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "磁开关"
catalog_vendor: "多维科技"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["TMR1102","TMR1148","TMR1162"]
official_url: "https://www.dowaytech.com/sensor/switch_sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 输出区别 | 1102为推挽；1148和1162为开漏 |
| 连续模式 | 1102／1148目录典型1.5µA，1.8～5.5V |
| 间歇模式 | 1162为占空比采样，目录200nA；不是连续同频响条件 |
| 检测方向 | 按磁场敏感轴及磁体极性布置 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/sensor/switch_sensors.html)。

## 工作方式与型号定位

TMR1102、1148和1162都用于磁状态检测，但输出级和采样方式不同。1102为推挽，1148与1162为开漏；连续感测与占空比采样不能按最低电流一个指标互相替代。

## 安装、接口与配置

开漏接入需要外部上拉，推挽则应确认电平兼容。连续版1.5µA与1162的200nA属于不同工作方式，后者还需核对采样周期是否能捕捉应用中的最短磁事件。

## 校准与选型验证

单极开关需要匹配磁体极性与敏感方向，动作点和释放点组成磁滞窗口。验收应同时测靠近、离开和温度变化，避免只用一块强磁铁证明会翻转，却没有确定实际安装公差。

## 官方资料

- [TMR1102／1148／1162 官方资料](https://www.dowaytech.com/sensor/switch_sensors.html)
