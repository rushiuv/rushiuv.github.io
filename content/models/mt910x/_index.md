---
title: MT910x系列
description: 模拟比例输出线性霍尔系列，适用于磁场检测及磁路辅助的位移测量。
wiki: true
wiki_type: model
wiki_rank: 244
seed_count: 0
lastmod: '2026-10-30'
related_companies:
- 麦歌恩
- 纳芯微
wiki_category: 线性磁场
catalog_vendor: 麦歌恩
catalog_type: 线性磁场
catalog_form: 芯片
search_aliases:
- MT9101
- MT9102
- MT9103
- MT9105
- MT910x系列
official_url: https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf
document_version: 官方公开PDF，核对：2026-10-18；版本见下文
model_card: true
datasheet_url: https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf
datasheet_label: 官方公开PDF
catalog_level: 系列
---

MT910x是比例式线性霍尔系列。成员以灵敏度区分，灵敏度越高时仍需同时检查可用磁场范围和输出摆幅。

## 型号与核心异同

| 具体型号 | 典型灵敏度（5V、25°C） | 输出 |
| --- | --- | --- |
| MT9101 | 1.5mV/Gs | 比例式模拟电压 |
| MT9102 | 2.5mV/Gs | 比例式模拟电压 |
| MT9103 | 3.4mV/Gs | 比例式模拟电压 |
| MT9105 | 5.0mV/Gs | 比例式模拟电压 |

## 共同条件与参数依据

- **输出**：随供电比例变化的模拟电压，零场输出约VCC/2
- **供电条件**：手册磁特性表3.0～5.5V；灵敏度与场强范围须按供电一起核对

## 接入电路与配置

5V、25°C下的1.5/2.5/3.4/5.0mV/Gs不能离开供电条件比较。相同磁场下灵敏度越高，输出变化越大，但可用线性场强范围及输出摆幅也需要同时满足。

## 标定与应用验证

与ADC连接时应统一比例式电源参考，检查零场电压、负载和滤波。验收应覆盖磁体全行程与温度，保留电压曲线并识别饱和区；换成员后不能只改软件比例系数而不复测磁路。

## 官方资料

- [MT910x系列 官方资料](https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf)
