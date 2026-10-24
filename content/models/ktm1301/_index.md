---
title: "KTM1301"
wiki: true
wiki_type: "model"
catalog_type: "磁开关"
catalog_form: "芯片"
wiki_rank: 128
seed_count: 1
lastmod: "2026-10-24"
description: "KTM1301是昆泰芯全极型TMR磁开关系列，用于非接触状态感知。"
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁开关与状态检测"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 技术/逻辑 | TMR，全极型磁开关 |
| 供电 | 1.8～5.5V |
| T档 | 5000Hz；1.9µA@3V，官网目录 |
| M档 | 1600Hz；600nA@3V，官网目录 |
| S档 | 50Hz；160nA@3V，官网目录 |
| A/B/C/D/E动作场 | ±45/±30/±18/±9/±7Gs，完整成员后缀 |
| A/B/C/D/E释放场 | ±36/±21/±12/±6/±4Gs，完整成员后缀 |
| 输出 | CMOS状态输出 |
| 温度 | −40～125°C |
| 封装 | SOT-23-3L、TO-92S，按完整型号 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 纳安级版本测的是什么

KTM1301以TMR检测磁场门限，输出磁体是否到位。它不是连续位置编码器，不提供SPI角度。50Hz版本用低平均电流保持周期性检测，适合电池供电的低速状态事件。

## 电流与频率需成对读取

160nA、600nA和1.9µA分别对应50、1600和5000Hz目录工作点，不能将最低电流与最高频率合并。按频率计算的采样周期约20ms、625µs与200µs，也不是各条件下保证的最坏响应。

## 磁门限决定装配窗口

五档动作和释放门限形成不同磁迟滞。磁体尺寸、极性、轨迹和气隙决定机械触发距离；选择更低场门限时还应核对外部磁场及周围磁性件的影响。

## 怎样接入并验收

CMOS输出的电平和负载需与主控输入匹配，主控睡眠状态还要确认唤醒方式。测试最弱磁体、最大气隙、正负磁极以及全温动作/释放位置；快速掠过事件另测捕获率。

## 官方资料

- [KTM1301 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)
- [KTM1301 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTM1301%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
