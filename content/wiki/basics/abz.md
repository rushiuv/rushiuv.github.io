---
{
  "title": "ABZ：正交计数、四倍频与零位索引",
  "description": "通过四个状态解释方向与四倍计数，并用1000 PPR算清计数频率。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "接口与应用",
  "weight": 11,
  "related_basics": [
    "absolute-incremental",
    "interfaces",
    "singleturn-multiturn"
  ],
  "related_topics": [
    "编码器接口"
  ],
  "related_model_slugs": [
    "mt6835"
  ],
  "related_guides": [
    "rate-budget",
    "sample-time-contract"
  ],
  "related_applications": [
    "closed-loop-stepper"
  ]
}
---


AB两路数字信号通常相差四分之一周期。控制器观察哪一路先变化，判断运动方向；累计有效边沿，得到位移。Z是参考索引，常用于建立或核对位置基准。

## 方向来自状态顺序

下面把状态写成“A、B”的二进制组合。规定一种方向为：

| 边沿步骤 | 0 | 1 | 2 | 3 | 回到0 |
|---|---|---|---|---|---|
| AB状态 | 00 | 10 | 11 | 01 | 00 |
| 累计变化 | 0 | +1 | +2 | +3 | +4 |

反向运动走相反顺序。正方向取决于接线和软件约定，不能只写“A超前”而不说明相位定义。正常相邻状态一次只变一位；直接从00跳到11，说明采样漏状态或有异常，不能可靠判定方向。

## 四倍频没有产生四倍物理刻线

若手册明确PPR表示A路每机械圈的完整周期数，x4计数把A/B的上升沿、下降沿都计入，每圈计数为4×PPR。1000 PPR便得到4000计数/圈，计数步距为0.09°。

PPR与CPR的缩写在不同厂家资料中用法不统一，必须回到定义和时序图；看到“4000 CPR”不能不加判断再乘四。

## 转速决定控制器要接收多少边沿

1000 PPR在6000 rpm时，A路频率为100 kHz，x4合计计数速率为400 kcount/s。这是理想均匀边沿计算；实际接收能力还要留出最小边沿间隔、线缆和信号偏斜所需的余量。

Z常见为每机械圈一次，但也存在可配置周期、门控和相位。必须确认宽度、与AB的关系以及控制器在哪个事件锁存。Z不能记录掉电期间转过了多少整圈。

[TI eQEP接口文档](https://software-dl.ti.com/C2000/docs/C2000_driverlib_api_guide/f2838x/build/html/modules/eqep.html)；[雷尼绍数字正交信号FAQ](https://www.renishaw.com/en/optical-encoders-frequently-asked-questions--34674)。表中的方向与数字为本文定义和计算示例。

## 应答频率与机械转速同时验算

[欧姆龙日文选型表](https://www.fa.omron.co.jp/product/selection/34/func_spec.html)将分辨率、最高应答频率和允许最高转速分列；其中任一项合格都不能替代其余项。合成设1000周期/圈、应答上限100kHz，电信号容量对应6000rpm；x4接收端此时需处理400000边沿/秒。应先用慢速整圈核对计数，再提高速度查是否欠计。[速率预算](/topics/guides/rate-budget/)区分三种频率；[闭环步进](/applications/closed-loop-stepper/)还须把计数方向与控制坐标一致。

若达到机械允许转速前便开始丢边沿，继续提高输出分辨率会使容量缺口更大。
