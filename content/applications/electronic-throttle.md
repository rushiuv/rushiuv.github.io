---
{
  "title": "电子节气门：阀片角度、双通道与失效状态",
  "description": "把阀轴位置、输出传递关系与双通道诊断分开核对，避免共同磁路故障同时伪装成合法读数。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "汽车与交通",
  "weight": 301,
  "related_basics": [
    "sensor-transfer-function",
    "magnetic-encoder",
    "pwm",
    "crc",
    "mounting"
  ],
  "reference_topic": "电子节气门",
  "related_guides": [
    "safety-evidence-levels",
    "position-validity-state"
  ]
}
---

节气门控制需要阀轴实际位置。驱动电机的转数不能替代阀片反馈，因为齿轮间隙、回位弹簧、止挡和积碳都会改变动作。测量链应从阀轴目标开始，一直核到控制器采用数据的时刻。

## 磁场读数还要经过位置传递关系

[Melexis MLX90371](https://www.melexis.com/en/product/mlx90371/triaxis-performance-rotary-linear-position-sensor-ic-analog-pwm)提供模拟或PWM位置输出，[TI TMAG5170-Q1](https://www.ti.com/product/TMAG5170-Q1)提供三轴磁场与SPI路线；后者仍需设计磁路与位置映射。[KTH7801原厂系列页](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)列有相应车规型号，实际资格、接口与诊断应核对具体后缀，不能借用同系列另一封装的结论。

相同的阀轴运动可以对应不同输出斜率与端点区间，参见[传递关系](/wiki/basics/sensor-transfer-function/)。标定时应明确机械有效行程、输出有效区与诊断区；把越界值截断到“全关”或“全开”，会抹掉本应可见的异常。

## 双通道能相互比较，也可能一起出错

自设有效行程比例u在0到1之间，两通道输出比例分别为y1=0.1+0.8u、y2=0.9−0.8u，因此理想和为1。这个例子说明软件可以检查传递关系；它不是任何具体芯片的配置或安全阈值。

若共用磁体整体移位，两通道可能仍满足和为1，却同时对应错误阀角。双芯片封装增加独立信号路径，也不能自动消除磁体、供电或外场等共同原因。需要明确哪些故障由相关性检查覆盖，哪些必须依靠独立参照或其他诊断。

## 数据合法性与故障归宿分别定义

[PWM](/wiki/basics/pwm/)要核周期、极性、诊断占空比；数字接口则同时核[校验](/wiki/basics/crc/)、状态和数据新鲜度。通信正确只能证明传输规则满足，不能证明磁路没有变化。

验证应包括慢速贴近止挡、回位、不同温度与驱动电流，以及断线、供电异常和磁体偏移。允许哪些端点学习、故障后采取何种动作，应由系统设计确定。AEC-Q100资格、SEooC声明与整机安全论证是不同层级，依据见[安全证据层级](/topics/guides/safety-evidence-levels/)。
