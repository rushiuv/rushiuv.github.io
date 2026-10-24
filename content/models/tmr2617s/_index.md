---
title: "TMR2617S"
wiki: true
wiki_type: "model"
catalog_type: "线性磁场"
catalog_form: "芯片"
wiki_rank: 145
seed_count: 1
lastmod: "2026-10-24"
description: "TMR2617S在此对应多维官网的TMR2617S-AAC线性磁场传感器。"
official_url: "https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html"
related_companies: ["多维科技"]
wiki_category: "线性磁场与位移映射"
document_version: "公开资料核对：2026-10-16；文件版本见下载件"
model_card: true
product_image: "/images/wiki/tmr2617s-official.jpg"
product_image_caption: "TMR2617S 原厂产品／封装图"
product_image_source: "https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 对应型号 | TMR2617S-AAC |
| 感应技术 | TMR 线性磁场检测 |
| 测量输出 | 磁场分量 |
| 推荐供电 | 1.71～5 V |
| 敏感方向 | Z轴 |
| 线性场范围 | ±1000 Gs（±100 mT） |
| 灵敏度 | 用户可编程；具体设定需原厂配置依据 |
| 静态电流 | 官网列<300 µA |
| 输出摆幅 | 5%～95% VCC；比例式输出 |
| 封装 | SOT23-3 |

参数来源：本页所列[原厂产品资料与手册](https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html)。

## 工作方式与型号定位

TMR2617S-AAC把TMR传感与运放、DAC等调理电路集成，提供与Z向磁场成比例的模拟电压。它用于磁轴键盘及位置检测时，行程仍需由磁体几何映射。

## 安装、接口与配置

1.71～5V供电和5%～95%VCC输出摆幅需要与ADC参考和可用输入范围匹配。灵敏度可编程，不能只看大线性场范围就假定任意磁体距离都可得到足够分辨率。

## 校准与选型验证

官网给出±1000Gs线性范围及低于300µA静态电流，但没有给出所有配置的完整噪声表。样机应检查零点、饱和、温度及按键全行程，保留电压曲线而不是直接把ADC码称作位移精度。

## 官方资料

- [TMR2617S 原厂资料入口](https://www.dowaytech.com/TMR2617S-AAC-TMR-Linear-Sensors.html)
