---
{
  "title": "在轴、离轴、气隙与偏心：先把几何关系说清",
  "description": "分清读头位置、感应中心与旋转轴，避免用一个气隙数字概括安装质量。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁路与机械安装",
  "weight": 705,
  "related_basics": [
    "magnetic-encoder",
    "resolution-accuracy",
    "inductive-encoder"
  ],
  "related_topics": [
    "离轴",
    "磁编码器"
  ],
  "related_model_slugs": [
    "mlx90382"
  ],
  "related_applications": [
    "robot-joint",
    "servo-motor"
  ],
  "related_guides": [
    "eccentricity-budget",
    "magnetic-field-coordinates"
  ]
}
---
“在轴”与“离轴”首先描述读头相对旋转轴的位置。磁体充磁、敏感轴、码环结构和解算方式还需要单独说明。读头移离轴心后，通常必须重新确认信号轨迹和适用算法。

<figure class="basic-figure"><img src="/images/basics/magnetic-on-axis.webp" alt="轴端磁体中心位于芯片感应中心上方" loading="lazy"><figcaption>参考TI SLYA085图3-1重绘的轴端对齐关系。图中没有给出通用气隙数值，实际间隙应按具体型号手册确定。<a href="https://www.ti.com/lit/pdf/slya085" target="_blank" rel="noopener">原图所在应用笔记 ↗</a></figcaption></figure>

## 在轴与离轴怎么区分

轴端在轴方案常将双极磁体固定在轴端，芯片感应中心对准旋转轴。离轴方案把读头放到侧边，可读取环形磁栅，也可读取特定磁体的侧向磁场。两种离轴读法不是同一磁路。

空心轴有利于穿线或布置传动件，但“离轴”不自动保证空心，也不自动意味着多极磁环。具体机械剖面应以该产品的安装图为准。

## 三种偏差，不能都叫气隙

| 几何量 | 它表示什么 | 常见核对方法 |
|---|---|---|
| 气隙 | 指定工作面到感应面或读头基准的距离 | 依照手册定义的两个基准面量取 |
| 径向偏心 | 磁体、码环或读头中心与旋转中心横向错开 | 核对同轴度与旋转跳动 |
| 倾斜 | 码盘、磁体面或读头姿态偏转 | 核对角度与整圈间隙变化 |

封装表面并不一定是敏感层所在位置；外壳中心也不一定是感应中心。PCB装配时要使用手册给出的感应中心坐标。

## 气隙更小，为何未必更准

磁体更近通常会改变场强，但磁场均匀性和分量比例也随位置改变。若磁体表面附近的场方向畸变更大，缩小气隙并不必然改善角度误差。还须满足器件场强范围与机械最小间隙。

安装评估应在整圈检查误差和有效信号，而非只在某一角度读到一个“正常”幅值。温度、轴向移动与允许装配公差也要覆盖。

[ADI AN-1314：轴端磁体、感应中心与气隙](https://www.analog.com/en/resources/app-notes/an-1314.html)展示了特定AMR系统的布置和测量条件，不能将其尺寸与容差套到其他型号。

## 把一次安装扫描变成可比记录

自设一套轴端样机，保持同一磁体与PCB，分别在标称气隙及轴向增加0.2mm时采整圈；每组同时存参考角、两路原始信号和幅值范围。0.2mm只是试验步长，不能当容差结论。若均值场强仍合格而角误差增大，应继续检查分量轨迹，不能仅凭“有磁场”放行。[ADI的特定AMR布置研究](https://www.analog.com/en/resources/app-notes/an-1314.html)同样把磁体和偏移条件一起给出。先按[偏心分类](/wiki/basics/eccentricity/)明确变量，再用[几何预算](/topics/guides/eccentricity-budget/)安排测点；[机器人关节](/applications/robot-joint/)还应覆盖实际轴承负载。
