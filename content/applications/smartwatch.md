---
{"title":"智能手表：表冠旋转、按下和指南针是三件事","description":"局部磁体可以帮助读取表冠或按键动作，但不能将这种近场测量与地磁航向混为一谈。","date":"2026-10-18T10:00:00+08:00","lastmod":"2026-10-18","layout":"application-single","application_entry":true,"application_group":"消费电子","weight":7,"related_basics":["magnetic-encoder","absolute-incremental","stray-field"],"reference_topic":"智能手表"}
---

智能手表里的磁检测不只有指南针。围绕表冠布置磁体，可以评估旋转输入；让按键带动磁体位移，也可以评估非接触按压检测。这些都是局部近场测量，与利用地磁求航向的任务不同，不能因都叫磁传感器就共用同一套量程与标定。

## 表冠需要的是操作事件

围绕表冠，应把旋转与按下分别列成任务：

| 候选 | 测量量或输出 | 适用边界 | 原厂来源 |
|---|---|---|---|
| Infineon TLE493D-W2B6-A1 | 三轴磁场 | 旋转与按压需机构映射 | [详情](https://www.infineon.com/part/TLE493D-W2B6-A1) |
| TI TMAG5273 | 多轴场与角度计算 | 核对选轴及唤醒模式 | [详情](https://www.ti.com/product/TMAG5273) |
| 昆泰芯 KTH5502 | XY平面绝对角度 | 适合评估在轴旋转，不自动读出按压力 | [详情](https://www.conntek.com.cn/html/web/product/magneticAngleDetectionChip/kth5502/index.html) |
| 昆泰芯 KTH1701 | 全极霍尔开关 | 可评估按下事件，不提供连续转角 | [具体型号表](https://www.conntek.com.cn/html/web/product/switchPositionDetectionChip/microPowerSeries/index.html) |

这些是候选元件，不是某款手表采用该方案的证明。封装、电源、持续旋转功耗及第一步唤醒延迟要按同一交互要求比较，不能拿开关的待机功耗去对标角度器件持续测量功耗。

无限旋转的表冠通常需要连续判断方向与增量，并处理角度跨圈；可按下的表冠还要区分轴向移动与旋转。若按压改变气隙，角度计算使用的两路磁场也可能变化，应在旋转与按压同时发生时检查，而不是分别测完就结束。

## 省电状态可能改变交互感觉

低功耗模式、唤醒条件和采样节奏要与第一格滚动的响应一起验证。待机电流低，不代表持续旋转时也保持同样功耗；休眠后的第一组数据是否有效，也要按器件时序处理。过慢采样可能跨过多个刻度，主控不能从缺失样本中保证恢复真实转动方向。

## 磁吸附件是必测工况

充电座、磁吸表带、扬声器与外部磁体都可能影响局部读数。验证应保留整机装配状态、磁附件相对方向、表冠位置及原始磁场，并检查掉电重启后的状态。磁检测减少电接点需求，不等于整机自动防水，也不能从芯片参数推导防水等级或长期密封寿命。

## 原厂资料

- [Infineon TLE493D-W2B6-A1](https://www.infineon.com/part/TLE493D-W2B6-A1)
- [TI TMAG5273](https://www.ti.com/product/TMAG5273)
