---
title: "EPFL"
wiki: true
wiki_type: "company"
wiki_rank: 57
seed_count: 3
lastmod: "2026-10-22"
description: "洛桑联邦理工（EPFL）1853 年建校、1969 年改现名，设 ENAC、SB、STI、IC、SV 与 CDM，官网称机器人中心有 25 个实验室。"
official_url: "https://www.epfl.ch/about/"
wiki_category: "研究、原型与产品化"
related_models: []
---

EPFL 不是供应商，在编码器链上的位置是"指标第一次被写出来的地方"：论文与学位论文里给出测量原理、误差模型与实验数据，比产品手册更早、也更具体。看它的价值是拿到原始定义——同一个"精度"，实验室写的是标准差还是峰峰值，决定了后面所有比较是否成立。

## 公司与品牌

洛桑联邦理工学院（École Polytechnique Fédérale de Lausanne），官网历史页写明：1853 年成立时名为 École Spéciale de Lausanne，1969 年改为现名。校址在瑞士洛桑，治理结构由校务委员会（Direction）、学院（Schools）、中心（Colleges）、教师与员工代表机构组成。[组织与身份](https://www.epfl.ch/about/overview/)

学院分五块加一个管理技术学院：ENAC（建筑土木环境）、SB（基础科学）、STI（工程）、IC（计算机与通信）、SV（生命科学）、CDM（管理技术）。2025–2028 发展计划把重点写作健康、气候与数字技术三条。[工程学院 STI](https://sti.epfl.ch/)；[教育入口](https://www.epfl.ch/education/)

## 与角度测量相关的公开研究面

| 入口 | 官方公开的描述 | 与编码器/位置测量的关系 |
| --- | --- | --- |
| [机器人中心](https://www.epfl.ch/research/domains/robotics/) | 连接实验室、研究者、学生、初创与工业伙伴，页面写"25 个机器人实验室"，并自称欧洲第一 | 关节与末端执行器的原型多用现成编码器，论文会写清装了哪一类、几颗 |
| STI 工程学院 | 机械、微技术、材料与电气的教学科研集合 | 敏感元件、MEMS 与精密机构的研究常落在这一侧 |
| [创新与技术转移](https://www.epfl.ch/innovation/) | 从实验室到市场的通道，含初创与产业合作 | 论文里的原理后来变成公司产品的路径 |
| [教育](https://www.epfl.ch/education/) | 本科、硕士、博士与继续教育 | 学位论文常是唯一公开的实验细节来源 |

## 在编码器链上的位置

它在上游：提出原理、做原型、给误差模型，不承担量产与认证。这条边界很实用——论文里"0.1° 精度"通常是特定台架、特定温度、特定校准流程下的结果，不能直接搬到工业现场；反过来，厂商手册里的 ±角秒也不会告诉你测试方法与样本数。两边对照，才知道某个数字是在什么条件下成立的。

另一个容易搞错的地方是归属：瑞士两所联邦理工的分工与专利归属常被混写，看到"某专利属于 EPFL"时，要去专利页核对申请人，而不是按作者单位推。

EPFL 不公开任何器件 BOM、供应商选择与采购信息；实验室页面给研究方向与人员，不给器材清单。论文里的器件型号有时写、有时以"商用编码器"带过。

## 官方资料

- [EPFL 官网](https://www.epfl.ch/)
- [组织与身份](https://www.epfl.ch/about/overview/)
- [EPFL 机器人中心](https://www.epfl.ch/research/domains/robotics/)
- [工程学院 STI](https://sti.epfl.ch/)
- [创新与技术转移](https://www.epfl.ch/innovation/)
- [教育](https://www.epfl.ch/education/)
