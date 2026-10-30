---
title: KTH16系列
description: 包含双输出单极开关与高速锁存器；型号相近，检测逻辑和功耗并不相同。
wiki: true
wiki_type: model
wiki_rank: 202
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 昆泰芯
wiki_category: 磁开关
catalog_vendor: 昆泰芯
catalog_type: 磁开关
catalog_form: 芯片
search_aliases:
- KTH1604
- KTH1631
- KTH16系列
official_url: https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html
document_version: 官方公开产品页或目录，核对：2026-10-18
model_card: true
catalog_level: 系列
---

KTH16目录中的KTH1604与KTH1631具有不同状态逻辑和功耗等级。先判断磁体是靠近离开，还是正负磁极交替，再选采样和封装。

## 型号与核心异同

| 具体型号 | 逻辑／输出 | 供电 | 响应／电流（1.8V目录条件） | 封装 |
| --- | --- | --- | --- | --- |
| KTH1604 | 双输出单极；CMOS | 1.6～5.5V | 20Hz：3.3µA；5Hz：1.6µA | DFN/FBP 1×1mm-4L |
| KTH1631 | 双极锁存；CMOS | 1.8～5.5V | 40kHz；2.25mA | SOT-23-3L、TO-92S |

## 共同条件与参数依据

- **KTH1604阈值档**：动作/释放场绝对值46/34、33/23、22/16Gs，按完整型号
- **温度**：−40～85°C，官网目录

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
