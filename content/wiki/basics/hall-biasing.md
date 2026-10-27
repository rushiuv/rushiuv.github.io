---
{
  "date": "2026-10-27T00:00:00+08:00",
  "title": "霍尔偏置：恒流和恒压为什么会得到不同温漂",
  "description": "用两种激励关系区分载流子浓度、迁移率与自热，解释裸元件不能照搬IC的供电方式。",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "磁敏机理与器件",
  "weight": 303,
  "related_basics": [
    "hall-effect",
    "hall-element-materials",
    "hall-temperature-drift",
    "hall-element-vs-ic"
  ],
  "related_applications": [
    "brushless-dc-motor"
  ]
}
---
给裸霍尔元件恒流，和给它恒压，不只是电源画法不同。输入电阻随温度改变时，恒压下的电流会跟着变，输出温漂也随之改变。先确认手册采用哪一种激励，再比较灵敏度。

## 两种公式中的灵敏度不是同一个量

理想、单一载流子且忽略几何修正时，恒流近似为

\[
V_H=\frac{R_H}{t}I_B B_\perp,\qquad |R_H|\approx\frac{1}{nq}.
\]

\(t\) 为有效厚度，\(n\) 为载流子浓度，\(q\) 为电荷量的绝对值。符号取决于载流子及接线约定。恒流相关灵敏度的量纲可写为V/(A·T)。

恒压模式的理想关系可写为

\[
V_H\approx\mu_H\frac{W}{L}V_B B_\perp.
\]

此时输出与霍尔迁移率 \(\mu_H\) 有关，电压相关灵敏度为V/(V·T)。真实元件还受形状、接触和偏置范围限制；两个公式不能省掉各自条件，直接拿数据表数字相除。

## 固定电流也没有固定结温

自设纯电阻功耗算例：输入电阻1kΩ，偏置1mA时耗散1mW；若电阻升至1.2kΩ，恒流耗散升至1.2mW。相反，固定1V时耗散从1mW降至约0.83mW。这里只算激励功耗，不是器件温升实测；温升还取决于封装、PCB和热环境。

因此，即便环境温度相同，偏置不同也可能带来不同自热。还要核恒流源的电压余量和最大额定值，不能为增大输出任意提高激励。

## 先对齐测试条件，再谈哪一种更稳

[材料特性](/wiki/basics/hall-element-materials/)会改变两种驱动的结果。按实际温区分别记录输入电阻、零场失调与已知磁场下的增益，再检查重复性。[集成霍尔IC](/wiki/basics/hall-element-vs-ic/)内部可能已有稳流或补偿，不能仅从外部供电方式推断内部偏置。

来源：[AKM 霍尔元件驱动与公式](https://www.akm.com/eu/en/products/hall-sensor/tutorial/hall-elements/)。温漂如何进入位置结果，接着读[霍尔温漂](/wiki/basics/hall-temperature-drift/)。
