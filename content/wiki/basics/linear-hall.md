---
{
  "title": "线性霍尔：输出随磁场线性，不代表随位移线性",
  "description": "区分磁场线性、比例输出和机械映射，用输出摆幅检查量程与ADC参考。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "开关与连续检测",
  "weight": 403,
  "related_basics": [
    "hall-effect",
    "hall-element-vs-ic",
    "hall-temperature-drift",
    "3d-hall",
    "magnetic-encoder"
  ],
  "related_applications": [
    "handheld-joystick",
    "toilet-water-level"
  ]
}
---
线性霍尔保留磁场幅度。在规定范围内，可用 \(V_{out}=V_Q+SB_\perp\) 描述零场电平 \(V_Q\) 与灵敏度 \(S\)。磁铁每移动一毫米是否产生固定电压变化，取决于磁路，不能从“线性霍尔”四个字推出。

## 更高灵敏度会更早用完输出余量

自设模拟链路：供电3.3V、零场电平1.65V，假定保证线性输出范围0.2～3.1V，则两侧各有1.45V余量。若灵敏度50mV/mT，可容纳约±29mT；改为100mV/mT则约±14.5mT。实际设计还要减去失调、增益误差与ADC输入限制。

这是摆幅预算算例，不是器件规格。“接近电源轨”也不等于直到0V或供电电压都保持规定线性度。超出量程导致饱和后，提高ADC位数不能恢复丢失的信息。[AKM线性霍尔教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/linear-hall-effect-ic/)可作为功能入门，保证边界仍查具体手册。

## 比例式参考只处理特定供电误差

以[TI DRV5055](https://www.ti.com/product/DRV5055)为例，零场电平与灵敏度随供电关联；传感器供电与ADC参考采用同一合适电源时，比值读数可抵消部分供电变化。独立参考、供电压降或采样瞬态仍需检查。

这种比值不会消掉磁铁温漂、机械位移或电子残余失调；A/Z等版本的温补行为也不同。见[霍尔温漂](/wiki/basics/hall-temperature-drift/)。

## 连续输出也必须先证明位置可观测

单轴读数相同，可能对应多个角度或位移。[摇杆](/applications/handheld-joystick/)需在限定行程内检查单调性，[液位检测](/applications/toilet-water-level/)需区分到位事件与连续高度。要测完整旋转角度，应增加合适的多分量观测，而非把一条重复曲线强行拟合成一圈。

验收依次扫全行程和最大气隙，核输出余量、噪声，再覆盖温度、磁体批差与动态带宽；最终比较规定条件下的位置误差。
