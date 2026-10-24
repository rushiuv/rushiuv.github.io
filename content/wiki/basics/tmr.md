---
{
  "title": "TMR：隧道结的高响应不等于整机高精度",
  "description": "从自由层、参考层与隧穿电阻解释TMR，区分材料响应和角度系统指标。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与开关",
  "weight": 126,
  "related_basics": [
    "amr",
    "magnetic-encoder",
    "mounting",
    "resolution-accuracy"
  ],
  "related_applications": [
    "robot-joint",
    "servo-motor"
  ],
  "related_guides": [
    "amplitude-temperature-error",
    "magnetic-field-coordinates"
  ]
}
---

TMR 是隧道磁阻。两个磁性层之间夹着很薄的绝缘势垒，电流通过量子隧穿越过势垒。两层磁化方向的相对关系改变，电阻随之改变，这是它与普通电阻式位移传感器不同的地方。

## 固定参考与跟随磁场的自由层

角度感知结构中，参考层提供方向基准，自由层在规定磁场下跟随外部方向。把若干磁隧道结构组合成桥路，就能得到用于判断方向的信号。TDK 的 TAD2141 数据手册公开了这一结构和正弦、余弦桥路的原理。

这种角度路线可以区分完整一圈的磁场方向，但不能把这个特点推广到所有 TMR 产品。开关、电流、线性磁场和角度器件采用不同结构与电路，最终测量对象必须按具体手册判断。

## 输出大只是误差链中的一环

较大的磁阻变化有利于获取信号，但系统角度还受到桥路失调、增益差、正交误差、磁场轨迹和信号处理影响。“磁阻比高”“输出位数多”和“角度准确”是三个不同指标，不能互相代替。

磁铁偏心使方向轨迹畸变，附近电机产生附加磁场，这些都不会因材料换成 TMR 自动消失。部分器件针对外磁场设计了差分或补偿结构，也必须核对其规定的磁路和干扰条件，不能给整个材料家族贴上“天然抗干扰”的标签。

## 比较器件先对齐测试条件

选型先确认工作磁场范围、测量平面、输出接口、启动时间及延迟，再比较规定条件下的角度误差。样机应覆盖磁体批次、偏移、气隙与温度，并同时记录静态误差和运动误差。模拟桥路还要把外部放大器与采样误差计入；数字角度芯片则要检查配置、诊断和数据时序。

来源：[TDK TMR 原理说明](https://www.micronas.tdk.com/en/products/tmr-angle-sensors)、[TDK TAD2141 数据手册](https://product.tdk.com/info/en/documents/datasheet/tmr-angle/ds_sensor_tmr-angle_tad2141_en.pdf)。

## 信号变大之后，剩下哪项误差

自设理想两路峰值100mV、残余单通道偏置1mV，小扰动角误差幅值约\(1/100=0.01\)rad，即0.573°；峰值加倍且偏置不变时约减半。这只是信号链算例，不是TMR产品精度。[TDK原理说明](https://product.tdk.cn/zh/techlibrary/productoverview/tmr-angle-sensors.html)介绍自由层与固定层；这种结构本身不能消去外部放大器偏置。测试应分别保存偏置、峰值和角误差，详见[幅值与温度误差](/topics/guides/amplitude-temperature-error/)。再与[AMR](/wiki/basics/amr/)按同磁路比较，并覆盖[机器人关节](/applications/robot-joint/)工作电流造成的附加磁场。
