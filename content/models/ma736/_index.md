---
title: "MA736"
description: "小型低延时数字磁角度芯片，供对封装和响应时间敏感的设计比较。"
wiki: true
wiki_type: "model"
wiki_rank: 219
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MA736"]
official_url: "https://www.monolithicpower.com/en/ma736.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 分辨率 | 8～12.5位，依配置 |
| 时延 | 官网产品定位3µs低延时 |
| 形式 | 小型数字磁角度IC，不含磁体和机械轴承 |
| 验证 | 同一滤波配置下核对时延和角度抖动 |
| 推荐供电 | 3.0～3.6 V；3.3 V标称 |
| 工作温度 | −40～125°C |
| 供电电流 | 官网列11 mA |
| 磁场下限 | 30 mT |
| 滤波截止频率 | 官网列95、380、95,000 Hz；按配置选择 |
| 最高转速 | 60,000 rpm |
| 封装 | UTQFN-14，2 × 2 mm |
| 附加功能 | 可配置磁场阈值、角度变化中断、NVM配置保存 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/ma736.html)。

## 工作方式与型号定位

MA736提供小封装SPI角度输出，重点是3µs匀速延迟与8～12.5位配置范围。它和MA735都采用2×2mm封装，但输出功能不同，不能因尺寸相同就视为通用替换。

## 安装、接口与配置

滤波配置改变角度噪声和响应。产品页列95、380和95000Hz截止频率，实际使用需明确所选档位，不把最低噪声与最高带宽合成一个性能点。

## 校准与选型验证

磁场强度阈值及角度变化中断可参与诊断。验证时保存相同档位下的静止数据、匀速误差及加减速响应；SPI数据正确还不能证明磁体的偏心、倾斜和气隙已满足整机要求。

## 官方资料

- [MA736 官方资料](https://www.monolithicpower.com/en/ma736.html)
