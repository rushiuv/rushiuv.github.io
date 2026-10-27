---
{
  "title": "半导体磁阻：齿轮检测为何还要一块偏置磁铁",
  "description": "区分SMR与AMR/GMR/TMR，解释偏置磁路、齿距与A/B相位信号的关系。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 310,
  "related_basics": [
    "amr",
    "gmr",
    "air-gap",
    "abz"
  ],
  "related_applications": [
    "gearbox",
    "servo-motor"
  ]
}
---
半导体磁阻（SMR，产品资料也写SMRE）利用半导体在磁场中的电阻变化；它不等同于铁磁薄膜的[AMR](/wiki/basics/amr/)，也没有[GMR](/wiki/basics/gmr/)旋阀那样的同一层叠结构。选型先认清全称，再看测量磁路，不能只按“MR”三个字母换料。

## 齿轮改变的是已有磁路

一类SMR检测方案在传感器附近设置偏置磁铁。铁磁性齿轮旋转，齿顶与齿槽改变局部磁场分布，磁阻网络因此产生随齿位置变化的信号。磁铁、传感面与齿轮相互配合；普通金属齿轮并不是每个齿都天然带有N/S磁极。

AKM公开的SMRE产品采用InSb材料，并提供齿轮检测系列；部分封装自带偏置磁铁支架，部分小封装需要外部安排磁路。[AKM SMRE产品与结构](https://www.akm.com/global/en/products/semiconductor-magnetoresistive-element/) 这里的结构说明不保证任意钢齿轮、任意气隙都能正常工作。

## A/B波形不等于已经输出绝对角度

合理配置的多个敏感位置可形成具有空间相位差的通道，用于方向和细分。具体输出可能是模拟差分量，不能直接套用数字[ABZ](/wiki/basics/abz/)的电平规则。AKM的MS0031采用A+/A−、B+/B−差分输出；电子内插能力与整机绝对精度是不同指标。[AKM MS0031说明](https://www.akm.com/global/en/products/semiconductor-magnetoresistive-element/)

自设60齿、每齿一个信号周期，周期内均匀细分1024份，则名义机械刻度为 \(360/(60\times1024)=0.00586^\circ\)。这只是刻度计算：齿距误差、偏心、桥路非线性及错计周期仍可大于一个刻度；无参考标记时也不能知道上电后是哪一个齿。

## 安装验收要覆盖齿顶与齿槽的最差组合

先核对型号规定的齿距或模数、敏感方向与磁铁位置，再扫[气隙](/wiki/basics/air-gap/)、偏心及温度；同时保存通道幅度、直流中点、相位和漏计数。对[齿轮箱](/applications/gearbox/)，转速变低时应区分SMR静态信号与被动线圈速度幅度特性，相关差异见[感应线圈](/wiki/basics/inductive-magnetic-sensing/)。
