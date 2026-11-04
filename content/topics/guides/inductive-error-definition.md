---
title: 电感芯片的0.36°，是哪一层的角度？
description: 电角误差、模拟通道INL和整机机械误差不能放进同一列比较。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: R10
guide_group: 光学与电感
weight: 110
related_basics:
- inductive-encoder
- inl
- resolution-accuracy
related_model_slugs:
- mlx90520
- mt6901
related_guides:
- vernier-uniqueness
- three-track-observability
keywords:
- 电感编码器
- 电角度
- INL
- 误差预算
aliases:
- /wiki/engineering/inductive-error-definition/
topic_method: true
---


一份手册写±0.36°，另一份写1% INL，模组又给角秒。把三者排成精度榜，先排错的往往不是数值大小，而是它们描述的测量对象。

## 电角先换算，通道INL先别换

令机械归一化角为u，某一接收通道每机械圈重复N次，理想信号相位为 \(a=\operatorname{wrap}_{01}(Nu)\)。如果误差明确是这个相位的电角误差，局部机械误差才可按：

\[
\delta u=\frac{\delta a}{N}
\]

自设N=8，电角误差为0.36°，等于0.001电周期；折成机械角为0.045°，即162角秒。这个换算假设扇区身份正确，也没有加入线圈、靶体或装配的新误差。

反例是模拟信号路径INL。两个通道的传输函数各偏1%，经过比值和反正切后会怎样，取决于两路偏差的形状及相关性；不能把“1%”直接乘360°，再除N，冒充角度准确度。

## 三层数据不能相互顶替

| 标称量 | 它约束什么 | 尚未包含什么 |
| --- | --- | --- |
| 理想输入下的芯片相位误差 | 处理链自身的电角残差 | 实际线圈和靶体失真 |
| 模拟通道传输INL | 输入到输出的非线性 | 外部MCU最终角度误差 |
| 完整模组机械误差 | 指定装配和校准状态 | 未测试工况的结果 |

MLX90520手册将位置误差标为电角，并附理想输入、滤波及动态条件。TI LDC5072-Q1则明确区分通道传输INL与外部MCU计算的角度INL。脚注不是数值之外的附属说明，它决定了哪些量能比较。

## 用两次实验分开责任

第一轮给处理链注入可追溯的理想信号，固定幅度、共模和频率，检验其角度或通道误差。第二轮接回实际线圈与靶体，在相同读取配置下扫描整圈、气隙和偏心，比较新增残差。

两轮结果还需统一校准状态、温度及噪声定义。多轨游标一旦判错扇区，误差会整段跳变，已超出上面的局部除N模型；把这类错误也折成“每电周期百分比”会掩盖失效机制。

校准后的系统误差可以比裸链路的某项指标更小，但必须给出使用的参考与复测条件。不能把几层规格的最大值相减，声称剩下的就是装配贡献；各项是否相关、是否在同一工况测得，以及校准修正了哪一层，都要先说明。

## 公开依据

- [Melexis MLX90520数据手册](https://www.melexis.com/-/media/files/documents/datasheets/mlx90520-datasheet-melexis.pdf)，Rev.001第9～10页的位置误差和输入条件。
- [TI LDC5072-Q1数据手册](https://www.ti.com/lit/ds/symlink/ldc5072-q1.pdf)，查Signal Path电气表及ErrINL脚注。N=8与162角秒为本文换算例子。
