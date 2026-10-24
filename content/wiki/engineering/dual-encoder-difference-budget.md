---
title: "两路角差估扭矩，先算同步误差值多少钱"
description: "把角差统一到输出轴坐标，用明确自设刚度拆开量化误差和采样错位。"
date: "2026-10-24"
lastmod: "2026-10-24"
layout: "engineering-single"
engineering_entry: true
plan_id: "E06"
guide_group: "接入与诊断"
weight: 60
related_basics: ["latency", "resolution-accuracy", "singleturn-multiturn"]
related_model_slugs: ["reagles-kit", "reagles-kid"]
related_guides: ["system-acceptance-record", "position-validity-state", "sample-time-contract"]
related_applications: ["robot-joint", "gearbox"]
keywords: ["双编码器", "角差估扭矩", "同步预算"]
---

电机端角度除以减速比，再与输出端相减，得到传动链的一个观测量。只有在零位、方向、圈数和采样时刻一致，且所用刚度模型成立时，才能进一步估算扭矩。

## 先把坐标写全

取减速比\(N\)，把两路角度写成连续归一化圈数\(u_o,u_m\)（一圈为1），并对齐同一输出位置：

\[
\delta(t)=2\pi[u_o(t)-u_m(t)/N-u_0],\qquad \hat T=K\delta
\]

\(u_0\)是输出轴归一化零差，须记录建立时的负载条件。乘\(2\pi\)后\(\delta\)仍用rad进入\(K\delta\)，\(K\)用N·m/rad。本文扭矩正方向按δ的定义约定，若采用相反驱动扭矩方向应同步变号，以下误差幅值不变。连续多圈不能先丢掉圈数再相减；换向、迟滞或分段刚度不能被一个零点常数吸收。

## 一个明确自设的算例

以下全部是纸面预算：设\(K=10\,000\ \mathrm{N\cdot m/rad}\)、\(N=100\)，两端各用17bit单圈量化，输出端转速60rpm。它们不属于任何具体减速器或编码器的实测规格。

输出端一LSB为\(2\pi/2^{17}=47.94\ \mu\mathrm{rad}\)，乘刚度约0.479N·m；电机端一LSB折到输出端后约0.00479N·m。若采用四舍五入量化，两路最坏半LSB合计约0.242N·m，尚未计入精度、噪声与安装误差。

两路实际采样错位100µs，在匀速刚体运动假设下：

\[
\Delta T_t\approx K\omega_o\Delta t
=10^4\times2\pi\times10^{-4}=6.28\ \mathrm{N\cdot m}
\]

时差降至10µs变为0.628N·m；刚度加倍，以上扭矩等效误差也加倍。静止时这项为零，所以静态调零发现不了它。主机先后收到数据的间隔，也不能直接当成实际采样时差。

## 从预算走向可用模型

[Harmonic Drive工程目录](https://www.harmonicdrive.net/_hd/content/documents1/CSD_Component.pdf)将扭转曲线分段，并讨论迟滞及目录模型未包含的轴扭转。因此下一步是用独立扭矩参考，在规定温度、加载与卸载路径下测\(T\)—\(\delta\)，保留残差；在此之前仅称“角差观测”。采样一致性也要按具体器件实现，例如[ADMT4000手册的联合读取要求](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)只保证规定读法下内部两个位置寄存器的同次采样，不保证两颗芯片已经同步。
