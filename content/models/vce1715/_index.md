---
title: VCE1715
description: VCE1715 是双AMR惠斯通电桥角度传感器，输出模拟正余弦信息，基本角度范围180°；ADC、校准、反正切与半圈判别由系统另行承担。
wiki: true
wiki_type: model
wiki_rank: 237
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 圣邦微
wiki_category: 模拟角度
catalog_vendor: 圣邦微
catalog_type: 模拟角度
catalog_form: 芯片
search_aliases:
- VCE1715
- VCE1715S
official_url: https://www.sg-micro.com/cn/product/VCE1715
document_version: 2025-08 Rev.A，12页
model_card: true
datasheet_url: https://www.sg-micro.com/rect/assets/eb1206f7-9540-4af3-afdc-946624082e12/VCE1715.pdf
datasheet_label: 原厂数据手册（PDF）
product_image: /images/wiki/sgmicro/3c9d045f0e4c07d8.png
product_image_caption: VCE1715 官方页使用的原厂产品页共用SOIC-8封装示意；不是唯一可选封装
product_image_source: https://www.sg-micro.com/api/assets/7c267236-6f8a-43e4-82e1-128cee30031b
---

## 核心参数

依据[原厂手册](https://www.sg-micro.com/rect/assets/eb1206f7-9540-4af3-afdc-946624082e12/VCE1715.pdf)（2025-08 Rev.A，12页）。典型值、最大值与适用条件分别保留。

| 参数 | 数值与适用条件 |
| --- | --- |
| 感知与输出 | 双饱和模式AMR惠斯通电桥，模拟差分正余弦；非数字绝对角度编码器；180°角度范围（手册第1、6页） |
| 工作电源／温度 | 1～9 V；−40～125°C；推荐工作条件，不采用其他传感器3.3/5V窗口替代（手册第2、4页） |
| 饱和场 | 最低80 Gs（8 mT）；TA=−40～125°C；低于饱和场不能套用饱和模式方向不敏感结论（手册第4、6页） |
| 角度分辨率 | 典型0.01°；带宽10 Hz、VDD=5V；首页<0.01°不能去掉带宽条件（手册第4页） |
| 灵敏度 | 典型2.1 mV/°；VDD=5V、磁场80G、过零点条件（手册第4页） |
| 桥输出幅度 | 95～140 mVpp，典型120 mVpp；VDD=5V、磁场80G；按峰峰值进入前端预算（手册第4页） |
| 桥阻与零偏 | 桥阻800～1300Ω，典型1050Ω；桥偏移−3～+3mV/V；桥阻为每桥1mA测试，偏移为80G条件（手册第4页） |
| 噪声密度 | 典型6 nV/√Hz；1Hz、VDD=5V；不是全带宽输出噪声（手册第4页） |
| 封装／订货 | SOIC-8；VCE1715S；两桥供电/地及差分输出按引脚定义连接（手册第2、3页） |

## 180°桥输出怎样变成完整位置

AMR电桥的角度响应具有半圈周期。使用正余弦和反正切可得到该周期内的角度，若机构需要360°上电绝对位置，还必须提供可靠的半圈判别信息，不能仅给反正切结果换一个编码位数。

## 模拟前端需要跟磁体一起设计

先让全运动范围内的平面磁场高于饱和场，再核对桥输出共模、偏移、幅度及ADC输入窗口。正余弦通道的增益差、零点和采样时刻会产生角度误差，因此应保存两桥原始波形，分别校准偏置、增益和相位。

## 低带宽分辨率不能直接用于高速伺服

0.01°分辨率对应5V、10Hz带宽的手册条件。扩大带宽以跟踪高速运动时，需要重新核算积分噪声和相位延迟；桥输出器件没有省掉ADC和运算，这些部分同样属于反馈链预算。

## 资料版本与边界

- 官网“精度最高/不受气隙影响”等比较性宣传不作为无条件保证。
- 页首页称角度准确度可达0.1°，本次表格未给对应最大保证条件，未把该数字当全温最坏准确度。

## 官方资料

- [VCE1715产品页](https://www.sg-micro.com/cn/product/VCE1715)
- [VCE1715数据手册（2025-08 Rev.A，12页）](https://www.sg-micro.com/rect/assets/eb1206f7-9540-4af3-afdc-946624082e12/VCE1715.pdf)
