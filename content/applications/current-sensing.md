---
{
  "title": "磁式电流检测：先把电流变成磁场，再计算安培数",
  "description": "霍尔与闭环磁检测可以读取直流和交流电流，但导体几何、零点、温升与隔离条件一起决定结果。",
  "date": "2026-10-27T00:00:00+08:00",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 231,
  "related_basics": [
    "hall-effect",
    "linear-hall",
    "sensor-transfer-function",
    "sensor-noise-bandwidth",
    "fluxgate"
  ],
  "reference_topic": "磁式电流检测",
  "related_guides": [
    "parameter-conditions",
    "sample-time-contract"
  ],
  "lastmod": "2026-10-27"
}
---
同样是磁传感器，角度测量让磁体运动，电流测量则让导体中的电流产生磁场。器件感应的是某个位置、某个方向的场；要得到安培数，还需确定导体几何、磁路与校准关系。

## 开环读磁场，闭环读补偿量

[Allegro ACS712](https://www.allegromicro.com/en/products/sense/current-sensor-ics/integrated-current-sensors/acs712)把电流导体与霍尔检测集成在封装中，可输出与交流或直流电流对应的模拟电压。[AKM电流检测教程](https://www.akm.com/eu/en/products/current-sensor/tutorial/)将无磁芯磁传感、有磁芯路线与分流电阻方案分开讨论，说明磁式电流检测并非只有一种结构。

开环方案由[线性霍尔](/wiki/basics/linear-hall/)等敏感元件测场，再经过放大和输出。[AKM闭环电流示例](https://www.akm.com/eu/en/products/hall-sensor/tutorial/ultra-high-sensitivity/)用补偿线圈产生反向磁场，由补偿电流推回输入；采用[磁通门](/wiki/basics/fluxgate/)的产品还涉及激励与解调。是否闭环、是否带磁芯，与材料名称是不同问题。

## 零点误差在小电流时格外显眼

设某模拟传感链在规定范围内满足V=V0+S_I·I，换算为I=(V−V0)/S_I。自设S_I=100mV/A、零点残差5mV，则即使没有电流也可能读出0.05A。此例不对应ACS712某个版本，目的是把输出误差换回输入量。

提高ADC位数不能消掉这5mV。应分别核零点与增益随温度的变化，并按[噪声与带宽](/wiki/basics/sensor-noise-bandwidth/)说明滤波条件。电流环需要的是采样时刻对应的电流，不能只看界面上慢速平均后的平稳数值。


<figure class="basic-figure technical-figure"><div class="diagram-viewport" tabindex="0" role="region" aria-label="工程示意图，可左右滑动查看"><img src="/images/learning/current-feedback-20261027.svg" alt="用补偿绕组的反向安匝抵消原边安匝的闭环磁式电流检测框图" width="960" height="580" loading="lazy"></div><figcaption>零磁通附近的负反馈概念模型；绕组极性、环路稳定性和最大电流仍需具体设计。<a href="/images/learning/current-feedback-20261027.svg" target="_blank" rel="noopener">查看原图 ↗</a></figcaption></figure>

## 主电流路径和外磁路径要一起检查

集成导体仍有电阻和发热；非接触磁检测不等于主电流路径没有损耗。大电流后的温升可能继续影响零点，因此验收应包含冷态零点、正负电流扫幅及热态回零，并与有已知误差的参照仪器对比。

旁边母排、电感与[无刷电机](/applications/brushless-dc-motor/)相线也会产生磁场，要在真实位置和开关工况下测试。封装隔离额定值、PCB爬电距离与系统绝缘要求分别核对；不能由“磁式”两个字推定任意模块已满足隔离条件。
