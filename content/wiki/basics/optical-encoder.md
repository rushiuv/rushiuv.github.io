---
{
  "title": "光电编码器：从刻线、码道到角度",
  "description": "区分透射与反射、增量周期与绝对编码；理解电子细分怎样获得细刻度。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "检测原理与安装",
  "weight": 8,
  "related_basics": [
    "resolution-accuracy",
    "abz",
    "inductive-encoder"
  ],
  "related_topics": [
    "光电编码器"
  ],
  "related_model_slugs": [
    "kto9512"
  ],
  "related_applications": [
    "linear-motor",
    "servo-motor"
  ],
  "related_guides": [
    "optical-signal-chain",
    "reflective-code-validation",
    "optical-tolerance-evidence"
  ]
}
---


光电编码器用光读取码盘或光栅尺上的位置图案。图案随被测件运动，探测器接收的光分布发生变化，电子电路再从中提取位移或位置。

<figure class="basic-figure"><img src="/images/basics/optical-reflective.webp" alt="参考雷尼绍RESOLUTE光学示意重绘：保留反射式光路和部件关系，仅改变视觉风格。示意图不代表所有光电编码器结构。" loading="lazy"><figcaption>参考雷尼绍RESOLUTE光学示意重绘：保留反射式光路和部件关系，仅改变视觉风格。示意图不代表所有光电编码器结构。 <a href="https://www.renishaw.com.cn/zh/how-renishaw-optical-encoders-work--36979" target="_blank" rel="noopener">原理图来源 ↗</a></figcaption></figure>

## 透射与反射改变的是光路

透射式让光穿过码盘的透明区域，光源和探测器位于码盘两侧。反射式利用不同区域的反射特征，光源与探测器可以位于同一侧。具体结构还可加入透镜、掩模和探测阵列。

不能仅凭“光电编码器”判断它属于哪一种光路，也不能把一个厂商的读头剖面当作所有产品的内部结构。

## 周期刻线怎样变成细位置

均匀刻线提供重复的空间周期。合适的光学与探测结构可形成两路相位错开的信号，再通过信号处理与插值得到周期内位置。数字AB输出则把位移表示为可计数的边沿。

**光栅周期、插值倍数和最终输出分辨率是不同层次。** 增加插值能让数字格子更细，却不会自动修正刻线误差、码盘偏心或信号失真。

## 绝对编码需要能识别位置的图案

绝对式系统必须在指定测量范围内区分位置。多码道编码、单码道独特码序列、粗细信息组合都能参与实现，不能把“绝对式”限定为多条同心码道的格雷码盘。

读头识别位置图案后，还可提取周期内的细位置。粗位置解决“是哪一段”，细位置解决“这一段内走到哪里”。具体怎么组合，以相应器件公开说明为准。

## 选型时先看三个实际条件

读头与码盘的间隙、倾斜和偏心是否满足安装规范；污染是否影响光路；输出边沿或串行速率是否能被控制器可靠接收。防护能力要看整机结构和额定条件，不能仅由检测原理判断。

[雷尼绍：光栅工作原理](https://www.renishaw.com.cn/zh/how-renishaw-optical-encoders-work--36979)介绍了其反射式光学、绝对图案解码与细分方式。本文透射/反射分类不意味着所有产品采用同样的光学结构。

## 插值之前先确认前端没有削顶

自设TIA的线性输出范围0.2至3.1V，偏置2.5V、反馈100kΩ，光电流20±2µA对应0.3至0.7V；光照加倍便要求负电压，已超出假定范围。数字位数再多也恢复不了此前削顶的波形。[TI光电TIA设计资料](https://www.ti.com/lit/an/sboa324a/sboa324a.pdf)用于核增益、偏置与稳定性，数值并非其中器件指标。与[分辨率](/wiki/basics/resolution-accuracy/)分开检查，沿[光学信号链](/topics/guides/optical-signal-chain/)逐级留波形；[直线电机](/applications/linear-motor/)还要在实际污染和间隙下复测。
