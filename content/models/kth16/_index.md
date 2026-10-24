---
title: "KTH16系列"
description: "包含双输出单极开关与高速锁存器；型号相近，检测逻辑和功耗并不相同。"
wiki: true
wiki_type: "model"
wiki_rank: 202
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["昆泰芯"]
wiki_category: "磁开关"
catalog_vendor: "昆泰芯"
catalog_type: "磁开关"
catalog_form: "芯片"
search_aliases: ["KTH1604","KTH1631"]
official_url: "https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值、配置与条件 |
| --- | --- |
| 系列成员 | KTH1604双输出单极开关；KTH1631双极锁存器 |
| KTH1604供电 | 1.6～5.5V |
| KTH1604采样/电流 | 20Hz：3.3µA；5Hz：1.6µA，均为官网1.8V条件 |
| KTH1604阈值档 | 动作/释放场绝对值46/34、33/23、22/16Gs，按完整型号 |
| KTH1631供电 | 1.8～5.5V |
| KTH1631响应/电流 | 40kHz；2.25mA（1.8V），官网目录口径 |
| 输出 | CMOS；两个成员的状态逻辑不同 |
| 温度 | −40～85°C，官网目录 |
| 封装 | 1604：DFN/FBP 1×1mm-4L；1631：SOT-23-3L、TO-92S |

参数依据：[原厂产品与型号选型表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html)。

## 为什么不能只按16系列选型

KTH1604使用两路单极输出区分磁极作用，KTH1631则以相反磁极切换锁存状态。一个适合磁体靠近和离开事件，另一个适合转子磁极交替通过。两者既不是同一输出逻辑，也不是同一功耗等级。

## 采样速度怎样影响机械动作

1604的5Hz、20Hz版本分别对应约200ms和50ms采样间隔。这是按目录频率计算的周期，不是手册保证的最坏动作延迟。磁体快速掠过时，应先核对它在有效检测区内停留多久，再选择采样版本。

## 磁体与主控接入

磁阈值以芯片敏感点的场强表示，不直接给出安装距离。磁体尺寸、充磁方向、气隙和周围导磁材料会改变触发位置。主控还应确认两路状态的真值关系，并针对上电、慢速接近和临界位置往返检查输出。

## 验收重点

记录完整后缀和封装方向，分别测试动作点、释放点和电源变化。锁存器应使用正负磁场完成一个完整切换循环；单极检测则检查磁体移走后的释放。不能只测一次靠近，就判定两个成员可以互换。

## 官方资料

- [KTH16系列 官方资料](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html)
