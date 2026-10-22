---
title: "Anthropic"
wiki: true
wiki_type: "company"
wiki_rank: 37
seed_count: 5
lastmod: "2026-10-22"
description: "Anthropic 是公益公司，做 Claude 与 Claude Code，并维护开放协议 MCP（文档版本 2026-07-28），把外部输入变成可指认的接口。"
official_url: "https://www.anthropic.com/company"
wiki_category: "工程资料与人工智能工具"
related_models: []
---

Anthropic 与编码器没有产品关系，它在这个站的位置与 OpenAI 同类：工程资料的读写工具。差别在于它把"模型如何接外部系统"做成了一个公开协议（MCP），这对工程场景的意义比模型本身的分数更具体——手册、测试数据、本地脚本可以按同一套接口挂进去。

## 公司与品牌

官网自述为公益公司（public benefit corporation），目标写作"确保 AI 的收益、降低其风险"，并把要建的系统描述成"可靠、可解释、可操控"的前沿模型；组织按研究、政策、产品、运营四块分工。[公司页](https://www.anthropic.com/company)

产品线上，Claude 是通用入口，[Claude Code](https://www.anthropic.com/claude-code) 是面向工程任务的编码代理，官网标题直接写"AI 编码代理，终端与 IDE"。[Claude](https://www.anthropic.com/claude)

## MCP 是它公开的那一层接口

MCP（Model Context Protocol）官方文档的定位是"把 AI 应用接到外部系统的开源标准"：通过它，模型可以连数据源（本地文件、数据库）、工具（搜索引擎、计算器）与工作流，文档用"AI 应用的 USB-C 接口"来打比方；并写明 Claude 与 ChatGPT 都能用这套协议。[MCP 文档](https://modelcontextprotocol.io/docs/getting-started/intro)

对工程场景，这一层的用处是可指认的：把一份厂商手册目录挂成数据源，把一段解析脚本挂成工具，模型调用的每一步都能落在具体文件上，而不是凭记忆生成。文档当前版本标注 2026-07-28。

## 在编码器链上的位置

它不在链上任何一格：不产器件、不做测量、不提供接口。可用的位置只有三处，且都在"资料已经到手之后"：手册与专利的抽取、跨型号差异的比对、测试脚本与报告的生成。这三件事的产出必须能回到原文链接，否则不能进选型记录。

## 公开资料的边界

官网不给模型的训练数据、参数规模与具体版本的评测细节（这些分散在研究页与发布说明，且随版本变），不给商业条款与报价。模型对"官网没写的精度指标"会给出看似合理的补值——这是使用这类工具时最需要在流程上拦住的一点：凡是数字，必须能指到来源页。

## 官方资料

- [Anthropic 公司页](https://www.anthropic.com/company)
- [Claude](https://www.anthropic.com/claude)
- [Claude Code](https://www.anthropic.com/claude-code)
- [新闻与发布](https://www.anthropic.com/news)
- [MCP 文档：什么是 MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
- [MCP 首页](https://modelcontextprotocol.io/)
