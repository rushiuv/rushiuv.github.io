---
title: "雷赛"
wiki: true
wiki_type: "company"
wiki_rank: 54
seed_count: 4
lastmod: "2026-11-05"
description: "雷赛智能（Leadshine）以步进与伺服驱动为主业，EL8 伺服驱动给差分 ABZ 加 OCZ 并支持第二编码器，配套 ELM2 电机用 23 位光学绝对值编码器。"
official_url: "https://www.leadshine.com/"
wiki_category: "驱动、控制与系统配套"
related_models: []
---

雷赛站在“驱动 + 电机”这一层，产品结构是从步进起家、往闭环与伺服上走。它在编码器链上的价值有两处：一是把编码器接口写进了驱动器的公开卖点清单（差分 ABZ、第二编码器），这类信息在国产驱动厂里不算常见；二是它同时卖闭环步进与一体化伺服，等于把“编码器从可选件变标准件”这条路径展示了一遍。读它的资料，最该看的是驱动器接口表与电机反馈档位，而不是营销页里的精度形容。

## 从步进驱动做到伺服与机器人部件

官网把产品分成 Fieldbus Products（EtherCAT、EtherNet/IP、CANopen、Modbus RTU 四条总线各自列驱动器）、Stepper Products（步进电机、步进驱动、一体机）、Closed Loop Steppers（闭环步进电机、闭环步进驱动、一体机）、Servo Products（伺服电机、伺服驱动、一体化伺服）、Controls（PLC 的 MC500 与 S 系列、远程 IO 的 R2 与 R3、HMI 的 LT2000）、Robot Components（无框电机 FM2、一体化执行器 HJ2 与 PJ3、灵巧手 DH116、DH2116、DH116S）、Other Products（电源 LSP 与 SPS、减速机 PLF）。[官网产品目录](https://www.leadshine.com/)

站点分全球英文、简体中文与日文三套，产品命名一致但页面分属不同路径，查中文资料要认准 `leadshine.com` 下的分类页。配件类目里单独列了 Motor Cables、Encoder Cables、Brake Cables、Tuning Cables、Communication Cables——**编码器线缆被当成一个独立品类卖**，这是判断一家驱动厂把编码器当附件还是当系统件的一个侧面。[伺服产品分类](https://www.leadshine.com/products/servo.html)

## 编码器相关产品线与公开规格

| 系列 | 类型 | 公开分辨率与编码器接口 | 其他公开参数 |
| --- | --- | --- | --- |
| [EL8 系列伺服驱动](https://www.leadshine.com/products/servo/servo-drive/el8-series.html) | 驱动器 | 编码器侧给差分 ABZ 与 OCZ 输出，支持接入第二个编码器 | 频响最高 3.5 kHz（上一代 3.2 kHz）、STO SIL3、400–2000 W |
| [EL8-EC 与 EL8-RS 子型号](https://www.leadshine.com/products/servo/servo-drive/el8-series.html) | 驱动器 | 同一平台，接口能力按总线版本分档 | EL8-EC 为 8 入 3 出、2 模拟入 2 模拟出；EL8-RS 为 10 入（最高 4 MHz）、6 出 |
| [ELM2 交流伺服电机](https://www.leadshine.com/products/servo/servo-motor/elm2-series.html) | 电机 | 23 位光学绝对值编码器 | 50–7500 W、机座 40–180 mm、220 或 400 VAC、IP65 或 IP67 |
| [ELM1 交流伺服电机](https://www.leadshine.com/products/servo/servo-motor/elm2-series.html) | 电机 | 系列页未单列编码器档位，作 EL8 的配套 | 与 ELM2 并列在伺服电机目录下 |
| [ELD2 等系列伺服驱动](https://www.leadshine.com/products/servo/servo-drive/eld2-series.html) | 驱动器 | 系列页未公开编码器接口细节 | 与 EL7、EL6、ELD3 同列，覆盖不同功率与总线 |
| [iSV2-RS 一体化伺服](https://www.leadshine.com/products/servo/integrated-servo-motor/isv2-rs-series.html) | 驱动与电机同体 | 反馈内置，官网未公开位数 | 分 CAN 与 RS485 两个版本 |
| [编码器线缆](https://www.leadshine.com/products/servo.html) | 配件 | 官网把编码器线缆单列为配件品类 | 与电机、刹车、调试、通信线缆并列 |
| [B23M-C 整体式光编](https://www.leisai.com/product/product_details_1172.html?cid=M001173) | 编码器整机（中文站单列） | 绝对值旋转编码器，单圈 23 位、多圈 16 位 | 重复定位精度 <±3 角秒；RS485；弹片连接；直轴与锥轴 |
| [分体光编 B25M / B23M / B23MP](https://www.leisai.com/product/product_details_1113.html?cid=M001114) | 编码器整机（中文站单列） | 单圈 23～25 位、多圈 16 位 | B25M 机身厚 14.9 mm、重复定位精度 <±3 角秒；通信线缆最长 50 m |
| [分体磁编 M23M / M17M / M17MP](https://www.leisai.com/product/product_details_1101.html?cid=M001101) | 编码器整机（中文站单列） | 单圈 23 位或 17 位、多圈 16 位 | RS485、2.5/5 Mbps；通信线缆最长 50 m |

表里最值得记住的一条是 EL8 的“支持第二编码器”。这意味着驱动器有两路反馈入口：一路接电机内置的 23 位绝对值件做换相与速度环，另一路留给人接外置光栅、磁栅或负载端的独立编码器做全闭环。对做反馈件的一方，这是一条明确的落点——不必挤进电机内部，从第二编码器入口进去同样能参与控制，但要接受驱动器侧的协议与采样节拍。

另外 EL8 明确写“可选配 23 位磁或光学的电机”，这句把磁与光放在同一档位上：磁编在伺服电机侧已经能进 23 位这一层，不再只是低速或低成本场合的替代品。这是官网自己的配置口径，不是精度比较结论。

产品页给的是系列级的卖点参数（功率段、机座、防护等级、总线类型、频响），不是选型表。各订货号上的编码器分辨率分档、绝对精度（分体光编只给到重复定位精度）、ABZ 输出的最高频率与线缆长度上限、第二编码器的采样延时与同步方式、各总线下的最小控制周期，以及闭环步进用的编码器线数与细分，都在对应型号的手册里。

## 在编码器链上的位置

雷赛两头都占：它既采购编码器或其中的敏感元件装进 ELM 系列电机与一体化伺服里，也在中文站（leisai.com）把整体式光编、分体光编、分体磁编三组编码器作为独立品类对外销售——这与英文站（leadshine.com）只列电机、驱动器、机器人部件的目录结构不同，查中文产品要认 leisai.com，查英文站会看不到编码器整机。所以它的公开页能给三类信息——电机侧装了哪一档反馈（23 位光学绝对值），编码器侧自己卖到哪一档（光编 23～25 位、磁编 17～23 位，多圈均为 16 位），驱动器侧能接哪种信号（差分 ABZ 加 OCZ、第二编码器）。编码器供应商与内置件是自制还是外购，官网没有对应的公开条目。

真正决定选型的人在两头：整机厂的电气工程师按总线与 IO 选驱动器型号，机械工程师按安装尺寸选电机；编码器在中间跟着电机型号走。要在雷赛这条线上替换编码器，先过驱动器协议，再过电机轴端结构，最后才是精度。

## 官方资料

- [雷赛官网产品目录](https://www.leadshine.com/)
- [伺服产品分类页](https://www.leadshine.com/products/servo.html)
- [EL8 系列伺服驱动](https://www.leadshine.com/products/servo/servo-drive/el8-series.html)
- [ELM2 系列交流伺服电机](https://www.leadshine.com/products/servo/servo-motor/elm2-series.html)
- [ELD2 系列伺服驱动](https://www.leadshine.com/products/servo/servo-drive/eld2-series.html)
- [iSV2-RS 一体化伺服](https://www.leadshine.com/products/servo/integrated-servo-motor/isv2-rs-series.html)
- [整体式光电系列 B23M-C](https://www.leisai.com/product/product_details_1172.html?cid=M001173)
- [分体光电系列绝对值旋转编码器](https://www.leisai.com/product/product_details_1113.html?cid=M001114)
- [分体磁电系列绝对值旋转编码器](https://www.leisai.com/product/product_details_1101.html?cid=M001101)
