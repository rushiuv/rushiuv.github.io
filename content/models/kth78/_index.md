---
title: KTH78系列
linkTitle: KTH78
catalog_vendor: 昆泰芯
catalog_type: 数字角度
catalog_form: 芯片
search_aliases:
- KTH7801
- KTH7803
- KTH7812
- KTH7813
- KTH7814
- KTH7815
- KTH7816
- KTH7823
description: KTH78 是 KTH78xx 霍尔角度编码器系列简称，覆盖 KTH7801、KTH7812、KTH7813、KTH7814、KTH7815、KTH7816、KTH7823
  等成员。下列具体数值仅标注其对应型号。
wiki: true
wiki_type: model
wiki_rank: 9
seed_count: 16
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
official_url: https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html
datasheet_url: https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
datasheet_label: KTH7812 数据手册（系列代表型号）
document_version: KTH7812 官方公开手册，32 个 PDF 页面；其他成员以系列页同名手册为准
model_card: true
product_image: /images/wiki/kth78-diagram.webp
product_image_caption: 图片来源：KTH7812 官方数据手册，第 5 个 PDF 页面，功能框图局部。本图仅代表 KTH7812。
product_image_source: https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf
catalog_level: 系列
---

KTH78是霍尔角度传感器系列，成员的温度等级、码宽和接口组合不同。先按应用等级与所需输出筛选，再到具体型号页核对供电、噪声与响应条件。

## 型号与核心异同

| 具体型号 | 位置码／输出格式 | 接口 | 温度条件 |
| --- | --- | --- | --- |
| [KTH7801](/models/kth7801/) | N：16位；C：12位角度+4位CRC，按后缀 | 官网QN16：SSI/PWM/SPI/ABZ；SOP8：PWM/SPI | 官网新表−40～150°C；官网另一表−40～125°C，须按完整订货号确认 |
| [KTH7803](/models/kth7803/) | 16位，官网N-QN16版本 | SSI、PWM、SPI、ABZ，官网对应完整型号行 | 官网新表−40～150°C |
| [KTH7812](/models/kth7812/) | 16位绝对角度 | 四线SPI、ABZ、UVW，依配置 | −40～125°C |
| [KTH7813](/models/kth7813/) | 16位绝对角度 | SPI、ABZ、UVW，官网QN16对应行 | 官网−40～125°C；QFN-16L |
| [KTH7814](/models/kth7814/) | 官网C-QN16：12位角度+4位CRC；16位帧不等于16位位置 | SPI、ABZ与反相ABZ，官网对应行 | −40～125°C；QFN-16L |
| [KTH7815](/models/kth7815/) | 16位，按实际后缀/帧格式确认 | QN16和SOP8对应行均列PWM、SPI；SPI、ABZ及反相ABZ；与官网新表存在冲突；PWM、SPI；不能沿用QN16增量输出 | −40～125°C；QFN-16L、SOP8，按订货号 |
| [KTH7816](/models/kth7816/) | N：16位；C：12位角度+4位CRC，按封装后缀 | 官网N-QN16：SSI、PWM、SPI、ABZ；PWM、SPI；N/C版本数据格式不同 | −40～125°C |
| [KTH7823](/models/kth7823/) | 消费类成员；N：16位，C：12位角度+4位CRC | 官网：SSI、PWM、SPI、ABZ，按N/C具体版本；官网C-SOP8：PWM、SPI | 官网−40～105°C；具体订货等级按正式资料 |

上表沿用各成员资料的适用口径；官网新旧表与部分手册存在差异，不将某一版本的结论推广为全系列保证。

## KTH7812的参数条件

- **供电**：3.3V模式3.0～3.6V；5V模式按对应电气表
- **噪声/INL**：0.015°（1σ）；±0.35°，具体条件见其手册
- ** ABZ/UVW**：4～4096步/圈；1～8对极
- **电流/启动**：11.6mA（3.3V）典型；1ms典型
- **磁场**：30～150mT，典型60mT
- **数据更新**：1µs，不等于所有运动下测量链路无延时

## 码宽、封装与信号链一起确认

N与C版本涉及数据表达：12位角度加4位CRC虽然占16位帧，位置内容仍是12位。SPI、SSI、ABZ和PWM也应分别核对码宽与更新方式。

QN16与SOP8的可用引脚不同，不能把大封装的全部输出移植到小封装。MTP保存方向、零点与滤波等配置；换成员后应核对默认值和已写入参数，实转一圈验证绝对角度与增量计数的关系。

多个输出共享上游磁体和角度处理，同时读取SPI与ABZ不构成两套独立测量。诊断状态、实际刷新率与动态误差仍须在对应模式下测试。


## 官方资料

明确型号、配置与版本后使用对应文件。


- [官方产品入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [KTH7812 数据手册（系列代表型号）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7812%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
