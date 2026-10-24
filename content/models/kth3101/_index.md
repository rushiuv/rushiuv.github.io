---
title: "KTH3101"
description: "低灵敏度档线性霍尔器件，适合较大场强范围的模拟检测。"
wiki: true
wiki_type: "model"
wiki_rank: 266
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "线性磁场"
catalog_vendor: "昆泰芯"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["KTH3101"]
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth31"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH31 系列官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 感应类型 | 比例式线性霍尔，模拟电压输出 |
| 供电 | 3.0～5.5V |
| 典型灵敏度 | 1.00mV/Gs（3.3V）；1.5mV/Gs（5V） |
| 目录场强范围 | ±1400Gs（3.3V）；±1500Gs（5V） |
| 典型电流 | 4.5mA（3.3V）；5.4mA（5V），系列目录 |
| 工作温度 | −40～125°C |
| 封装选择 | SOT-23、TO-92S、DFN1616，按实际订货号 |
| 测量输出 | 磁场相关电压，不内置位移或数字角度接口 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 低灵敏度档的用途

KTH3101在KTH31系列中采用较低灵敏度，适合需要覆盖较大磁场变化的磁路。与KTH3105相比，它在相同磁场变化下输出电压变化更小，但目录允许的磁场范围更宽。

## 供电改变换算比例

3.3V与5V下的灵敏度分别列出，不能用1.5mV/Gs处理3.3V供电的数据。若ADC参考不随芯片供电变化，需要把电源波动计入磁场与位移误差。

## 磁体安装怎样检查

先以目标行程扫出电压曲线，确认整个有效区间没有饱和或折返，再确定控制器分辨率和标定方法。零场电压只提供电气中心，不自动等于机构零位。

## 验收重点

分别测试正负磁场方向、最大负载和全温零偏。保留磁体规格、封装朝向、气隙及供电条件，比较不同批次时使用相同磁路；单看ADC码稳定，无法证明线性度和温漂满足需求。

## 官方资料

- [KTH3101 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html)

- [KTH31系列官方手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
