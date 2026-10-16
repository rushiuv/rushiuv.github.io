---
title: "雷尼绍"
description: "Renishaw 雷尼绍：开放式光学编码器、刻度与测量系统，代表系列包括 RESOLUTE、TONiC。"
wiki: true
wiki_type: "company"
wiki_rank: 19
seed_count: 11
lastmod: "2026-10-16"
official_url: "https://www.renishaw.com/"
related_models: []
related_companies: []
---

## 公司与品牌

雷尼绍英文名为 Renishaw。在位置反馈领域，其官网提供光学编码器读头、直线刻度、圆光栅及配套接口和诊断工具。相对于单颗光电芯片，产品定义通常覆盖读头与匹配刻度的组合，因此参数需要放在完整测量系统中理解。

官网将开放式光学编码器按绝对式和增量式区分，RESOLUTE、EVOLUTE、TONiC、VIONiC、QUANTiC、ATOM 等构成不同系列。本页重点介绍阅读这些产品的路径，不把各系列的最佳指标拼合成一个统一产品。[官方系列目录](https://www.renishaw.com/en/range-of-renishaw-open-optical-encoders--48432)

## 相关业务与技术路线

增量式系统读取周期性刻度，产生连续位移相关信号，并通过计数或细分得到位置。参考标记用于建立基准。绝对式系统则读取当前位置对应的编码信息，支持上电后取得位置；具体通信与启动条件仍须查对应型号。

RESOLUTE 属于绝对光学编码器系列，官网介绍其不需运动即可在启动后取得位置。TONiC 属于增量光学系统，强调信号处理、低细分误差和低抖动。两者首先在位置建立方式上不同，选型时应结合设备是否允许回参考点。[光学工作原理](https://www.renishaw.com/en/how-optical-encoders-work--36979)

开放式结构将读头和刻度分别安装进机器，有利于低惯量、紧凑或大通孔设计。与此同时，刻度安装、读头间隙、对准和污染条件都成为系统设计的一部分。能否达到目标表现，取决于完整组合及安装条件。

## 产品系列与代表方向

| 方向 | 代表系列 | 选型线索 |
| --- | --- | --- |
| 绝对式 | RESOLUTE、EVOLUTE | 上电位置、接口、刻度与速度 |
| 增量式 | TONiC、VIONiC、QUANTiC | 参考点、分辨率、接口与安装 |
| 小尺寸读头 | ATOM、ATOM DX | 机械空间和匹配刻度 |
| 刻度系统 | 直线尺、圆光栅与环 | 基材、直径、精度和热行为 |
| 诊断与资料 | ADT 等工具、安装指南 | 信号状态、对准与系统调试 |

接口并非所有系列通用。例如官方 FAQ 明确说明 RESOLUTE 不支持 SSI，不能因为绝对编码器常用 SSI，就给某个产品自动补上该接口。选型应查看实际提供的协议和完整订货代码。

## 官方资料

- [开放式光学编码器产品地图](https://www.renishaw.com/en/range-of-renishaw-open-optical-encoders--48432)
- [雷尼绍光学编码器工作原理](https://www.renishaw.com/en/how-optical-encoders-work--36979)
- [RESOLUTE 产品资料与下载](https://www.renishaw.com/en/resolute-absolute-encoder-downloads--37856)
- [官方编码器常见问题](https://www.renishaw.com/en/optical-encoders-frequently-asked-questions--34674)
- [非接触式编码器官方选型指南 PDF](https://www.renishaw.com/media/pdf/en/3600cf80a50043788c1d89e256f9de0f.pdf)
