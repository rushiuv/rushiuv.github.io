---
{"title":"无人机旋翼：数到转速，还没有得到推力","description":"转子磁检测可服务换向或测速，磁极对数、时间延迟和机械传动决定读数如何进入控制链。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"消费电子","weight":8,"related_basics":["pole-pairs","abz","latency"],"reference_topic":"无人机旋翼"}
---

无人机旋翼相关的磁检测，首先测的是电机转子或附加磁环的运动，不是飞机姿态，也不是直接测推力。同样转速下，桨叶、空气密度与来流条件不同，推力也可能不同。因此需要先写清信号进入电机换向、测速记录还是更外层的控制环。

## 磁极经过与机械一圈不同

不同输出对应的时间与磁极定义必须分别核对：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| TI TMAG5115 | 霍尔锁存状态 | 由控制器数边沿与确定相序 | [详情](https://www.ti.com/product/TMAG5115) |
| Allegro A1233 | 双通道速度、方向路线 | 需匹配磁环及输出版本 | [详情](https://www.allegromicro.com/en/products/sense/switches-and-latches/latches/a1233) |
| 昆泰芯 KTH7101 | 磁绝对角度，SPI等路线 | 要核实动态延迟、滤波和磁场条件 | [型号详情](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/magneticencoder/index.html) |

KTH7101的连续角度可以作为另一种反馈路线研究，但官网更新率不能直接当作控制环总延迟；也不能把上述数字磁事件器件的带宽直接换成允许机械转速。三者都不是完整飞控或电调方案。

假设磁目标为7对极，机械转速为6000转/分，则机械频率为100赫兹，磁场周期频率为700赫兹。控制器若数上升沿、双边沿或多通道状态，计数系数还会不同。这是合成算例，不是某型号电机或芯片的额定工作点。

## 时间误差会变成转动相位误差

高速下应核对磁检测响应、边沿抖动、输入滤波、计时器和控制任务的完整链路。数据手册里的单项响应时间，不能直接当成整机反馈延迟。低速起转、停在阈值附近、反向外力带动和快速加减速也需要单独测试，不能只用匀速方波证明可靠。

## 先在台架核对，而不是飞起来猜

验证应比较独立转速参考，保留磁极对数、计数方式、时间戳及漏边沿记录，并覆盖电机通电后的大电流干扰与温升。如果目标直接利用电机磁场，还须验证绕组磁场是否改变触发位置。传感器读数正常不能证明桨叶连接可靠或推力充足；台架测试也需隔离旋转部件，未经系统验证的反馈链不应直接用于飞行试验。

## 原厂资料

- [TI TMAG5115](https://www.ti.com/product/TMAG5115)
- [Allegro A1233](https://www.allegromicro.com/en/products/sense/switches-and-latches/latches/a1233)
