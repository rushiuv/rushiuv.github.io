---
{
  "title": "电子罗盘：先找地磁方向，再处理机内磁场与倾斜",
  "description": "三轴磁场不直接等于航向角，硬铁偏置、软铁变形、坐标与倾斜补偿决定读数能否解释。",
  "date": "2026-10-27T00:00:00+08:00",
  "layout": "application-single",
  "application_entry": true,
  "application_group": "消费电子",
  "weight": 12,
  "related_basics": [
    "magnetic-field-quantities",
    "sensor-transfer-function",
    "stray-field",
    "3d-hall"
  ],
  "reference_topic": "电子罗盘与磁航向",
  "related_guides": [
    "magnetic-field-coordinates",
    "calibration-validation"
  ],
  "lastmod": "2026-10-27"
}
---

电子罗盘测量环境中的地磁场方向，轴角编码器测量磁体相对芯片的位置。两者都可能输出“角度”，参照物却不同；罗盘读数不能直接替代关节轴角，轴端强磁体也可能压过地磁信号。

## 磁场要先转到约定的坐标系

[AKM罗盘教程](https://www.akm.com/eu/en/products/electronic-compass/tutorial/)说明了静止设备也可利用地磁定向的基本路径。水平放置且完成轴向与符号约定时，可由两个水平磁场分量的atan2计算磁航向；设备一旦倾斜，水平投影就需要重新求取。

[NXP AN4248](https://www.nxp.com.cn/docs/en/application-note/AN4248.pdf)使用三轴加速度计与磁强计构造倾斜补偿。先核对传感器封装轴与整机坐标，并确认[三轴霍尔](/wiki/basics/3d-hall/)等具体器件的轴向与读出定义，再组合数据；不能把PCB丝印朝向当作算法坐标已正确。强加减速时，加速度计读数包含运动分量，直接当作重力会影响补偿，须明确适用工况。

## 硬铁平移与软铁变形是两件事

机内固定磁源可造成磁场偏置，铁磁结构还会改变场的比例与方向关系。[NXP AN4246](https://www.nxp.com.cn/docs/en/application-note/AN4246.pdf)以硬铁偏置与软铁矩阵建立校准模型：只减去三轴均值，通常不能同时消除各方向的比例和耦合误差。

采集姿态要覆盖空间方向，而不是在桌面上转一圈就宣称完成三维校准。拟合之后还要用独立姿态与已知航向验证，方法接到[校准与验证分开](/topics/guides/calibration-validation/)。拟合残差小，只说明给定数据与模型相容。

## 改变整机状态，检查校准还能否成立

校准参数能处理的是模型覆盖的、相对稳定的[外磁干扰](/wiki/basics/stray-field/)。[磁吸合盖](/applications/laptop-lid/)附件、扬声器和电流改变的磁场，可能使先前模型不再适用。应切换附件、电机与充电状态，记录原始三轴场、航向和有效性标志；单靠滤波让航向平滑，可能只是把错误变慢。

输出还要标清磁北或真北。真北转换需要位置、日期对应的磁偏角信息；不能在所有地区加同一个常数。罗盘、惯性器件与定位系统的融合属于进一步的导航任务，本条只解释磁航向如何建立、何时需要重新验证。
