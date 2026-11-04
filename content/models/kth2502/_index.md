---
title: KTH2502
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH2502 是双极锁存Hall开关系列，具有宽电源和开漏输出；QA/QB/QC门限、封装磁方向和上电状态决定其在旋转或位置事件检测中的用法。
wiki_rank: 314
catalog_type: 磁开关
wiki_category: 磁开关
official_url: https://chat.connteck.com/products/switches/KTH2502/
catalog_source: https://chat.connteck.com/products/switches/KTH2502/
search_aliases:
- KTH2502
datasheet_url: https://conntek.github.io/files/KTH2502%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/kth2502-original-figure.png
product_image_caption: KTH2502 产品特点、锁存与应用电路（原手册第1页）
product_image_source: https://conntek.github.io/files/KTH2502%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf#page=1
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 检测逻辑 | 数字双极锁存型Hall开关，开漏NMOS输出；需要跨越相反极性门限切换，移走磁体不能默认释放（手册第1、4、6、8、16页） |
| 推荐工作电源 | 2.7～32 V；在规定自由空气工作温度范围内，除特别说明外；36V为保护/绝对最大口径（手册第10、17页） |
| 输出电压/灌电流 | OUT：0～32 V；灌电流0～30 mA；推荐条件，必须同时遵守功耗和热限制（手册第10页） |
| 工作温度 | −40～150 °C；Q等级；不改写为AEC-Q100 Grade 0（手册第3、10页） |
| 工作电流 | 25°C典型2.7 mA；150°C典型2.7 mA、最大4.5 mA；VCC=2.7～32 V（手册第11页） |
| 上电时间 | 典型35 µs，最大50 µs；A/B/C版本；输出有效前按手册处理高阻状态（手册第11、14、15页） |
| 导通电阻 | 25°C典型11 Ω；150°C典型15 Ω、最大20 Ω；VCC=3.3 V、IO=10 mA（手册第11页） |
| 磁场变化带宽 | 最小20 kHz，典型30 kHz；手册第12页定义为能转换为输出的最快变化磁场；非主控链路频率（手册第12页） |
| QA磁门限 | BOP最小/典型/最大=-25/-15/-5 Gs；BRP=5/15/25 Gs；典型磁滞30 Gs；TA=−40～150°C；保留表中符号，极性必须结合第6—8页封装磁方向图（手册第6、7、8、12页） |
| QB磁门限 | BOP最小/典型/最大=-45/-30/-15 Gs；BRP=15/30/45 Gs；典型磁滞60 Gs；TA=−40～150°C；保留表中符号，极性必须结合第6—8页封装磁方向图（手册第6、7、8、12页） |
| QC磁门限 | BOP最小/典型/最大=-90/-60/-30 Gs；BRP=30/60/90 Gs；典型磁滞120 Gs；TA=−40～150°C；保留表中符号，极性必须结合第6—8页封装磁方向图（手册第6、7、8、12页） |
| ESD | HBM ±4000 V；CDM ±500 V；ESD额定表，不等于系统级ESD能力（手册第10页） |
| 封装引脚 | SOT23/SOT-23-3L：VCC1、OUT2、GND3；TO-92S：VCC1、GND2、OUT3；俯视图；换封装时OUT/GND不能沿用（手册第4、5页） |
| 输出边沿 | 上升典型160 ns；下降典型80 ns；10%～90%/90%～10%，R1=1kΩ、CO=50pF、VCC=3.3V（手册第11页） |

## 锁存器不能只用移走磁体测试

该系列由相反极性的磁场门限完成切换，磁体移远后可能保留原状态。旋转磁环适合产生正负交替磁场；若用于翻盖或单次接近检测，必须先确认机构能完成整个切换路径，不能把普通开关的有磁/无磁逻辑直接套入。

## 门限符号与封装方向一起读取

QA/QB/QC是不同灵敏度档。原厂磁参数表保留BOP与BRP的符号，而SOT-23-3L与SOT23/TO-92S的磁方向说明不同；选择磁体前应先固定封装和观察面，再测动作/释放裕量。换封装还会改变OUT与GND脚序。

## 开漏负载要满足热与边沿条件

手册将输出灌电流限制与功耗、热条件一起规定。上拉电阻决定低电平负载及上升边沿，附加输出电容又影响带宽；接控制器输入、LED或感性负载时分别检查，不能只凭30mA数字认定所有负载可直驱。

## 上电与电源保护各自验证

上电有效前OUT处于高阻状态，主控应等到规定时间后再解释磁状态。手册区分2.7～32V工作电源、36V负载突降保护和反接保护；这些条件不能合成36V长期工作保证，也不能由器件保护推出整车瞬态测试已经通过。


## 公开资料与型号核对

参数采用既有公开原厂KTH2502系列手册，Q等级为−40～150°C；不采用网页AEC-Q100 Grade 0、HBM8kV及5/8mA等冲突数字。

原厂手册确认双极锁存，而非任意有磁/无磁状态开关；封装磁方向需按原图确认。

原厂手册应用例不构成任意继电器直驱、无需外围保护或系统合规保证。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH2502 产品手册.pdf](https://conntek.github.io/files/KTH2502%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
- [KTH2502_Datasheet_CN.pdf](https://chat.connteck.com/downloads/KTH2502/KTH2502_Datasheet_CN.pdf)

[来源产品页](https://chat.connteck.com/products/switches/KTH2502/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

