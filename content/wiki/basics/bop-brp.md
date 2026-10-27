---
{
  "title": "动作与释放阈值：磁滞窗口怎样变成位置窗口",
  "description": "按BOP与BRP的保证边界设计到位窗口，用局部磁场斜率区分磁滞、重复性和动态误差。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "开关与连续检测",
  "weight": 401,
  "related_basics": [
    "switch-polarity",
    "latch",
    "hall-temperature-drift",
    "mounting",
    "latency"
  ],
  "related_applications": [
    "laptop-lid",
    "toilet-water-level"
  ]
}
---
动作阈值 \(B_{OP}\) 与释放阈值 \(B_{RP}\) 不同，会形成磁滞。它能减少临界磁场附近反复跳变，也会使进、退过程在不同位置翻转。先区分这种有意设置的保持区，与器件批差和噪声。


<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/switch-hysteresis-20261027.svg" alt="正阈值低有效开关，自设动作4 mT、释放2 mT；实线增场，虚线减场。" width="960" height="600" loading="lazy"></div><figcaption>正阈值低有效开关，自设动作4 mT、释放2 mT；实线增场，虚线减场。<a href="/images/learning/switch-hysteresis-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 磁滞不是固定的毫米数

以正向单极开关为例，磁场增加到动作阈值后切换，减小到释放阈值后恢复。同一器件、同一条件下的磁滞可记为 \(B_H=B_{OP}-B_{RP}\)；[全极](/wiki/basics/switch-polarity/)还要分别看两支曲线，[锁存](/wiki/basics/latch/)的门限可位于零点两侧，不能丢掉符号套公式。

自设局部线性算例：\(B_{OP}=5\text{mT}\)、\(B_{RP}=3\text{mT}\)，磁场随位置斜率的绝对值为2mT/mm，往返位置差约1mm。换一条斜率为0.5mT/mm的磁路，则约4mm；跨越较大行程时，应直接求两门限与实测磁场曲线的交点。

## 保证触发和保证释放分别检查最坏边界

必须触发的位置，要让最弱磁场超过动作阈值的最坏边界；必须释放的位置，要让最强残留磁场进入保证释放区。磁体批差、气隙、偏移与温度都要纳入。手册里的最小、典型和最大值含义不同，典型动作距离不能作为批量保证。也不能把动作阈值的最大值与释放阈值的最小值相减，就当作某一颗器件的实际磁滞；两项可能来自不同样品或条件。

[TI数据手册读法](https://www.ti.com/lit/pdf/SLIA086)给出门限设计方法；实际器件如[DRV5032](https://www.ti.com/product/DRV5032)还须匹配订货后缀和采样版本。

## 位置重复性还多一笔时间账

若机构速度为 \(v\)，总延时为 \(t_d\)，延时带来的附加位移近似为 \(v t_d\)。这是动态偏移，不是磁滞本身。间歇采样、软件去抖与控制器处理都可能进入延时。

因此验收应分别报告动作/释放位置、重复性分布和不同速度下的偏移。[AKM的磁滞解释](https://www.akm.com/eu/en/products/hall-sensor/tutorial/hall-effect-ic/)是功能基础，不能代替实际机构的全温全容差验证。
