---
{
  "title": "更新率、延迟与带宽：读得快是否跟得上",
  "description": "用6000 rpm与10 μs算例，将数据刷新、信息年龄和动态跟踪分开。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-16",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "看懂性能参数",
  "weight": 6,
  "related_basics": [
    "angle-noise",
    "interfaces",
    "resolution-accuracy"
  ],
  "related_topics": [
    "FOC",
    "编码器接口"
  ],
  "related_model_slugs": [
    "as5047p"
  ]
}
---


主控每10 μs收到一帧，并不代表角度只滞后10 μs。数据可以更新很频繁，但每帧仍来自更早的采样；内部滤波也能让变化后的读数慢慢跟上。

## 先把三个时间概念分开

| 指标 | 它描述什么 | 不能直接推出什么 |
|---|---|---|
| 更新率 | 每秒产生多少次新结果 | 每个结果相对运动的延迟 |
| 延迟 | 指定输入事件到指定输出事件的时间差 | 所有频率下的跟踪能力 |
| 带宽 | 对不同频率变化的幅值与相位响应 | 一次接口读操作耗时 |

手册的“延迟”起止点也不同：采样锁存到数据可读、磁场变化到角度输出、串行读请求到帧完成，含义不能混用。流水处理中的不同环节可以重叠，不能不看时序就把所有周期相加。

## 过时10 μs，角度差多少

对匀速旋转，若使用的角度相对当前位置落后 \(T_d\)：

\[
\Delta\theta_m=\omega_mT_d
\]

6000 rpm等于每秒100圈，即36000°/s。10 μs的信息年龄对应0.36°机械角。若电机为7对极，同一机械滞后对应2.52°电角度。这里的7是电机对极数，不是编码器磁环对极数。

这是匀速、无预测补偿条件下的计算示例。加速时误差还与运动变化有关，滤波器则需结合频率响应分析，不能把整个动态链条都压成一个固定延迟。

## 应该向手册和时序图确认什么

确认角度在哪一刻采样、是否有时间戳、读操作是否锁存、连续读取是否会拿到同一结果，以及滤波设置怎样改变响应。控制器最终使用数据的时刻，才是系统信息年龄的终点。

[Allegro：A31315信号链延迟说明](https://www.allegromicro.com/-/media/files/application-notes/an296263-a31315-signal-path-delay-for-a31315-3d-sensor.pdf?sc_lang=en)区分了器件内部不同延迟；[RLS AksIM-2手册](https://www.rls.si/ko/fileuploader/download/download/?d=1&file=custom%2Fupload%2FMBD01_10EN_datasheet_bookmark.pdf)给出了其具体锁存和输出定义。
