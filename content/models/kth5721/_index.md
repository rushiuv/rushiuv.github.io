---
title: KTH5721
wiki: true
wiki_type: model
catalog_form: 芯片
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
model_card: true
description: KTH5721 的公开手册首页提供XYZ磁场、温度及XY/XZ/YZ平面CORDIC角度输出，内部采用16位ADC；AQ2工业级与AQ3消费级需要按后缀分别选型。
wiki_rank: 303
catalog_type: 线性磁场
wiki_category: 线性磁场
official_url: https://chat.connteck.com/products/3d-hall/KTH5721/
catalog_source: https://chat.connteck.com/products/3d-hall/KTH5721/
search_aliases:
- KTH5721
datasheet_url: https://chat.connteck.com/downloads/KTH5721/KTH5721_Datasheet_CN.pdf
datasheet_label: 数据手册原链接
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
product_image: /images/catalog/kth5721-browser-original.jpg
product_image_caption: KTH5721 原厂典型磁体安装示意，公开手册第1页
product_image_source: https://chat.connteck.com/downloads/KTH5721/KTH5721_Datasheet_CN.pdf
---

## 核心参数

| 项目 | 内容与条件 |
| --- | --- |
| 检测输出 | XYZ三轴磁场；温度输出；XY/XZ/YZ平面CORDIC角度；公开手册首页功能说明；角度输出与磁场分量分开理解（手册第1页） |
| ADC | 16 bit；首页明确ADC位数；不能写成16位机械精度（手册第1页） |
| 磁场量程 | XY典型±130 mT；Z典型±80 mT；首页标注典型量程；使用平面角度输出建议该平面场强大于20 mT（手册第1页） |
| 主电源与IO | 主电源2.8～5.5 V；IO可低至1.8 V；两类电源不能混为1.8V主电源工作（手册第1页） |
| 温度等级 | AQ2工业级−40～105°C；AQ3消费级−40～85°C；按完整订货等级区分，不能把一个等级温区覆盖全系列（手册第1页） |
| 封装与接口 | QFN3×3-16L或DFN2×2.5-8L；SPI或I²C；封装与订货后缀一一对应；接口速率未在首页给出（手册第1页） |
| 测量模式 | 持续感应、唤醒睡眠、单次测量；按键检测/Trigger；首页功能说明；采样时间、电流及寄存器值仍需核读对应表格（手册第1页） |

## 同一磁场数据可以服务不同测量平面

原PDF首页列出XYZ磁场以及XY、XZ、YZ平面CORDIC角度输出，XY典型量程±130mT、Z典型±80mT。设计时先确定机构运动平面和对应磁场轨迹，不能把磁场量程直接换成位移或角度准确度。

## ADC位数与角度精度分别理解

手册首页明确内部16bitADC；这不是矩阵中“12bit”口径可直接覆盖的参数，也不是16位机械精度保证。实际误差还取决于磁体几何、信号范围和校准，应在全行程对照位置参考验证。

## 等级与封装必须连同订货后缀

首页分别列AQ2工业级−40～105°C与AQ3消费级−40～85°C，并提供QFN3×3-16L或DFN2×2.5-8L路径。选择时应匹配完整订货后缀，不能把更宽温区、不同封装与另一等级的条件混在一个料号上。

## 测量模式确定后再核总线与响应

首页列SPI或I²C，以及持续感应、唤醒睡眠和单次测量等模式。当前核读仅到第1页，接口速率、采样时间、电流和寄存器细节还需对应表格；不根据矩阵中的5KSPS或AEC标签直接做整机响应或车规承诺。


## 公开资料与型号核对

本页采用目视核读的原PDF第1页功能说明；仅确认该页所列AQ2/AQ3和封装路径，未完整核读电参数表或确认所有订货后缀。

原PDF首页16bitADC、SPI或I²C与XYZ/CORDIC能力优先于矩阵12bit及详情I²C-only等冲突说法；ADC位数不作为机械精度。

AQ2为−40～105°C、AQ3为−40～85°C；不从矩阵AEC-Q100、SPI/5KSPS标签增加资格、速率或温度保证。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH5721_Datasheet_CN.pdf](https://chat.connteck.com/downloads/KTH5721/KTH5721_Datasheet_CN.pdf)

[来源产品页](https://chat.connteck.com/products/3d-hall/KTH5721/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)

