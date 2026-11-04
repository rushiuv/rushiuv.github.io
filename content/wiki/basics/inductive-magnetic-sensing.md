---
{
  "title": "感应线圈：测到的是磁通变化，不是静止磁场",
  "description": "用法拉第定律区分被动拾取线圈、主动激励位置检测和磁通积分测量。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 312,
  "related_basics": [
    "fluxgate",
    "hall-effect",
    "inductive-encoder",
    "pole-pairs"
  ],
  "related_applications": [
    "gearbox",
    "brushless-dc-motor"
  ]
}
---
一只被动拾取线圈最直接响应的是穿过线圈的**磁通变化率**。用它感应旋转磁极很方便，但磁体静止后电压接近零，并不表示当地磁场已经消失。若需要零速仍有位置读数，就必须另看[霍尔](/wiki/basics/hall-effect/)、磁阻或主动激励路线。


<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/induction-boundary-20261027.svg" alt="被动线圈与主动激励的边界；固定位置不等于没有交变磁通。" width="960" height="570" loading="lazy"></div><figcaption>被动线圈与主动激励的边界；固定位置不等于没有交变磁通。<a href="/images/learning/induction-boundary-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 波形幅度会随变化速度改变

理想条件下，\(e=-N\,\mathrm d\Phi/\mathrm dt\)。若磁场在有效面积A内近似均匀、方向固定，则 \(\Phi\approx AB\)。负号描述感应方向，不是“测出了负磁场”。[UCLA线圈实验原理](https://demoweb.physics.ucla.edu/node/113)

本站自设N=100匝、A=10mm²，垂直磁场从0升到1mT、耗时1ms，忽略负载和寄生，平均感应电压幅值约1mV；相同磁通变化若耗时10ms，只剩0.1mV。直接用同一个电压门限检测，会把低速可检出性也变成系统约束。

## 停止运动后，不能靠软件凭空得到静态量

电压积分能恢复**磁通变化量**，但仍需要已知参考状态、线圈有效面积/匝数和漂移控制。磁通计可以通过移入移出或变化磁场完成测量，不等于一只静止线圈自带绝对直流磁场读数。[Lake Shore磁测量设备选择指南](https://www.lakeshorecryotronics.com/hubfs/Downloads/Choosing%20the%20right%20magnetic%20measurement%20equipment_FINAL.pdf)

对[齿轮转速](/applications/gear-speed/)检测，应分别测最低转速、启动、停车和反转。不能把高转速大幅度波形的测试结果，直接用作零速位置能力的证据。

## 主动电感编码器有自己的载波

[PCB电感编码器](/wiki/basics/inductive-encoder/)用电路主动发射交流磁场，靶片静止时仍可改变耦合，因此能够测静态位置。磁通门也主动激励，但它测的是外场引起的磁芯响应。两者都含线圈，测量对象和解调链却不同。

阅读框图时先找激励从哪里来，再找输出随时间还是随位置变化；最后分开记录载波频率、机械频率与解调带宽，避免把“三种频率”当成一个速度指标。
