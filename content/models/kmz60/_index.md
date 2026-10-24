---
title: "KMZ60"
wiki: true
wiki_type: "model"
catalog_type: "模拟角度"
catalog_form: "芯片"
wiki_rank: 124
seed_count: 1
lastmod: "2026-10-24"
description: "KMZ60是NXP历史磁角度传感器件，提供与磁场方向有关的正余弦模拟信息。"
official_url: "https://www.nxp.com/part/KMZ60"
related_companies: ["NXP"]
wiki_category: "模拟角度信号与外部解算"
document_version: "NXP 产品页标注 End of Life；数据手册 Rev. 2，2014-02-07；核对：2026-10-24"
model_card: true

datasheet_url: "https://www.nxp.com/docs/en/data-sheet/KMZ60.pdf"

datasheet_label: "NXP KMZ60 数据手册 Rev. 2"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 敏感结构 | MR角度桥与放大器双芯片同封装 |
| 输出 | 两路单端、比例式SIN/COS；仍需外部ADC和角度解算 |
| 供电 | 2.7～5.5 V，Rev.2第2页 |
| 环境温度 | −40～150°C |
| 磁场方向周期 | 输出cos(2α)/sin(2α)，α为机械磁场角；不能仅凭模拟相位得到上电唯一360°机械位置 |
| 片上功能 | 放大、温度幅度补偿、比例式温度参考、掉电控制 |
| 封装 | SO8（SOT96-1）；原厂产品页列本体4.9 × 3.9 × 1.75 mm、引脚间距1.27 mm |
| 生命周期 | NXP当前产品页标注End of Life，产品归档页注明不再制造；用于存量维护时须另核可获得性 |
| 资料版本 | NXP KMZ60 Rev.2，2014-02-07；历史技术资料，不作为新产品长期供货承诺 |

参数来源：[NXP KMZ60 Rev.2数据手册](https://www.nxp.com/docs/en/data-sheet/KMZ60.pdf)第1～4页及[NXP产品页](https://www.nxp.com/part/KMZ60)。生命周期另见[原厂归档页](https://www.nxp.com/products/KMZ60)。

## 工作方式与型号定位

KMZ60把磁阻角度桥与放大器集成在同一封装，输出随磁场方向变化的单端正弦、余弦。温度补偿调整幅度，VTEMP提供比例式温度参考，掉电控制可使输出进入高阻。它不直接输出SPI角度或ABZ脉冲。

原厂第4页描述输出为cos(2α)和sin(2α)，机械磁场转动180°便重复一次。外部atan2得到的是信号相位；若需要上电唯一机械全圈位置，还需独立的半圈消歧信息，不能只把计算结果做比例换算。

## 安装、接口与配置

后端ADC应匹配单端输出、共模、摆幅和供电比例关系。两个通道应同步或严格控制采样时差；错时采样在快速运动下会形成额外相位误差。TCC_EN选择温度补偿，POWERDOWN_EN与未用引脚按手册连接。

原厂应用包括偶数极对BLDC转子位置，以及EPS、雨刷、方向盘和执行器检测。是否能形成所需机械角度范围仍取决于磁体极对数、感应方向、气隙和上电消歧，不能由应用名称直接推出。

## 校准与选型验证

先保存原始SIN/COS电压，校正零偏、幅差和正交误差，再和机械参考比较周期残差。换用其他器件时，要核对供电、模拟输出类型、敏感周期、温漂、焊盘和失效输出，不只比较室温静态曲线。

该型号已处于原厂归档/生命周期末期。存量替代还应检查实际可获得料号、接口电气与长期维护安排，现有历史PDF不能自动证明当前有稳定量产供货。

## 官方资料

- [KMZ60 原厂产品页](https://www.nxp.com/part/KMZ60)
- [KMZ60 数据手册 Rev.2（PDF）](https://www.nxp.com/docs/en/data-sheet/KMZ60.pdf)
- [KMZ60 原厂归档页](https://www.nxp.com/products/KMZ60)
