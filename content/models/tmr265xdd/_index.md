---
title: "TMR265xDD系列"
description: "带信号调理与温度补偿配置的TMR线性场系列，按成员区分量程。"
wiki: true
wiki_type: "model"
wiki_rank: 232
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["多维科技"]
wiki_category: "线性磁场"
catalog_vendor: "多维科技"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["TMR2651DD","TMR2652DD","TMR2653DD"]
official_url: "https://www.dowaytech.com/TMR2651DD-TMR-Linear-Sensors.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 共同方向 | 经调理的磁场相关电压输出 |
| TMR2651DD | 官网列±1000Gs，DC～2MHz，典型3.3V／5V |
| 可编程项目 | 灵敏度、零偏、温度补偿 |
| 参数边界 | 2651DD的量程和频响不能直接套到2652DD／2653DD |
| TMR2651DD封装 | DFN6L，3 × 2 × 0.75 mm |
| TMR2651DD敏感轴 | X轴 |
| TMR2651DD非线性 | 官网特性列0.5%；仅限该成员及适用条件 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR2651DD-TMR-Linear-Sensors.html)。

## 工作方式与型号定位

TMR265xDD在TMR桥路后加入调理电路，对零偏、增益及相应温度系数进行调整。2651DD、2652DD与2653DD需按各自量程和订货条件选择。

## 安装、接口与配置

本页能直接核对的±1000Gs与DC～2MHz属于TMR2651DD，不能扩展成全系列共同性能。输出反映磁场，固定电压输出方式也要与后端参考电压安排一致。

## 校准与选型验证

高频响应用应检查模拟带宽、负载与PCB噪声，低频应用则关注零点和温漂。参数编程之后需要在正负场和温度下复测，不能用室温零点正确证明整量程线性及温补都正确。

## 官方资料

- [TMR265xDD系列 官方资料](https://www.dowaytech.com/TMR2651DD-TMR-Linear-Sensors.html)
