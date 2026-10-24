---
title: "KTH7814"
description: "KTH7814是KTH78霍尔角度系列成员；接口和编码格式按具体封装及后缀区分。"
wiki: true
wiki_type: "model"
wiki_rank: 212
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "数字角度"
catalog_vendor: "昆泰芯"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["KTH7814"]
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
series_parent: "kth78"
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7814%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "KTH7814 官方产品手册"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 有效编码 | 官网C-QN16：12位角度+4位CRC；16位帧不等于16位位置 |
| 输出 | SPI、ABZ与反相ABZ，官网对应行 |
| 工作供电 | 下载PDF5V关键表4.5～5.5V；其他模式按对应表 |
| 典型电流 | 13.6mA（5V），PDF关键表 |
| 磁场条件 | 30～150mT，典型60mT，PDF |
| 噪声 | 0.015°（1σ），PDF及官网对应行 |
| 启动/延时 | 典型1ms；表列1µs |
| INL/温漂 | PDF关键表±0.35°；0.002°/°C |
| 最高转速 | 120000rpm，按手册条件 |
| 温度/封装 | −40～125°C；QFN-16L |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7814%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## CRC占位会改变有效角度字

官网KTH7814-X-C-QN16对应12位角度加4位CRC。接收端必须先按协议分离角度和校验，不应把完整16位帧按65536刻度换算。CRC用于检测部分传输错误，无法检测全部机械角度误差。

## 反相信号与差分链路

ABZ和反相ABZ提供互补电气信号，但引脚输出不能不经核对就当成任意工业差分线驱动器。长线接入还要确认电平、驱动能力、终端与接收器。

## 校验正确不表示安装正确

磁体偏心、倾斜或气隙变化会产生有效但偏离真实位置的角度码，CRC依然能够正确。安装验收需要外部角度参考，并与通信错误统计分别记录。

## 替换条件

7814与7812的区别涉及输出组合和数据帧，不能只改软件型号名。核对引脚、C后缀、计数倍率和零点，再在相同滤波下测整圈误差、动态响应和温度变化。

## 官方资料

- [KTH7814 官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

- [KTH7814 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7814%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
