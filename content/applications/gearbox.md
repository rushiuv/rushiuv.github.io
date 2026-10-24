---
{
  "title": "齿轮箱：用两端位置区分理想传动与实际输出",
  "description": "从输入输出测点理解传动误差、方向分支和扭转变形，避免把角差直接当扭矩。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-24",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 211,
  "related_basics": [
    "vernier",
    "inl",
    "latency"
  ],
  "reference_topic": "齿轮箱",
  "related_guides": [
    "dual-encoder-difference-budget",
    "system-acceptance-record"
  ],
  "related_model_slugs": [
    "ma732",
    "ktm5900",
    "ktm5200"
  ]
}
---

输入转了一百圈，名义减速比为一百的齿轮箱输出应转一圈，这是理想运动约束。真实输出还受齿形、装配、轴承、负载与换向历史影响。要研究这些变化，先把传感器测点放在需要比较的两个实体上，而不是只读取电机控制器的指令位置。

## 芯片位于哪一段测量链

轴端磁角度与外部读头方案的边界不同，应把输入量和输出路径一起列出：

- [MPS MA732](https://www.monolithicpower.com/en/ma732.html)：轴端磁角→可调滤波角度输出；滤波配置会改变动态响应。
- [iC-Haus iC-MN](https://www.ichaus.de/product/ic-mn/)：多通道正余弦→插值与Nonius角度；仍需前端和匹配码道。
- [昆泰芯KTM5900](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrTMPMagnrticEncoderChip/index.html)：TMR角度链→SPI、ABZ等；输出位数不能代替输入、输出两测点的同步与标定。
- [昆泰芯KTM5200](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM52XX/index.html)：在轴AMR角→SPI、ABZ等；应验证实际磁场与校准后的误差。

这不是齿轮箱已采用或各路线能直接互换的证明。

## 最先约束的是坐标与有效时刻

输入角必须保存累计圈数，再按实际拓扑统一方向并折算到输出侧。若把单圈输入码直接除以减速比，每次输入过圈都会制造假跳变。两路滤波与读取时刻不同，也会把运动速度变成角差，即使齿轮没有新增变形。

无载记录仍可能包含损耗和预载状态。正反向曲线不同，只证明观测存在方向依赖，不能唯一认定为齿隙。轴、联轴器和壳体的柔性也可能进入两测点之间的差值；乘一个目录刚度不等于完成整机扭矩标定。

## 验证保留方向与负载历史

用同方向重复轨迹建基线，再用未参与拟合的轨迹验证，反向分支单独保存。改变温度、速度、输出载荷后检查基线是否仍适用。若要发布扭矩结果，应使用独立负载参照识别刚度与迟滞，并明确测到的是哪段传递扭矩，不把它自动叫作末端接触力。

选型验收因此应同时写清绝对位置误差、换向行为、时间同步和覆盖工况；只有一张平滑的空载曲线，还不足以判定齿轮箱状态。


## 目录刚度不能直接替代整机负载曲线

[Nabtesco德文刚度说明](https://www.nabtesco.de/service/faq/begriffserklaerung/torsionssteifigkeit)给出固定输入、对输出加载卸载的测量方式，并在指定载荷区间取斜率。先按[INL](/wiki/basics/inl/)区分传感器误差，按[延迟](/wiki/basics/latency/)排除运动中的采样错位，再使用[双编码器预算](/topics/guides/dual-encoder-difference-budget/)。

自设同一加载支路中，输出扭矩由10增至20N·m、扭角增加0.5角分，局部斜率是20N·m/角分；这不代表零载附近或卸载支路也相同。用独立负载参考同步记录两端连续圈数和扭矩，卸载数据保持原样；判定对象是当前两测点间的传动链，不能把轴和联轴器柔性都归给齿轮。把加载范围、温度、预载与参考写入[整机验收记录](/topics/guides/system-acceptance-record/)，再决定目录值是否适用。
