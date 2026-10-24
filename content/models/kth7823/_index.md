---
title: "KTH7823"
series_parent: "kth78"
wiki: true
wiki_type: "model"
catalog_type: "数字角度"
catalog_form: "芯片"
wiki_rank: 85
seed_count: 2
lastmod: "2026-10-24"
description: "KTH7823是KTH78系列中官网归入消费类应用的磁角度型号，使用霍尔检测与数字处理，支持对轴或离轴位置反馈。"
official_url: "https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html"
related_companies: ["昆泰芯"]
datasheet_url: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7823%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
datasheet_label: "官方数据手册"
wiki_category: "磁角度测量"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/kth7823-datasheet-figure.jpg"
product_image_caption: "KTH7823 手册中的 KTH78 系列磁体布置示意，非内部码道结构图"
product_image_source: "https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7823%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf"
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 等级/编码 | 消费类成员；N：16位，C：12位角度+4位CRC |
| QN16输出 | 官网：SSI、PWM、SPI、ABZ，按N/C具体版本 |
| SOP8输出 | 官网C-SOP8：PWM、SPI |
| 工作供电 | 手册3.3V模式3.0～3.6V；5V模式4.5～5.5V，分别使用 |
| 磁场条件 | 关键表30～150mT，典型60mT |
| 典型工作电流 | 11.6mA（3.3V）；5V表另核对 |
| 启动时间 | 典型1ms，关键表 |
| 数据更新/表列延时 | 1µs；匀速补偿与加减速响应不能混用 |
| INL | 手册关键表±0.35°，按安装和校准条件 |
| 温度漂移 | 手册关键表0.002°/°C，保留原测试口径 |
| 最高转速 | 手册关键表120000rpm，不能与任意滤波设置拼接 |
| 噪声 | 0.015°（1σ），手册关键表 |
| 温度 | 官网−40～105°C；具体订货等级按正式资料 |
| 封装 | QFN-16L或SOP8，按订货号 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7823%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 消费级不等于可以跳过安装条件

KTH7823用于旋钮、舵机、云台等位置反馈时，仍需按磁体与敏感点的几何关系设计。支持离轴与多极对是应用能力，不意味着任意磁环、任意气隙都保持同一个绝对精度。

## 单极对与多极对角度

多极对输入时，电周期与机械一圈不是同一个范围。控制器需要明确读数代表哪一层位置，以及整圈消歧和启动定位由哪一环节完成；不能把每个电周期的16位编码当成机械全圈唯一位置。

## 输出与温度等级

C版本的CRC占用数据位，SOP8减少可用输出。工业781x的温度上限与接口组合不能移到7823。选型表中的105°C应与具体订货号、封装和手册一起确认。

## 验证方法

在目标磁体和安装条件下保存整圈原始角度，并测试低速往返、最快运动和最大气隙。分辨率、静止噪声、非线性与重复性分别记录；置零和平均处理不能替代对周期安装误差的验证。

## 官方资料

- [KTH7823 原厂资料入口](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)
- [KTH7823 数据手册（官方 PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7823%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)
