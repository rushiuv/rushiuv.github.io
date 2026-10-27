---
{
  "title": "单极与全极霍尔：响应两种磁极不等于识别磁极",
  "description": "按磁响应曲线区分单极、全极和锁存，继续检查敏感轴、输出接法与采样周期。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "开关与连续检测",
  "weight": 400,
  "related_basics": [
    "hall-effect",
    "hall-element-vs-ic",
    "latch",
    "bop-brp",
    "latency"
  ],
  "related_applications": [
    "laptop-lid",
    "robot-cleaner-dustbin"
  ]
}
---
“全极”表示正、负两个方向足够强的磁场都能触发，不表示三个空间方向都能检测，也不保证一根输出线能告诉控制器是哪一个磁极。选型先看完整磁响应曲线。

## 磁极响应与状态保持是两条分类线

| 类型 | 触发与恢复的典型路径 | 容易误用的地方 |
|---|---|---|
| 单极开关 | 指定磁极靠近触发，离开释放 | 极性或封装方向装反 |
| 全极开关 | 任一磁极足够强时触发，减弱后释放 | 把全极当成磁极识别 |
| 双极锁存 | 一方向磁场置位，反方向磁场复位 | 只靠同一极靠近再撤走 |

表只描述常见行为，门限正负、逻辑电平与启动状态以具体手册为准。个别双输出器件能分别报告磁极，不能从“全极”名称推断。英文资料中的bipolar也可能用于不同分类，应核响应曲线而非直译标签。

## 高低电平还取决于输出级

“低电平表示有磁铁”并非通则。开漏输出要接合适的上拉，推挽输出则主动驱动高低。检查允许的上拉电压、MCU输入门限、负载与漏电；引脚兼容不代表电气行为兼容。

[AKM霍尔IC教程](https://www.akm.com/eu/en/products/hall-sensor/tutorial/hall-effect-ic/)还区分连续与间歇检测。间歇检测在休眠期间保持旧输出，省电代价包括等待下次采样；短暂磁事件可能漏掉，不能把保持状态理解成一直在观察。

## 到位检测需要一个可保证的窗口

[合盖](/applications/laptop-lid/)或[尘盒安装](/applications/robot-cleaner-dustbin/)先定义必须触发与必须释放的位置，再按[动作/释放阈值](/wiki/basics/bop-brp/)核磁路容差。装反、缺磁铁及外部磁附件也应覆盖。开关翻转本身不能证明锁扣、密封或机构已满足其他要求。

原厂例子：[TI DRV5033全极开关](https://www.ti.com/product/DRV5033)、[DRV5032不同极性及采样版本](https://www.ti.com/product/DRV5032)。


在[磁浮子液位](/applications/toilet-water-level/)中，极性选择要连同浮子姿态和箱壁公差检查；检测轴正确仍不能排除浮子卡滞。
