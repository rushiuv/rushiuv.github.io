---
title: 增量与绝对：上电后知道什么
description: 用断电移动与重新上电的例子，讲清增量位置、绝对位置和机器零点。
date: '2026-10-16T10:00:00+08:00'
lastmod: '2026-10-24'
layout: basic-single
basic_entry: true
basic_group: 认识编码器
weight: 2
related_basics:
- abz
- singleturn-multiturn
- interfaces
related_topics:
- 编码器接口
related_model_slugs:
- as5047p
related_applications:
- closed-loop-stepper
- robot-joint
related_guides:
- position-validity-state
- vernier-uniqueness
- reference-recovery
---



增量输出告诉控制器“又走了几步”；绝对输出告诉控制器“当前在测量范围的哪个位置”。区别在位置信息如何建立，不能只看接口插头或输出位数。

<figure class="basic-figure"><img src="/images/basics/incremental-position.webp" alt="增量位置图：从参考标记建立基准，再累计到当前位置的计数" loading="lazy"><figcaption>按雷尼绍增量位置图重绘：重复刻线提供位移变化，参考标记用于建立基准。图中直线尺说明的信息关系同样适用于旋转计数。<a href="https://www.renishaw.com.cn/zh/introduction-to-encoder-systems--47256" target="_blank" rel="noopener">原理图来源 ↗</a></figcaption></figure>

## 增量位置怎样建立

以旋转AB输出为例，控制器根据两路信号的状态变化累加或减小计数。已经有参考位置时，后续计数便可换算为角度。首次启动、计数器复位或掉电丢失计数后，需要重新建立参考。

Z索引提供一个可重复识别的标记。控制器常用它配合回零流程，但“收到一次Z”并不天然等于机器零点：安装角度、回零方向和机械限位仍须定义。

## 绝对位置为什么能直接读

绝对编码器在规定范围内保留能够区分位置的物理信息。它可以来自唯一编码图案，也可以来自磁场方向、多码道组合等。上电并完成器件规定的启动流程后，读头解码当前位置，不必先累计一段运动。

| 场景 | 普通增量计数系统 | 单圈绝对系统 |
|---|---|---|
| 刚上电，轴不动 | 没有历史计数便缺少位置基准 | 可读当前圈内角度 |
| 掉电时转动90° | 未供电的计数链无法记录这段变化 | 上电后读到新的圈内角度 |
| 掉电时多转完整一圈 | 圈数信息缺失 | 圈内读数相同，也无法识别多出的整圈 |

以上对比针对相应测量链没有备用计数装置的情况。增量信号配备独立的持续供电计数器，也能保留历史位置。

## 绝对角度仍要设机器零点

编码器的零度取决于码盘、磁体或出厂定义。机器的零度取决于机械基准。两者之间通常需要设置零位偏移，并规定方向。绝对编码器解决位置读取问题，不会自动完成整机坐标标定。

[雷尼绍：绝对式与增量式的工作差异](https://www.renishaw.com.cn/zh/introduction-to-encoder-systems--47256)。

## 断电跨零位，先问是否保留了圈数

自设单圈读数从u=0.95断电后转到1.05，上电只得到0.05；没有额外多圈信息，无法区分前进0.10圈与倒退0.90圈。[HEIDENHAIN德文测量原理](https://content.heidenhain.de/presentation/LMG/de/index/N101F5/N1052A/N10586/N10586.html)说明绝对码尺直接提供范围内位置，不等于无限圈数。测试应同时保存启动有效状态与独立运动记录，再核[单圈和多圈](/wiki/basics/singleturn-multiturn/)。按[位置有效性](/topics/guides/position-validity-state/)通过检查后，[闭环步进](/applications/closed-loop-stepper/)才能把读数送入机器坐标。
