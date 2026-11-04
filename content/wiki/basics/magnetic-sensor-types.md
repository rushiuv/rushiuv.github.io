---
{
  "title": "磁传感器怎么分：先问测静态场、方向还是变化",
  "description": "以测量任务组织线圈、霍尔、磁阻、磁通门与SQUID，避免拿材料名称代替功能。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁场与信号基础",
  "weight": 201,
  "related_basics": [
    "hall-effect",
    "amr",
    "inductive-magnetic-sensing",
    "fluxgate",
    "squid"
  ],
  "related_applications": [
    "gear-speed",
    "electronic-compass",
    "current-sensing"
  ]
}
---
先判断任务需要磁场幅值、磁场方向、阈值事件还是磁通变化，再选机理。名称中都有“磁”，并不意味着可以互换，也不能仅凭机理名称给功耗和精度排固定顺序。

![暖纸风格磁传感器场景插画：拾取线圈、薄片元件、绕线磁芯与独立低温装置](/images/learning/magnetic-sensing-landscape-20261027.webp)

## 输入是否必须随时间变化

| 路线 | 直接观察什么 | 先查什么边界 |
|---|---|---|
| [被动拾取线圈](/wiki/basics/inductive-magnetic-sensing/) | 磁通随时间的变化 | 静止没有感应电压；低速幅度不足 |
| [霍尔元件](/wiki/basics/hall-effect/) | 与敏感结构对应的磁场分量 | 偏置、失调、敏感轴与量程 |
| [AMR](/wiki/basics/amr/)/[GMR](/wiki/basics/gmr/)/[TMR](/wiki/basics/tmr/) | 磁状态引起的电阻变化 | 场或方向模式、饱和及输出结构 |
| [磁通门](/wiki/basics/fluxgate/) | 激励磁芯的非线性响应变化 | 激励、解调、剩磁与外场范围 |
| [SQUID](/wiki/basics/squid/) | 超导环路对磁通的响应 | 低温、屏蔽、反馈与系统成本 |

主动[电感编码器](/wiki/basics/inductive-encoder/)有自己的交变激励，可以在目标静止时测耦合；不能套用“线圈静止没有输出”的结论。静态磁场检测中，磁通门虽然内部有交流激励，测量对象仍可以是直流场。

其他入口：[半导体磁阻SMR](/wiki/basics/semiconductor-mr/)关注载流子路径变化；[干簧管](/wiki/basics/reed-switch/)通过实际触点输出状态。

## 材料、器件与系统是三个层次

同一种AMR材料可以进入开关，也可以进入角度双桥。霍尔裸元件与霍尔IC的外围工作不同；具有SPI的磁传感器可能输出磁场码，也可能输出已解算角度。接口数字化不代表输出已经是机械位置。

选择路线时，写清上电是否需要绝对位置、是否要求零速有效、允许多少气隙和外场、控制器要读哪一种量。接着分别核[传递关系](/wiki/basics/sensor-transfer-function/)与[噪声带宽](/wiki/basics/sensor-noise-bandwidth/)，最后再进入具体型号页。

## 弱场测量是邻近知识，不是编码器等级

磁通门与SQUID解释了磁检测还有位置反馈以外的尺度。它们的弱场能力不能直接推出适合紧凑伺服；反过来，适合角度反馈的读头也不一定适合地磁导航。这里按任务建立入口，不将课堂中的综合比较表变成器件采购排行榜。

阅读依据：[AKM磁传感路线概览](https://www.akm.com/eu/en/products/hall-sensor/tutorial/magnetic-sensor/)、[MPS磁传感概览](https://www.monolithicpower.com/en/learning/resources/magnetic-sensors-common-types-key-components-parameters-usage-considerations-and-applications)、[ESM 2024 Magnetic Sensors课程](https://magnetism.eu/esm/2024/slides/esm2024-vallejo-fernandez-slides.pdf)。各路线的条件和进一步一手依据见所链接的独立词条。
