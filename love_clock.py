import streamlit as st
import pandas as pd
import pydeck as pdk
from datetime import datetime
import time
import os
import random
import glob
import base64
from PIL import Image, ImageOps

def load_image_corrected(path):
    """加载图片并自动校正 EXIF 旋转方向（解决手机竖拍照片横显问题）"""
    try:
        img = Image.open(path).convert("RGB")
        return ImageOps.exif_transpose(img)
    except Exception:
        return Image.open(path).convert("RGB")

def show_image(path, caption="", width="stretch"):
    """显示图片（自动校正 EXIF 旋转）"""
    img = load_image_corrected(path)
    st.image(img, caption=caption, width=width)

# 1. 网页基础设置
st.set_page_config(page_title="ruby和羊习习的恋恋メモ", page_icon="📝", layout="wide")

# 2. 设置在一起的日子：2025年10月26日
start_date = datetime(2025, 10, 26, 0, 0) 

# --- 主界面标题 ---
st.title("📝 ruby和羊习习的恋恋メモ")
st.subheader("“记忆会褪色，但代码和爱永远鲜活。”")

# --- 模块一：实时陪伴计时器 ---
st.markdown("---")
st.write("### 🕰️ 时光存证")
placeholder = st.empty()

# --- 模块二：相濡以沫 —— 庄子典故插画 ---
st.markdown("---")
st.header("🐟 相濡以沫：跨越千年的温柔")
st.markdown("")
st.markdown("""
<div style="
    background: linear-gradient(90deg, #e8f4f8 0%, #f0e8f4 100%);
    border-radius: 12px; padding: 1rem 1.5rem; margin-bottom: 1rem;
    border-left: 4px solid #5c7c9e; font-size: 0.95rem; color: #444; font-style: italic;">
    「泉涸，鱼相与处于陆，相呴以湿，相濡以沫。」—— 《庄子·大宗师》
</div>
""", unsafe_allow_html=True)
st.markdown("还记得刚在一起时，我们在沙发上依偎着读《庄子》吗？那时候，书里的文字在空气中流淌，我们一字一句读完那段关于相濡以沫的典故。")
st.markdown("")

def draw_xiangru_xiamo_svg():
    return '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 280" style="max-width:100%; height:auto; border-radius:12px;">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#faf8f5"/>
      <stop offset="100%" style="stop-color:#efe8e0"/>
    </linearGradient>
    <linearGradient id="mountain1" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" style="stop-color:#6b7b8c"/>
      <stop offset="100%" style="stop-color:#8a9aa8"/>
    </linearGradient>
    <linearGradient id="mountain2" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" style="stop-color:#5c6b7a"/>
      <stop offset="100%" style="stop-color:#7a8a98"/>
    </linearGradient>
    <linearGradient id="water" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#a8c4d8;stop-opacity:0.6"/>
      <stop offset="100%" style="stop-color:#7a9ab5;stop-opacity:0.8"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="2" dy="2" stdDeviation="2" flood-opacity="0.15"/>
    </filter>
  </defs>
  <rect width="700" height="280" fill="url(#bg)"/>
  <path d="M0 280 L0 160 Q120 200 200 120 Q280 80 350 140 Q420 100 500 160 Q580 120 700 180 L700 280 Z" fill="url(#mountain2)" opacity="0.4"/>
  <path d="M0 280 L0 200 Q150 150 280 180 Q400 130 520 170 Q620 140 700 200 L700 280 Z" fill="url(#mountain1)" opacity="0.6"/>
  <ellipse cx="350" cy="240" rx="320" ry="50" fill="#d4cfc4"/>
  <path d="M180 220 Q220 195 280 210 Q340 200 380 215 Q420 195 470 208 Q520 200 550 218 L540 245 Q400 240 280 250 Q200 248 180 220 Z" fill="url(#water)" filter="url(#shadow)"/>
  <circle cx="310" cy="218" r="6" fill="none" stroke="#c5dce8" stroke-width="1.5" opacity="0.9"/>
  <circle cx="330" cy="210" r="5" fill="none" stroke="#c5dce8" stroke-width="1.2" opacity="0.85"/>
  <circle cx="350" cy="215" r="7" fill="none" stroke="#b8d4e8" stroke-width="1.5" opacity="0.95"/>
  <circle cx="370" cy="208" r="5" fill="none" stroke="#c5dce8" stroke-width="1.2" opacity="0.85"/>
  <circle cx="390" cy="218" r="6" fill="none" stroke="#c5dce8" stroke-width="1.5" opacity="0.9"/>
  <g transform="translate(230, 225)">
    <ellipse cx="0" cy="0" rx="28" ry="12" fill="#8b7355" stroke="#6b5344" stroke-width="0.8"/>
    <path d="M-28 -5 L-38 0 L-28 5 Z" fill="#8b7355" stroke="#6b5344"/>
    <circle cx="12" cy="-2" r="3" fill="#3d2c1e"/>
    <path d="M-20 0 Q-15 -8 -10 0" stroke="#6b5344" stroke-width="0.6" fill="none"/>
    <path d="M-8 0 Q-3 -6 2 0" stroke="#6b5344" stroke-width="0.5" fill="none"/>
  </g>
  <g transform="translate(470, 225) scale(-1,1)">
    <ellipse cx="0" cy="0" rx="28" ry="12" fill="#7a6b5c" stroke="#5c4d3e" stroke-width="0.8"/>
    <path d="M-28 -5 L-38 0 L-28 5 Z" fill="#7a6b5c" stroke="#5c4d3e"/>
    <circle cx="12" cy="-2" r="3" fill="#3d2c1e"/>
    <path d="M-20 0 Q-15 -8 -10 0" stroke="#5c4d3e" stroke-width="0.6" fill="none"/>
    <path d="M-8 0 Q-3 -6 2 0" stroke="#5c4d3e" stroke-width="0.5" fill="none"/>
  </g>
  <ellipse cx="350" cy="230" rx="80" ry="15" fill="none" stroke="#a8c4d8" stroke-width="0.5" opacity="0.4"/>
</svg>
'''
col_svg, col_text = st.columns([3, 1])
with col_svg:
    svg_b64 = base64.b64encode(draw_xiangru_xiamo_svg().strip().encode("utf-8")).decode("utf-8")
    st.markdown(f'<img src="data:image/svg+xml;base64,{svg_b64}" style="max-width:100%; height:auto; border-radius:12px;" alt="相濡以沫" />', unsafe_allow_html=True)
with col_text:
    st.markdown("### 我们的秘密暗号")
    st.write("只要交换一个泡泡")
    st.write("我们就拥有了全世界的温润。")
    st.success("💕 比起相忘于江湖，我更贪恋和你一起吐泡泡的每一个瞬间。")

st.markdown("---")

# --- 模块三：龙岩冠豸山记忆画卷 ---
st.markdown("---")
st.header("🏞️ 龙岩冠豸山之恋：记忆画卷")

col_hotel_text, col_hotel_img = st.columns([2, 1])
with col_hotel_text:
    st.write("🏨 **山景酒店：** 推开窗，冠豸山就在眼前。清晨的鸟鸣和晚上的星空，是我们独有的静谧。")
with col_hotel_img:
    try: show_image("酒店图片.jpg", caption="我们的窗外风景")
    except: st.info("💡 请放入：酒店图片.jpg")

st.markdown("### 🍜 舌尖上的龙岩")
col_food_img, col_food_text = st.columns([1, 2])
with col_food_img:
    try: show_image("龙岩美食.jpg", caption="竹荪鸡汤")
    except: st.info("💡 请放入：龙岩美食.jpg")
with col_food_text:
    st.write("🍲 那一碗鲜美的竹荪鸡汤和Q弹的特色煮干粉，藏进了心里的旅行记忆。")

st.markdown("### ⛰️ 冠豸山游船")
cp1, cp2 = st.columns(2)
with cp1:
    try: show_image("冠豸山合照1.jpg", caption="us")
    except: st.info("💡 请放入：冠豸山合照1.jpg")
with cp2:
    try: show_image("冠豸山合照2.jpg", caption="you&me")
    except: st.info("💡 请放入：冠豸山合照2.jpg")

# --- 芭蕾模块：足尖上的守护（HTML/CSS 绝对定位 + 放射线）---
def image_to_base64(path, fallback=None):
    """将图片转为 base64，用于 HTML 内嵌（GIF 保留动效，其他格式校正 EXIF）"""
    try:
        from io import BytesIO
        ext = os.path.splitext(path)[1].lower()
        if ext == ".gif":
            with open(path, "rb") as f:
                data = f.read()
            return "data:image/gif;base64," + base64.b64encode(data).decode()
        img = load_image_corrected(path)
        buf = BytesIO()
        fmt = "PNG" if ext == ".png" else "JPEG"
        img.save(buf, format=fmt, quality=85)
        mime = "image/png" if fmt == "PNG" else "image/jpeg"
        return f"data:{mime};base64,{base64.b64encode(buf.getvalue()).decode()}"
    except Exception:
        return fallback or "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Crect fill='%23f0e6f0' width='120' height='120'/%3E%3Ctext x='50%25' y='50%25' dominant-baseline='middle' text-anchor='middle' fill='%23999' font-size='12'%3E暂无图片%3C/text%3E%3C/svg%3E"

st.markdown("---")
st.header("🩰 足尖上的守护：我的首席观众")
st.subheader('"芭蕾是极致的克制，而你给了我最极致的纵容。"')
st.markdown("")

# 芭蕾模块：剧院全景图（四向放射线 + 中心图 + emoji 卡片）
bar_img = image_to_base64("实物芭杆.jpg")
show_img = image_to_base64("芭蕾演出.jpg")
# 中心图：优先 芭蕾剧院中心图.jpg，或 Cursor 附件路径
center_img = image_to_base64("芭蕾剧院中心图.jpg")
if "暂无" in center_img:
    _ap = os.path.normpath(os.path.expanduser("~/.cursor/projects/c-Users-10459-Desktop-rubiax/assets/c__Users_10459_AppData_Roaming_Cursor_User_workspaceStorage_32acb30c34c474288885740c55c3dc0c_images_9412e47f-ff51-4b31-b022-22336f6c6f9e-1a581d08-e059-4cbf-8da3-65cca1367abe.png"))
    if os.path.exists(_ap):
        center_img = image_to_base64(_ap)

ballet_html = (
    '<div class="ballet-panorama">'
    '<svg class="ballet-radial-lines" viewBox="0 0 800 520">'
    '<line x1="400" y1="260" x2="140" y2="100" stroke="#ffb6c1" stroke-width="1.2" stroke-dasharray="6,4" opacity="0.7"/>'
    '<line x1="400" y1="260" x2="660" y2="100" stroke="#ffb6c1" stroke-width="1.2" stroke-dasharray="6,4" opacity="0.7"/>'
    '<line x1="400" y1="260" x2="140" y2="420" stroke="#ffb6c1" stroke-width="1.2" stroke-dasharray="6,4" opacity="0.7"/>'
    '<line x1="400" y1="260" x2="660" y2="420" stroke="#ffb6c1" stroke-width="1.2" stroke-dasharray="6,4" opacity="0.7"/>'
    '</svg>'
    '<div class="ballet-center-scene"><img src="' + center_img + '" alt="剧院与芭蕾" class="ballet-theater-img"/></div>'
    '<div class="ballet-card ballet-tl"><div class="ballet-card-inner">'
    '<img src="' + bar_img + '" alt="芭杆"/>'
    '<span class="ballet-card-label">你买的芭杆，让我在家里也能起舞</span></div></div>'
    '<div class="ballet-card ballet-tr"><div class="ballet-card-inner">'
    '<img src="' + show_img + '" alt="演出"/>'
    '<span class="ballet-card-label">舞台上的高光时刻，总有你在台下。</span></div></div>'
    '<div class="ballet-card ballet-bl"><div class="ballet-card-inner ballet-icon-card">'
    '<span class="ballet-emoji-icon">👗</span>'
    '<span class="ballet-card-label">你买的体服，让每一颗汗水都闪闪发光。</span></div></div>'
    '<div class="ballet-card ballet-br"><div class="ballet-card-inner ballet-icon-card">'
    '<span class="ballet-emoji-icon">💃</span>'
    '<span class="ballet-card-label">那晚的《吉赛尔》，是我们共鸣的心跳。</span></div></div>'
    '</div>'
)

ballet_css = (
    '<style>'
    '.ballet-panorama{position:relative;width:100%;max-width:800px;height:520px;margin:0 auto 2rem;background:#faf6f2;border-radius:12px;overflow:hidden;}'
    '.ballet-radial-lines{position:absolute;top:0;left:0;width:100%;height:100%;pointer-events:none;}'
    '.ballet-center-scene{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);}'
    '.ballet-theater-img{width:240px;height:220px;display:block;object-fit:contain;}'
    '.ballet-card{position:absolute;width:160px;}.ballet-card-inner{background:#fff;border-radius:10px;padding:10px;box-shadow:0 2px 12px rgba(0,0,0,0.06);border:1px solid rgba(255,182,193,0.25);height:100%;display:flex;flex-direction:column;align-items:center;}'
    '.ballet-card img{width:100%;height:100px;object-fit:contain;border-radius:6px;}'
    '.ballet-icon-card{min-height:120px;}.ballet-emoji-icon{font-size:2.5rem;display:block;margin:12px 0;}'
    '.ballet-card-label{font-size:0.7rem;color:#8b7355;line-height:1.4;margin-top:8px;text-align:center;}'
    '.ballet-tl{top:30px;left:30px;}.ballet-tr{top:30px;right:30px;}.ballet-bl{bottom:30px;left:30px;}.ballet-br{bottom:30px;right:30px;}'
    '</style>'
)
st.markdown(ballet_css + ballet_html, unsafe_allow_html=True)

st.markdown("---")

# --- 模块四：屋檐下的温柔 (新增：圣诞、芭蕾、诗歌、衣柜) ---
st.markdown("---")
st.header("🏠 屋檐下的温柔：琐碎而伟大的爱")

col_ballet, col_lego = st.columns(2)
with col_ballet:
    st.markdown("### 🪑 并肩奋斗的微光")
    st.write("敲击键盘的每一声，都有你在一旁的呼吸。")
    try: show_image("办公桌.jpg", caption="你把最好的位置留给我，最舒服的支撑也留给了我")
    except: st.info("💡 请放入：办公桌.jpg")

with col_lego:
    st.markdown("### 🎄 圣诞积木童话")
    st.write("- **圣诞树与你：** 我们一砖一瓦拼凑的浪漫。")
    try: show_image("圣诞积木.jpg", caption="我们拼成的浪漫。")
    except: st.info("💡 请放入：圣诞积木.jpg")

st.markdown("---")
col_poem, col_closet = st.columns(2)
with col_poem:
    st.markdown("### ✍️ 墨香情缘")
    st.info("**【宝宝亲笔】**\n\n夜来清梦好，丝雨细如缠") 
    try: show_image("藏头诗.jpg", caption="名隐其中，情深意切。")
    except: st.info("💡 请放入：藏头诗.jpg")

with col_closet:
    st.markdown("### 👗 挂起来的宠溺")
    st.write("“我不喜欢折衣服，希望它们都挂起来。”")
    st.success("✅ 成就达成：专属大衣柜组装完毕！")
    try: show_image("大衣柜.jpg", caption="你亲手组装的港湾。")
    except: st.info("💡 请放入：大衣柜.jpg")

# --- 模块五：舌尖上的爱：家常菜 & 外出觅食 ---
st.markdown("---")
st.header("🍽️ 舌尖上的爱：生活里的烟火情调")
st.markdown("")
st.markdown("""
<div style="
    background: linear-gradient(90deg, #fff5f5 0%, #fff9e6 50%, #f0fff4 100%);
    border-radius: 12px; padding: 1rem 1.5rem; margin-bottom: 1rem;
    border-left: 4px solid #ff6b6b; font-size: 1rem; color: #555;">
    "每一场味蕾的冒险，因为有你对坐，才显得格外惊艳。"
</div>
""", unsafe_allow_html=True)

FOOD_DIR = "food"
FOOD_SECTIONS = [
    ("家常菜", "🏠 宝宝厨房", "每一餐都是我们共同创作的生活作品"),
    ("西餐", "🍴 刀叉与烛光", "每一口都是被宠溺的幸福感"),
    ("日料", "🍣 刺身与寿司", "把爱都融进每一道菜里"),
    ("海鲜", "🦞 鲜活滋味", "喂饱灵魂的仪式感"),
]

def render_food_grid(folder, exts=["jpg", "jpeg", "png", "webp"], layout_by_orientation=False):
    paths = []
    for e in exts:
        paths.extend(glob.glob(os.path.join(folder, f"*.{e}")))
    paths.sort()
    if not paths:
        st.info(f"💡 将美食图片放入 `{folder}/` 文件夹即可自动展示。")
        return
    if layout_by_orientation:
        landscape, portrait = [], []
        for p in paths:
            try:
                img = load_image_corrected(p)
                w, h = img.size
                (landscape if w >= h else portrait).append(p)
            except Exception:
                landscape.append(p)
        # 上排：横图两张
        top = landscape[:2]
        # 下排：竖图两张
        bottom = portrait[:2]
        if top:
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if j < len(top):
                    with col:
                        path = top[j]
                        name = os.path.splitext(os.path.basename(path))[0]
                        try:
                            img = load_image_corrected(path)
                            st.image(img, caption=name, width="stretch")
                        except Exception:
                            st.image(path, caption=name, width="stretch")
        if bottom:
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if j < len(bottom):
                    with col:
                        path = bottom[j]
                        name = os.path.splitext(os.path.basename(path))[0]
                        try:
                            img = load_image_corrected(path)
                            st.image(img, caption=name, width="stretch")
                        except Exception:
                            st.image(path, caption=name, width="stretch")
        # 若有多于 4 张，其余按 3 列继续排
        rest = landscape[2:] + portrait[2:]
        for i in range(0, len(rest), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(rest):
                    with col:
                        path = rest[i + j]
                        name = os.path.splitext(os.path.basename(path))[0]
                        try:
                            img = load_image_corrected(path)
                            st.image(img, caption=name, width="stretch")
                        except Exception:
                            st.image(path, caption=name, width="stretch")
    else:
        for i in range(0, len(paths), 3):
            cols = st.columns(3)
            for j, col in enumerate(cols):
                if i + j < len(paths):
                    with col:
                        path = paths[i + j]
                        name = os.path.splitext(os.path.basename(path))[0]
                        try:
                            img = load_image_corrected(path)
                            st.image(img, caption=name, width="stretch")
                        except Exception:
                            st.image(path, caption=name, width="stretch")

# 手风琴式折叠布局：纵向展开，像菜单一样
for cat, label, desc in FOOD_SECTIONS:
    with st.expander(f"**{label}** · {desc}", expanded=(cat == "家常菜")):
        render_food_grid(os.path.join(FOOD_DIR, cat), layout_by_orientation=(cat == "家常菜"))

st.markdown("---")

# --- 模块六：周末时光：一起唱歌、爬山、游泳、打球 ---
st.markdown("---")
st.header("🌅 周末时光：专属的充电日")
st.markdown("")
st.markdown("""
<div style="
    background: linear-gradient(90deg, #fff8e7 0%, #e8f5e9 50%, #e3f2fd 100%);
    border-radius: 12px; padding: 1rem 1.5rem; margin-bottom: 1rem;
    border-left: 4px solid #ff9800; font-size: 1rem; color: #555;">
    "世界很大，但这个周末只想和你虚度。"
</div>
""", unsafe_allow_html=True)

WEEKEND_DIR = "weekend"
WEEKEND_MEDIA_HEIGHT = 260  # 统一高度（像素），四个素材一致

def get_first_media_path(folder, exts):
    paths = []
    for e in exts:
        paths.extend(glob.glob(os.path.join(folder, f"*.{e}")))
    paths.sort()
    return paths[0] if paths else None

# 统一尺寸：限制周末视频高度，与同栏图片视觉平衡
st.markdown(f"""
<style>
/* 仅限制周末模块视频高度，避免过大 */
div[data-testid="stVideo"] video {{
    max-height: {WEEKEND_MEDIA_HEIGHT}px !important;
    width: 100% !important;
    object-fit: contain !important;
}}
</style>
""", unsafe_allow_html=True)

# 2x2 网格，每格一个主素材，统一尺寸
col_sing, col_hike = st.columns(2)
with col_sing:
    st.markdown("### 🎤 麦克风的秘密")
    st.caption("在 KTV 里，我是你永远的头号粉丝，你是我唯一的专属听众。")
    sing_video = get_first_media_path(os.path.join(WEEKEND_DIR, "唱歌"), ["mp4", "webm", "mov"])
    if sing_video:
        st.video(sing_video)
    else:
        st.info("💡 将唱歌视频放入 `weekend/唱歌/` 文件夹即可展示。")

with col_hike:
    st.markdown("### ⛰️ 山海步道的呼吸")
    st.caption("山高路远，有你陪就不累。")
    hike_img = get_first_media_path(os.path.join(WEEKEND_DIR, "爬山"), ["jpg", "jpeg", "png", "webp"])
    if hike_img:
        try:
            img = load_image_corrected(hike_img)
            st.image(img, caption=os.path.splitext(os.path.basename(hike_img))[0], width="stretch")
        except Exception:
            st.image(hike_img, caption=os.path.splitext(os.path.basename(hike_img))[0], width="stretch")
    else:
        st.info("💡 将图片放入 `weekend/爬山/` 文件夹即可展示。")

col_swim, col_badminton = st.columns(2)
with col_swim:
    st.markdown("### 🏊 水中的自由")
    st.caption("像两条真正的小鱼，在碧波中扑腾出最纯粹的笑声。")
    swim_img = get_first_media_path(os.path.join(WEEKEND_DIR, "游泳"), ["jpg", "jpeg", "png", "webp"])
    if swim_img:
        try:
            img = load_image_corrected(swim_img)
            st.image(img, caption=os.path.splitext(os.path.basename(swim_img))[0], width="stretch")
        except Exception:
            st.image(swim_img, caption=os.path.splitext(os.path.basename(swim_img))[0], width="stretch")
    else:
        st.info("💡 将图片放入 `weekend/游泳/` 文件夹即可展示。")

with col_badminton:
    st.markdown("### 🏸 球场上的较量")
    st.caption("挥洒汗水，在每一次挥拍中感受生命力的跳动。")
    bad_img = get_first_media_path(os.path.join(WEEKEND_DIR, "羽毛球"), ["jpg", "jpeg", "png", "webp"])
    if bad_img:
        try:
            img = load_image_corrected(bad_img)
            st.image(img, caption=os.path.splitext(os.path.basename(bad_img))[0], width="stretch")
        except Exception:
            st.image(bad_img, caption=os.path.splitext(os.path.basename(bad_img))[0], width="stretch")
    else:
        st.info("💡 将图片放入 `weekend/羽毛球/` 文件夹即可展示。")

st.markdown("---")

# --- 模块七：光影与书页：我们一起看的电影、书籍、游戏 ---
st.markdown("---")
st.header("🎬 光影与书页：我们一起看的电影、书籍、游戏")
st.subheader('"从大银幕到指尖，每一次共度的时光都是浪漫。"')
st.markdown("")

POSTER_DIR = "poster"
MOVIES = [
    ("五十度灰", "五十度灰"),
    ("色戒", "色戒"),
    ("遇见你之前", "遇见你之前"),
    ("BJ单身日记", "BJ单身日记"),
    ("疯狂动物城2", "疯狂动物城2"),
    ("周处除三害", "周处除三害"),
]
BOOKS = [("失落的卫星", "失落的卫星")]
GAMES = [("闪耀暖暖", "闪耀暖暖"), ("Tengami", "Tengami"), ("纪念碑谷", "纪念碑谷")]

def render_poster(name, folder, ext=["jpg", "jpeg", "png", "webp"]):
    for e in ext:
        path = os.path.join(folder, f"{name}.{e}")
        if os.path.exists(path):
            show_image(path, caption=f"《{name}》")
            return True
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px; padding: 1.5rem; text-align: center;
        color: white; font-weight: bold; min-height: 120px; display: flex;
        align-items: center; justify-content: center; font-size: 1.1rem;">
        《{name}》
    </div>
    """, unsafe_allow_html=True)
    st.caption(f"💡 放入 {folder}/{name}.jpg 可显示海报")
    return False

# Tab 切换：电影 | 书籍 | 游戏
tab_movie, tab_book, tab_game = st.tabs(["🎞️ 电影海报墙", "📖 书籍", "🎮 游戏"])

with tab_movie:
    st.markdown("我们一起窝在沙发、捧着爆米花看过的故事。")
    for i in range(0, len(MOVIES), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(MOVIES):
                with col:
                    render_poster(MOVIES[i + j][0], POSTER_DIR)
    st.success("📽️ 6 部电影，每一帧都是回忆。")

with tab_book:
    st.markdown("我们一起翻过的书页，走过的远方。")
    if len(BOOKS) == 1:
        _, col, _ = st.columns([1, 2, 1])
        with col:
            render_poster(BOOKS[0][0], POSTER_DIR)
    else:
        for i in range(0, len(BOOKS), 2):
            c1, c2 = st.columns(2)
            with c1:
                if i < len(BOOKS):
                    render_poster(BOOKS[i][0], POSTER_DIR)
            with c2:
                if i + 1 < len(BOOKS):
                    render_poster(BOOKS[i + 1][0], POSTER_DIR)
    st.info("📚 《失落的卫星》—— 中亚的旅程，我们一起读过。")

with tab_game:
    st.markdown("我们一起闯关、一起冒险的快乐时光。")
    g1, g2, g3 = st.columns(3)
    with g1:
        render_poster(GAMES[0][0], POSTER_DIR)
    with g2:
        render_poster(GAMES[1][0], POSTER_DIR)
    with g3:
        render_poster(GAMES[2][0], POSTER_DIR)
    st.success("🎲 3 款游戏，每一局都是陪伴。")

# 互动区：随机推荐 + 预告片
st.markdown("---")
st.markdown("### 🎲 互动小彩蛋")
r1, r2, r3 = st.columns([1, 2, 1])
with r2:
    if st.button("🎰 随机挑一个今晚一起看/玩", width="stretch"):
        pool = [f"电影《{m[0]}》" for m in MOVIES] + [f"书《{b[0]}》" for b in BOOKS] + [f"游戏《{g[0]}》" for g in GAMES]
        pick = random.choice(pool)
        st.balloons()
        st.success(f"✨ 今晚就选它：**{pick}**")
st.markdown("---")

# --- 模块八：展望·星月之国浪漫之旅 (地图修复版) ---
st.markdown("---")
st.header("🇹🇷 展望：星月之国的浪漫之旅")
st.subheader("“从博斯普鲁斯的海风，到卡帕多西亚的星空。”")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"])
with tab1: st.write("🌊 **博斯普鲁斯海峡游船**：穿梭欧亚。")
with tab2: st.write("🕌 **帝国盛景**：圣索菲亚大教堂、蓝色清真寺。")
with tab3: st.write("🗿 **奇迹地貌**：卡帕多西亚地下城与峡谷。")
with tab4: st.write("🎈 **梦幻热气球**：格雷梅晨曦，内飞安塔利亚。")
with tab5: st.write("🌊 **蔚蓝海边**：地中海自由活动，内飞回程。")

st.markdown("### 📍 我们的星月之旅足迹")

# 1. 定义坐标数据
map_df = pd.DataFrame({
    'city': ['伊斯坦布尔', '卡帕多西亚', '安塔利亚'],
    'lat': [41.0082, 38.6431, 36.8969],
    'lon': [28.9784, 34.8289, 30.7133],
    'desc': ['海峡游船', '热气球', '地中海']
})

# 2. 渲染地图 (使用最稳健的 st.map 确保底图显示)
st.map(map_df, color='#FF4B4B', size=40)

# --- 实时刷新循环 (必须在最后) ---
while True:
    now = datetime.now()
    diff = now - start_date
    days, hours, minutes, seconds = diff.days, diff.seconds // 3600, (diff.seconds // 60) % 60, diff.seconds % 60
    with placeholder.container():
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("相爱天数", f"{days} 天")
        c2.metric("小时", f"{hours} 小时")
        c3.metric("分钟", f"{minutes} 分钟")
        c4.metric("秒", f"{seconds} 秒")
        st.markdown(f"### 💌 我们已经在一起陪伴了 **{days}** 天")
    time.sleep(1)