---
{
  "date": "2026-10-27T00:00:00+08:00",
  "title": "霍尔元件材料：InSb、GaAs、InAs改变的是哪笔误差账",
  "description": "区分裸元件灵敏度、偏置与温度稳定性，不把材料名称当作完整传感器精度排序。",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 302,
  "related_basics": [
    "hall-biasing",
    "hall-temperature-drift",
    "hall-element-vs-ic",
    "angle-noise"
  ],
  "related_applications": [
    "brushless-dc-motor",
    "servo-motor"
  ]
}
---
相同磁场下，裸霍尔元件的输出大小与温度变化可能差很多。材料影响载流子的迁移率、浓度及其温度特性，但整颗传感器还包括偏置、封装与读出电路，不能只按材料选精度。

## 三类材料对应不同取舍

AKM 的裸霍尔元件教程给出以下产品路线。它是这些系列的比较，不是所有厂商和全部工作条件下的通用排名。

| 材料与AKM系列 | 教程强调的特点 | 选型时继续追问 |
|---|---|---|
| InSb，HW | 三类中输出灵敏度高 | AKM示例中恒压温度特性较稳，仍核额定激励与失调 |
| GaAs，HG | 三类中温度特性稳定 | AKM示例中恒流温度特性较稳，还需核读出噪声 |
| InAs，HQ | 灵敏度与温度特性的折中 | AKM示例中恒压温度特性较稳，仍核温区与匹配 |

教程中的硅材料不列入这三组裸元件产品，并不意味着硅霍尔无法做高性能IC。集成放大、[斩波](/wiki/basics/chopper/)和补偿会改变最终能力，应回到[元件与IC的层级](/wiki/basics/hall-element-vs-ic/)比较。

## 大输出能减轻失调比例，不能证明动态更快

自设读出算例：两路在同一磁场变化下分别输出10mV与100mV，后级同有1mV残余失调，失调占信号的比例分别为10%与1%。提高信号幅度能减轻这笔相对误差，但不说明前端带宽、延迟或输出噪声已经改善。不同器件的失调也不能默认相同。

[无刷电机](/applications/brushless-dc-motor/)的磁极交界处，失调会让比较器提前或滞后翻转；判断影响应看该处的磁场斜率，而不只看磁极中心的峰值。

## 比较材料前先固定偏置与温区

恒流和恒压的温度行为不同，见[霍尔偏置](/wiki/basics/hall-biasing/)。对室温输出做一次归一化，只消掉一个标定点的差异；还要比较全温失调、灵敏度漂移、功耗和[噪声带宽](/wiki/basics/sensor-noise-bandwidth/)。

来源：[AKM InSb教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/ultra-high-sensitivity/)、[GaAs教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/low-drift/)、[InAs教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/high-sensitivity-hall-element/)。
