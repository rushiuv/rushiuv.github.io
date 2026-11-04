---
title: MT6813QT
wiki: true
wiki_type: model
model_card: true
wiki_rank: 404
lastmod: '2026-10-30'
catalog_type: 数字角度
catalog_form: 芯片
wiki_category: 数字角度
description: MT6813QT 是MT6813 AMR角度系列的QFN16型号，以数字绝对角度和PWM路径为主；封装变化不等于额外获得目录未列的ABZ或UVW。
official_url: https://www.novosns.com/product/MT6813QT-LAD
related_companies:
- 纳芯微
- 麦歌恩
search_aliases:
- MT6813
- MT6813QT
- MT6813QT-LAD
- MT6813QT-PAD
document_version: 官网目录与完整订货号，核对：2026-10-30；PDF版本见原件
datasheet_url: https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf
datasheet_label: 原厂数据手册
product_image: /images/wiki/novosns/36ddf827b24fee09.png
product_image_caption: 原厂系列产品／封装图；本型号封装以完整订货行核对
product_image_source: https://wwwapi.novosns.com/dms/userfiles/docs/RFHEbF85Io209CxN8y7ciOPKnSf.png
---

## 核心参数与配置

以下为官网目录中 **MT6813QT-LAD** 这一配置的标注。最大值、典型值及测试条件以对应手册为准；不同订货号的差异列在后文。

| 项目 | 数值、配置与条件 |
| --- | --- |
| 产品定位 | AMR磁角度编码器 |
| 目录类别 | 工业编码器 |
| 封装 | QFN16 |
| 目录等级 | Industrial |
| 数字接口 | I²C/3wire SPI/4-wireSPI；官网目录标注，适用于上述订货配置 |
| 核心分辨率 | 14bit；官网目录标注，适用于上述订货配置 |
| PWM输出 | 9~12bit；官网目录标注，适用于上述订货配置 |
| 目录最高转速 | <6000RPM；官网目录标注，适用于上述订货配置 |
| 匀速传播延迟 | 100μs~400μs；官网目录标注，适用于上述订货配置 |
| 温度范围 | -40~125；官网目录标注，适用于上述订货配置 |
| 目录供电 | 3.3~5.0；官网目录标注，适用于上述订货配置 |

## QT封装要重新核对物理连接

与SOP8的CT成员相比，本型号使用QFN16。应以QT引脚图、暴露焊盘和推荐布局安排电源与信号，不能仅凭共享系列图识别封装。

## 角度读取与位置控制的边界

I²C/SPI读取给出离散时间点的角度，PWM则需要额外捕获周期。选型时把控制器采样周期、目录延时及协议时间一起考虑，避免把14bit码宽误当成高速跟踪能力。

## 预设配置差异

官网目录中的不同QT完整OPN共享参数字段，但其预设差异尚未由完整寄存器文档确认。采购和固件记录保留整个订货号，不能只保存MT6813。

## 完整订货号与资料

| 完整订货号 | 封装、等级、状态及对应手册 |
| --- | --- |
| [MT6813QT-LAD](https://www.novosns.com/product/MT6813QT-LAD) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf) |
| [MT6813QT-PAD](https://www.novosns.com/product/MT6813QT-PAD) | QFN16；Industrial；Active；[英文／原版手册](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf) |

## 版本与适用条件

完整订货号区分预设配置与供货形式；CT、QT、GT、SGT、SJT等型号字母还对应不同成员或封装。

这些OPN的目录参数相同，寄存器预设、包装和其他功能仍应按完整订货号确认。

## 原厂资料

- [产品详情](https://www.novosns.com/product/MT6813QT-LAD)
- [DatasheetEN)MT6813_Rev.3.1.pdf](https://wwwapi.novosns.com/dms/userfiles/docs/Xmfvb3avzoZOiixA6OtcMz8RnEe.pdf)
- [工业编码器目录](https://www.novosns.com/industrial-encoder)
