---
title: 3.3V供电和5V总线，兼容性要查四项
description: 推荐电压、输入容限、逻辑门限和掉电隔离分别核对，不能只看供电范围。
date: '2026-10-24'
lastmod: '2026-10-24'
layout: engineering-single
engineering_entry: true
plan_id: E03
guide_group: 接入与诊断
weight: 30
related_basics:
- spi-ssi
- interfaces
related_model_slugs:
- admt4000
related_guides:
- first-power-interface
- system-acceptance-record
related_applications:
- servo-motor
- pneumatic-cylinder
keywords:
- 混压
- 反供电
- 掉电隔离
aliases:
- /wiki/engineering/mixed-voltage-backpower/
topic_method: true
---


器件能用3.3V供电，不足以说明它能直接接5V主机。供电范围描述芯片如何工作；输入容限描述引脚能承受什么。主机先上电时，还要问传感器断电的IO是什么状态。

## 在原理图旁写四列

| 项目 | 要找的证据 |
| --- | --- |
| 推荐工作条件 | 每个电源域正常工作的上下限 |
| 引脚电压容限 | 正常及断电时的输入范围，不能拿绝对最大额定值当连续工作范围 |
| 逻辑门限 | 发送端最差VOH/VOL能否满足接收端VIH/VIL，并保留负载条件 |
| 掉电行为 | 是否明确给出Ioff、隔离条件、上电顺序及控制脚参考电源 |

例如[ADMT4000 Rev.C表4](https://www.analog.com/media/en/technical-documentation/data-sheets/admt4000.pdf)把数字输入的绝对最大范围上限写为VDRIVE+0.3V。若VDRIVE=3.3V，5V输入已高于这个上限。这里比较的是额定值，不能进一步推测它会经哪个内部结流过多少电流。

## 转换器也有自己的条件

[SN74LVC1T45手册](https://www.ti.com/lit/ds/symlink/sn74lvc1t45.pdf)给出双电源、Ioff和VCC隔离：任一电源接地时，两端口进入高阻；DIR参考VCCA。这些条款能用于设计电源顺序，但“任一端为0V”不能外推成任意缓慢爬坡电压下都已隔离。

固定方向SPI信号应分别核方向和负载。转换器的数据率上限也不能替代整块板的时序裕量；传播延迟、时钟与返回数据路径仍须按实际频率检查。

台架上先以限流电源验证双方正常供电，再验证允许的单侧上电组合，同时记录被断电电源轨与IO波形。该顺序应先经手册确认，不通过超额电压“试耐压”。若掉电侧电源被抬起，先停测并查允许的掉电路径；只见电压抬升尚不足以定位某颗保护二极管。

没有输入容限或掉电条款时，记录“兼容性未证实”，向原厂补证或换有明确规格的接口方案。不要凭供电范围勾选兼容，也不要用一个串联电阻把未知注入电流变成默认可接受。接着按[首次上电核对](/topics/guides/first-power-interface/)重新检查全链路。
