---
title: "MAQ800／820／850系列"
description: "带磁性按压检测的8位角度器件组，三款输出选择不同。"
wiki: true
wiki_type: "model"
wiki_rank: 224
seed_count: 0
lastmod: "2026-10-24"
related_companies: ["MPS"]
wiki_category: "数字角度"
catalog_vendor: "MPS"
catalog_type: "数字角度"
catalog_form: "芯片"
search_aliases: ["MAQ800","MAQ820","MAQ850"]
official_url: "https://www.monolithicpower.com/en/maq800.html"
document_version: "官方公开产品页或目录，核对：2026-10-18"
model_card: true
---

## 核心参数

| 参数 | 数值与适用条件 |
| --- | --- |
| 共同功能 | 8位角度与按压检测 |
| 成员区别 | MAQ820带ABZ；MAQ850带PWM |
| 车规 | 官方标注AEC-Q100；不等于整机安全认证 |
| 比较方法 | 按所需输出选型号，不把三款接口合成单款能力 |

参数来源：本页所列[原厂产品资料与手册](https://www.monolithicpower.com/en/maq800.html)。

## 工作方式与型号定位

MAQ800、MAQ820与MAQ850面向磁性旋钮及按压检测。8位角度一圈256个位置码，按压功能观察磁体轴向运动造成的场强变化，与旋转角度是两个输出用途。

## 安装、接口与配置

MAQ820增加ABZ，MAQ850提供PWM，选择时按主控需要确定成员。三款功能不能相加后写成每颗都具备；同一系列的封装与可用引脚也需分别核对。

## 校准与选型验证

旋转时磁体气隙变化会影响按压阈值，按下时也会改变角度噪声。应组合测试旋转、按压与倾斜，核对误触发、阈值回差和温度影响；器件车规资格不能代替整机交互与安全验收。

## 官方资料

- [MAQ800／820／850系列 官方资料](https://www.monolithicpower.com/en/maq800.html)
- [官方补充资料1](https://www.monolithicpower.com/en/maq820.html)
- [官方补充资料2](https://www.monolithicpower.com/en/maq850.html)
