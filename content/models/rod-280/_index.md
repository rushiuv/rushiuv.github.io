---
title: ROD 280系列
description: ROD 280以模拟增量信号给出角运动，具体位置还依赖下游细分与参考恢复。ROD 280C的距离编码原点缩短寻找参考的移动，不等于上电静止即获得绝对位置。
wiki: true
wiki_type: model
wiki_rank: 300
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 海德汉
wiki_category: 光学增量角度
catalog_vendor: 海德汉
catalog_type: 光学增量角度
catalog_form: 完整编码器
search_aliases:
- ROD 280 / ROD 280C
- rod 280
- ROD 280系列
official_url: https://www.heidenhain.de/fileadmin/pdf/ja/Produktinformation/PI_ROD_200_700_800_ID1385973_ja.pdf
document_version: 日文产品资料ID1385973，07/2022，表印刷页2–3
model_card: true
catalog_level: 系列
---

ROD 280系列是带轴承与外置联轴器的模拟增量角度编码器。两款主要区别在参考标记；ROD 280C仍需移动恢复参考位置。

## 型号与核心异同

| 具体型号 | 增量信号 | 参考标记 | 位置恢复方式 |
| --- | --- | --- | --- |
| ROD 280 | 18000线，约1Vpp正弦 | 一个原点 | 移动至参考标记 |
| ROD 280C | 18000线，约1Vpp正弦 | 距离编码参考标记 | 移动读取距离编码，非静止上电绝对 |

## 共同条件与参数依据

- **形态**：内置轴承、外置联轴器的增量角度编码器；非裸读头
- **系统精度**：±5角秒；一个信号周期内位置误差≤±0.7角秒
- **频率**：−3dB截止频率≥180kHz，不等价于任意精度目标下的最高机械转速
- **供电**：5V±0.5V，空载电流≤150mA
- **机械边界**：实心轴10mm，机械允许转速≤10000rpm；使用转速还受电气与处理链限制
- **环境**：固定电缆−20～70°C；反复弯折−10～70°C；IP64按安装条件

## 接入与验证

选型时分开机械转速上限、模拟频率响应和外部细分器限值。18000周期在600rpm下对应180kHz，这是频率换算；不能据截止频率直接给精度放行。联轴器传递误差也应纳入系统。参见[参考标记与绝对位置](/topics/guides/reference-recovery/)和[速率预算](/topics/guides/rate-budget/)。

## 官方资料

- [日文原厂产品资料07/2022](https://www.heidenhain.de/fileadmin/pdf/ja/Produktinformation/PI_ROD_200_700_800_ID1385973_ja.pdf)
- [原厂日文测量原理](https://product.heidenhain.de/JPBC/image/HWP.EN/hlr-system/1078628-J3.pdf)
