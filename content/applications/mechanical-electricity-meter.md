---
{"title":"机械电表：读到转盘标记，才有可换算的脉冲","description":"反射光检测可研究转盘标记，但玻璃反光、污染与计量常数必须独立核实。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"工业与运动","weight":206,"related_basics":["optical-encoder","absolute-incremental","angle-noise"],"reference_topic":"机械电表"}
---

感应式机械电表的转盘可提供可见标记。外部读数装置可以研究标记经过时的反射变化，但不应开封、改造或干扰受监管的计量机构。外部记录只能在合法授权与不改变原表工作的条件下验证。

## 光电器件先测反射，不直接测电能

Vishay TCRT5000将红外发射与光电晶体管集成在一起；ROHM RPR-0730是带红外VCSEL及光电晶体管的模拟反射传感器。二者可按相同玻璃、标记、距离与环境光条件比较反射信号，都不是已经获准的机械电表读数模块。

[昆泰芯KTO9512](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/cursorabsoluteencoder/index.html)属于另一条光学路线：它读取专用光栅码盘，输出相位阵列相关的正余弦信号，再由后级插值。这个任务不同于隔着原表玻璃读取一个黑标，所以不列为本页外部读数的直接候选。若从零设计编码码盘，可以另行比较，但那已经改变了光学目标与系统范围，不能拿“也是光电芯片”作为替换依据。

当标记与背景产生足够反射差，电路可把变化转为事件。假设表盘常数写着600转每千瓦时，一转对应1/600千瓦时。若只在一个标记处计数，每漏一次就少记一转；这些数字是换算示例，不代表实际表盘常数。

## 肉眼黑色未必在红外下同样黑

标记、铝盘和保护玻璃的反射特性决定信噪比。玻璃多次反射、直射环境光、污渍与传感器距离变化，会让亮暗差变小或改变基线。不能只在打开外壳的实验条件下调好门槛，再宣称隔着完整表壳也能稳定工作。

## 验证累计数，也验证没有转时不乱计

应在授权测试装置上比较人工或独立基准的转数，覆盖极慢运动、停在边界、突然变速及外界光照变化。发光电流和比较器迟滞要连同温度、老化一起验证。只有单个标记时无法凭一个通道判断方向，外部计数也不能代替原表计量检定或作为独立结算依据。

## 原厂资料

- [Vishay TCRT5000](https://www.vishay.com/en/product/83760/)
- [ROHM RPR-0730](https://www.rohm.com/products/optical-sensors/reflective-type-photosensors/rpr-0730-product)
