---
{
  "title": "AMR：同一种磁阻，怎样做角度与开关",
  "description": "分清AMR材料响应、饱和双桥的半圈周期，以及三端AMR开关的阈值输出。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 307,
  "related_basics": [
    "gmr",
    "tmr",
    "bop-brp",
    "absolute-incremental"
  ],
  "related_applications": [
    "laptop-lid",
    "servo-motor"
  ],
  "related_guides": [
    "channel-angle-harmonics"
  ]
}
---
AMR（各向异性磁阻）描述电阻随**磁化方向与电流方向的夹角**变化的现象。材料名称还不能回答器件输出什么：模拟桥路可以测方向，桥路加比较器也可以只报“磁体到了”。

![暖纸配色的AMR、GMR与TMR材料结构概念插图](/images/learning/mr-family-v2-20261027.webp)


<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/amr-angle-20261027.svg" alt="饱和双桥的理想二倍频模型；半圈等价不代表所有AMR成品都只有半圈功能。" width="960" height="630" loading="lazy"></div><figcaption>饱和双桥的理想二倍频模型；半圈等价不代表所有AMR成品都只有半圈功能。<a href="/images/learning/amr-angle-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 饱和双桥的方向信号每半圈重复

在足以使磁化方向跟随外场的条件下，可用 \(R=R_\perp+(R_\parallel-R_\perp)\cos^2(2\pi u)\) 理解理想响应。这里 \(u\) 是磁化方向相对电流方向的归一化转角，一圈为1；代入 \(u+0.5\) 电阻不变。

对经过布置的理想正交双桥，信号可写成 \(x=A\cos(4\pi u),y=A\sin(4\pi u)\)。自设 \(u=0.1\) 与0.6，读数相同。连续运动可借历史解包，但上电未知位置无法仅凭这两路区分36°和216°。要获得整圈绝对位置，须核对额外极性或粗位置信息；不能泛化成“所有AMR成品只能测半圈”。[ADI AN-1314](https://www.analog.com/en/resources/app-notes/an-1314.html)讨论的是这种高场角度模式。

## 三端AMR开关输出的是阈值事件

村田教程展示的是另一条信号链：磁阻元件组成桥路，桥中点差分电压经电路判断，超过设定条件后改变OUT状态；三端封装提供电源、地和输出，并可通过间歇采样降低平均功耗。这里的OUT不是正余弦角度数据。[村田AMR工作原理](https://www.murata.com/products/sensor/amr/overview/basic/principle)

因此“有电桥”不能推出“有连续角度”。做[合盖检测](/applications/laptop-lid/)时，应看敏感方向、动作区和释放区；做[伺服反馈](/applications/servo-motor/)时，要看周期、启动歧义和模拟采样。

## 磁饱和、输出限幅与回差不能混称

AMR角度模式的“饱和”指磁化状态；输出撞到电源轨是电路限幅；开关防抖依赖的是动作与释放阈值不同。三者的修复办法不同。角度路线先保证全温度、全气隙下满足工作磁场，再查[通道误差](/topics/guides/channel-angle-harmonics/)；开关路线则按[BOP/BRP](/wiki/basics/bop-brp/)验证容差窗口。
