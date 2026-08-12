# KieranHoward · 个人主页 / Personal Homepage

> **中文** · **English** — 一个把「金融 × AI × 吉他」并置在同一页里的双面个人站点。
> A single-page personal site that places *Finance × AI × Guitar* side by side.

![Vanilla](https://img.shields.io/badge/Stack-Vanilla%20HTML%2FCSS%2FJS-58a6ff) ![Zero Deps](https://img.shields.io/badge/Dependencies-None-3fb950) ![Dark](https://img.shields.io/badge/Theme-Dark%20%2F%20Light-f0883e) ![Responsive](https://img.shields.io/badge/Responsive-375px%E2%86%92%E2%88%9E-a371f7) ![Offline](https://img.shields.io/badge/Offline-Single%20File-58a6ff)

---

## 项目概览 · Overview

**中文** — 不是一份普通的名片网页，而是一个可以双击打开、离线运行、又能讲清楚「我是谁」的小作品。整站只有一个 `index.html`：所有样式写在 `<style>`、所有逻辑写在 `<script>`，没有任何框架、打包器或外部资源；五张图片全部以 base64 内联，因此完全离线、双击即开。

**English** — Not just another business-card page, but a small, offline-runnable artifact that actually explains who I am. The whole site is a single `index.html`: all styles in `<style>`, all logic in `<script>`, with no framework, bundler, or external asset. Five images are inlined as base64, so it runs fully offline and opens with a double-click.

### 双面结构 · Two Sides

| | 中文 | English |
|---|---|---|
| **🅰️ A 面 · 专业** | 人大财金金融工程的底色：券商实习、美赛 / 创新杯、心镜 Mind·Mirror AI 智能体。 | Roots in Finance Engineering at RUC: research internships, MCM / innovation awards, the Mind·Mirror AI agent. |
| **🅱️ B 面 · 生活** | 極爱乐队（JIAI）主笔与吉他手，自运营乐队公众号、吉他视频号。 | Lead writer & guitarist of JIAI band; runs its official account and a guitar video channel. |
| **🌗 日夜双模** | 右上角按钮切换，偏好写入 localStorage。 | Top-right toggle; choice persisted in localStorage. |
| **🧭 锚点导航** | Hero 双胶囊平滑滚到 A / B。 | Hero pills smooth-scroll to A / B. |

---

## 为什么是「双面」 · Why Two-Sided

**中文** — 简历讲「我做了什么」，爱好讲「我热爱什么」，硬塞进一个模版两边都失真。于是用**反差**：A 区冷色深海蓝 + 系统衬线，像克制在线 CV；B 区暖橙 Glassmorphism，像被阳光照亮的仪表盘。冷与暖在同一屏对望，比「统一风格」更真实。

**English** — A résumé says what I did; a hobby says what I love. Forcing both into one template flattens each. So I leaned into **contrast**: Side A is cool ocean-blue with serif — a restrained CV; Side B is warm-orange Glassmorphism — a sunlit dashboard. They describe “me” more honestly than any single style.

---

## 功能特性 · Features

- 📄 **单文件离线 / Single-file offline** — 一个 index.html 含全部内容，无服务器、无网络、无依赖。
- 🌗 **日夜模式 / Day & Night** — 右上角按钮切换，localStorage 记忆，连续点击稳定。
- 📱 **响应式 / Responsive** — 桌面双栏，375px 窄屏自动堆叠，无横向滚动。
- 🧊 **玻璃质感 / Glassmorphism** — `backdrop-filter` 半透明卡片，日夜间都看得出层次。
- 🪪 **媒体卡片 / Media cards** — 公众号 / 视频号双卡，头像 + 二维码 base64 内联，附外链。
- 🔒 **隐私优先 / Privacy-first** — 不放真名、手机号、邮箱、Token、学号。

---

## 技术栈与约束 · Tech & Constraints

| 维度 Aspect | 实现 Implementation |
|---|---|
| 语言 Language | 原生 HTML + CSS + JavaScript |
| 框架 Framework | 无（不依赖 React / Vue / Tailwind） |
| 外部资源 External | 无外部图片 / 字体 / 库；图片 base64 内联 |
| 主题 Theming | CSS 变量 + `body.dark` 切换 |
| 持久化 Persist | localStorage 记忆日夜偏好 |
| 字体 Fonts | 系统栈：PingFang/雅黑 + Georgia 衬线 |
| 构建 Build | `build.py` 注入 base64，一键重生成 |

---

## 页面结构 · Page Structure

```
index.html  (≈ 1 MB, 单文件)
├─ Hero           昵称 · 副标题 · 4 标签 · A/B 锚点导航
├─ Zone A · 专业  (深海蓝)
│  ├─ 成长：我的简历（教育/技能 ↔ 心镜 AI 主卡）
│  ├─ 项目荣誉 · 截至 2026/07（3 奖项 badge）
│  ├─ 3 项竞赛卡（美赛 / 创新杯 / 求是）
│  ├─ 券商实习时间轴（中信 / 国泰海通）
│  └─ 学工一行
├─ 渐变分界        深海蓝 → 蜜橙
└─ Zone B · 生活  (蜜橙玻璃)
   ├─ 極爱乐队主卡（logo / JIAI / 5 栏目 / 5 成员）
   ├─ 乐队海报 + 意象云
   └─ 公众号 / 视频号 双媒体卡（二维码 base64）
```

---

## 快速开始 · Quick Start

**中文** — 下载仓库后，**双击 `index.html`** 即可在浏览器打开，无需服务器、联网或安装。改内容：所有素材与文案由 `build.py` 注入，运行一条命令重生成：

```bash
python build.py   # 重新生成 index.html（注入 base64 图片）
```

**English** — After cloning, **double-click `index.html`** to open in a browser — no server, network, or install needed. To edit: all assets and copy are injected by `build.py`; regenerate with:

```bash
python build.py   # regenerate index.html (injects base64 images)
```

---

## 设计背后的思考 · Design Notes

- **玻璃感在两种底色上都成立**：卡片底色用半透明白、叠在暖橙渐变上，再配暖色低透明度阴影——亮背景不“飘”，暗背景不“脏”。
- **1:1 篇幅控制**：用「单页滚动分区」而非「左右双栏常驻」，移动端堆叠更稳，也更易满足“窄屏无横向滚动”。
- **公众号 / 视频号展示**：5 张素材全部 base64 内联；视频号无公开网页 embed，做成「封面 + 标题 + 跳转链接」。
- **奖项标注时间戳**：心镜项目下抽“项目荣誉 · 截至 2026/07”，浅蓝背景 + 深海蓝竖条包住 3 个奖项，比纯胶囊更有“被认证”感。

*Glass works on both backgrounds · 1:1 held via zoning · accounts shown via inlined base64 · awards stamped with a date for credibility.*

---

## 未来计划 · Roadmap

- 🎸 吉他历程板块：补学琴年限、主攻风格与音乐偶像（已预留位置，未编造）。
- 🎬 视频号封面：为 3 条视频抓取封面，卡片升级为「封面 + 标题」。
- 📷 真人中页照片（可选）：如接受，加入一张职业/乐队照。
- 🌐 双语站点：把 `index.html` 文案也做成 CN/EN 切换。

---

## 隐私与边界 · Privacy & Boundaries

> ⚠️ 本页不展示真名、手机号、邮箱、API Key、Token 或学号。对外统一以「主笔 · Kieran Howard」呈现，学校与专业作为背景标签保留。仓库中同样不含上述敏感信息。
>
> ⚠️ This page shows no real name, phone, email, API keys, tokens, or student ID. It presents “Lead writer · Kieran Howard” externally; school and major are kept as background tags only. The repo contains none of the above.

---

*KieranHoward · 个人主页 — 用一支笔，写理性与感性。 / one pen for reason and feeling.*
