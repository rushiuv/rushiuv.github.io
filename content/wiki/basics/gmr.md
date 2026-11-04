---
{
  "title": "GMR：金属多层怎样把磁方向变成电阻",
  "description": "从自旋相关散射理解GMR，区分多层、旋阀、磁场强度与角度输出。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 308,
  "related_basics": [
    "amr",
    "tmr",
    "magnetic-hysteresis",
    "stray-field"
  ],
  "related_applications": [
    "gearbox",
    "servo-motor"
  ]
}
---
GMR（巨磁阻）的关键结构是磁性层与非磁性**金属**层组成的薄膜体系。电子通过不同磁化排列时经历的散射不同，整体电阻随之变化。它与[TMR](/wiki/basics/tmr/)的区别不在名字里的“大”，而在中间层及输运机制。[诺贝尔奖官方物理说明](https://www.nobelprize.org/uploads/2018/06/popular-physicsprize2007.pdf)


<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/mr-structures-20261027.svg" alt="层结构概念对照，非工艺尺寸；未指定GMR的电流几何。" width="960" height="560" loading="lazy"></div><figcaption>层结构概念对照，非工艺尺寸；未指定GMR的电流几何。<a href="/images/learning/mr-structures-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 多层结构与旋阀不能当成同一输出

一种旋阀结构让参考层方向保持稳定，自由层响应外场，两层的相对方向影响电阻。但GMR还有其他多层结构，未必都用相同参考方式。NVE目录同时介绍多层和旋阀路线，其传输曲线可以不同；不能看到“GMR”就直接写成360°角度传感器。[NVE GMR介绍](https://www.nve.com/Downloads/intro.pdf)

先查横轴是什么：磁场强度、梯度，还是磁场方向。即使都输出模拟电压，信息也不相同。NVE的AA系列测磁场，AB系列测空间梯度；梯度结构抑制共同外场的程度还取决于两位置匹配和干扰空间分布。[AA/AB手册](https://www.nve.com/Downloads/analog_catalog.pdf)

## 桥路电压还需经过位置映射

磁性齿轮靠近时，局部磁场改变，再经桥路转成电压。对自设的100齿均匀齿轮，若每齿形成一个完整信号周期，周期内相位误差0.5°只对应0.005°机械角；但错计一个齿就跳3.6°。这两个误差不能靠增加小数位合并解决，推导还要求齿数与有效周期数确实一致。

因此[齿轮箱](/applications/gearbox/)要分开验证周期内细分、方向判别、丢齿/漏脉冲与上电参考。模拟桥的温漂和供电误差也要计入，不能把材料磁阻比当作编码器精度。

## 先往返扫场，再讨论可重复性

低场响应可能受磁化历史影响。单方向扫一次看起来平滑，不等于升场与降场重合。保持温度、供电、位置和采样设置一致，做双向扫场，再检查强场暴露后是否恢复；[材料磁滞](/wiki/basics/magnetic-hysteresis/)与芯片人为设置的开关回差须分别解释。具体可恢复范围按该型号手册，不能从某种GMR材料推到整个家族。
