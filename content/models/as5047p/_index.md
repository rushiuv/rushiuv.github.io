---
title: "AS5047P"
description: "AS5047P 是 14 位在轴霍尔磁角度传感器，集成 DAEC 动态角度补偿，提供 SPI 绝对位置、ABI 增量及 UVW 换向输出。"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 16
seed_count: 12
lastmod: "2026-10-24"
related_companies: ["ams OSRAM", "英飞凌"]
official_url: "https://www.infineon.com/part/AS5047P"
datasheet_url: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5047p-datasheet-en.pdf"
datasheet_label: "AS5047P 数据手册"
document_version: "英飞凌附 2026 年归属说明；原 ams 技术正文 v2-00，2021-07-22"
model_card: true
product_image: "/images/wiki/as5047p.webp"
product_image_caption: "图片来源：英飞凌 AS5047P 产品页，为 TSSOP-14 封装示意。"
product_image_source: "https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5047p-datasheet-en.pdf"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 感应方式 | 在轴霍尔磁角度测量 |
| 绝对角度 | 14 位，SPI 读取 |
| 转速能力 | 最高 28,000 rpm |
| 输出 | 四线 SPI、ABI、UVW、PWM |
| ABI 二进制模式 | 最高 1024 脉冲／圈，4096 步／圈 |
| ABI 十进制模式 | 最高 1000 脉冲／圈，4000 步／圈 |
| UVW | 1～7 对极可编程 |
| 封装／温度 | TSSOP-14，−40～125°C |
| 供电模式 | 3.3 V 模式 3.0～3.6 V；5 V 模式 4.5～5.5 V |
| 动态补偿 | DAEC，面向运动过程中的处理延时补偿 |
| 理想数字码距 | 按14位全圈换算：360°/2^14 ≈ 0.02197266°；计算值，不是准确度保证 |
| 工作磁场 | 35～70 mT，按芯片表面半径1.1mm圆周的垂直场分量；低于35mT噪声性能下降 |
| 供电电流上限 | 15 mA，正文第6页 |
| INL（最佳安装） | 25°C最大±0.8°；全温最大±1° |
| 噪声上限 | 0.068° RMS（1σ），含PWM；按规定磁场，设计保证而非生产测试 |
| SPI核心传播延迟 | 90～110 µs，正文第7页；与经DAEC补偿的输出延迟分开 |
| ABI／UVW动态补偿后延迟 | 1.5～1.9 µs，正文第7页 |
| SPI数据刷新间隔 | 典型222 ns，范围202～247 ns；不是核心传播延迟 |
| 启动时间 | 最大10 ms，电源达到工作下限到首个有效角度 |
| 动态误差示例 | 1700rpm匀速最大0.02°；14500rpm匀速最大0.18°；25000rad/s²恒加速度最大0.175°，均按正文第8页参考磁体条件 |

参数来源：本页所列[原厂产品资料与手册](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5047p-datasheet-en.pdf)。

资料定位：AS5047P v2-00（2021-07-22）正文第6～8页，当前PDF前置两页英飞凌归属说明；第7页表中0.068°为Max列、90/110µs及1.5/1.9µs分别为Min/Max列，已核对原表。

## 工作方式与型号定位

AS5047P面向同时需要上电绝对位置、增量计数和电机换向的系统。14位SPI角度、ABI脉冲和UVW电角度是同一转动的不同表达，控制器要分别配置方向、零点及电机极对数。

## 安装、接口与配置

DAEC用于运动中的动态角度误差补偿。匀速旋转下的相位误差、加减速响应与静止噪声应分别评估，不能由最高转速或补偿功能推导出任意轨迹的误差。磁体的偏心与倾斜还会产生独立的周期误差。

## 校准与选型验证

二进制ABI档1024脉冲/圈对应四倍频4096步，十进制档1000脉冲对应4000步。主控应核对计数口径、Z相与机械零点；供电按3.3V或5V模式接线，不能把两种电路的去耦和引脚连接混用。

## 官方资料

- [官方产品介绍](https://www.infineon.com/part/AS5047P)
- [下载AS5047P 数据手册（官方 PDF）](https://www.infineon.com/assets/row/public/documents/30/49/infineon-as5047p-datasheet-en.pdf)
- 资料版本：英飞凌附 2026 年归属说明；原 ams 技术正文 v2-00，2021-07-22
