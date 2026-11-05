---
title: "电机控制之载波频率为什么是20KHz"
date: '2026-10-06T15:43:00+08:00'
slug: "ozKgREmDQ6qsGO6LS0i39Q"
description: "电机控制载波频率为什么选20KHz？结论是：20Khz是“人耳听不见+开关损耗可接受+控制性能够用”三重约束下的工程转折点。"
original: "https://mp.weixin.qq.com/s/ozKgREmDQ6qsGO6LS0i39Q"
original_from: "转载自公众号「嵌入式阿江」"
tags: ["电机控制", "载波频率", "PWM", "开关损耗"]
---

电机控制载波频率为什么选20KHz？

结论是：20Khz是“人耳听不见+开关损耗可接受+控制性能够用”三重约束下的工程转折点。它不是理论最优，而是各约束恰好 都能满足的“甜点”值

![ace5e0ffeae0c634b4f29382bb49e529.png](/images/wx/ace5e0ffeae0c634b4f29382bb49e529.png)

![14ffc37e9bdd2454b4235c2ca554eed1.png](/images/wx/14ffc37e9bdd2454b4235c2ca554eed1.png)

![7348b0f1a48d22a9714cc9cb19114f8b.png](/images/wx/7348b0f1a48d22a9714cc9cb19114f8b.png)

![c2848018e4136207ab30c87b8da0faea.png](/images/wx/c2848018e4136207ab30c87b8da0faea.png)

![add51325d2c5c5a51a7aa6591735b6cb.png](/images/wx/add51325d2c5c5a51a7aa6591735b6cb.png)

![7279cabf1bcb58d7746b1110100aa9b9.png](/images/wx/7279cabf1bcb58d7746b1110100aa9b9.png)

![b8bfd1d05e886747fe724b96c77a68e9.png](/images/wx/b8bfd1d05e886747fe724b96c77a68e9.png)

![b6ef43e4642f6d4f42fcdca72dc40114.png](/images/wx/b6ef43e4642f6d4f42fcdca72dc40114.png)

热管理中的水泵属于 低压MOSFET小功率场景，20Khz是标准选择
