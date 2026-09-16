import os
from PIL import Image, ImageDraw, ImageFont

font_regular_path = 'C:/Windows/Fonts/malgun.ttf'
font_bold_path = 'C:/Windows/Fonts/malgunbd.ttf'

def get_font(size, bold=False):
    path = font_bold_path if bold else font_regular_path
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

def draw_text_centered(draw, text, y, font, fill, width=800):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    draw.text(((width - w) / 2, y), text, font=font, fill=fill)

def create_insta_feed_images():
    w, h = 800, 1000
    
    # 1. insta_gunsan.jpg
    img_g = Image.new('RGB', (w, h), color='#FFFFFF')
    draw_g = ImageDraw.Draw(img_g)
    
    # Instagram Header
    draw_g.ellipse([40, 30, 84, 74], fill='#A855F7')
    draw_g.text((54, 40), "영", font=get_font(20, True), fill='#FFFFFF')
    draw_g.text((96, 42), "connect0cha_official", font=get_font(22, True), fill='#262626')
    draw_g.text((96, 70), "영등포 전통시장 · 군산집", font=get_font(16, False), fill='#8E8E8E')
    draw_g.text((730, 42), "•••", font=get_font(24, True), fill='#262626')

    # Main Image Container
    # Background market blue glow
    for i in range(110, 680):
        t = (i - 110) / 570
        r = int(140 + (220 - 140) * t)
        g = int(170 + (230 - 170) * t)
        b = int(220 + (245 - 220) * t)
        draw_g.line([(30, i), (770, i)], fill=(r, g, b))
        
    draw_g.rectangle([60, 140, 740, 250], fill='#1E40AF', outline='#FFFFFF', width=3)
    draw_text_centered(draw_g, "군  산  집", 160, get_font(56, True), '#FFFFFF')
    draw_text_centered(draw_g, "생삼겹살 · 생오겹살 · 닭볶음탕 · 야장 포차", 225, get_font(18, False), '#DBEAFE')
    
    draw_g.rectangle([60, 270, 740, 520], fill='#F1F5F9', outline='#CBD5E1', width=2)
    draw_g.rectangle([100, 310, 340, 480], fill='#FFFFFF', outline='#94A3B8', width=2)
    draw_g.text((120, 330), "냉방중 ❄️", font=get_font(22, True), fill='#1D4ED8')
    draw_g.text((120, 375), "생삼겹살 / 생오겹살", font=get_font(18, True), fill='#1E293B')
    draw_g.text((120, 415), "시원한 실내 & 야장", font=get_font(18, False), fill='#475569')

    draw_g.rectangle([380, 330, 700, 460], fill='#EF4444', outline='#B91C1C', width=2)
    draw_text_centered(draw_g, "🔥 시원한 가을 야장 삼겹살 🔥", 370, get_font(20, True), '#FFFFFF', width=1080)

    # Purple bottom band with flowers
    draw_g.rectangle([30, 530, 770, 538], fill='#3B0764')
    for cx in [630, 690]:
        draw_g.ellipse([cx-18, 534-18, cx+18, 534+18], fill='#3B0764', outline='#A855F7', width=2)
        draw_g.text((cx-7, 534-12), "✦", font=get_font(16, True), fill='#FFFFFF')

    draw_text_centered(draw_g, "영차의  또또또간집", 570, get_font(38, True), '#1E1B4B')
    draw_text_centered(draw_g, "‘군산집’을  소개합니다", 620, get_font(42, True), '#111827')

    # Instagram interaction icons
    draw_g.text((40, 700), "❤️", font=get_font(28, False), fill='#EF4444')
    draw_g.text((90, 700), "💬", font=get_font(26, False), fill='#262626')
    draw_g.text((140, 700), "↗️", font=get_font(26, False), fill='#262626')
    draw_g.text((720, 700), "🔖", font=get_font(26, False), fill='#262626')

    # Likes & Caption
    draw_g.text((40, 755), "좋아요 6개", font=get_font(20, True), fill='#262626')
    draw_g.text((40, 795), "connect0cha_official", font=get_font(20, True), fill='#262626')
    draw_g.text((265, 795), "이번 주말 뭐하지? 영등포시장 구경하고...", font=get_font(20, False), fill='#262626')
    draw_g.text((40, 835), "야장에서 삼겹살에 소주 한 잔! 🥩🍻 #군산집 #영등포시장맛집", font=get_font(18, False), fill='#4B5563')
    draw_g.text((40, 880), "인스타그램에서 카드뉴스 전체 보기 ➔", font=get_font(20, True), fill='#7C3AED')
    
    img_g.save('images/insta_gunsan.jpg', quality=95)

    # 2. insta_7bun.jpg
    img_7 = Image.new('RGB', (w, h), color='#FFFFFF')
    draw_7 = ImageDraw.Draw(img_7)
    
    # Instagram Header
    draw_7.ellipse([40, 30, 84, 74], fill='#7C3AED')
    draw_7.text((54, 40), "영", font=get_font(20, True), fill='#FFFFFF')
    draw_7.text((96, 42), "connect0cha_official", font=get_font(22, True), fill='#262626')
    draw_7.text((96, 70), "영등포 전통시장 · 7번집", font=get_font(16, False), fill='#8E8E8E')
    draw_7.text((730, 42), "•••", font=get_font(24, True), fill='#262626')

    # Main Image Container
    for i in range(110, 680):
        t = (i - 110) / 570
        r = int(245 - 20 * t)
        g = int(240 - 25 * t)
        b = int(255 - 15 * t)
        draw_7.line([(30, i), (770, i)], fill=(r, g, b))

    # Stall signage
    draw_7.rectangle([60, 140, 740, 240], fill='#4C1D95', outline='#DDD6FE', width=3)
    draw_text_centered(draw_7, "🏮 7  번  집 🏮", 155, get_font(48, True), '#FDE047')
    draw_text_centered(draw_7, "돼지꼬리 · 닭발 · 비빔국수 · 잔치국수", 215, get_font(18, False), '#E9D5FF')

    # Grandmother stall photo mock
    draw_7.rectangle([60, 260, 740, 520], fill='#FEF3C7', outline='#F59E0B', width=2)
    draw_g_stall = ImageDraw.Draw(img_7)
    draw_7.text((100, 300), "🐷 쫀득쫀득 돼지꼬리", font=get_font(24, True), fill='#92400E')
    draw_7.text((100, 350), "🐔 매콤달콤 닭발", font=get_font(24, True), fill='#92400E')
    draw_7.text((100, 400), "🍜 새콤 비빔국수 / 잔치국수", font=get_font(24, True), fill='#92400E')
    draw_7.rectangle([440, 290, 700, 480], fill='#FFFFFF', outline='#E5E7EB', width=2)
    draw_text_centered(draw_7, "42년 손맛의\n시장판 오마카세", 355, get_font(24, True), '#4C1D95', width=1140)

    # Purple bottom band
    draw_7.rectangle([30, 530, 770, 538], fill='#3B0764')
    for cx in [630, 690]:
        draw_7.ellipse([cx-18, 534-18, cx+18, 534+18], fill='#3B0764', outline='#A855F7', width=2)
        draw_7.text((cx-7, 534-12), "✦", font=get_font(16, True), fill='#FFFFFF')

    draw_text_centered(draw_7, "영등포  시장판  오마카세", 570, get_font(38, True), '#1E1B4B')
    draw_text_centered(draw_7, "‘7번집’을  소개합니다", 620, get_font(42, True), '#111827')

    # Instagram interaction icons
    draw_7.text((40, 700), "❤️", font=get_font(28, False), fill='#EF4444')
    draw_7.text((90, 700), "💬", font=get_font(26, False), fill='#262626')
    draw_7.text((140, 700), "↗️", font=get_font(26, False), fill='#262626')
    draw_7.text((720, 700), "🔖", font=get_font(26, False), fill='#262626')

    # Likes & Caption
    draw_7.text((40, 755), "좋아요 4개", font=get_font(20, True), fill='#262626')
    draw_7.text((40, 795), "connect0cha_official", font=get_font(20, True), fill='#262626')
    draw_7.text((265, 795), "노포 러버 여기로 모여라 ❤️", font=get_font(20, False), fill='#262626')
    draw_7.text((40, 835), "저렴한 가격에 푸짐한 안주를 즐길 수 있는... #7번집 #영등포노포", font=get_font(18, False), fill='#4B5563')
    draw_7.text((40, 880), "인스타그램에서 카드뉴스 전체 보기 ➔", font=get_font(20, True), fill='#7C3AED')

    img_7.save('images/insta_7bun.jpg', quality=95)

create_insta_feed_images()
print("Generated insta_gunsan.jpg and insta_7bun.jpg successfully!")
