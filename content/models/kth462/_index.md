---
title: "KTH462系列"
description: "二维锁存霍尔系列，分别提供独立轴状态或速度与方向输出。"
wiki: true
wiki_type: "model"
wiki_rank: 208
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "磁开关"
catalog_vendor: "昆泰芯"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["KTH4621","KTH4622"]
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 成员结构 | KTH4621：独立X/Y锁存状态；KTH4622：速度和方向双输出 |
| 供电 | 2.5～5.5V |
| AT版本频率/电流 | 1.7kHz；1.9mA（2.5V） |
| AM版本频率/电流 | 30Hz；33µA（2.5V） |
| 目录动作/释放 | 25/−25Gs，符号按敏感轴与封装图确认 |
| 输出 | NMOS开漏，双输出 |
| 温度 | −40～125°C |
| 封装 | SOT-23-6L |

参数依据：[原厂产品与型号选型表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html)。

## 两种双输出含义不同

KTH4621提供两个轴的锁存状态，主控可据状态序列判断运动。KTH4622则把速度与方向作为两路功能输出。原理图上都是两根信号线，不表示协议、采样或软件解释相同。

## 采样档与最高运动频率

AT和AM版本在频率与电流之间折衷，不能把33µA与1.7kHz列成同一工作点。运动磁极数会将机械转速转换为电气变化频率，应先确定磁体结构再核算采样裕量。

## 锁存状态与磁体极性

锁存器需要相反磁极完成状态切换，磁体远离不一定代表释放。X/Y敏感轴、封装方向和磁场轨迹共同决定两个输出的先后关系，方向判断应在正反转下分别确认。

## 验证方法

开漏端使用适当上拉后，同时采集两路波形。检查低速往返、高速通过、上电时磁体处于临界位置和短暂停留的行为；不要只用万用表看到一次高低变化，就判断速度方向链路完成。

## 官方资料

- [KTH462系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html)
