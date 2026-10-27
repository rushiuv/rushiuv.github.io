---
{
  "title": "水表：磁脉冲能记转数，体积还要靠计量关系",
  "description": "把磁场事件、方向与体积标定分开，按最大流量下的有效脉宽检查采样、漏计与电池寿命。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 219,
  "related_basics": [
    "bop-brp",
    "latch",
    "abz",
    "magnetic-encoder"
  ],
  "reference_topic": "水表",
  "related_guides": [
    "rate-budget",
    "position-validity-state"
  ],
  "related_model_slugs": [
    "ktm1301"
  ]
}
---

旋转计量机构把流动变成机械运动，磁体再把运动带到干区传感器。芯片读到的是磁场事件；体积还要经过整表结构和标定关系。若在规定流量范围内，整表标定为每个有效脉冲对应体积K，才可以用V=NK累计，不能由磁极数量直接推出K。

## 低功耗必须带着最短事件宽度比较

[DRV5032](https://www.ti.com/product/DRV5032)和[Allegro A1171](https://www.allegromicro.com/en/products/sense/switches-and-latches/switches/a1171)是可审查的霍尔磁事件候选，采样、极性和阈值按具体版本核对。[KTM1301](/models/ktm1301/)采用TMR开关路线，50Hz与5000Hz等版本不能混用功耗和计数结论；[KTH4622原厂页](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highsensitive2Dhallswitch/index.html)提供二维速度与方向路线，也不直接输出多少升。

休眠采样降低平均电流，却会留下两次观测之间的空窗。自设磁场越过动作阈值仅持续6ms、理想采样间隔50ms，即使平均事件频率很低，也可能整段错过。这是观测时序算例，不是某型号漏计率。应在最大流量、最差气隙和最小磁有效宽度下量波形，参见[速率预算](/topics/guides/rate-budget/)。

## 磁极、边沿与累计量不能混着计数

[锁存器](/wiki/basics/latch/)需要相反磁极驱动两种状态；[磁开关阈值](/wiki/basics/bop-brp/)则决定单次触发与释放位置。一个磁极经过可能产生两个边沿，固件若从“每脉冲”改为“双边沿”，标定系数也必须对应同一种事件定义。

单通道通常只有经过信息，不能单靠计数判断反流。双通道可用空间相位形成[方向状态序列](/wiki/basics/abz/)，还要覆盖停水摆动、极低速换向和非法跳态。未确认方向的事件不能一律算成正向体积。

## 用体积参照区分漏观测和标定错误

台架同时保留开关边沿、时间、方向状态和已知体积，在启动小流量、最大流量、反流与电池末期分别核对。若边沿数量偏少，先查有效脉宽、采样和气隙；用修改K补平总量，会把漏计藏进标定。

系统耗电还包括上拉、主控唤醒、存储及通信。强外磁监测需独立定义判据，普通开关翻转不自动构成篡改证据。超声水表属于另一种计量架构，也不套用叶轮每圈模型；器件可用与整表计量检验分别验收。
