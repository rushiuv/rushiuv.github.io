---
title: KTH7801
description: KTH7801 是 Hall 绝对角度编码器，来源列出数字、增量与 PWM 等接口，可用于电机位置和旋转机构反馈；具体接口组合与车规等级需要按订货资料核对。
wiki: true
wiki_type: model
wiki_rank: 209
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 数字角度
catalog_vendor: 昆泰芯
catalog_type: 数字角度
catalog_form: 芯片
search_aliases:
- KTH7801
official_url: https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html
document_version: 版本以链接文件名及原件为准；公开链接核对：2026-10-30
model_card: true
series_parent: kth78
datasheet_url: https://chat.connteck.com/downloads/KTH7801/KTH7801_Datasheet_CN.pdf
datasheet_label: 数据手册原链接
catalog_source: https://chat.connteck.com/products/angle/KTH7801/
product_image: /images/catalog/kth7801-original-figure.png
product_image_caption: KTH7801 SOP-8引脚与磁感中心（原手册第7页）
product_image_source: https://conntek.github.io/files/KTH7801%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf#page=7
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 编码 | N：16位；C：12位角度+4位CRC，按后缀 |
| 输出配置 | 官网QN16：SSI/PWM/SPI/ABZ；SOP8：PWM/SPI |
| 工作供电 | 手册3.3V模式3.0～3.6V；5V模式4.5～5.5V，分别使用 |
| 磁场条件 | 关键表30～150mT，典型60mT |
| 典型工作电流 | 11.6mA（3.3V）；5V表另核对 |
| 启动时间 | 典型1ms，关键表 |
| 数据更新/表列延时 | 1µs；匀速补偿与加减速响应不能混用 |
| INL | 手册关键表±0.35°，按安装和校准条件 |
| 温度漂移 | 手册关键表0.002°/°C，保留原测试口径 |
| 最高转速 | 手册关键表120000rpm，不能与任意滤波设置拼接 |
| 噪声 | 手册及官网对应行0.015°（1σ） |
| 工作温度 | 官网新表−40～150°C；官网另一表−40～125°C，须按完整订货号确认 |
| 封装 | QFN-16L或SOP-8，接口受引脚约束 |

参数依据：[原厂数据手册及型号选型表](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7801%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)。

## 车规成员如何选版本

KTH7801的完整料号包含电源兼容项、角度/CRC格式及封装。需要16位纯角度还是带CRC的数据帧，应从控制器需求出发选择，不能在软件里把CRC低位当作角度继续运算。

## 高温能力的资料冲突

官网新选型表将7801列为−40～150°C，另一张旧表列到125°C。页面保留两种口径，不把其中较高上限自动当成所有7801订货号的保证。量产前应取得适用手册与等级确认。

## 安装与校准

在轴与离轴都需要规定磁场条件。线性幅值调整修正信号链的一部分，不能将任意磁体偏心或磁化不均自动消除。比较整圈误差时应保持相同磁体、气隙、滤波和校准状态。

## 控制接口验收

QN16与SOP8的输出组合不同，替换时先核对引脚。绝对值读数用于位置初始化，ABZ用于增量计数；最高转速还受接收端边沿频率和滤波配置限制，不能单凭120000rpm标注决定可用系统速度。

## 官方资料

- [KTH7801 官方资料](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)

- [KTH7801 官方产品手册（PDF）](https://www.conntek.com.cn/api/resource/freeDownload?name=KTH7801%20%E4%BA%A7%E5%93%81%E6%89%8B%E5%86%8C.pdf)

## 选型补充

### 电机反馈先区分机械角和电角

传感器输出机械角，换向所需电角还取决于电机极对数、安装方向和电角零点。设置完角度方向与零点后，应在目标转速下比较位置与控制采样的时间关系，避免静态正确而高速换向偏移。

### 多接口需要逐项核对引脚

SPI/SSI 读取、ABZ 计数和 PWM 采样使用不同主控资源。应根据完整封装的复用关系选择可用组合，同时检查未用输入的处理要求，不从“多接口”描述推断任意信号都能同时启用。

### 车规与功能安全资料各自核验

AEC-Q100 是器件可靠性资格口径，故障诊断则需要具体状态位和测试条件。汽车系统仍需核对完整订货型号、资格文件及失效响应，不能把网站的功能安全措辞直接写成整机安全等级保证。


## 公开资料与型号核对

来源首屏和介绍列UVW，所示16脚表未出现UVW；另列SOP8但未给对应完整引脚表，输出组合待手册确认。

源页AEC-Q100 Grade 0与−40～150°C的并列口径需核对实际资格文件，不将网站标签作为等级证明。

按完整型号、等级和版本选择手册。公开链接核对日期：2026-10-30。

- [KTH7801_Datasheet_CN.pdf](https://chat.connteck.com/downloads/KTH7801/KTH7801_Datasheet_CN.pdf)

[来源产品页](https://chat.connteck.com/products/angle/KTH7801/) · [昆泰芯型号目录](/wiki/?vendor=昆泰芯)
