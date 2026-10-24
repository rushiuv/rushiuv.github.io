---
{
  "title": "磁编码器：霍尔、AMR与TMR怎样读角度",
  "description": "从磁场分量和磁阻方向响应出发，区分传感原理、周期与单圈绝对信息。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "检测原理与安装",
  "weight": 7,
  "related_basics": [
    "mounting",
    "absolute-incremental",
    "optical-encoder"
  ],
  "related_topics": [
    "磁编码器",
    "AMR",
    "TMR"
  ],
  "related_model_slugs": [
    "mlx90382",
    "tle5012b"
  ],
  "related_applications": [
    "brushless-dc-motor",
    "robot-joint"
  ],
  "related_guides": [
    "magnetic-field-coordinates",
    "amplitude-temperature-error"
  ]
}
---


磁编码器读取的是磁场提供的位置特征。一个常见轴端方案把径向充磁的双极磁体固定在轴上，读头留在定子侧。轴转动时，传感器位置处的磁场方向随之变化。

<figure class="basic-figure"><img src="/images/basics/magnetic-on-axis.webp" alt="按TI SLYA085图3-1重绘：径向充磁磁体位于芯片上方，磁体中心与感应中心对齐。磁力线仅示意方向，不是磁场仿真。" loading="lazy"><figcaption>按TI SLYA085图3-1重绘：径向充磁磁体位于芯片上方，磁体中心与感应中心对齐。磁力线仅示意方向，不是磁场仿真。 <a href="https://www.ti.com/lit/pdf/slya085" target="_blank" rel="noopener">原理图来源 ↗</a></figcaption></figure>

## 两路信号为什么能组成角度

理想模型中，两个正交磁场分量可写作 \(B_x=B\cos\theta\)、\(B_y=B\sin\theta\)。通过 \(\operatorname{atan2}(B_y,B_x)\)可恢复方向。真实系统还要处理失调、增益不一致、非正交和谐波。

这一模型要求测量分量、磁体布置和角度定义相匹配。磁体移到芯片侧面后，磁场轨迹不再自动满足理想圆，不能照搬轴端公式便宣布角度正确。

## 三类敏感元件的差异

| 原理 | 元件怎样响应 | 做角度时要留意 |
|---|---|---|
| 霍尔 | 载流结构在磁场下产生横向电压 | 敏感轴、线性范围与失调 |
| AMR | 电阻随磁化方向与电流夹角改变 | 常见饱和型双桥具有180°机械重复周期 |
| TMR | 磁隧道结电阻随磁化相对方向改变 | 自由层、参考层及器件规定的工作磁场 |

常见AMR双桥输出含二倍角项，磁体转过180°可得到相同读数。因此单靠这组信号不能区分整圈的两个半圈；完整360°器件须加入额外判别信息。具体产品已经集成什么，应查框图与手册。

## 多极磁环的位置信息会重复

沿圆周排列多个磁极，能够增加局部信号变化次数；周期信号重复也会让单一路径出现位置歧义。需要粗码道、参考信息或组合解算，才能得到规定范围内的绝对位置。磁极对数也不总等于电信号周期数，AMR等响应机理还会改变周期关系。

[TI：线性霍尔与角度测量](https://www.ti.com/product-category/sensors/magnetic/linear-hall-effect/overview.html)；[ADI AN-1314：AMR周期与双桥](https://www.analog.com/en/resources/app-notes/an-1314.html)；[TDK：TMR检测原理](https://product.tdk.com/ja/techlibrary/productoverview/tmr-angle-sensors.html)。

## 加强磁场之前，先检查方向误差

自设目标场沿x为20mT，另叠加恒定y向1mT，当前位置方向偏转为\(\arctan(1/20)=2.86^\circ\)。这是单一角度的向量算例，不能当整圈误差上限。目标场增至40mT时同点偏转约1.43°，但仍须满足器件场强与磁路条件。[TDK日文产品说明](https://product.tdk.com/ja/products/sensor/angle/tmr-angle/index.html)将外乱磁场列为需处理的问题，并未承诺材料天然免疫外场。结合[安装关系](/wiki/basics/mounting/)与[坐标检查](/topics/guides/magnetic-field-coordinates/)，在[无刷电机](/applications/brushless-dc-motor/)样机上同步记录通电与断电场轨迹。
