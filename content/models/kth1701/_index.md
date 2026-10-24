---
title: "KTH1701"
series_parent: "kth17"
wiki: true
wiki_type: "model"
catalog_type: "磁开关"
catalog_form: "芯片"
wiki_rank: 83
seed_count: 2
lastmod: "2026-10-24"
description: "KTH1701是昆泰芯微功耗霍尔开关系列，用于检测磁体靠近或离开等状态，常见于电池供电位置检测。"
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1701%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁开关与状态检测"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth1701-product.png"
product_image_caption: "KTH1701 原厂手册产品／安装图（PDF 第 1 页）"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1701%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 检测方式 | 全极霍尔开关，输出状态量 |
| 供电 | 1.8～5.5V |
| F/T/S采样 | 500/100/25Hz |
| 对应平均电流 | 10.4/2.4/0.9µA@1.8V，官网目录 |
| H档动作/释放 | ±48/±28Gs，目录值 |
| L档动作/释放 | ±36/±20Gs，目录值 |
| U档动作/释放 | ±26/±14Gs，目录值 |
| 输出 | CMOS |
| 温度/封装 | −40～85°C；SOT-23-3L、TO-92S，按订货号 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1701%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 从磁体到开关状态

KTH1701把磁场是否越过门限转换为逻辑输出。H/L/U等磁阈值档与F/T/S等采样档分别影响触发条件和平均电流。目录中例如FH与SH均属H档，但采样速度不同，不能把后缀看成封装代号。

## 低功耗不是持续高速测量

25Hz版本的约40ms采样周期适合变化较慢的事件，500Hz版本约2ms。频率换算只表示观察节奏；实际最坏响应和有效脉冲宽度仍需按手册及目标动作验证。

## 磁迟滞怎样影响机构

动作场与释放场之间的差值防止临界位置频繁翻转，同时也使接近和远离的触发位置不同。磁体轨迹、磁路梯度和机构回差共同决定位置窗口，不能直接把Gs换成毫米。

## 订货与验证

中文与英文手册的可选档位需按实际版本核对，不能仅凭系列名拼后缀。确认供电、输出负载和封装敏感方向后，再测试全温动作点、弱磁体、最大气隙、上电状态及快速掠过捕获率。

## 官方资料

- [KTH1701 原厂资料入口](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html)
- [KTH1701 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH1701%20Series%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
