---
title: "雷尼绍"
description: "雷尼绍 Renishaw：英国 Wotton 的开放式光学编码器厂，RESOLUTE 绝对式到 1 nm 与 100 m/s、SDE ±40 nm，TONiC、VIONiC、QUANTiC、ATOM DX 分工明确。"
wiki: true
wiki_type: "company"
wiki_rank: 19
seed_count: 11
lastmod: "2026-10-22"
official_url: "https://www.renishaw.com/"
related_models: []
related_companies: []
---

雷尼绍站在“读头 + 刻度”这一层：它不卖装在轴上的整机编码器，而是把光学读头和金属或玻璃刻度分开卖，由整机厂装进自己的机械结构。这个位置决定了它的资料重点与众不同——参数永远绑在“读头 + 某种刻度”的组合上，脱开刻度谈分辨率没有意义。

## 公司与品牌

英文名 Renishaw plc，编码器业务在其产品线里归“位置与运动控制”一类。官网把开放式光学编码器按绝对式与增量式两族分开，绝对式下是 RESOLUTE 与 EVOLUTE，增量式下是 VIONiC、TONiC、QUANTiC、ATOM 与 ATOM DX。[产品地图](https://www.renishaw.com/en/range-of-renishaw-open-optical-encoders--48432)

它的产品语言有一个特征：几乎每个系列都配“应用变体”——超高真空（UHV）、扩展温区（ETR）、功能安全（FS）。这说明它把同一套光学系统按环境重做，而不是按精度重做。

## 编码器相关产品线与公开规格

| 系列 | 类型 | 公开分辨率与速度 | 其他公开参数 |
| --- | --- | --- | --- |
| [RESOLUTE](https://www.renishaw.com/en/resolute-encoder-series--37823) | 真绝对式光学，上电即得位置 | 分辨率到 1 nm，速度到 100 m/s（约 36000 rpm） | SDE ±40 nm、抖动小于 10 nm RMS、BiSS-C 与 BiSS Safety、FANUC、三菱、松下、西门子 DRIVE-CLiQ、安川 Σ-5／Σ-7 |
| [EVOLUTE](https://www.renishaw.com/en/evolute-encoder-series--42473) | 真绝对式，50 µm 刻度周期 | 分辨率到 50 nm，速度到 100 m/s | 基于 RESOLUTE 技术，强调安装容差宽与抗污染，接口同族 |
| [VIONiC](https://www.renishaw.com/en/vionic-encoder-series--38973) | 增量式，读头内置插值 | 公开标称在其增量系列里最高 | 超低 SDE、抗污、配合 ZeroMet 低膨胀刻度与 REXM 环 |
| [TONiC](https://www.renishaw.com/en/tonic-encoder-series--37824) | 增量式，外置 Ti 接口 | 配 Ti 接口时到 1 nm，速度到 10 m/s | RTLC20 钢带刻度 ±5 µm/m、刻度周期 20 µm、热膨胀 10.1 µm/m/°C、长度到 10 m |
| [QUANTiC](https://www.renishaw.com/en/quantic-encoder-series--43210) | 增量式，数字与模拟两种输出 | 速度到 24 m/s | 强调宽安装容差与内置校准 |
| [ATOM DX](https://www.renishaw.com/en/atom-dx-encoder-series--42875) | 增量式，最小读头，数字输出直出 | 按刻度与插值分档 | 20 µm 与 40 µm 两种刻度；RTLF 钢带 20 µm 档 ±5 µm/m、40 µm 高精度档 ±5 µm/m、普通 40 µm 档 ±15 µm/m；RCLC 玻璃栅 ±3 µm/m |

两条读数最值得记住：RESOLUTE 的卖点是“上电即得位置，不需要运动”，这对不能回参考点的机床与量测设备是硬需求；EVOLUTE 把刻度周期放到 50 µm，用更粗的刻度换安装容差与抗污染，代价是分辨率上限降到 50 nm。

刻度那一侧同样有取舍：钢带热膨胀约 10.1 µm/m/°C，玻璃栅约 8 µm/m/°C 且长度只到 130 mm 量级，ZeroMet 是低膨胀路线。选型时先定“热行为能不能接受”，再谈分辨率。

诊断是这套体系里被低估的一环。官方为各增量与绝对系列配了 ADTpro-100 与 ADTi-100 两种诊断工具，配 ADT View 软件读实时信号与安装状态；读头本身带安装指示灯。这说明这类开放式系统的实际精度有很大一部分由安装现场决定，厂商把“装得对不对”做成了产品的一部分。

官网给了分辨率、速度、SDE、抖动、刻度精度与热膨胀，以及接口清单。接口不能想当然：官方 FAQ 明确写过 RESOLUTE 不支持 SSI，不能因为“绝对式常用 SSI”就给某个系列默认补上该协议。选型必须看订货代码。

## 在编码器链上的位置

它买激光器或 LED、光电探测器阵列、专用插值 ASIC 与刻度基材，做读头；刻度单独作为耗材与精度源卖给整机厂。因此它在链上的角色是“把光学与插值做到一个模块里”，机械精度的一半责任交给用户的安装。

**不能推断**的是某台机床用了它的哪套组合——官网给的是系列能力，不给客户配置。**能推断**的是它对“绝对式要不要上”的判断：RESOLUTE 与 EVOLUTE 都是真绝对，说明它把绝对位置当成高端线的基本能力，而不是选配。

## 官方资料

- [开放式光学编码器产品地图](https://www.renishaw.com/en/range-of-renishaw-open-optical-encoders--48432)
- [RESOLUTE 绝对式系列](https://www.renishaw.com/en/resolute-encoder-series--37823)
- [EVOLUTE 绝对式系列](https://www.renishaw.com/en/evolute-encoder-series--42473)
- [VIONiC 增量式系列](https://www.renishaw.com/en/vionic-encoder-series--38973)
- [TONiC 增量式系列](https://www.renishaw.com/en/tonic-encoder-series--37824)
- [QUANTiC 增量式系列](https://www.renishaw.com/en/quantic-encoder-series--43210)
- [ATOM DX 增量式系列](https://www.renishaw.com/en/atom-dx-encoder-series--42875)
