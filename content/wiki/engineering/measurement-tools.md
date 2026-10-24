---
title: "三个小计算：频率、数据年龄与噪声统计"
description: "把PPR和边沿率、时延与电角、RMS和标准差分开计算；结果旁边保留单位与适用条件。"
date: "2026-10-24"
lastmod: "2026-10-24"
layout: "engineering-single"
engineering_entry: true
plan_id: "TOOLS"
guide_group: "测量与统计"
weight: 99
measurement_tools: true
related_basics: ["abz", "latency", "angle-noise"]
related_model_slugs: ["as5047p"]
related_guides: ["rate-budget", "noise-statistics", "spi-data-age"]
keywords: ["计算器", "PPR", "CPR", "边沿频率", "电角度", "RMS", "标准差"]
---

先确认输入的物理量，再按公式算。下面三个工具只在当前浏览器计算，不发送输入数据。转速为机械转速；编码器信号周期数与电机对极数分别输入，不共用一个“极对数”。

## 频率：每圈周期与每秒边沿分开

若AB每圈各有P个完整周期，四倍频每圈计数为4P。机械转速r单位rpm，则 \(f_{AB}=Pr/60\)，\(f_{edge}=4Pr/60\)。另输入编码器每圈模拟信号周期数N，得到 \(f_{signal}=Nr/60\)。

校验点：P=1024、r=6000时，AB基波102400Hz，四倍频合计边沿409600次/s；r=0时均为0。CPR在不同厂家处含义不同，不能把标成4096CPR的值未经确认再乘4。额定边沿能力、电缆与控制器计数上限仍须另核。

## 时间：只计算未补偿的匀速滞后

机械位置归一化为圈，数据年龄为t秒，匀速滞后 \(\Delta u=rt/60\)。换成机械角再乘电机对极数p，得到电角滞后。校验点：6000rpm、10μs、7对极分别为0.36°机械角和2.52°电角；0μs为0。

该结果不是滤波带宽。加减速、预测补偿和随频率变化的相位响应，回到[动态测试](/wiki/engineering/dynamic-latency-test/)单独建模。

## 统计：先说清RMS有没有含偏置

工具对一列有限实数计算均值、含均值RMS、总体标准差、样本标准差和极差。总体标准差分母N，样本标准差分母N−1；没有“自动识别噪声”步骤。

校验点：输入1,2,3，均值2，RMS约2.16025，总体σ约0.81650，样本s=1，峰峰值2。输入5,5,5，RMS为5而σ为0，说明固定偏差不会因为末位不跳而消失。

[下载合成统计示例CSV](/downloads/encoder-noise-example.csv)。工具只接收数值列表，带表头或双列CSV请先取其中一列；不得让时间戳与角度混算。过圈数据应先按[角度噪声的环绕规则](/wiki/basics/angle-noise/)处理。本工具不估置信区间、有效样本数或器件精度。

公式与统计解释参见[噪声算例](/wiki/engineering/noise-statistics/)与[速率预算](/wiki/engineering/rate-budget/)。
