---
title: "VCS2395"
description: "平面二维全极AMR开关，采用开漏输出，采样频率与VCS238x不同。"
wiki: true
wiki_type: "model"
wiki_rank: 240
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["圣邦微"]
wiki_category: "磁开关"
catalog_vendor: "圣邦微"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["VCS2395"]
official_url: "https://www.sg-micro.com/product/VCS2395"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 输出 | 开漏，外部上拉条件须匹配 |
| 采样／电流 | 60Hz，典型0.45µA |
| 供电 | 2～5.5V |
| 封装／温度 | SOT23-3，−40～125°C |

参数来源：本页所列[原厂产品资料与手册](https://www.sg-micro.com/product/VCS2395)。

## 工作方式与型号定位

VCS2395为平面二维全极AMR开关，60Hz采样与典型0.45µA属于其自身工作条件。它采用开漏输出，与VCS238x推挽版本不能只换料不查上拉。

## 安装、接口与配置

外部上拉电阻与供电、输入阈值和线缆电容共同决定边沿。全极检测表示两种磁极都可触发，不表示空间任意方向的磁场都具有相同动作点。

## 校准与选型验证

测试应覆盖靠近、离开、临界停留和快速通过，尤其检查短磁事件能否跨过采样窗口。供电2～5.5V与温度范围需结合后缀，不能从低功耗数值直接推导更高检测带宽。

## 官方资料

- [VCS2395 官方资料](https://www.sg-micro.com/product/VCS2395)
