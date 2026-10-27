---
{
  "title": "电感编码器：线圈和金属靶怎样测位置",
  "description": "聚焦PCB发射—接收耦合路线，讲清激励、涡流、接收信号与靶片位置的关系。",
  "date": "2026-10-16T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "编码原理",
  "weight": 602,
  "related_basics": [
    "magnetic-encoder",
    "mounting",
    "absolute-incremental"
  ],
  "related_topics": [
    "电感编码器"
  ],
  "related_model_slugs": [],
  "related_applications": [
    "servo-motor",
    "robot-joint"
  ],
  "related_guides": [
    "inductive-error-definition",
    "three-track-observability"
  ]
}
---
一类PCB电感位置传感器由发射线圈、接收线圈、接口芯片和导电靶片组成。靶片不必是永磁体，位置变化通过线圈之间的电磁耦合进入测量结果。

## 为什么金属靶能改变读数

发射线圈由交流信号激励，产生交变磁场。附近导电靶片中形成涡流，涡流产生的次级磁场改变接收端的耦合信号。靶片相对线圈的覆盖位置变化，接收信号随之改变。

这里的关键是**发射端主动产生变化磁场**。不能把它画成静止金属自行产生永磁场，也不能把金属靶简单描述成完全不透磁的挡板。

## 接收线圈为何有特殊形状

接收线圈的空间绕线与靶片形状共同决定位置响应。通过设计，可形成与位置相关的两路信号，经过载波解调、失调与幅值处理，再计算角度或位移。

两路“正余弦”通常指解调后的包络随位置变化，并非两路原始高频载波天然相差90°。绘制波形时应分开载波时间轴与机械位置轴。

## 信号重复时，仍要解决绝对位置

如果单组线圈每机械圈形成多个重复周期，周期内角度不能直接区分当前位于哪个周期。整圈绝对测量需要额外位置约束或码道组合。不能只看到铜齿数量就推断它的绝对解算架构。

## 没有磁铁，仍然有安装条件

气隙、靶片倾斜、偏心、材料导电性、厚度及附近导体都能改变耦合。PCB版图也是传感结构的一部分，不能把线圈视为任意可挪动的普通走线。对静态外部磁场的抑制能力，也不等于对所有频率电磁干扰都免疫。

[Microchip：电感位置传感器](https://www.microchip.com/en-us/products/sensors-touch/inductive-position-sensors)；[研究论文：基于PCB线圈耦合的电感位置传感](https://arxiv.org/abs/2503.14627)。本页讨论该类发射—接收路线，不把所有电感、变压器式或谐振测量结构混为一种。

## 电角误差必须先确认周期数

自设每机械圈有8个解调周期，且当前周期判定正确，0.4°电角相位误差折算为\(0.4/8=0.05^\circ\)机械角。若错认一个周期，跳变却达45°；两者不能并入一个小数精度。[TI LDC5072-Q1手册](https://www.ti.com/lit/ds/symlink/ldc5072-q1.pdf)也区分输出通道INL与外部计算角度误差。因此先看[游标判区](/wiki/basics/vernier/)，再按[电感误差定义](/topics/guides/inductive-error-definition/)分开记录原始包络、计算角与独立参考；[伺服电机](/applications/servo-motor/)反转时尤其要留整周期跳变。
