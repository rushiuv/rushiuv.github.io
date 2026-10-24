---
title: "QRD1114"
wiki: true
wiki_type: "model"
wiki_rank: 139
seed_count: 1
lastmod: "2026-10-24"
description: "QRD1114是onsemi反射式光电传感器，将红外发射与光电晶体管检测组合，用反射光强判断物体或条纹变化。"
official_url: "https://www.onsemi.com/pdf/datasheet/qrd1113-d.pdf"
datasheet_url: "https://www.onsemi.com/pdf/datasheet/qrd1113-d.pdf"
datasheet_label: "官网文档入口"
wiki_category: "反射检测与条纹读取"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
---

## 核心参数

| 参数 | 数值、功能与适用条件 |
| --- | --- |
| 检测方式 | 红外反射式 |
| 组成 | 红外发射器与光电晶体管 |
| 输出 | 光电晶体管电流，需外部阈值或 ADC 处理 |
| 发射波长 | 940nm典型，IF=20mA、TA=25°C，Rev.6 |
| 导通接收电流 | QRD1114最小1mA；IF=20mA、VCE=5V、D=0.050英寸(1.27mm)、90%漫反射白卡 |
| 发射正向电压 | 最大1.7V@20mA、25°C；不是推荐供电值 |
| 响应时间 | 上升10µs、下降50µs典型；VCE=5V、RL=100Ω、IC(ON)=5mA |
| 温度范围 | −40～85°C，手册额定范围 |

参数依据：[原厂产品页或对应资料](https://www.onsemi.com/pdf/datasheet/qrd1114-d.pdf)。

## 产品功能与测量链

QRD1114由红外发射器和光电晶体管构成，利用目标反射光强检测存在或条纹变化。需要外部限流与接收电路，模块板上的比较器和数字输出不属于裸器件内部功能。

## 接入与配置

发射电流决定光功率，接收负载决定电压摆幅与响应速度。目标距离、颜色、光泽和环境红外都会影响接收电流；不能把一种白纸测试结果当成所有目标的探测距离。

## 使用与验证

用于简易码盘时应检查黑白反射对比、阈值迟滞与速度下的边沿。单只探头不能独立判断运动方向，方向识别需要额外空间相位信息；QRD1113与1114的筛选规格也应分开。

码盘印刷应在实际红外波长下测反差；人眼看来很黑的油墨仍会反射红外，不能只按可见光外观判断。

## 官方资料

- [QRD1114 原厂资料入口](https://www.onsemi.com/pdf/datasheet/qrd1113-d.pdf)
- [官网文档入口（官方入口）](https://www.onsemi.com/pdf/datasheet/qrd1113-d.pdf)

- [QRD1113/QRD1114 Rev.6，第1～2页，2026-06](https://www.onsemi.com/pdf/datasheet/qrd1114-d.pdf)
