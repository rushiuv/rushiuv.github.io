---
title: 有距离编码原点，为什么上电后仍要移动？
description: 区分单原点、距离编码参考标记和绝对码，给恢复动作保留方向与信号身份。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
topic_method: true
plan_id: G02
guide_group: 几何与解算
weight: 150
related_basics:
- absolute-incremental
- abz
- singleturn-multiturn
related_model_slugs:
- rod-280
- resolute-rl
related_applications:
- linear-motor
- servo-motor
related_guides:
- position-validity-state
- system-acceptance-record
keywords:
- 有距离编码原点
- 几何与解算
---

增量尺装了“距离编码原点”，不等于变成静止上电就有位置的绝对尺。它把参考标记之间的距离编码成身份，控制器仍要读到足够的标记，才能恢复参考关系。

## 周期位置还缺一个整数

设线性信号周期为p、周期内归一化位置为u，坐标可写为 \(x=p(k+u)+x_0\)。模拟插值能提高u的分辨率，却不能独自知道整数k和机器零位 \(x_0\)。单个相同周期波形在整条尺上会重复。

绝对码在规定启动流程后给当前位置身份；增量系统则依赖计数历史与参考恢复。即使读数小数位很细，未知的k也不会因此自动确定。

## 两个标记为什么比一个有用

[HEIDENHAIN日文测量原理](https://product.heidenhain.de/JPBC/image/HWP.EN/hlr-system/1078628-J3.pdf)说明，距离编码参考标记具有不同间隔，依次越过相邻两标记后可用较短移动建立参考。其规定还涉及运动过程中不改变方向与适用后续电子设备，不能删掉条件只说“任意两点就能回零”。

以自设教学序列为例，若相邻间距分别是100、101、103个信号周期，测得101只能在这套已定义码本中帮助判区；漏标记、反向或测得两段之和时，解释会变化。这不是厂商真实编码规则，更不是可以替换其解码器的算法。

## 恢复之后还要核机器坐标

[ROD 280/280C日文产品资料](https://www.heidenhain.de/fileadmin/pdf/ja/Produktinformation/PI_ROD_200_700_800_ID1385973_ja.pdf)将一个原点与距离编码原点分别列出。标记恢复的是尺的参考关系，机器坐标还取决于安装零位、方向和传动关系。

测试时分别记录断电后首次读数、参考移动、标记序列、建立有效坐标的时刻，以及漏标记/途中反向时的状态。未完成参考恢复的数据可以用于某些受控的相对观察，但不能无标志地当作已恢复的绝对机器坐标。
