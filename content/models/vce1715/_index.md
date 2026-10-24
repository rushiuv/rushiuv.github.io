---
title: "VCE1715"
description: "双饱和模式电桥的AMR角度器件，原生方向测量周期为180°。"
wiki: true
wiki_type: "model"
wiki_rank: 237
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["圣邦微"]
wiki_category: "模拟角度"
catalog_vendor: "圣邦微"
catalog_type: "模拟角度"
catalog_form: "芯片"
search_aliases: ["VCE1715"]
official_url: "https://www.sg-micro.com/product/VCE1715"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 角度范围 | 180°，不能单独当360°绝对编码器使用 |
| 输出链 | 被动双桥模拟信号，后端需采样与解算 |
| 电源／桥阻 | 官网手册推荐1～9V，桥阻典型1050Ω |
| 封装／温度 | SOIC-8，−40～125°C |

参数来源：本页所列[原厂产品资料与手册](https://www.sg-micro.com/product/VCE1715)。

## 工作方式与型号定位

VCE1715采用双饱和模式AMR桥，原生角度周期为180°。若系统需要上电后唯一360°机械位置，还需独立的极性信息或其他消歧结构。

## 安装、接口与配置

1～9V推荐桥路电源、典型1050Ω桥阻与后端输入电路应一起设计。两路模拟信号的偏置、幅值和正交性会进入反正切结果，不能直接用ADC位数评价角度精度。

## 校准与选型验证

应按敏感平面与磁场饱和要求安装磁体，再保存完整180°周期波形及温度变化。软件把角度乘二或延长计数不能补出上电时缺失的半圈信息，增量跟踪与绝对位置要分开说明。

## 官方资料

- [VCE1715 官方资料](https://www.sg-micro.com/product/VCE1715)
