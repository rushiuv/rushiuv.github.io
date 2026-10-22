---
title: "传周科技"
wiki: true
wiki_type: "company"
wiki_rank: 44
seed_count: 5
lastmod: "2026-10-22"
description: "传周科技：2018 年建在上海张江的光电编码芯片公司，透射式 512CPR 量产，反射式用 16 位 M 序列，另有无磁电感在售。"
official_url: "https://www.time-vision.com/about/overview"
wiki_category: "传感器与测量前端"
related_models: []
---

传周科技站在"芯片 + 码盘 + 读数头"这一层：它把光电探测器阵列、码盘、角度解算芯片和整只光栅尺系统分开报价，客户可以直接买一颗芯片，也可以买读数头加栅尺的成品。读它的产品页最该注意两件事——分辨率用的是 CPR、栅距还是 M 序列位数三种口径；以及型号状态（已量产 / 可送样 / 预发布），状态比参数更能说明现在能不能用。

## 公司与品牌

传周半导体科技（上海）有限公司，官网自述 2018 年成立于上海张江，国家级高新技术企业。产品线自述覆盖光栅尺芯片及直线光栅尺系统、光电编码器芯片、电感编码器芯片、光电探测器、特种光学器件，并承接光电传感芯片定制开发。官网自报行业经验 7 年以上、员工 50 余人、专利与软件著作权 100 余项，均为公司口径，无第三方数据佐证。

技术链条的说法值得留意：它把光学架构设计、光电 ASIC、微弱信号算法、精密光机结构、封装测试列为自主环节，并称已实现高、中、低端光电编码芯片与中高端光栅尺系统量产。对选型的人，这句话的实际含义是码盘与光源也自己做，客户不必再找第二家配光学件。[公司简介](https://www.time-vision.com/about/overview)

## 编码器相关产品线与公开规格

官网用四组目录组织编码器件：透射式光电编码芯片、反射式光电编码芯片、角度解算芯片、电感式位置传感器芯片，另有光源、码盘、开发板套件与光栅尺系统。下表数值取自各目录页的选型表，是系列级典型值，不构成选型保证。

| 系列 | 类型 | 公开分辨率/关键指标 | 其他公开参数 |
| --- | --- | --- | --- |
| [TVOET3309E / 2609G / 3309G](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 透射式绝对值（相位阵游标） | 512 CPR | 码盘 26 / 33 mm、4.1~5.5 V、QFN32、−40~125 °C、5×5×0.9 mm、已量产 |
| [TVOET2611F](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 透射式绝对值 | 2048 CPR | 26 mm 码盘、4.1~5.5 V、QFN32、−40~125 °C、预发布 |
| [TVOETL225P / 225U](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 低分辨率透射式增量 | 最大 2500 CPR | 光学中心 11 mm 设计、标准 CPR 50~2500、Z 信号 1T / 0.5T / 0.25T 可选、预发布 |
| [TVOERA127A](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 反射式绝对值 | 绝对码道 12 位 M 序列 + 增量码道 512 CPR（栅距 127 µm） | 26 mm 码盘、3.3/5 V、QFN32、−40~125 °C、5×5×0.8 mm、可送样 |
| [TVOERA204N / 262N](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 反射式绝对值 | 绝对码道 16 位 M 序列，增量栅距 204.8 / 262.6 µm | 码盘 ≥44.6 mm 与 16.2~44.6 mm、5 V、LGA32、−40~125 °C、可送样 |
| [TVOERH300A / 300M](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 反射式增量（无透镜） | 栅距 80 µm | 内置蓝光 LED、1X~16X 插值、ABZ 或差分 sin-cos 输出、QFN24 4×4 / LGA16 3×3 mm、预发布 |
| [TVOERH180B / 360B](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1) | 反射式增量 | 180 / 360 LPI | LGA8 3×3×0.9 mm、−40~85 °C 与 −40~115 °C、预发布 |
| [TVCAxxCxMx](https://www.time-vision.com/product/encoder/calculation-angle) | 角度解算芯片 | 双 16 位 ADC，读差分 sin/cos、Z 与 M 序列 | 3.3 V、−40~105 °C、QFN 5×5×0.75 mm、串口输出、SPI 可配、支持线性校准与温度补偿 |
| [TVHEPAC00A](https://www.time-vision.com/product/inductive-encoder-chip/inductive-encoder-chip) | 电感式编码器芯片（无磁铁，涡流检测） | 2 组两相或三相线圈，分辨率由线圈与靶标设计决定 | 3~5.5 V、QFN32、−40~125 °C、5×5×0.75 mm、可送样 |
| [TVHECHL00X](https://www.time-vision.com/product/inductive-encoder-chip/integration-inductive-encoder-chip) | 全集成式电感编码器芯片 | 最高 23000 RPM、码盘外径 28~73 mm | 4.5~5.5 V、LGA8 6×5×0.9 mm、−40~125 °C、预发布 |
| [TVMDGH020D / 080D / TVMDGA102N](https://www.time-vision.com/product/grating-scale-system-solution/grating-scale-readout-head/grating-scale-readout-head) | 光栅尺读数头 | 分辨率 2.5 / 10 / 10 nm，精度 ±20 / ±50 / ±100 nm | 栅距 20 / 80 / 102.4 µm、速度 12 / 8 / 4 m/s、0~70 °C、RS485 |

三点值得单独记。**透射式绝对值走相位阵游标**：官方描述是特殊光电二极管阵列加数字轨道识别游标刻度，VCC 关闭时可由 VB 备用电源维持扇区检测——"备用电源维持扇区"在绝对值方案里不常见。**反射式绝对值用 M 序列码道**：TVOERA127A 给 12 位，204N / 262N 给 16 位，增量码道另给 512 CPR 或 204.8、262.6 µm 栅距。**电感式走无磁铁涡流**：靶标可以是铝、钢或带铜层的 PCB，不是磁铁，这一点直接决定它在强杂散场场合的定位。[透射与反射式目录](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1)；[光栅尺系统](https://www.time-vision.com/product/grating-scale-system-solution)

## 在编码器链上的位置

传周同时卖芯片、码盘、光源、读数头与整只栅尺系统。向下它直接对整机编码器厂、伺服与机床客户；向上它要自己解决晶圆、封装与光学件，所以它既不是纯 fabless 芯片公司，也不是只做整机的编码器厂，而是"光学件 + 芯片"打包卖的一层。

能推断的是取舍：给 M 序列绝对码道、给 512 CPR 到 2500 CPR 的宽档增量、同时给无磁电感，说明它把"绝对值怎么实现"按成本与码盘尺寸分成了三条路。不能推断的是代工方与客户名单：官网不公布晶圆厂，不公布哪家编码器厂用了它的芯片，也不公布各型号出货结构。

## 公开资料的边界

目录页给的是系列级上限，而且三种口径混在一列里：既有"512 CPR"，也有"绝对码道 12 位 M 序列"，电感芯片那一格写的是"2 组两相或三相线圈"，没有等效位数。读数头给了 nm 级分辨率与 ±20~±100 nm 精度，但那是含栅尺与安装的系统指标，不能与芯片位数直接换算。

没有公开的：逐型号 INL 与角秒级精度、重复性、温漂、各接口下的输出延时、码盘与芯片的对位公差、气隙范围、MTBF。预发布型号（TVOERH300A / 300M、TVHECHL00X、TVMDGH020D、各栅尺）参数仍可能变。报价、MOQ 与交期不在官网，只走线上商城或销售。

## 官方资料

- [传周科技官网](https://www.time-vision.com/)
- [公司简介](https://www.time-vision.com/about/overview)
- [透射式与反射式编码器芯片目录](https://www.time-vision.com/product/encoder/optical/optical-encoder-chip?tp=1)
- [角度解算芯片 TVCA](https://www.time-vision.com/product/encoder/calculation-angle)
- [电感式编码器芯片 TVHEPAC00A](https://www.time-vision.com/product/inductive-encoder-chip/inductive-encoder-chip)
- [全集成式电感编码器芯片 TVHECHL00X](https://www.time-vision.com/product/inductive-encoder-chip/integration-inductive-encoder-chip)
- [TVHECHL00X 产品页](https://www.time-vision.com/product/inductive-encoder-chip/integration-inductive-encoder-chip/130)
- [光栅尺系统解决方案](https://www.time-vision.com/product/grating-scale-system-solution)
- [光栅尺读数头](https://www.time-vision.com/product/grating-scale-system-solution/grating-scale-readout-head/grating-scale-readout-head)
- [栅尺](https://www.time-vision.com/product/grating-scale-system-solution/scale/scales)
