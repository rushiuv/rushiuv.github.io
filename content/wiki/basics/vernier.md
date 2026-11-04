---
{
  "title": "游标编码：两条周期怎样确定绝对位置",
  "description": "从相邻周期的相位差理解游标与Nonius，区分判区能力、细分位数和实际精度。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "basic-single",
  "basic_entry": true,
  "basic_group": "编码原理",
  "weight": 604,
  "related_basics": [
    "absolute-incremental",
    "singleturn-multiturn",
    "inl",
    "optical-encoder"
  ],
  "related_topics": [
    "游标编码器"
  ],
  "related_model_slugs": [],
  "related_applications": [
    "robot-joint",
    "gearbox"
  ],
  "related_guides": [
    "vernier-uniqueness",
    "three-track-observability"
  ]
}
---
一条每圈重复很多次的正弦轨道，能把小范围运动看得很细，却不知道当前处于哪一个周期。游标编码再加一条不同周期的轨道，用两路相位之间的关系确定区间，再由细轨给出区间内位置。它解决的是重复图案的歧义，不是凭空提高每条轨道的精度。

## 相邻周期给出一个直观例子

用归一化机械角u表示一圈。假设两条轨道分别有十六和十五个周期，理想相位为`a=wrap01(16u)`和`b=wrap01(15u)`，其中`wrap01(x)=x−floor(x)`。两相位之差再按一圈取模，就能恢复u的粗位置。这个例子依赖两轨方向、相位零点与对应关系都已确定，不能直接当通用解码程序。

粗位置接近某个区间边界时，噪声或轨道误差会把判区推到另一侧。后果不只是少一个最低有效位，而可能跳过一个细周期。因此要核对判区裕量，而不是只看输出字长。周期组合改变后，唯一范围与误差放大关系也会改变。

## 芯片需要完整的多轨信号链

[iC-Haus iC-MN](https://www.ichaus.de/product/ic-mn/)提供两轨或三轨Nonius计算及多通道采样，是公开的插值与解算器件例子。它不是自带码盘的完整编码器；光电或磁阻前端、信号幅值、安装与轨道图形仍是系统的一部分。标出的高位数不等于同位数机械精度。

多轨测量还要关注时间一致性。运动时若两路相位来自不同时间，即使各自读数正确，也会形成错误的相位组合。同步采样、状态检查和上电有效性因此与分辨率同样重要。

## 验证要故意接近歧义边界

用独立参考遍历整圈，观察上电、正反转、低速微动和不同气隙下有无整周期跳变。保留各轨原始相位，而不只存最终角度。游标通常给出某一有限范围内的绝对位置；断电后能否保留机械多圈，必须另查结构与计数方案。

## 互质不等于差相位只转一圈

自设两轨7与4周期，完整相位组合一圈内唯一，但差相位为\(\operatorname{wrap}(3u)\)，在u=0、1/3、2/3相同。因此“互质即可直接用相位差当机械角”是反例；8与6则连完整组合也每半圈重复。以上只讨论理想相位且零点方向已确定，实际还要量判区裕量。[iC-MN原厂页](https://www.ichaus.de/product/ic-mn/)给出多轨Nonius解算器件入口。沿[绝对位置范围](/wiki/basics/absolute-incremental/)和[唯一性推导](/topics/guides/vernier-uniqueness/)核对后，再定义[减速器](/applications/gearbox/)的断电移动测试。
