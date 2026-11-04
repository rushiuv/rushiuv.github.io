---
{
  "title": "灵敏度、量程与位置映射：电压线性不等于位移线性",
  "description": "把传感器V(B)与磁路B(x)分开，识别饱和、零点和无法唯一反解的位置。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁场与信号基础",
  "weight": 202,
  "related_basics": [
    "linear-hall",
    "magnetic-field-quantities",
    "sensor-noise-bandwidth"
  ],
  "related_applications": [
    "camera-lens-position",
    "electronic-throttle"
  ]
}
---
读头把磁场变成电信号，机构把位置变成磁场。只有两段关系都明确，控制器才能把电压解释成位置。

<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/sensor-chain-20261027.svg" alt="位置经磁路成为磁场，再经敏感元件和调理成为读数，最后按标定映射恢复位置" width="960" height="520" loading="lazy"></div><figcaption>本站原创测量链：每个箭头代表一次映射；接口输出不能跳过前面的物理条件。<a href="/images/learning/sensor-chain-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 灵敏度是斜率，量程是可用区间

小信号线性近似 \(V=V_0+S_B B_s\)。\(V_0\) 是零场输出，\(S_B\) 是电压对磁场的斜率。自设 \(V_0=1.65\) V、\(S_B=50\) mV/mT、允许输出0.25–3.05 V，按摆幅算出的范围为±28 mT；这只是该理想链的上限，还要与器件保证的磁量程、线性误差和负载条件取交集。

斜率加倍，在相同摆幅下量程会缩小。量程太窄会截顶；量程太宽则浪费转换刻度。不能只追求最大的mV/mT。

## 机械位置必须沿磁路再换算

若位置为 \(x\)，则 \(dV/dx=S_B\,dB_s/dx\)。即便芯片的 \(V(B)\) 是直线，磁场梯度也可能随位置变化。自设两处梯度分别2和0.2 mT/mm，相同50 mV/mT对应100与10 mV/mm的位置斜率，相同电压误差会成为相差十倍的位移误差。

行程中还要检查映射是否单调。两处位置若给出相同读数，单通道查表不能唯一反解。增加ADC位数不能增加缺失的观测信息。[镜头位移反馈](/applications/camera-lens-position/)中的双元件方案也必须检查差和比在全行程内是否单值。

## 两点校准只能修正两类线性误差

两点校准可估计零点与增益，不能自动消除磁路非线性、温漂差或动态延迟。验收时分开记录原始磁场、输出码和机械基准，观察到底哪一段偏离模型，再决定改磁路、校准表或量程。

依据：[TI DRV5055数据手册：线性输出与量程](https://www.ti.com/lit/ds/symlink/drv5055.pdf)、[TI正面位移检测设计](https://www.ti.com/lit/ab/sbaa519a/sbaa519a.pdf)。本文数值均为本站自设推导，不对应具体型号保证值。
