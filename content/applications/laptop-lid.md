---
{
  "title": "笔记本与平板合盖检测：检测到磁体，不等于知道铰链角度",
  "description": "磁开关适合生成开合事件，折叠姿态识别还需要检查磁路歧义、阈值窗口和外部磁附件。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "消费电子",
  "weight": 9,
  "related_basics": [
    "switch-polarity",
    "bop-brp",
    "amr",
    "air-gap",
    "stray-field"
  ],
  "reference_topic": "笔记本与平板合盖检测",
  "related_guides": [
    "rate-budget",
    "magnetic-field-coordinates"
  ]
}
---

合盖检测首先需要一个可靠事件：屏幕到了约定位置，系统可以休眠。磁开关测到的是敏感方向上的磁场越过阈值；想知道铰链转了多少，还需要连续读数和能区分各个姿态的磁路。这两种任务应在结构设计前分清。

## 先选输出任务，再选敏感机理

[TI DRV5032](https://www.ti.com/product/DRV5032)是按阈值输出状态的霍尔开关；[Allegro A1266](https://www.allegromicro.com/en/products/sense/switches-and-latches/switches/a1266)是三维磁开关。增加检测方向不代表得到三轴连续磁场，更不能直接计算任意铰链角度。

现有候选中，[KTH4603](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/highlysensitive3dhallswitch/index.html)属于XYZ全极霍尔开关，[KTM1301](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/magnetoresistiveSwitchSeries/index.html)属于平面内感应的全极TMR开关。比较时要对准具体后缀的敏感轴、阈值与输出逻辑，封装接近也不能据此换料。

[村田AMR检测示例](https://www.murata.com/products/sensor/amr/overview/basic/example)给出不同磁体与器件相对位置的开关检测布局。它提醒的是磁路要与方向响应匹配；[AMR材料机理](/wiki/basics/amr/)本身不规定成品一定输出连续角度。

## 磁滞窗口要覆盖结构容差

先沿真实开合轨迹测磁场，再按[动作与释放阈值](/wiki/basics/bop-brp/)画窗口：最弱磁体、最大气隙、最不利温度下，合盖仍应可靠触发；最强磁体、最小气隙时，明确打开的位置又应可靠释放。不能只测一台样机的典型触发角。

磁滞可减少临界位置反复翻转，却不能消除完全合盖与背折姿态的歧义。若两种姿态在敏感轴上产生相同磁场，软件去抖也不能把它们重新区分。连续铰链测量应另核对磁场到角度的唯一映射。

## 响应验收带上采样和磁吸附件

DRV5032不同版本采用不同更新速率，低功耗与唤醒时间应按订货号一起核算。传感器观测、主控去抖和操作系统唤醒是三段时间，输出翻转不是屏幕立即点亮；具体做法见[速率预算](/topics/guides/rate-budget/)。

最后加入保护套、耳机盒及外部磁体，改变方向和距离，记录误休眠、无法释放与快速开盖响应。通过[外磁干扰](/wiki/basics/stray-field/)检查后的合盖事件，仍只证明磁检测状态；不能证明铰链完好或设备已进入平板姿态。
