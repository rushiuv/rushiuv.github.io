---
{
  "title": "霍尔效应：芯片测到的是哪一个磁场分量",
  "description": "从载流子的横向偏转理解敏感轴、霍尔电压与机械位置，区分裸元件和集成输出。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 300,
  "related_basics": [
    "hall-element-vs-ic",
    "hall-biasing",
    "vertical-hall",
    "3d-hall"
  ],
  "related_applications": [
    "brushless-dc-motor",
    "handheld-joystick"
  ]
}
---
磁铁靠近后读数改变，首先说明敏感方向上的磁场变了。芯片是否能由此判断距离或角度，还要看磁铁的运动路径、充磁方向和观测通道。[霍尔元件与霍尔IC](/wiki/basics/hall-element-vs-ic/)回答的是不同层次的问题。

<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/hall-axes-20261027.svg" alt="平面霍尔俯视：偏置电流沿x、磁场沿z，两横向端形成差分测量" width="960" height="560" loading="lazy"></div><figcaption>平面霍尔的方向约定；不是具体封装的引脚图。端子电压定义与所用公式必须配套。<a href="/images/learning/hall-axes-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 横向电压来自载流子的偏转

载流子沿通电薄片运动，磁场使它们向横向偏转，边缘电荷积累形成反向电场。稳定后，两侧测量端之间出现霍尔电压。理想弱场近似可写成 \(V_H=S_I I_B B_\perp\)：偏置电流为 \(I_B\)，\(S_I\) 是电流相关灵敏度，\(B_\perp\) 是与感知结构对应的磁场分量。实际信号还叠加失调与噪声。

静止磁场也能产生霍尔响应；这与依赖磁通变化的被动线圈不同。磁场翻转时，霍尔电压的符号可翻转，但符号还取决于载流子类型、接线和手册的正方向定义，不能仅从封装朝向猜。

## 敏感轴决定它看得见什么

普通平面霍尔结构与[垂直霍尔](/wiki/basics/vertical-hall/)的感知方向不同。[三轴霍尔](/wiki/basics/3d-hall/)提供多个分量，也不自动获得唯一位置：两处机械位置可能产生相同或相近的磁场向量。应从手册查磁敏中心、敏感轴与封装坐标，再检查全行程是否存在歧义。

同一颗磁铁移近、侧滑或转动，都能改变读数。只有约束了磁路，才能把磁场换算成位移；“输出随磁场线性”也不能推出“输出随距离线性”。

## 输出形式决定后级还剩多少信息

[线性霍尔](/wiki/basics/linear-hall/)保留幅度，[磁开关](/wiki/basics/switch-polarity/)只判断门限，[锁存器](/wiki/basics/latch/)还带有状态保持。按到位、位移或角度任务选择，再核量程、温漂与带宽；数字位数不能替代磁路验证。

来源：[AKM 磁传感原理](https://www.akm.com/eu/en/products/hall-sensor/tutorial/magnetic-sensor/)、[AKM 霍尔传感器分类](https://www.akm.com/eu/en/products/hall-sensor/tutorial/hall-sensors/)。进一步核对：[TI 霍尔数据手册读法](https://www.ti.com/lit/pdf/SLIA086)。
