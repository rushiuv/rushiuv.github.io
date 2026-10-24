---
title: "KTH31系列"
description: "比例输出线性霍尔系列，按灵敏度选择磁场量程，再由磁路转换为位移。"
wiki: true
wiki_type: "model"
wiki_rank: 206
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "线性磁场"
catalog_vendor: "昆泰芯"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["KTH3101","KTH3102","KTH3103","KTH3105"]
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH31 系列官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 器件类型 | 比例输出线性霍尔系列 |
| 供电 | 3.0～5.5V |
| 典型电流 | 4.5mA（3.3V）；5.4mA（5V），官网目录 |
| KTH3101灵敏度与场强范围 | 5 V：1.5 mV/Gs，±1500 Gs；3.3 V：1.00 mV/Gs，±1400 Gs。官网目录口径 |
| KTH3102灵敏度与场强范围 | 5 V：2.5 mV/Gs，±900 Gs；3.3 V：1.65 mV/Gs，±840 Gs。官网目录口径 |
| KTH3103灵敏度与场强范围 | 5 V：3.4 mV/Gs，±660 Gs；3.3 V：2.25 mV/Gs，±620 Gs。官网目录口径 |
| KTH3105灵敏度与场强范围 | 5 V：5.0 mV/Gs，±450 Gs；3.3 V：3.30 mV/Gs，±420 Gs。官网目录口径 |
| KTH3110灵敏度与场强范围 | 5 V：10 mV/Gs，±225 Gs；3.3 V：6.60 mV/Gs，±210 Gs。官网目录口径 |
| KTH3113灵敏度与场强范围 | 5 V：13.5 mV/Gs，±165 Gs；3.3 V：8.90 mV/Gs，±150 Gs。官网目录口径 |
| 输出 | 与磁场相关的比例模拟电压 |
| 温度/封装 | −40～125°C；SOT-23、TO-92S、DFN1616，按具体成员 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 先按磁路选灵敏度

KTH31测量磁场分量，磁体和机构把位移转换为场强，再由芯片转换为电压。灵敏度越高，相同磁场变化带来的电压越大，同时可用场强范围更小。六个成员并非数字分辨率不同的同一颗芯片。

## 比例输出怎样接ADC

灵敏度随供电变化，评估时要同时记录供电和ADC参考。若两者使用同一稳定基准，可按比例式链路核算；若参考独立，则供电变化会进入电压到磁场的换算。

## 磁场范围不等于机构行程

±1500Gs与±165Gs是不同成员的目录范围，不能直接对应相同毫米数。磁体在整个行程内还应保持单调映射，避开场强饱和或位移曲线折返。

## 标定与验收

保留零场电压、两端电压、ADC原始码及磁体位置。按完整型号核对输出负载、带宽与温度条件，再测试供电、气隙、磁体批次和温度变化；用室温两点拟合得到的行程精度不能替代全温结果。

## 官方资料

- [KTH31系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/proportionallinerhalleffectsensor/index.html)

- [KTH31系列官方手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH31%20Series%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
