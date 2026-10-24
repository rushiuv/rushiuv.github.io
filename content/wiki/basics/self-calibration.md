---
{
  "title": "自校准：先问它在修正哪种误差",
  "description": "把出厂校准、在线幅相修正和整机查表分开，明确无参考校准所依赖的运动条件。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "看懂性能参数",
  "weight": 142,
  "related_basics": [
    "inl",
    "magnetic-encoder",
    "mounting",
    "angle-noise"
  ],
  "related_topics": [
    "自校准",
    "非线性校准"
  ],
  "related_model_slugs": [],
  "related_guides": [
    "calibration-evidence",
    "calibration-validation",
    "calibration-data-integrity"
  ],
  "related_applications": [
    "robot-joint"
  ]
}
---

“支持自校准”没有统一的修正范围。有的器件在出厂时修正自身偏置，有的运行时更新两路信号的幅值、偏置或正交参数，还有的需要整机转动后写入误差表。名字相同，所需输入和能消掉的误差并不相同。

## 波形变圆，不等于机械角已知

假设两路信号为`x=A cosθ+bx`、`y=B sinθ+by`。去偏置并校正幅值，可以改善由它们计算的角度。但磁场方向本身若已随偏心、钢件或磁体形状发生畸变，把椭圆变圆不一定能恢复真实机械角。算法能看到的是信号，不会自动获得一根更准确的参考轴。

[Infineon TLE5012B](https://www.infineon.com/part/TLE5012B-E1000)把出厂存储参数与可选内部自校准分别说明；[MPS MA600A](https://www.monolithicpower.com/en/ma600a.html)则提供整机用户修正表。它们是两种不同功能入口，不能互相套用校准流程、转速条件或最终精度。

## 无外部参考，也要交代假设

一种无参考思路是利用已知运动规律，把时间或多次观测当约束。例如假定匀速，再把采样点不均匀归因于角度误差。如果运动本身有速度波动，两者就会混在一起。宣称支持非匀速的方案，也仍需检查覆盖角度、采样量、收敛范围和失败标志，不能理解成任意晃动都能成功。

## 校准结果必须经得起下一次

测试前保存原参数与原始数据，记录运动方向、速度、温度和磁路状态。观察完成标志之外，还要用未参与建表的记录复测；换向、重新上电和更换磁体后的结果应分别检查。失败后应保留有效旧参数，不能把一次中断留下的半张表当正式结果。

选型时直接问：它修哪几项、需要什么参考、怎样触发与保存、哪些条件下拒绝更新，以及能否读取校准状态。完成时间短只是效率指标，不能替代校准后的整机误差证据。

## 确认校准改了信号，还是改了角度映射

[MLX90382手册第21页](https://www.melexis.com/-/media/files/documents/datasheets/mlx90382-datasheet-melexis.pdf#page=21)分别描述I/Q相对灵敏度、正交度自校准和16点线性化，不能合成一项“自动消除所有误差”。合成设信号相位为u+0.001sin(2πu)，轨迹即使完全成圆，机械角仍有最大0.36°偏差。验收要保留校准前后的独立参考残差，并在重启后复测；[校准证据](/topics/guides/calibration-evidence/)解释为何圆形轨迹不是[INL](/wiki/basics/inl/)合格证明。

如果机械运动覆盖不到手册要求的区域，先核对适用条件，不能由完成标志推断全圈已经校准。
