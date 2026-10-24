---
title: "MT910x系列"
description: "模拟比例输出线性霍尔系列，适用于磁场检测及磁路辅助的位移测量。"
wiki: true
wiki_type: "model"
wiki_rank: 244
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["麦歌恩","纳芯微"]
wiki_category: "线性磁场"
catalog_vendor: "麦歌恩"
catalog_type: "线性磁场"
catalog_form: "芯片"
search_aliases: ["MT9101","MT9102","MT9103","MT9105"]
official_url: "https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf"
document_version: "官方公开PDF，核对：2026-10-18；版本见下文"
model_card: true
datasheet_url: "https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf"
datasheet_label: "官方公开PDF"
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 成员 | MT9101／9102／9103／9105 |
| 输出 | 随供电比例变化的模拟电压，零场输出约VCC/2 |
| 灵敏度 | 5V、25°C典型值依次1.5／2.5／3.4／5.0mV/Gs |
| 供电条件 | 手册磁特性表3.0～5.5V；灵敏度与场强范围须按供电一起核对 |

参数来源：本页所列[原厂产品资料与手册](https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf)。

## 工作方式与型号定位

MT9101、9102、9103与9105均输出随磁场变化的比例电压，主要差别之一是灵敏度。它们没有直接输出毫米位移或数字角度，机械量需要磁路映射。

## 安装、接口与配置

5V、25°C下的1.5/2.5/3.4/5.0mV/Gs不能离开供电条件比较。相同磁场下灵敏度越高，输出变化越大，但可用线性场强范围及输出摆幅也需要同时满足。

## 校准与选型验证

与ADC连接时应统一比例式电源参考，检查零场电压、负载和滤波。验收应覆盖磁体全行程与温度，保留电压曲线并识别饱和区；换成员后不能只改软件比例系数而不复测磁路。

## 官方资料

- [MT910x系列 官方资料](https://www.magntek.com.cn/upload/pdf/202404/%E7%A3%81%E6%80%A7%E7%94%B5%E6%B5%81-%E7%BA%BF%E6%80%A7%E9%9C%8D%E5%B0%94%E8%8A%AF%E7%89%87MT9102%E4%BA%A7%E5%93%81%E8%A7%84%E6%A0%BC%E4%B9%A6.pdf)
