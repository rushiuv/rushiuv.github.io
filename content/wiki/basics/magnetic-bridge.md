---
{
  "title": "磁阻电桥：四个电阻怎样变成可读的差分信号",
  "description": "从分压关系推导桥路输出，分清共模、差模、失配与真正被抵消的变化。",
  "date": "2026-10-27T00:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁场与信号基础",
  "weight": 203,
  "related_basics": [
    "amr",
    "gmr",
    "tmr",
    "magnetoresistance-ratio"
  ],
  "related_applications": [
    "camera-lens-position",
    "servo-motor"
  ]
}
---
磁阻元件改变的是电阻，控制器通常读取的是电压。电桥把几个电阻的相对变化转换成差分量，再由放大与采样电路读出；桥上没有电流，就没有可读取的桥压。

<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/magnetic-bridge-20261027.svg" alt="两个串联电阻分支共用激励，左上R1左下R2，中点A；右上R3右下R4，中点B，输出定义为VA减VB" width="960" height="650" loading="lazy"></div><figcaption>理想高输入阻抗读出，忽略连线和接触电阻。R编号、分压公式和差分极性保持一致。<a href="/images/learning/magnetic-bridge-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 中点电压由分压比决定

按图的节点定义：\(V_A=V_E R_2/(R_1+R_2)\)，\(V_B=V_E R_4/(R_3+R_4)\)，输出 \(V_D=V_A-V_B\)。四臂相等时两中点都是 \(V_E/2\)，差分为零，却不表示中点对地电压为零。

自设 \(R_1=R_4=1.01R\)、\(R_2=R_3=0.99R\)，则 \(V_A=0.495V_E\)、\(V_B=0.505V_E\)，所以 \(V_D=-0.01V_E\)。在3.3 V激励下为−33 mV。交换放大器输入会翻转符号，不能只看波形正负判断磁场朝向。

## 公共变化抵消需要明确条件

若四臂都乘同一个系数，每个分压比保持不变。这解释了电桥能抑制部分共同电阻变化；各臂温度系数不同、局部应力不同或自热不一致时，就会出现残余失调与增益变化。它不保证“所有温漂自动消失”。

电桥输出往往还随激励变化。用同一电源作ADC参考，可以抵消满足比例条件的供电变化，但放大器失调、共模范围及参考布线仍须核对。

## 双桥相位由布局与物理响应共同决定

AMR双桥通过不同的元件方向得到正交信号；单个三端AMR开关则可以把桥信号送到比较器，最终只保留ON/OFF。外壳上同样写“磁阻”，可用信息却不同。继续读[AMR的角度与开关两种工作方式](/wiki/basics/amr/)，再核对具体成品框图。

依据：[ADI ADA4571：双桥与调理](https://www.analog.com/media/en/technical-documentation/data-sheets/ADA4571.pdf)、[村田AMR：桥路到ON/OFF](https://www.murata.com/products/sensor/amr/overview/basic/principle)。本页节点模型及电阻变化例为本站独立推导。
