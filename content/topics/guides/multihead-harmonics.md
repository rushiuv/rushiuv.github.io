---
title: 两个读头平均，先问要消哪一阶
description: 90度与180度布局抑制不同空间谐波；同一尺度双读头与传动两端双编码器要分开。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: R02
guide_group: 几何与解算
weight: 102
related_basics:
- eccentricity
- angle-noise
- mounting
related_model_slugs:
- tle5012b
related_guides:
- eccentricity-budget
- channel-angle-harmonics
keywords:
- 双读头
- 180度
- 90度
- 空间谐波
aliases:
- /wiki/engineering/multihead-harmonics/
topic_method: true
---


同一圆周刻度上放两个读头，平均以后误差没有明显减小，并不一定是平均程序写错。读头间隔决定它会压低哪些空间阶次；摆在90°和180°，处理的对象不同。

## 先把两路变成同一个角度

令两读头沿刻度相隔归一化角 \(\Delta u\)，均已换算到同一机械位置 \(u\)、同一采样时刻。假设两路同阶误差等幅，按空间位置平移，且采用等权平均。第 \(n\) 阶的残余比例为：

\[
G_n=\left|\frac{1+e^{-j2\pi n\Delta u}}2\right|
=|\cos(\pi n\Delta u)|
\]

| 圆周间隔 | 一次残余 | 二次残余 | 四次残余 |
| --- | --- | --- | --- |
| 180°，即1/2圈 | 0 | 1 | 1 |
| 90°，即1/4圈 | 0.707 | 0 | 1 |

设单头一次误差峰值为100角秒，90°等权平均后仍有70.7角秒；180°才在理想模型中消掉这一项。若主要是四次误差，两种摆位都不消除。

## 两颗不一致时，零点会漏出残差

以180°消一次为例：若一颗该阶幅值100角秒，另一颗只有90角秒，平均仍剩5角秒。安装角偏差、各自校准、不同延迟，也会破坏“同一误差的空间平移”前提。

两路不相关的随机噪声则按标准差约降为原来的 \(1/\sqrt2\)，与90°还是180°无关。这个噪声收益不能当作周期误差也被消除的证据。

## 验收看频谱，不只看峰峰值

同时保存两路原始角度和独立参考，先统一方向、零点、环绕与时间，再比较平均前后的机械阶次幅值。故意改变转速：随转速增加的差值还要排查采样错位，不能全部归到空间布局。

模型描述同一尺度的读头，并不解释电机端与负载端两个编码器的角差。后者还包含减速比、回差和弹性。封装朝向转90°也不等于读头沿圆周相隔90°。

平均前还要处理环绕：359°与1°描述接近零点的两个角，直接算术平均却是180°。应先统一到连续分支，或使用适用的圆周平均，再做空间误差分析。否则一次跨零错误足以淹没原本想观察的谐波抑制效果。

## 公开依据

- [Renishaw：多读头与旋转测量误差](https://www.renishaw.com/en/the-accuracy-of-rotary-encoders--47130)，介绍对径读头与奇次重复误差。
- [RLS：准确度、分辨率和重复性](https://www.rls.si/eng/faq/what-do-accuracy-resolution-and-repeatability-mean)，说明刻度与读头对误差的不同贡献。上式和100角秒例子为本文理想模型。

<figure class="technical-figure"><div class="technical-diagram-scroll" role="region" aria-label="可横向查看的技术图" tabindex="0"><img src="/images/technical/multihead-harmonics.svg" alt="等幅、等权且同采样时刻时，90°与180°的空间阶次响应。" loading="lazy" decoding="async"></div><figcaption>等幅、等权且同采样时刻时，90°与180°的空间阶次响应。</figcaption></figure>
