---
title: "宇树 G1 头部的深度视觉芯片，为什么还不是中国造？奥比中光、图漾、海康、光鉴...加油"
date: 2026-05-22T00:00:00+08:00
slug: "UV_um9MzI1Ztx7ZLI4TkYw"
description: "宇树 G1 的头部感知里，有一个很有意思的组合：Livox MID-360 激光雷达 + Intel RealSense D435i 深度相机。前者是国产，后者是 Intel RealSense 系列。也就是说，在这台国产人形机器人身上，激…"
original: "https://mp.weixin.qq.com/s/UV_um9MzI1Ztx7ZLI4TkYw"
---

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DBrlpXS1RIX30oxCZ03EGciaxHtrhogxLicS0BXvxk77Exbg1Fibyk6icqNOtFeqhoeZiaayXgJSnq6WtexWU2bL50xUHfN6KZvSgTHSY7tjicczc/640?wx_fmt=jpeg&from=appmsg)

## 宇树 G1 头部的深度视觉芯片，为什么还不是中国造？奥比中光、图漾、海康、光鉴...加油

### 01 G1 头部这颗“眼睛”，卡的不是摄像头，而是深度视觉默认件

宇树 G1 的头部感知里，有一个很有意思的组合：**Livox MID-360 激光雷达 + Intel RealSense D435i 深度相机**。前者是国产，后者是 Intel RealSense 系列。也就是说，在这台国产人形机器人身上，激光雷达这类看起来更“贵”的传感器已经国产了，但深度视觉模块这条链路，仍然能看到国外方案。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXwvEouRRZOBj19NmDEE3AXfqPyWYiamt5ARP0uweuwzO0er1utCQX3TnhhqR3rNUAtVRZhEYe9LQl2vKNOLYUHlB2OFtTd0Zfc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIXxVV34b0pS0MicpicRfFSdfqhDOxU0VibzKBJ6nib7q7wVnw2XbFVQkia2PFQhtX6CY3ZH5uPw4nlQocrZVqEeAmm12HjUEwibztV5M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIVClhbYUo0nQaUT2CV8eVR1bLM89iaXRvNJpAg3WMlbpeicNMXLzvp8Wp4ymUVIUVTQUcXNAjDwJubguFYHibpNfzXsx0nt7txdU0/640?wx_fmt=png&from=appmsg)

这不是因为中国做不出深度相机。国产厂商现在已经有不少产品可以对标 D435i，比如奥比中光 Gemini 330 系列里的 **Gemini 335、Gemini 335L、Gemini 336、Gemini 336L、Gemini 335Lg、Gemini 335Le**，还有 Femto 系列、图漾工业 3D 相机、海康机器人 3D 视觉产品。真正的问题是：G1 头部这种位置要的不是“能出深度图”的相机，而是一个能被机器人算法栈直接相信的深度视觉默认件。

D435i 的优势不只是硬件。它是 **D430 双目深度模组 + D4 深度处理器 + IR 主动纹理 + RGB + IMU + librealsense SDK + ROS 生态** 的组合。客户用它，不只是因为参数够用，而是因为大量机器人开发者已经围绕它调过 SLAM、避障、点云滤波、外参标定和异常处理。

国产替代真正要替的，不是一个 Intel logo，而是这套“默认可用”的系统位置。

### 02 D435i 难替的第一层：D4 把双目深度计算做成了低功耗 ASIC

D435i 最核心的芯片不是 RGB sensor，而是 **Intel RealSense Vision Processor D4**。Intel D400 系列数据手册明确写到，D4 的主要功能是做 stereo depth processing，也就是把双目图像在相机端处理成深度数据，再通过 USB 或 MIPI 交给主机。([Intel CDRD][2])

这件事很关键。双目深度不是两个摄像头拍完，随便写个算法就行。它要做左右目同步、去畸变、极线校正、视差搜索、代价聚合、置信度判断、孔洞填补、边缘保护，最后把 disparity 转成 depth。这里最吃资源的是 stereo matching，因为每个像素都要在另一幅图上沿极线找对应点。

D435i 的公开参数是 **1280×720 深度分辨率，最高 90fps**。单路 1280×720×90fps 已经是每秒约 8290 万像素，双目输入就是 1.66 亿像素级别。每个像素还要做多个视差候选的匹配和过滤。如果这件事丢给机器人主控 CPU/GPU 做，当然也能算，但功耗、延迟和确定性都会变。

D4 的价值就在这里：它不是“能算”，而是把这套 pipeline 固化在相机端，用比较稳定的功耗和延迟持续吐出 depth stream。对人形机器人来说，确定性很重要。头部感知链路后面接的是避障、建图、运动规划和控制安全边界，偶发延迟比平均延迟更可怕。

国产很多方案现在已经开始补这一层。比如奥比中光 Gemini 33X 系列明确强调 **MX6800 自研深度引擎 ASIC**，也是把深度计算放在相机端，而不是完全丢给主机。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXwRwbSUdYwDzz7T7Ma2IQrichkh6JupS0Tsv2lSiajsAiaQ8l4h2xoUQP50mUHVyOMFaHh5IRww7tZjTzGxzSN34oA1fg9wwwUic0/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIW2VHicA5maBoMpgJHVJEVc3fPcOCBibmGfibFgJEIrGUdcdxoULmqsUF3QQYHabVoEM8UkhThWGrQObJicibNId58Z2sXE8vzibtDeo/640?wx_fmt=png&from=appmsg)

但从“有 ASIC”到“客户敢直接替 D435i”，中间还有距离。因为 ASIC 不只是算出深度图，还要把输出格式、时间戳、同步方式、SDK 行为、异常恢复做成客户可预期的东西。芯片算力只是第一关，系统确定性才是签字关。

### 03 国产新型号已经追上很多纸面参数，但替换时卡在动态场景

国产现在不是没产品。奥比中光 Gemini 330 系列已经不是早期那种“能出 3D 图就行”的开发板思路，而是明显朝机器人、AMR、工业自动化去做工程化。Gemini 330 系列公开资料里写了主动/被动双目融合、自研 MX6800 深度 ASIC、宽视场、深度和彩色帧同步、多设备同步，并且支持 NVIDIA Isaac ROS 和 Omniverse。

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUupVgjMk1MueJEW9emmPQol8BgJcLBfOQ9kjoRmsTrpXXDltf572EMMdCicg2lpBW6TKAQeZiavmGagyxTNkYTE4lh1savyQynQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DBrlpXS1RIUIKQ9ib849DxxEYicX8pVRytYbCm6vibiaHOy5us65xibGTrRNuoyzazhhPbuiaw4qPLA06yRsxybwRoI3r39VGRzPKic9icQj5Mrice4E/640?wx_fmt=png&from=appmsg)

具体到型号，**Gemini 335 / 336** 更像标准 USB 机器人双目相机；**Gemini 335L / 336L** 加了 IP65、全局快门 RGB 和 IR，更偏工业机器人和移动机器人；**Gemini 335Lg** 走 GMSL2/FAKRA，强调 6Gbps 带宽、15m 线缆、抗振连接和 IP65，明显是给移动机器人、机械臂、严苛工业场景准备的；**Gemini 335Le** 则走 PoE/M12，以太网供电和长距离布线更方便。

这些产品说明国产已经在补 RealSense 的短板。D435i 过去强在开发者生态，但它毕竟是 USB 小模块形态，工业现场里长线缆、振动、EMC、IP 防护并不是它最擅长的方向。Gemini 335Lg 的 GMSL2/FAKRA、Gemini 335Le 的 PoE/M12，反而更像真正要上机器人量产的接口形态。

但问题是，G1 头部这种位置，不是换一个接口就结束。D435i 的强项是 **1280×720@90fps** 和成熟 RealSense pipeline。Gemini 335 这类产品常见公开参数是 **1280×800@30fps**，部分新资料提到 Gemini 330 系列可支持更高帧率模式，但客户在替换时不会只看“最高帧率”几个字，而会问：在我需要的分辨率、曝光、IR 模式、同步模式、SDK 输出格式下，实际能不能稳定跑？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DBrlpXS1RIXqcnOMg87knxo5iaD40FaJjC4xJJNE8ScxwooNUHSYiazcN50hicLrH7QXd5ibNm8Hnlb7d5KE2a9ATp2AB9VubDexXcjraIhiaadw/640?wx_fmt=png&from=appmsg)

这就是动态场景的坑。静态测 2m 白墙，国产相机可能很好看；但机器人走起来以后，头部会摆动，机身会振动，图像会有运动模糊，IMU 和 depth frame 要对齐，点云还要投到机器人坐标系。30fps 和 90fps 的差异，不是视频流畅度，而是感知链路的时间裕量。

### 04 真正难补的是时间戳：深度图晚几毫秒，机器人看到的世界就偏了

深度视觉在固定工位上很容易显得“够用”。相机架在三脚架上，拍一块标定板，中心区域误差很小，参数表也能写得漂亮。但人形机器人不是三脚架。它走路时头部在晃，腰在摆，脚落地会有冲击，传感器数据必须和机身状态对齐。

D435i 里那个 “i” 就是 IMU。RealSense D400 系列资料里，D435i 使用 D430 模组、D4 处理器，并带 IMU；新版本文档还提到 BMI085 替代 BMI055。

IMU 的意义不是“多一个惯导”。它真正的价值是给 VIO、SLAM、运动补偿提供时间基准。depth frame、RGB frame、gyro、accel 如果不是同一个时钟域，或者时间戳 jitter 太大，机器人动起来以后，点云就会错位。

举个现场里很容易遇到的问题：静态时，国产相机和 D435i 都能测出 2m 平面；但机器人一边走一边转头，depth frame 晚了 15ms，IMU 姿态用的是另一个时刻的数据，点云投到 base_link 坐标系时就会产生空间偏差。这个偏差在 RViz 里可能只是边缘发毛，在避障算法里可能就是“桌腿宽了一圈”或者“地面高度浮起来了”。

所以国产替代不是说“我也有 IMU”。客户要看的是：depth、RGB、IMU 是否硬件同步；timestamp 是不是同一个 clock domain；ROS topic 到达时间 jitter 多大；长时间运行后时钟漂不漂；外参标定能不能固化到出厂文件里；固件升级后这些标定参数会不会变。

这类细节不够硬，客户不会签字。因为出了问题以后，很难解释到底是相机、IMU、驱动、USB、ROS、SLAM 还是运动控制的问题。

### 05 双目相机最怕的不是精度不够，而是批量标定漂

D435i 的 D430 模组 baseline 是 **50mm**。这个 50mm 看起来只是一个机械尺寸，但对双目深度非常关键。双目测距本质上依赖 baseline、焦距和视差，任何一个量漂了，深度尺度都会漂。

这就是双目相机比普通 RGB 相机难的地方。普通摄像头镜头稍微有点畸变，很多应用还能靠 ISP 或后端算法兜住。但双目不行，左右目相对位置、镜头畸变、极线关系、IR 投射器位置、RGB-depth 外参、IMU 外参，只要一个漂，最后输出的不是“图像不好看”，而是“距离不可信”。

国产替代最容易低估的是批量一致性。一个样品测得好，不代表 1000 台都好。结构件热胀冷缩、镜头座应力、胶水固化、跌落振动、长期温升，都可能让外参慢慢漂。相机开机前 5 分钟测得准，不代表连续运行 4 小时后还准。

Gemini 330 系列往工程化方向走，比如 IP65、GMSL2、FAKRA、PoE/M12，这些都是对的。但客户在 G1 这种机器人上要看的不是“有没有防护等级”，而是这套防护结构、镜头结构、模组结构在振动和温漂下会不会影响内外参。

这也是为什么很多国产方案参数看起来能打，但客户替换慢。不是客户看不懂参数，而是客户知道深度相机真正出问题时，往往不是规格书里的典型值，而是装配、温漂、标定、时间同步这些脏细节。

### 06 国产没有完全替掉的，不是单点参数，而是失败模式的可预测性

深度视觉最难测的不是标准平面，而是烂场景。白墙、黑色桌腿、玻璃门、反光地砖、阳光直射、暗光走廊、毛绒物体、斜坡边缘，这些才是机器人现场会遇到的东西。

主动双目靠 IR 投射器给低纹理场景增加纹理，但强光下红外纹理会被淹没，黑色材料会吸收红外，反光材料会制造错误匹配。ToF 可以直接测飞行时间，但会遇到多径反射、强光、边缘 mixed pixel、黑色吸光材料等问题。结构光近距离精度好，但在室外强光和运动平台上也有短板。

所以深度视觉没有万能路线。D435i 的优势不是每个场景都最好，而是它的失败模式被大量开发者摸过。大家知道它在白墙上会怎样，在反光地面上会怎样，在 USB 带宽不够时会怎样，在 ROS 里 topic 掉帧怎么查。

国产方案要替掉它，必须让客户知道：你什么时候会坏，坏成什么样，坏了以后后端算法怎么识别。这个比平均误差更重要。

比如一张深度图里，少几个点不可怕；可怕的是错误深度点很自信地出现在障碍物边缘。后端避障算法可能会把一片反光误认为墙，也可能把黑色桌腿漏掉。对人形机器人来说，深度视觉不是拍照，它是安全链路的一部分。

### 07 奥比最有机会，但它要替的不是 D435i 参数，而是 RealSense 生态

国产玩家里，奥比中光是最接近直接对标 RealSense 的。原因不是它型号多，而是它确实在做深度 ASIC、SDK、机器人接口和工程化产品线。Gemini 330 系列里的 MX6800 深度引擎，是国产替代必须走的一步；Gemini 335Lg 的 GMSL2/FAKRA、Gemini 335Le 的 PoE/M12，则是在补机器人量产里的线缆、抗振、供电和工业连接问题。

但奥比真正要打赢的不是 D435i 的单项参数，而是 RealSense 的默认生态。RealSense 有 librealsense，有 ROS 驱动，有大量开源案例，有大量算法工程师踩过坑。国产 SDK 即使写得好，客户也会问一句：我现有代码改多少？

这句话很现实。机器人公司不是相机评测机构，它不会为了替换一个深度相机，把 SLAM、避障、标定、日志、运维全部重写一遍。国产方案最需要提供的不是“我比 D435i 参数更强”，而是“你原来用 D435i 的地方，我能用最小代价换上去”。

所以未来谁能替掉 D435i，谁就必须同时补四件事：相机端深度 ASIC、稳定标定体系、ROS/Isaac 生态兼容、现场 FAE 闭环能力。少一件，都可能卡在客户验收表上。

### 08 图漾、海康、光鉴的机会不一样，不应该混在一起看

图漾科技更偏工业 3D 视觉。它的优势不是直接复刻 RealSense，而是在工业检测、机器人引导、测量类场景里积累了很多工程经验。这样的公司如果切入人形机器人，优势会在标定、工业可靠性和场景交付，但要补的可能是小体积头部模块、ROS 开发者生态和动态运动场景。

海康机器人强在工业视觉渠道、工程交付和客户服务体系。深度视觉国产替代最后不是只有芯片工程师打仗，现场 FAE、应用工程、工业客户验证都很重要。海康这类公司如果做机器人 3D 视觉，优势是能把复杂项目落地，但未必天然最像 D435i 这种开发者默认件。

光鉴这类更底层的 3D sensing 公司，潜力在芯片和传感路线，比如 ToF、SPAD、深度计算、传感器融合。但要进人形机器人头部，它要解决的不只是芯片指标，还包括强光、多径、黑色物体、边缘 mixed pixel、功耗、体积和生态接入。

所以国产深度视觉不是一个赛道。**奥比更像“RealSense 替代者”，图漾更像“工业 3D 视觉工程派”，海康更像“交付体系派”，光鉴更像“底层芯片路线派”**。最后谁能进 G1 这种机器人头部，不一定取决于谁单项参数最强，而取决于谁能把算法链路和验收责任一起接住。

### 09 真正的验收表，不会只测 2m 白墙

如果我在客户现场验证一颗国产深度视觉模块，绝不会只看宣传页参数。

第一组一定是静态精度：0.3m、0.5m、1m、2m、3m、5m，各距离测中心区和 80% FOV 区域的 Z accuracy、RMS noise、fill rate 和边缘 flying pixels。只测中心点没有意义，因为边缘畸变和匹配错误最容易藏问题。

第二组是动态同步。把相机装到机器人头部或六轴平台上，模拟走路摆头，记录 depth frame、RGB frame、IMU frame 的 timestamp，再看 ROS 端到端延迟和 jitter。静态白墙测得再准，时间戳不稳，机器人一动就会露馅。

第三组是烂场景。白墙、黑布、桌腿、玻璃门、反光地砖、强光、暗光、毛绒物体，每个场景不只看有没有深度图，还要看错误点云会不会骗过后端算法。深度视觉最怕的不是空洞，而是错误深度点看起来很像真的。

第四组是热稳定和批量一致性。连续跑 8 小时，记录机身温度、深度尺度漂移、RGB-depth 外参漂移、IMU bias 变化。再换 30 台样机重复测，看批间差异。很多国产样品的问题不是一台不行，而是一台很好，十台开始散。

第五组是软件链路。SDK API、ROS driver、Isaac ROS 支持、固件升级、异常日志、掉线恢复、参数保存、标定工具、现场定位文档，这些都要测。客户最后签的不是“参数可用”，而是“出了问题有人能解释”。

### 10 为什么激光雷达能国产，深度视觉反而还要等一等

G1 头部的 Livox MID-360 是国产，这说明中国机器人传感器不是整体弱。激光雷达这几年国产化推进很快，是因为它的数据形态相对清楚：点云、距离、反射强度、扫描频率、视场角。客户替换时当然也要验证，但后端接口和数据语义相对直接。

深度视觉更麻烦。它既是传感器，又是算法前端；既输出深度图，又绑定 RGB、IMU、SDK、ROS、标定文件、滤波行为和失败模式。一个机器人团队用 D435i 两年，算法里可能到处都是围绕 RealSense 行为调出来的经验参数。

这就是为什么国产替代在深度视觉上会慢一点。不是因为硬件做不到，而是因为它牵着一整条 perception pipeline。你换掉 D435i，不是换一个 BOM，而是在动机器人“怎么看世界”的底层假设。

宇树 G1 头部的深度视觉芯片为什么还不是中国造？最准确的答案不是“国产没有”，而是国产还没有在这类人形机器人头部位置上，完全替掉 RealSense 的系统确定性。

奥比 Gemini 330 系列已经很接近，它有 MX6800，有 Gemini 335/336，有 335Lg 的 GMSL2，有 335Le 的 PoE/M12，也开始对接机器人生态。图漾、海康、光鉴也都有各自路线。但要真正替掉 D435i，还要跨过几道硬门槛：高分辨率高帧率下的低延迟深度 ASIC，depth/RGB/IMU 的硬同步，批量标定一致性，复杂场景失败模式，ROS/Isaac 生态迁移成本，以及现场问题闭环能力。

所以这件事最后不是谁能做出深度相机，而是谁能把深度相机做成机器人公司敢默认使用的标准件。

参数追上，只是第一步。

让客户换上去以后不用重写系统，才是国产深度视觉芯片真正进 G1 这类机器人的那道门。
