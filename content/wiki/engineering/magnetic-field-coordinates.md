---
title: 对径两点的磁场同向还是反向？先固定坐标
description: 理想偶极子的点反演、局部坐标和敏感分量是三件事；箭头不能替代坐标定义。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: R06
guide_group: 几何与解算
weight: 106
related_basics:
- mounting
- amr
- vertical-hall
related_model_slugs:
- kmz60
- kth5701
related_guides:
- multihead-harmonics
- amplitude-temperature-error
keywords:
- 磁场方向
- 坐标系
- 敏感轴
- 偶极子
---

同一张双点测量示意图，写“两个磁场相反”或“两个磁场相同”，都可能显得顺口。真正需要说明的是：两个点在哪里，箭头用哪套坐标，以及传感器读的是哪个分量。

## 先用理想模型固定一个答案

令旋转磁矩方向为 \(\mathbf m(u)\)，\(u\) 是归一化机械角。远场理想偶极子模型为：

\[
\mathbf B(\mathbf r)\propto
\frac{3(\mathbf m\cdot\hat{\mathbf r})\hat{\mathbf r}-\mathbf m}{r^3}
\]

把观测位置整体换成 \(-\mathbf r\)，两个 \(\hat{\mathbf r}\) 同时反号，乘积不变，因此 \(\mathbf B(-\mathbf r)=\mathbf B(\mathbf r)\)。这是点反演关系，包含三个坐标一起变号。

作一个可重算例子：磁矩沿全局x轴，观测点在正、负y轴且距原点同为R。两点都有 \(\mathbf m\cdot\hat{\mathbf r}=0\)，场均沿负x方向；它们没有因为位于直径两端就变成相反的全局矢量。

## 局部坐标反了，数字也会反

若第二个测点的局部x、y轴都相对全局转180°，同一个全局面内矢量，在局部坐标中两个分量都会反号。原始通道符号变了，并不意味着物理磁场变了。

对方向响应为两倍相位的理想AMR桥，磁场方向相差半圈又会重复。Hall器件则要看它具体测Bx、By还是Bz。不能从“封装转了180°”直接推导所有器件都应该求和或求差。

## 一张图至少留下三组箭头

画出全局坐标、每颗器件敏感轴和每个测点的场分量，再把读数转换到同一坐标比较。实验可用三轴场传感器在固定磁体下逐点测量，并改变传感器姿态，检查符号变化能否由坐标变换解释。

真实有限尺寸磁体近场不一定适合偶极子近似。同一高度平面上的两个对径点，也不等于三维点反演；面内分量与垂直分量不能混说。这里的对称式不构成任意磁环、钢件和安装位置下的精度保证。

磁场矢量与器件输出还隔着传递函数。磁场反向时，某个桥路可以给相同输出，另一种器件却会翻转状态；即使两者都称“磁传感器”，也没有统一的符号规则。核图时应把物理场、局部坐标和电气输出分成三行检查，避免用一支箭头代替全部关系。

## 公开依据

- [ADI AN-1314](https://www.analog.com/en/resources/app-notes/an-1314.html)，对照轴端、离轴配置与AMR方向重复关系。
- [TI TMAG5170数据手册](https://www.ti.com/lit/ds/symlink/tmag5170.pdf)，核对三轴测量、感应方向和可选测角平面。偶极子算例仅用于解释坐标。
