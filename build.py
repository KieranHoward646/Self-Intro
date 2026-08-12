"""一次性生成 index.html（单文件、内联 CSS/JS、base64 图片、双面反差+玻璃感）。"""
import base64
from pathlib import Path

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"


def b64(name: str) -> str:
    return base64.b64encode((ASSETS / name).read_bytes()).decode()


LOGO = b64("band-logo.jpg")
POSTER = b64("band-poster.jpg")
GZH_AVATAR = b64("gzh-avatar.jpg")
GZH_QR = b64("gzh-qr.jpg")
VIDEO_AVATAR = b64("video-avatar.jpg")

CSS = r"""
:root {
  --bg-page: #FBE5D4;
  --text: #2B2118;
  --text-soft: #8A7B6B;
  --a-bg: linear-gradient(135deg, #E6F1FB 0%, #C7DCF0 100%);
  --a-card-bg: rgba(255,255,255,0.78);
  --a-accent: #185FA5;
  --a-text: #0C447C;
  --b-bg: radial-gradient(120% 80% at 80% 100%, #EFA980 0%, #F4C9A8 45%, #FBE5D4 100%);
  --b-card-bg: rgba(255,255,255,0.55);
  --b-card-border: rgba(255,255,255,0.85);
  --b-accent: #F08A5D;
  --b-text: #633806;
  --border: rgba(0,0,0,0.08);
  --shadow: 0 6px 28px rgba(240,138,93,0.14);
}
body.dark {
  --bg-page: #1A1410;
  --text: #F0E6DA;
  --text-soft: #B8A89B;
  --a-bg: linear-gradient(135deg, #042C53 0%, #0C447C 100%);
  --a-card-bg: rgba(255,255,255,0.07);
  --a-text: #B5D4F4;
  --b-bg: radial-gradient(120% 80% at 80% 100%, #5C3A20 0%, #3B2418 45%, #1A1410 100%);
  --b-card-bg: rgba(255,255,255,0.06);
  --b-card-border: rgba(255,255,255,0.12);
  --b-text: #FAC775;
  --border: rgba(255,255,255,0.12);
  --shadow: 0 6px 28px rgba(0,0,0,0.45);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
html, body { margin: 0; padding: 0; }
body {
  font-family: system-ui, -apple-system, "PingFang SC", "Microsoft YaHei", "Hiragino Sans GB", sans-serif;
  color: var(--text);
  background: var(--bg-page);
  line-height: 1.6;
  overflow-x: hidden;
  transition: background 0.4s ease, color 0.3s ease;
}
.serif { font-family: Georgia, "Times New Roman", "Songti SC", "SimSun", serif; }
.container { max-width: 1100px; margin: 0 auto; padding: 0 24px; }

/* 日夜按钮 */
.theme-toggle {
  position: fixed; top: 20px; right: 20px; z-index: 100;
  width: 52px; height: 52px; border-radius: 50%;
  border: 1px solid var(--border); background: var(--b-card-bg);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  color: var(--b-text); font-size: 14px; font-weight: 500;
  cursor: pointer; box-shadow: var(--shadow);
  display: flex; align-items: center; justify-content: center;
  transition: transform 0.2s ease, background 0.3s ease;
}
.theme-toggle:hover { transform: scale(1.06); }
.theme-toggle:active { transform: scale(0.94); }

/* Hero */
.hero {
  min-height: 56vh; padding: 96px 0 64px;
  background: var(--b-bg);
  position: relative; overflow: hidden;
}
.hero::before {
  content: ""; position: absolute; inset: 0;
  background: radial-gradient(circle at 85% 90%, rgba(255,200,140,0.55) 0%, transparent 45%);
  pointer-events: none;
}
.hero-inner { position: relative; }
.hero h1 {
  font-family: Georgia, "Times New Roman", "Songti SC", "SimSun", serif;
  font-size: clamp(40px, 7vw, 72px); font-weight: 700;
  margin: 0 0 12px; letter-spacing: -0.02em;
  color: var(--text);
}
.hero .sub { font-size: clamp(15px, 1.8vw, 18px); color: var(--text-soft); margin: 0 0 24px; }
.hero .tag-row { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 8px; }
.tag {
  display: inline-block; padding: 6px 14px; border-radius: 999px;
  background: var(--b-card-bg); backdrop-filter: blur(8px);
  border: 1px solid var(--b-card-border);
  color: var(--b-text); font-size: 13px; font-weight: 500;
}

/* Hero 区导航跳转键 */
.nav-jump { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 26px; }
.nav-jump a {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 11px 22px; border-radius: 999px;
  text-decoration: none; font-size: 14px; font-weight: 600;
  color: #fff; box-shadow: var(--shadow);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.nav-jump a:hover { transform: translateY(-2px); }
.nav-jump a:active { transform: translateY(0); }
.nav-jump a.a { background: var(--a-accent); }
.nav-jump a.b { background: var(--b-accent); }
.nav-jump a .arrow { font-size: 16px; line-height: 1; }

/* 通用区块 */
.zone { padding: 80px 0; position: relative; }
.zone-a { background: var(--a-bg); color: var(--a-text); }
.zone-b { background: var(--b-bg); color: var(--b-text); }
.zone-label {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 13px; font-weight: 500;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--text-soft); margin-bottom: 12px;
}
.zone-title {
  font-family: Georgia, "Times New Roman", "Songti SC", serif;
  font-size: clamp(28px, 4vw, 42px); font-weight: 700;
  margin: 0 0 8px; letter-spacing: -0.01em;
}
.zone-tagline { font-size: 15px; margin: 0 0 32px; opacity: 0.85; }

/* 卡片网格 */
.grid-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }
.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }
.card {
  background: var(--a-card-bg);
  backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
  border: 1px solid var(--border);
  border-radius: 18px; padding: 24px;
  box-shadow: var(--shadow);
  transition: transform 0.25s ease;
}
.zone-b .card { background: var(--b-card-bg); border-color: var(--b-card-border); }
.card:hover { transform: translateY(-2px); }
.card h3 { margin: 0 0 8px; font-size: 17px; font-weight: 600; }
.card .meta { font-size: 12px; color: var(--text-soft); margin-bottom: 8px; }
.card .body { font-size: 14px; line-height: 1.7; }

/* A 区时间轴 */
.timeline { display: flex; flex-direction: column; gap: 14px; }
.timeline .item {
  display: grid; grid-template-columns: 110px 1fr; gap: 16px;
  padding: 14px 18px; border-radius: 14px;
  background: var(--a-card-bg); border: 1px solid var(--border);
  backdrop-filter: blur(10px);
}
.timeline .when { font-size: 13px; color: var(--a-text); font-weight: 600; }
.timeline .what b { display: block; font-size: 15px; margin-bottom: 4px; }
.timeline .what p { margin: 0; font-size: 13px; opacity: 0.85; }

/* A 区英雄项目 */
.hero-project {
  display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
  padding: 28px; border-radius: 20px;
  background: var(--a-card-bg); border: 1px solid var(--border);
  backdrop-filter: blur(14px); box-shadow: var(--shadow);
}
.hero-project h3 { font-family: Georgia, "Times New Roman", serif; font-size: 22px; margin: 0 0 10px; }
.hero-project .awards {
  margin-top: 16px; padding: 14px 16px; border-radius: 14px;
  background: rgba(24,95,165,0.09); border-left: 3px solid var(--a-accent);
}
body.dark .hero-project .awards { background: rgba(181,212,244,0.10); }
.hero-project .awards-label {
  font-size: 12px; font-weight: 600; color: var(--a-accent);
  letter-spacing: 0.05em; margin-bottom: 10px;
}
.hero-project .awards-list { display: flex; flex-wrap: wrap; gap: 8px; }
.hero-project .badge {
  padding: 6px 13px; border-radius: 999px;
  background: rgba(24,95,165,0.18); color: var(--a-text);
  font-size: 13px; font-weight: 600;
  border: 1px solid rgba(24,95,165,0.25);
}
body.dark .hero-project .badge { background: rgba(181,212,244,0.20); border-color: rgba(181,212,244,0.30); }

/* B 区乐队主卡 */
.band-main { display: grid; grid-template-columns: 1fr 1.2fr; gap: 28px; align-items: center; }
.band-main .logo-wrap {
  background: var(--b-card-bg); border: 1px solid var(--b-card-border);
  backdrop-filter: blur(14px); border-radius: 20px;
  padding: 24px; display: flex; align-items: center; justify-content: center;
}
.band-main .logo-wrap img { width: 100%; max-width: 260px; height: auto; }
.band-main .info h3 {
  font-family: Georgia, "Times New Roman", serif; font-size: 32px;
  margin: 0 0 6px; color: var(--text);
}
.band-main .info .romaji { font-size: 14px; color: var(--text-soft); margin-bottom: 16px; }
.band-main .info p { font-size: 14px; line-height: 1.75; margin: 0 0 10px; }

.band-poster {
  width: 100%; max-height: 320px; object-fit: cover;
  border-radius: 16px; margin-top: 24px;
  border: 1px solid var(--b-card-border);
}

/* 栏目 */
.columns { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; margin-top: 16px; }
.columns .col {
  padding: 10px 12px; border-radius: 12px;
  background: var(--b-card-bg); border: 1px solid var(--b-card-border);
  font-size: 12px; text-align: center; backdrop-filter: blur(8px);
}
.columns .col b { display: block; font-size: 13px; margin-bottom: 2px; }

/* 成员 */
.members { display: flex; flex-wrap: wrap; gap: 10px; }
.member {
  padding: 8px 14px; border-radius: 999px;
  background: var(--b-card-bg); border: 1px solid var(--b-card-border);
  font-size: 13px; backdrop-filter: blur(8px);
}
.member b { font-weight: 600; }

/* 意象云 */
.imagery { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 12px; }
.imagery span {
  padding: 4px 12px; border-radius: 999px;
  background: rgba(240,138,93,0.15); color: var(--b-text);
  font-size: 12px;
}
body.dark .imagery span { background: rgba(250,206,117,0.12); }

/* 公众号 / 视频号媒体双卡 */
.media-pair { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 32px; }
.media-card {
  background: var(--b-card-bg); border: 1px solid var(--b-card-border);
  backdrop-filter: blur(16px); border-radius: 20px; padding: 24px;
  box-shadow: var(--shadow);
}
.media-head { display: flex; align-items: center; gap: 14px; margin-bottom: 16px; }
.media-head img { width: 52px; height: 52px; border-radius: 50%; object-fit: cover; border: 2px solid var(--b-card-border); }
.media-head .name { font-weight: 600; font-size: 17px; }
.media-head .badge {
  display: inline-block; margin-left: 6px; padding: 2px 8px; border-radius: 999px;
  background: rgba(240,138,93,0.18); color: var(--b-text);
  font-size: 11px; font-weight: 500;
}
.media-head .desc { font-size: 13px; color: var(--text-soft); margin-top: 2px; }

.qr-wrap { display: flex; align-items: center; gap: 18px; margin-bottom: 16px; }
.qr-wrap img { width: 96px; height: 96px; border-radius: 10px; border: 1px solid var(--b-card-border); background: #fff; padding: 4px; }
.qr-wrap .tip { font-size: 12px; color: var(--text-soft); line-height: 1.6; }
.qr-wrap .tip b { color: var(--b-accent); }

.article-list { display: flex; flex-direction: column; gap: 8px; }
.article-list a {
  display: flex; align-items: center; justify-content: space-between;
  padding: 10px 14px; border-radius: 12px;
  background: var(--b-card-bg); border: 1px solid var(--b-card-border);
  color: var(--text); text-decoration: none; font-size: 13px;
  transition: background 0.2s ease;
}
.article-list a:hover { background: rgba(240,138,93,0.18); }
.article-list a span { opacity: 0.6; font-size: 11px; }

/* 分界 */
.divider {
  height: 2px; background: linear-gradient(90deg, var(--a-accent), var(--b-accent));
  margin: 0;
}

/* Footer */
.footer {
  padding: 48px 0; text-align: center;
  background: var(--b-bg); color: var(--b-text);
  font-size: 13px;
}
.footer p { margin: 6px 0; opacity: 0.85; }

/* 响应式 */
@media (max-width: 768px) {
  .grid-2, .grid-3, .band-main, .hero-project, .media-pair { grid-template-columns: 1fr; }
  .timeline .item { grid-template-columns: 1fr; gap: 6px; }
  .timeline .when { font-size: 12px; }
  .columns { grid-template-columns: repeat(2, 1fr); }
  .hero { min-height: 50vh; padding-top: 80px; }
  .zone { padding: 56px 0; }
  .container { padding: 0 18px; }
  .theme-toggle { top: 14px; right: 14px; width: 44px; height: 44px; font-size: 13px; }
}
@media (max-width: 380px) {
  .hero h1 { font-size: 36px; }
  .band-main .info h3 { font-size: 26px; }
  .qr-wrap { flex-direction: column; align-items: flex-start; }
  .qr-wrap img { width: 80px; height: 80px; }
}
"""

JS = r"""
(function () {
  var btn = document.getElementById('theme-toggle');
  var saved = null;
  try { saved = localStorage.getItem('kieran-theme'); } catch (e) {}
  if (saved === 'dark') document.body.classList.add('dark');
  function paint() {
    var isDark = document.body.classList.contains('dark');
    btn.textContent = isDark ? '\u2600 日' : '\u263E 夜';
    btn.setAttribute('aria-label', isDark ? '切换到日间模式' : '切换到夜间模式');
  }
  paint();
  btn.addEventListener('click', function () {
    document.body.classList.toggle('dark');
    var isDark = document.body.classList.contains('dark');
    try { localStorage.setItem('kieran-theme', isDark ? 'dark' : 'light'); } catch (e) {}
    paint();
  });
})();
"""

HTML = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>KieranHoward · 金融 × AI × 吉他</title>
<meta name="description" content="KieranHoward 的个人名片：A 专业（金融工程+AI），B 生活（極爱乐队与吉他）。" />
<style>{CSS}</style>
</head>
<body>

<button id="theme-toggle" class="theme-toggle" aria-label="切换主题">☾ 夜</button>

<!-- Hero -->
<header class="hero">
  <div class="container hero-inner">
    <div class="zone-label serif">A &nbsp;×&nbsp; B</div>
    <h1 class="serif">KieranHoward.</h1>
    <p class="sub">在 RUC 写诗、写代码，也写代码让机器读懂人心 ♡</p>
    <div class="tag-row">
      <span class="tag">人大财金 · 金融工程</span>
      <span class="tag">美赛 Finalist Top1%</span>
      <span class="tag">心镜 AI 智能体</span>
      <span class="tag">極爱乐队吉他手</span>
    </div>
    <div class="nav-jump">
      <a class="a" href="#zone-a"><span class="arrow">→</span> A 专业</a>
      <a class="b" href="#zone-b"><span class="arrow">→</span> B 生活</a>
    </div>
  </div>
</header>

<!-- A 区 · 专业 -->
<section class="zone zone-a" id="zone-a">
  <div class="container">
    <div class="zone-label">A · 专业</div>
    <h2 class="zone-title serif">成长：我的简历</h2>
    <p class="zone-tagline">从量化建模到 AI 智能体——把数据与代码当作理解世界的另一支笔。</p>

    <!-- 教育/技能 + 主理项目 -->
    <div class="hero-project">
      <div>
        <div class="meta">教育 / 技能</div>
        <h3 style="font-family:Georgia,serif;font-size:18px;margin:0 0 8px;">中国人民大学 · 财政金融学院</h3>
        <p style="margin:0;font-size:13px;line-height:1.7;">
          金融工程（本科）· 2028 届<br />
          2025 三好学生 · 2026 财政金融学院优秀共青团员<br />
          Python · Wind/iFind/Choice · Stata · LaTeX · PR/Au/PS<br />
          CET-4 630 · CET-6 552
        </p>
      </div>
      <div>
        <div class="meta">主理项目 · AI 方向</div>
        <h3 class="serif">心镜 Mind·Mirror</h3>
        <p style="margin:0 0 10px;font-size:14px;line-height:1.75;">
          心理健康多领域一站式引擎。基于神经网络的时序情绪识别，串联 C 端深度感知、个性疏导与预警，
          与高校 / 企业 B 端构建闭环商业模式，面向 AI 情绪陪伴、企业 EAP、ESG 市场。
        </p>
        <div class="awards">
          <div class="awards-label">项目荣誉 · 截至 2026/07</div>
          <div class="awards-list">
            <span class="badge">挑战杯 · 三等奖</span>
            <span class="badge">大创 · 国家级立项</span>
            <span class="badge">百融杯 · 三等奖</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 竞赛 -->
    <h3 class="serif" style="margin:36px 0 14px;font-size:20px;">竞赛荣誉</h3>
    <div class="grid-3">
      <div class="card">
        <div class="meta">2025/01 · 队长 · 编程+建模</div>
        <h3>美赛 MCM/ICM · Finalist</h3>
        <p class="body">特特奖提名 (Top 1%)。Lotka-Volterra + ESM 生态稳定性模型；AHP/EWM 多指标定权；python 爬虫 + odeint/Matplotlib 鲁棒性检验。</p>
      </div>
      <div class="card">
        <div class="meta">2026/04 · 论文第一作者</div>
        <h3>创新杯 · 特特等奖</h3>
        <p class="body">《"归零问效，以数证因"：零基预算改革的资源配置效应》——160 个地级市多期 DID、PSM-DID、IV、IW 估计量。</p>
      </div>
      <div class="card">
        <div class="meta">2025/05 · 北京市级立项</div>
        <h3>求是学术品牌 · 研究项目</h3>
        <p class="body">显性/隐性消费 + 以旧换新挤出效应框架；双重差分分析消费者异质性，问卷 + 政策可行性研究。</p>
      </div>
    </div>

    <!-- 实习 -->
    <h3 class="serif" style="margin:36px 0 14px;font-size:20px;">实习经历</h3>
    <div class="timeline">
      <div class="item">
        <div class="when">2025/05 → 2025/09</div>
        <div class="what">
          <b>国泰海通证券 · 研究所 · 机械组</b>
          <p>东华测试、凌云光首次覆盖报告；从经济业务 / 季度表现 / 债务承销 / 业务布局 / 风险提示拆解投资逻辑。</p>
        </div>
      </div>
      <div class="item">
        <div class="when">2024/12 → 2025/04</div>
        <div class="what">
          <b>中信证券 · 研究所 · 汽车组</b>
          <p>独立撰写车载 DRAM 深度研报；梳理智能驾驶 L0–L4 容量与方案；监测美光 / 三星 / 兆易创新动态。</p>
        </div>
      </div>
    </div>

    <p style="margin-top:24px;font-size:13px;opacity:0.8;">
      学工：中国人民大学财政金融学院学生会社会实践部负责人 · 2025 千村百巷强国大调研项目负责人。
    </p>
  </div>
</section>

<div class="divider"></div>

<!-- B 区 · 生活 -->
<section class="zone zone-b" id="zone-b">
  <div class="container">
    <div class="zone-label">B · 生活</div>
    <h2 class="zone-title serif">吉他 &nbsp;·&nbsp; 乐队 &nbsp;·&nbsp; 写"我们"</h2>
    <p class="zone-tagline">温柔的孤独 · 热烈的纯粹 —— 在暗调胶片里，把孤独唱成温柔。</p>

    <!-- 乐队主卡 -->
    <div class="band-main">
      <div class="logo-wrap">
        <img src="data:image/jpeg;base64,{LOGO}" alt="極爱乐队 logo" />
      </div>
      <div class="info">
        <div class="meta">校园乐队 · 2024.11 成立</div>
        <h3 class="serif">極爱乐队</h3>
        <div class="romaji">JIAI / Jiài · Kieran Howard 主笔</div>
        <p>从中国人民大学百团走出来的学生乐队，文艺抒情 × 现代摇滚双轨并行。</p>
        <p>5 大固定栏目：成员画像 → 演出记录 → 诗性独白 → 互动测试 → 纪念总结。</p>
        <div class="members">
          <span class="member"><b>Kieran Howard</b> · 主笔</span>
          <span class="member"><b>唐sir</b></span>
          <span class="member"><b>韵霏</b></span>
          <span class="member"><b>克憨</b></span>
          <span class="member"><b>DogBark</b></span>
        </div>
      </div>
    </div>

    <!-- 海报 -->
    <img class="band-poster" src="data:image/jpeg;base64,{POSTER}" alt="極爱乐队 海报" />

    <!-- 风格与意象 -->
    <h3 class="serif" style="margin:36px 0 6px;font-size:20px;">风格 · 意象 · 情绪光谱</h3>
    <p style="margin:0 0 8px;font-size:14px;line-height:1.7;">
      诗性长句跨语种（英文 / 俄文 / 古英文 thy · doth）+ 口语自嘲（"你这个笨蛋" "oi~" "doge"）双轨并行；
      以抒情承载叛逆，用温柔消解矫情。
    </p>
    <div class="columns">
      <div class="col"><b>温柔</b>★★★★★</div>
      <div class="col"><b>孤独</b>★★★★☆</div>
      <div class="col"><b>热烈</b>★★★★☆</div>
      <div class="col"><b>陪伴</b>★★★★☆</div>
      <div class="col"><b>自嘲</b>★★★☆☆</div>
    </div>
    <div class="imagery">
      <span>夏日</span><span>雨季</span><span>夜</span><span>月</span><span>海</span>
      <span>斑马线</span><span>站台</span><span>旷野</span><span>琥珀</span><span>胶片</span>
      <span>猫</span><span>灵魂</span><span>故事</span><span>释怀</span><span>重生</span>
    </div>

    <!-- 媒体双卡 -->
    <h3 class="serif" style="margin:44px 0 0;font-size:20px;">公众号 &nbsp;×&nbsp; 视频号</h3>
    <div class="media-pair">
      <!-- 公众号 -->
      <div class="media-card">
        <div class="media-head">
          <img src="data:image/jpeg;base64,{GZH_AVATAR}" alt="極爱乐队公众号头像" />
          <div>
            <div class="name">極爱乐队<span class="badge">公众号</span></div>
            <div class="desc">校园乐队官方发声地 · 18 个月纪念</div>
          </div>
        </div>
        <div class="qr-wrap">
          <img src="data:image/jpeg;base64,{GZH_QR}" alt="公众号二维码" />
          <div class="tip">
            <b>扫码关注</b><br />
            接收成员画像、演出记录、诗性独白与纪念总结。
          </div>
        </div>
        <div class="article-list">
          <a href="https://mp.weixin.qq.com/s/wwpekrD8zgvp7_s46uw2vg" target="_blank" rel="noopener">
            最近更新 · 一篇推文 <span>↗</span>
          </a>
        </div>
      </div>

      <!-- 视频号 -->
      <div class="media-card">
        <div class="media-head">
          <img src="data:image/jpeg;base64,{VIDEO_AVATAR}" alt="KieranHoward 视频号头像" />
          <div>
            <div class="name">KieranHoward<span class="badge">视频号</span></div>
            <div class="desc">吉他演奏与乐队日常</div>
          </div>
        </div>
        <p style="font-size:13px;line-height:1.7;margin:0 0 12px;">
          这里记录琴房里的练习片段、演出前后的即兴，还有偶尔的翻唱。
          在微信视频号搜索 <b style="color:var(--b-accent);">KieranHoward</b> 关注。
        </p>
        <div class="article-list">
          <a href="https://weixin.qq.com/sph/AVLn7gofc5" target="_blank" rel="noopener">视频 01 <span>↗</span></a>
          <a href="https://weixin.qq.com/sph/ASRfJiPkGL" target="_blank" rel="noopener">视频 02 <span>↗</span></a>
          <a href="https://weixin.qq.com/sph/AEybfpTOx5" target="_blank" rel="noopener">视频 03 <span>↗</span></a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <p class="serif" style="font-size:18px;margin:0 0 8px;">— 理性与浪漫的分界 —</p>
    <p>KieranHoward · 个人名片 · 2026</p>
    <p style="opacity:0.7;font-size:12px;">双击 index.html 即可打开 · 日/夜按钮连续点击三次仍然稳定</p>
  </div>
</footer>

<script>{JS}</script>
</body>
</html>
"""

(ROOT / "index.html").write_text(HTML, encoding="utf-8")
print(f"index.html 已生成：{(ROOT / 'index.html').stat().st_size / 1024:.1f} KB")