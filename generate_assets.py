import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('images', exist_ok=True)

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

def create_gunsan_1():
    w, h = 800, 1060
    img = Image.new('RGB', (w, h), color='#F6F6FA')
    draw = ImageDraw.Draw(img)
    
    for i in range(700):
        r = int(70 + (220 - 70) * (i / 700))
        g = int(100 + (230 - 100) * (i / 700))
        b = int(180 + (245 - 180) * (i / 700))
        draw.line([(0, i), (w, i)], fill=(r, g, b))
    
    draw.rectangle([40, 60, 760, 220], fill='#2B5597', outline='#FFFFFF', width=4)
    draw_text_centered(draw, "군  산  집", 90, get_font(72, True), '#FFFFFF')
    draw_text_centered(draw, "삼겹살 · 오겹살 · 닭볶음탕 · 제육볶음 · 생선구이", 175, get_font(22, False), '#D1E3FF')
    
    draw.rectangle([60, 260, 740, 640], fill='#E8EBF2', outline='#CAD2E0', width=2)
    draw.rectangle([100, 300, 360, 600], fill='#DCE4EE', outline='#9AA8BA', width=2)
    draw.text((120, 320), "냉방중 ❄️", font=get_font(26, True), fill='#2B5597')
    draw.text((120, 380), "생삼겹살", font=get_font(28, True), fill='#333333')
    draw.text((120, 420), "생오겹살", font=get_font(28, True), fill='#333333')
    draw.text((120, 470), "소주 4,000원", font=get_font(22, False), fill='#555555')
    
    draw.rectangle([400, 340, 700, 480], fill='#EA580C', outline='#C2410C', width=3)
    draw_text_centered(draw, "🔥 시원한 영등포 야장 테이블 🔥", 380, get_font(24, True), '#FFFFFF', width=1100)
    draw.rectangle([420, 500, 680, 590], fill='#DC2626', outline='#991B1B', width=2)
    draw_text_centered(draw, "선선한 가을 바람과 함께 한 잔 🍻", 530, get_font(22, True), '#FFFFFF', width=1100)

    draw.rectangle([0, 680, w, h], fill='#FFFFFF')
    draw.rectangle([0, 880, w, 888], fill='#3B0764')
    for cx in [640, 700]:
        draw.ellipse([cx-22, 884-22, cx+22, 884+22], fill='#3B0764', outline='#A855F7', width=2)
        draw.text((cx-9, 884-14), "✦", font=get_font(20, True), fill='#FFFFFF')
        
    draw_text_centered(draw, "영차의  또또또간집", 730, get_font(46, True), '#1E1B4B')
    draw_text_centered(draw, "‘군산집’을  소개합니다", 800, get_font(50, True), '#111827')
    draw_text_centered(draw, "영등포 전통시장 야장 삼겹살 성지 🥩", 920, get_font(24, False), '#6D28D9')
    
    img.save('images/gunsan_1.jpg', quality=95)

def create_gunsan_2():
    w, h = 800, 1060
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    draw_text_centered(draw, "선선한 바람이 불기 시작한 요즘,", 70, get_font(30, False), '#333333')
    draw_text_centered(draw, "야장에서 맛있는 고기에", 120, get_font(32, True), '#1F2937')
    draw_text_centered(draw, "한 잔하기 딱 ~~~ 좋은 곳 🍻", 170, get_font(32, True), '#6D28D9')
    
    draw.rectangle([40, 240, 760, 800], fill='#F3F4F6', outline='#E5E7EB', width=2)
    for y in range(240, 800, 4):
        draw.line([(40, y), (760, y)], fill=(240 - int((y-240)/10), 242 - int((y-240)/12), 248 - int((y-240)/15)))
    
    draw.rectangle([80, 270, 300, 370], fill='#C2410C')
    draw.text((100, 290), "맛있는집", font=get_font(24, True), fill='#FFFFFF')
    draw.text((100, 325), "군 산 집", font=get_font(30, True), fill='#FFFFFF')
    
    for ox in [350, 540]:
        draw.rectangle([ox, 440, ox+160, 600], fill='#EF4444', outline='#B91C1C', width=3)
        draw.ellipse([ox+10, 450, ox+150, 540], fill='#FCA5A5')
        draw.rectangle([ox+50, 480, ox+110, 520], fill='#10B981')
        draw.text((ox+35, 620), "야장 좌석", font=get_font(20, True), fill='#374151')

    draw.rectangle([80, 660, 720, 760], fill='#1E1B4B')
    draw_text_centered(draw, "✨ 영등포 전통시장 야외 포차 감성 100% 충전 ✨", 695, get_font(24, True), '#FBBF24')

    draw_text_centered(draw, "영등포 시장의 삼겹살 맛집", 860, get_font(30, False), '#374151')
    draw_text_centered(draw, "[ 군산집 ]을 소개합니다 ~! 💜", 915, get_font(36, True), '#6D28D9')
    
    img.save('images/gunsan_2.jpg', quality=95)

def create_gunsan_3():
    w, h = 800, 1060
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([40, 240, 760, 750], fill='#1F2937', outline='#374151', width=4)
    draw.rectangle([80, 280, 720, 420], fill='#FDA4AF', outline='#F43F5E', width=2)
    draw.text((120, 330), "🥩 지글지글 두툼한 생삼겹살 & 생오겹살", font=get_font(26, True), fill='#881337')
    
    draw.rectangle([80, 440, 220, 710], fill='#FEF08A', outline='#CA8A04', width=2)
    draw.text((100, 560), "아삭\n콩나물", font=get_font(24, True), fill='#854D0E')
    
    draw.rectangle([240, 440, 380, 710], fill='#78350F', outline='#451A03', width=2)
    draw.text((260, 560), "고소한\n고사리", font=get_font(24, True), fill='#FEF3C7')
    
    draw.rectangle([400, 440, 540, 710], fill='#86EFAC', outline='#16A34A', width=2)
    draw.text((420, 560), "향긋한\n미나리", font=get_font(24, True), fill='#14532D')

    draw.rectangle([560, 440, 720, 710], fill='#F87171', outline='#DC2626', width=2)
    draw.text((580, 560), "칼칼한\n묵은지", font=get_font(24, True), fill='#7F1D1D')

    draw.rectangle([50, 40, 360, 200], fill='#F3F4F6', outline='#111827', width=3)
    draw.text((70, 60), "와라와라! 와X3!", font=get_font(24, True), fill='#111827')
    draw.text((180, 110), "쩌억~ 😮", font=get_font(34, True), fill='#DC2626')
    draw.text((70, 150), "(행복 폭발 먹방 모드)", font=get_font(18, False), fill='#6B7280')

    draw_text_centered(draw, "기본적으로 올라가는 반찬은", 800, get_font(28, False), '#1F2937')
    draw_text_centered(draw, "콩나물, 고사리, 미나리,", 845, get_font(32, True), '#7C3AED')
    draw_text_centered(draw, "그리고 김치까지!", 890, get_font(32, True), '#6D28D9')
    draw_text_centered(draw, "곁들일 수 있는 반찬이 너무 많아 행복해요.. 🤤", 950, get_font(24, False), '#374151')

    img.save('images/gunsan_3.jpg', quality=95)

def create_gunsan_4():
    w, h = 800, 1060
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([0, 80, w, 86], fill='#3B0764')
    draw.ellipse([30, 83-20, 70, 83+20], fill='#3B0764')
    draw.text((42, 69), "✦", font=get_font(18, True), fill='#FFFFFF')

    draw_text_centered(draw, "!! 다들 주목 !!", 140, get_font(38, True), '#111827')
    draw_text_centered(draw, "사장님께서 강추해주신 이 두 반찬", 200, get_font(30, False), '#374151')
    
    draw.rectangle([60, 270, 740, 730], fill='#FDF4FF', outline='#E9D5FF', width=3)
    
    draw.ellipse([100, 340, 380, 620], fill='#FFFFFF', outline='#D1D5DB', width=3)
    draw.ellipse([130, 370, 350, 590], fill='#FEF9C3')
    draw_text_centered(draw, "🥒 새콤달콤 파프리카 오이 피클", 460, get_font(20, True), '#3F6212', width=480)
    
    draw.ellipse([420, 340, 700, 620], fill='#FFFFFF', outline='#D1D5DB', width=3)
    draw.ellipse([450, 370, 670, 590], fill='#FEF3C7')
    draw_text_centered(draw, "🌶️ 특제 비법 고추장아찌", 460, get_font(20, True), '#92400E', width=1120)

    draw.rectangle([0, 960, w, 966], fill='#3B0764')
    draw.ellipse([730, 963-20, 770, 963+20], fill='#3B0764')
    draw.text((742, 949), "✦", font=get_font(18, True), fill='#FFFFFF')

    draw_text_centered(draw, "특히 매콤하고 아삭한 고추장아찌는", 780, get_font(30, False), '#1F2937')
    draw_text_centered(draw, "고기 한 점에 곁들여 먹기 딱 좋은 조합.. 🤤", 830, get_font(30, True), '#6D28D9')
    draw_text_centered(draw, "기름기를 싹 잡아주는 마법의 킥!", 885, get_font(24, False), '#059669')
    
    img.save('images/gunsan_4.jpg', quality=95)

def create_gunsan_5():
    w, h = 800, 1060
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    
    draw.polygon([(60, 80), (220, 50), (260, 120), (230, 190), (120, 210), (50, 150)], fill='#FFFFFF', outline='#111827')
    draw.text((90, 95), "맛있다!", font=get_font(34, True), fill='#111827')
    
    draw.rectangle([450, 60, 740, 200], fill='#38BDF8', outline='#0284C7', width=3)
    draw_text_centered(draw, "폭 . 력 . 적", 100, get_font(44, True), '#0C4A6E', width=1190)

    draw.rectangle([60, 240, 740, 720], fill='#F0FDF4', outline='#BBF7D0', width=3)
    
    draw.ellipse([120, 300, 680, 660], fill='#4ADE80', outline='#16A34A', width=3)
    draw.rectangle([250, 420, 550, 520], fill='#BE123C', outline='#881337', width=2)
    draw_text_centered(draw, "노릇노릇 삼겹살", 450, get_font(22, True), '#FFFFFF', width=800)
    draw.rectangle([280, 380, 520, 410], fill='#15803D')
    draw.ellipse([460, 480, 520, 540], fill='#FEF08A')
    draw_text_centered(draw, "+ 미나리 + 마늘 + 콩나물", 550, get_font(24, True), '#14532D', width=800)

    draw_text_centered(draw, "저희 영차는 상추 쌈에 미나리, 고기, 마늘,", 760, get_font(26, False), '#1F2937')
    draw_text_centered(draw, "콩나물 조합을 참 좋아합니다.", 805, get_font(26, False), '#1F2937')
    draw_text_centered(draw, "맛없없 조합 맞죠 💜", 860, get_font(34, True), '#7C3AED')
    draw_text_centered(draw, "????????????????????????????", 915, get_font(22, True), '#A78BFA')
    draw_text_centered(draw, "한 입 가득 차오르는 극상의 행복!", 960, get_font(24, True), '#E11D48')

    img.save('images/gunsan_5.jpg', quality=95)

def create_7bun_cards():
    w, h = 800, 1060
    # 7bun_1
    img = Image.new('RGB', (w, h), color='#FAF5FF')
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 240], fill='#4C1D95')
    draw_text_centered(draw, "영등포 전통시장 42년 터줏대감", 60, get_font(28, False), '#DDD6FE')
    draw_text_centered(draw, "시장판 오마카세 ‘7번집’", 120, get_font(48, True), '#FDE047')

    draw.rectangle([50, 280, 750, 720], fill='#FFFFFF', outline='#DDD6FE', width=3)
    draw.rectangle([70, 300, 730, 480], fill='#1E1B4B')
    draw_text_centered(draw, "🏮 7 번 집 🏮", 360, get_font(44, True), '#F87171')
    
    draw.rectangle([100, 510, 700, 690], fill='#FEF3C7', outline='#D97706', width=2)
    draw.text((130, 535), "🐷 쫀득쫀득 돼지꼬리구이", font=get_font(24, True), fill='#92400E')
    draw.text((130, 580), "🐔 매콤달콤 닭발볶음", font=get_font(24, True), fill='#92400E')
    draw.text((130, 625), "🍜 새콤달콤 비빔국수 & 푸짐한 잔치국수", font=get_font(24, True), fill='#92400E')

    draw_text_centered(draw, "“42년의 시간이 쌓인 자리,”", 770, get_font(30, True), '#1F2937')
    draw_text_centered(draw, "편하게 앉아 한잔하고 이야기 나눌 수 있는 곳 🍻", 820, get_font(28, False), '#6D28D9')
    draw_text_centered(draw, "단골부터 MZ 청년, 외국인 손님까지 반하는 로컬 감성", 880, get_font(22, False), '#4B5563')
    draw.rectangle([200, 940, 600, 1000], fill='#7C3AED')
    draw_text_centered(draw, "영차 추천 맛집 #01", 955, get_font(24, True), '#FFFFFF')
    img.save('images/7bun_1.jpg', quality=95)

    # 7bun_2
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 140], fill='#6D28D9')
    draw_text_centered(draw, "7번집 인터뷰 Q&A", 35, get_font(24, False), '#E9D5FF')
    draw_text_centered(draw, "마흔셋, 떡볶이 500원 시절의 시작", 75, get_font(32, True), '#FFFFFF')
    
    draw.rectangle([50, 180, 750, 420], fill='#FAF5FF', outline='#DDD6FE', width=2)
    draw.text((80, 205), "Q. 언제부터 영등포 시장을 지켜오셨나요?", font=get_font(24, True), fill='#6D28D9')
    draw.text((80, 255), "“제가 마흔셋에 시작했으니 벌써 42년이 흘렀네요.\n그 시절엔 떡볶이 한 접시에 500원 하던 때였어요.\n세월은 참 빠르게 흘렀지만 손님들께 푸짐하게 내어드리는\n그 마음만큼은 첫날 그대로입니다.”", font=get_font(21, False), fill='#374151', spacing=10)

    draw.rectangle([50, 460, 750, 720], fill='#FAF5FF', outline='#DDD6FE', width=2)
    draw.text((80, 485), "Q. 요즘 젊은 손님과 외국인들도 많이 찾는다던데요?", font=get_font(24, True), fill='#6D28D9')
    draw.text((80, 535), "“유튜브 보고 찾아오는 청년들도 많고, 외국인들도 와서\n‘원더풀!’ 외치며 돼지꼬리랑 국수를 맛있게 비워요.\n나이 상관없이 다들 둘러앉아 친구가 되는 게\n우리 7번집 시장판 오마카세의 매력이지요.”", font=get_font(21, False), fill='#374151', spacing=10)

    draw.rectangle([50, 760, 750, 980], fill='#FEF3C7', outline='#F59E0B', width=2)
    draw_text_centered(draw, "✨ 사장님의 따뜻한 한마디 ✨", 790, get_font(24, True), '#B45309')
    draw_text_centered(draw, "“영차 청년들 덕분에 시장 골목이 한층 환해졌어!”", 845, get_font(26, True), '#1F2937')
    draw_text_centered(draw, "팝업 기간 동안 7번집의 정겨운 손맛을 꼭 느껴보세요 💜", 905, get_font(22, False), '#6D28D9')
    img.save('images/7bun_2.jpg', quality=95)

    # 7bun_3
    img = Image.new('RGB', (w, h), color='#FAF5FF')
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 140], fill='#5B21B6')
    draw_text_centered(draw, "7번집 시그니처 메뉴 탐구", 35, get_font(24, False), '#DDD6FE')
    draw_text_centered(draw, "술이 술술 들어가는 대표 안주 4선 🍻", 75, get_font(32, True), '#FDE047')

    menus = [
        ("🐷 쫀득 쫄깃 '돼지꼬리'", "씹을수록 고소하고 콜라겐 가득! 7번집 1등 별미"),
        ("🐔 화끈한 불맛 '닭발'", "매콤달콤 비법 양념이 쏙 배어 멈출 수 없는 중독성"),
        ("🍜 새콤달콤 '비빔국수'", "입맛 돋우는 양념장과 아삭한 채소의 꿀조합"),
        ("🍲 넉넉한 인심 '잔치국수'", "진한 멸치 육수에 면이 수북! 속까지 든든하게 풀어주는 맛")
    ]
    for idx, (m_title, m_desc) in enumerate(menus):
        top_y = 170 + idx * 190
        draw.rectangle([50, top_y, 750, top_y + 165], fill='#FFFFFF', outline='#C4B5FD', width=2)
        draw.text((80, top_y + 30), m_title, font=get_font(26, True), fill='#4C1D95')
        draw.text((80, top_y + 85), m_desc, font=get_font(20, False), fill='#4B5563')

    draw.rectangle([0, 960, w, h], fill='#1E1B4B')
    draw_text_centered(draw, "사장님표 덤과 정이 넘치는 7번집으로 오세요!", 990, get_font(24, True), '#FDE047')
    img.save('images/7bun_3.jpg', quality=95)

    # 7bun_4
    img = Image.new('RGB', (w, h), color='#FFFFFF')
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, w, 160], fill='#4338CA')
    draw_text_centered(draw, "영등포 전통시장 속 살아 숨 쉬는 역사", 45, get_font(24, False), '#C7D2FE')
    draw_text_centered(draw, "오늘 저녁은 7번집에서 영차와 한잔? 🍻", 90, get_font(34, True), '#FFFFFF')

    draw.rectangle([50, 200, 750, 700], fill='#EEF2FF', outline='#A5B4FC', width=2)
    draw_text_centered(draw, "📍 위치: 영등포 전통시장 메인 골목 노점 7번", 240, get_font(24, True), '#3730A3')
    draw_text_centered(draw, "🕒 운영: 오후 ~ 늦은 밤까지 정겨운 영업", 290, get_font(22, False), '#4B5563')
    draw_text_centered(draw, "💳 결제: 온누리상품권 / 제로페이 / 현금 환영", 340, get_font(22, False), '#4B5563')
    
    draw.rectangle([90, 410, 710, 650], fill='#FFFFFF', outline='#818CF8', width=2)
    draw_text_centered(draw, "💡 영차 에디터의 방문 팁", 440, get_font(22, True), '#4F46E5')
    draw.text((120, 490), "1. 돼지꼬리와 비빔국수를 함께 시켜 싸 먹으면 감동 두 배!\n2. 사장님께 밝게 인사드리면 넉넉한 덤이 기다립니다 :)\n3. 9/18~19 야시장 기간에 방문하면 더 특별한 추억!", font=get_font(20, False), fill='#374151', spacing=14)

    draw_text_centered(draw, "전통시장의 진짜 매력, 7번집에서 만나요 💜", 770, get_font(30, True), '#6D28D9')
    draw.rectangle([180, 850, 620, 930], fill='#7C3AED')
    draw_text_centered(draw, "야시장 구글폼 참가 신청하기 ➔", 875, get_font(24, True), '#FFFFFF')
    img.save('images/7bun_4.jpg', quality=95)

def create_chuseok_banner():
    w, h = 900, 500
    img = Image.new('RGB', (w, h), color='#FAF5FF')
    draw = ImageDraw.Draw(img)
    
    draw.rectangle([0, 0, w, 110], fill='#4C1D95')
    draw_text_centered(draw, "🌕 2026 추석맞이 전통시장 환급행사 🌾", 25, get_font(22, False), '#DDD6FE', width=w)
    draw_text_centered(draw, "농축산물 구매 고객 온누리상품권 즉시 환급", 60, get_font(28, True), '#FDE047', width=w)

    draw.rectangle([40, 140, 860, 360], fill='#FFFFFF', outline='#DDD6FE', width=3)
    
    draw.rectangle([70, 165, 430, 335], fill='#F5F3FF', outline='#8B5CF6', width=2)
    draw_text_centered(draw, "34,000원 이상 구매 시", 190, get_font(22, False), '#4C1D95', width=500)
    draw_text_centered(draw, "10,000원 환급 🎁", 240, get_font(32, True), '#7C3AED', width=500)
    
    draw.rectangle([470, 165, 830, 335], fill='#FEF3C7', outline='#F59E0B', width=2)
    draw_text_centered(draw, "67,000원 이상 구매 시", 190, get_font(22, False), '#92400E', width=1300)
    draw_text_centered(draw, "20,000원 환급 🎁", 240, get_font(32, True), '#D97706', width=1300)

    draw.rectangle([40, 380, 860, 465], fill='#1E1B4B')
    draw.text((70, 398), "• 대상: 국내산 신선 농축산물 구매 고객 (당일 영수증 지참)", font=get_font(18, False), fill='#E9D5FF')
    draw.text((70, 428), "• 환급처: 시장 내 환급 부스 (1인당 기간 내 한도 적용) | 문의: 02-6956-2254", font=get_font(18, False), fill='#FDE047')

    img.save('images/chuseok_event.jpg', quality=95)

create_gunsan_1()
create_gunsan_2()
create_gunsan_3()
create_gunsan_4()
create_gunsan_5()
create_7bun_cards()
create_chuseok_banner()

print("All card news and banner assets generated successfully!")
