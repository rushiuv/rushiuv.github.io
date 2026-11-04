---
title: "AK09973D"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 684
seed_count: 1
lastmod: "2026-11-03"
description: "AK09973D 是旭化成微电子（AKM）的三轴霍尔磁智能开关，输出各轴 16 位磁场数字值，并带可编程阈值与开漏中断，面向折叠/卷轴手机形态检测与低功耗安防。"
official_url: "https://www.akm.com/global/en/products/tri-axis-magnetic-sensor/lineup-tri-axis-magnetic-sensor/ak09973d/"
related_companies: ["AKM"]
datasheet_url: "https://media.digikey.com/pdf/Data%20Sheets/AKM%20Semiconductor%20Inc.%20PDFs/AK09973D_Sep2020.pdf"
datasheet_label: "AK09973D 数据手册 200900045-E-00（2020/9）"
wiki_category: "线性磁场与位移映射"
document_version: "200900045-E-00，2020/9，43页；本次核对2026-11-03"
model_card: true
search_aliases:
  - AK09973D
---

## 核心参数

依据原厂数据手册 [200900045-E-00（2020/9，43页）](https://media.digikey.com/pdf/Data%20Sheets/AKM%20Semiconductor%20Inc.%20PDFs/AK09973D_Sep2020.pdf)。典型值、最值与适用条件分别保留；未在手册给出的项标明「数据手册未给出」。公开 PDF 与原厂产品页登记下载件同为该文档编号（43页／约932KB）。

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应类型 | 三轴霍尔；各轴独立检测弱至强磁场（手册第1页） |
| 数字输出 | 每轴 16 位磁场分量；另有三轴平方和 HV[23:0]（手册第1、32～33页） |
| 高灵敏度档 | 灵敏度典型 1.1 µT/LSB（25°C，SMR=0，min 0.99／max 1.21）；量程典型 ±36.04 mT（同条件，min ±32.44／max ±39.64）；表8.1，第9页 |
| 宽量程档 | 灵敏度典型 3.1 µT/LSB（25°C，SMR=1，min 2.79／max 3.41）；X/Y 典型 ±34.91 mT，Z 典型 ±101.57 mT；表8.2，第9页 |
| 测量时间 TSM | 低噪声驱动（SDR=0）典型 0.825 ms／最大 0.908 ms；低功耗驱动（SDR=1）典型 0.265 ms／最大 0.292 ms；两档量程表同值，第9页 |
| 噪声（设计参考） | 高灵敏度：低噪声 5.5 µTrms、低功耗 15.0 µTrms；宽量程：低噪声 6.8 µTrms、低功耗 18.0 µTrms；恒定磁场、无 Max 列，第9页注\*7 |
| 初始失调 | 高灵敏度 ±500 LSB；宽量程 ±177 LSB；出厂无外加磁场测得的测量数据寄存器值，第9页注\*8 |
| 接口 | I²C；Standard／Fast／Fast-mode Plus；SCL 最高 1000 kHz（第10页）；从地址可选手脚连接选 10h 或 11h（第5页） |
| 中断输出 | OD-INT 开漏、低有效；可报开关事件／DRDY／溢出错误（第1、19页） |
| 供电 | VDD 1.65～1.95 V（典型 1.8 V）；输入电平 VIN 1.1 V～VDD；工作温度 −30～+85°C（第6页） |
| 驱动电流 | 磁传感驱动中典型 1.4 mA／最大 2.2 mA；掉电典型 1.0 µA／最大 3 µA；自检驱动典型 5.6 mA；无电阻负载，第6页 |
| 平均电流（示例） | VDD=1.8 V、+25°C：低功耗驱动 3.5 µA＠10 Hz、22 µA＠100 Hz；低噪声驱动 11 µA＠10 Hz、101 µA＠100 Hz（第1页 Features） |
| 工作模式 | 掉电、单次测量、连续测量（5／10／20／50／100／500／1000／2000 Hz）、自检（第13～14页） |
| 连续 ODR 限制 | 1000 Hz 与 2000 Hz 仅在低功耗驱动（SDR=1）有效；低噪声驱动（SDR=0）下这两档按 500 Hz 测量（第13页） |
| 可编程开关 | 各轴及平方和可设 BOP／BRP 阈值与使能；阈值设定范围／灵敏度与当前测量档相同（第17页） |
| 片上角度解算 | 数据手册未给出整圈角度精度规格；无 arctan／角度输出寄存器（对照产品线公开表，本型号「Internal calculation」为空；本片仅给磁场与平方和） |
| 片内时钟 | 框图 OSC1 为传感测量时钟、OSC2 为周期控制时钟（第4页）；数据手册未给出 OSC1／OSC2 频率 |
| 封装 | 5 引脚 WL-CSP（BGA），1.18 mm × 0.78 mm × 0.55 mm（第1、40页） |
| 典型应用（原厂口径） | 与磁体配合检测相对距离与方位；折叠／卷轴手机形态；智能手表、耳机、安防等低功耗开关场景（原厂产品页；手册第1页写智能手机与可穿戴） |
| 兼容说明 | 原厂产品页写向上兼容 AK09970D |

## 产品功能与测量链

AK09973D 把三轴霍尔、斩波放大、ADC 与开关比较做在同一芯片里：主机经 I²C 读出 HX／HY／HZ 与平方和 HV，也可只依赖可编程阈值与 OD-INT 做事件唤醒。它输出的是磁场数字量与开关状态，不是编码器角度码；整机角度或开合行程需要外加磁路与标定。

## 接入与配置

从地址由 IF1／IF2 与 OD-INT／SDA 的两种脚位接法在 10h 与 11h 之间选择（第5页）。不用中断时须把 OD-INT 接到 VSS。量程（SMR）与驱动（SDR）改变灵敏度、噪声与单次测量时间，不能混用不同档的 LSB 解释。连续 1 kHz／2 kHz 只在低功耗驱动下成立。

## 使用与验证

溢出时 ERR 置位，超限轴输出被钳在手册给定的限值（高灵敏度约 36.04 mT；宽量程 X/Y 约 34.91 mT、Z 约 101.57 mT，第18～19页）。自检须在单次测量模式下使能，且强制低噪声＋高灵敏度；判据为 −120≤HX≤120、−120≤HY≤120、60≤HZ≤400（第18页）。验证应覆盖目标 ODR、驱动档、阈值迟滞与漏读（DOR）行为，不能把 Features 页的 10／100 Hz 平均电流外推到 2 kHz。

### 条件估算（非手册参数、未实测）

若以手册高灵敏度噪声为磁场噪声 σB、并假设平面内两轴合成场强 B=20 mT 恒定，则角度噪声粗算 σdeg≈57.2958×σB/B：低噪声驱动约 0.0158° RMS，低功耗驱动（含可达 2 kHz 的档）约 0.0430° RMS。分母必须是平面内两轴合成磁场幅度，不是单轴或总场任意分量；该换算不是数据手册指标，也不能当作整机角度精度。

## 版本与待核项目

- 本次按 200900045-E-00（2020/9）核对；原厂产品页登记下载件仍为同一文档编号，未见更新版本号。
- OSC1／OSC2 频率：数据手册未给出。
- 整圈／开合角度精度：数据手册未给出。
- SPI：数据手册未给出（仅 I²C）。
- 产品页规格表另列「Current Consumption when measuring 1.4 mA」，与手册第6页驱动电流典型值一致；平均电流仍以 Features／工作模式条件为准。

## 官方资料

- [AK09973D 原厂产品页](https://www.akm.com/global/en/products/tri-axis-magnetic-sensor/lineup-tri-axis-magnetic-sensor/ak09973d/)
- [三轴磁传感器产品线比较](https://www.akm.com/global/en/products/tri-axis-magnetic-sensor/lineup-tri-axis-magnetic-sensor/)
- [AK09973D 数据手册 200900045-E-00（2020/9，43页；经销商托管的同编号 PDF）](https://media.digikey.com/pdf/Data%20Sheets/AKM%20Semiconductor%20Inc.%20PDFs/AK09973D_Sep2020.pdf)
- 原厂站点下载需登记邮箱；文档编号与页数以产品页「AK09973D Datasheet English [200900045-E-00]（43 Pages PDF: 932KB）」为准
