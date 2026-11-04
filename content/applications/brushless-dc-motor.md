---
{
  "title": "无刷直流电机：先把转子位置换成正确电角度",
  "description": "从锁存霍尔的六种状态到连续角度，先对齐极对数、电零位与时间，再评价换相表现。",
  "date": "2026-10-18T10:00:00+08:00",
  "lastmod": "2026-10-27",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "工业与运动",
  "weight": 213,
  "related_basics": [
    "latch",
    "uvw",
    "pole-pairs",
    "latency",
    "magnetic-encoder"
  ],
  "reference_topic": "无刷直流电机",
  "related_guides": [
    "magnetic-field-coordinates",
    "sample-time-contract"
  ],
  "related_model_slugs": [
    "ma330",
    "tle5012b",
    "kth7812"
  ]
}
---

无刷电机真正需要的是转子磁场相对定子绕组的电位置。设机械归一化角度为u_m、极对数为p、电零位偏置为u_0，电角度可写成u_e=frac(pu_m+u_0)，frac表示取小数部分。输出位数增多不会自动确定p和u_0。

## 霍尔状态与连续角度承担不同任务

[锁存霍尔](/wiki/basics/latch/)利用交替磁极切换状态，三路信号可形成一个电周期内的六种有效组合。它提供换相区间；区间内进一步插值需要速度与运动假设。连续角度则输出更细的位置，但替换时还要修改坐标、接口及驱动软件。

候选包括[MPS MA330](https://www.monolithicpower.com/en/ma330.html)的绝对角与UVW路线、[TLE5012B](https://www.infineon.com/part/TLE5012B-E1000)的GMR角度路线、[KTH7812原厂系列页](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/hshrMagneticCodedAngleSensor/index.html)的霍尔角度路线，以及[KTM5200原厂页](https://www.conntek.com.cn/html/web/product/magneticCurrentLinearSensingChip/KTM52XX/index.html)的AMR路线。接口、封装与配置按具体订货号核对，不能把系列功能合成一个虚构版本。

## 极对数同时放大时间误差

[maxon安装手册3.5.2节](https://www.maxongroup.com/medias/sys_master/root/8873283846174/ecXXframeless-en-21-03.pdf)给出三路霍尔按电周期排列的换相图。自设4对极、6000rpm，电频率400Hz，每个60°电角区间约417µs，只对应15°机械角，不能把机械一圈当一个换相周期。

若反馈固定延迟10µs，同一转速下落后0.001机械圈，即0.36°；乘以4对极后为1.44°电角度。以上仅为换算例。[TMAG5115手册](https://www.ti.com/lit/ds/symlink/tmag5115.pdf)将传播延迟与抖动分列，也说明平均延迟与边沿不确定性应分别预算，刷新率不能代替两者。

## 通电以后再核对磁路和换相坐标

先用驱动器批准的限流流程确认[UVW相序](/wiki/basics/uvw/)、极对数、电零位和转向，再做静止启动、低速加载、反转及快速加减速。记录独立机械位置、三路状态或角度、相电流和故障状态。

最大相电流、温升、轴材与电机漏磁都可能改变实际磁场；空载断电读数准确不足以代表这些工况。按[磁场坐标核对](/topics/guides/magnetic-field-coordinates/)检查敏感分量，再按[采样时间约定](/topics/guides/sample-time-contract/)核对数据时刻。换相位置可用之后，才有依据评价转矩波动与效率。
