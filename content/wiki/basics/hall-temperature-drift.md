---
{
  "date": "2026-10-27T00:00:00+08:00",
  "title": "霍尔温漂：零点、增益和磁铁变化要分开算",
  "description": "把电压温漂换成等效磁场与位置偏差，说明单点校准和双通道比值各能抵消什么。",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 304,
  "related_basics": [
    "hall-biasing",
    "hall-element-materials",
    "linear-hall",
    "chopper",
    "magnetic-encoder"
  ],
  "related_applications": [
    "servo-motor",
    "handheld-joystick"
  ]
}
---
高温后零位变了，可能是电子零点偏移，也可能是灵敏度、磁铁或结构在变。只有先把它们分开，才知道应该改材料、补偿电路还是磁路。

## 一个读数里叠着三种变化

可用简化模型 \(V(T)=V_0(T)+S(T)B(x,T)\) 看问题：\(V_0\) 是零场失调，\(S\) 是灵敏度，\(B\) 同时取决于位置、磁铁温度与装配。失调使曲线平移，增益使曲线伸缩，磁路变化则可能改变曲线形状。只在一个位置升温，通常分不出是哪一项。

[AKM 的GaAs教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/low-drift/)说明材料和偏置对温度稳定性有影响；“低漂移”仍不能保证整套位置系统不漂移。[线性IC](/wiki/basics/linear-hall/)还可能配置特定磁铁温补，补偿对象与订货版本必须核对。

## 电压漂移要通过局部斜率换算

自设静态算例：残余失调改变2mV，灵敏度20mV/mT，对应0.1mT等效磁场变化；若工作点的磁场梯度为0.5mT/mm，局部位置误差约0.2mm。若运动到梯度仅0.1mT/mm的位置，同一失调约对应1mm。数字只是模型演算，不是某个型号保证值。

这说明同样的电子温漂，在平坦磁场区会被放大。标定与验收必须覆盖全行程，而不是只在斜率最好的中心点测。

## 双通道比值只消掉共同的乘性项

自设理想角度模型 \(x=A(T)\cos(2\pi u),y=A(T)\sin(2\pi u)\)，归一化角度 \(u\in[0,1)\)。经atan2解算时，共同的正幅度 \(A(T)>0\) 可抵消；两路失调、增益温漂差和相位误差不会因此消失。AKM 的[InAs教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/high-sensitivity-hall-element/)给出比值思路，应用时需保留这些条件。

测量上，先在固定磁场下分离失调和增益，再换实际磁体做全温全行程扫描。[斩波稳定](/wiki/basics/chopper/)主要处理电子失调，不能修正磁铁装偏。

器件温补示例：[TI DRV5055的A/Z版本](https://www.ti.com/product/DRV5055)。


差和比怎样进入实际机构，接着读[相机AF与OIS位置反馈](/applications/camera-lens-position/)；归一化成立的前提仍须逐项验证。
