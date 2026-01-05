import streamlit as st

st.title("🎈香香花園專屬AI調香師")
st.write("Let's start building! For help and inspiration.")
import streamlit as st
from datetime import date

# 1. 頁面配置
st.set_page_config(page_title="Aroma's Secret Lab", layout="centered")

# ==========================================
# 資料庫 A：78 種氣味清單 (根據照片整理)
# ==========================================
scent_map = {
    # 前調
    "前調 芳香 01": "富家千金 (小豆蔻/烏龍茶)", "前調 芳香 02": "夏天的風 (羅勒/百里香)",
    "前調 芳香 03": "野花 (小豆蔻/含羞草)", "前調 芳香 04": "肆意奔放 (小豆蔻/馬郁蘭)",
    "前調 芳香 05": "鄉愁 (梔子花/綠葉/甘草)", "前調 芳香 06": "茶樹 (茶樹)",
    "前調 芳香 07": "薄荷 (薄荷)", "前調 芳香 08": "馬鞭草 (馬鞭草)", "前調 芳香 09": "綠茶 (綠茶)",
    "前調 柑橘 01": "花園 (橘子/檸檬/開心果)", "前調 柑橘 02": "記憶蜜糖 (橘子/桃子)",
    "前調 柑橘 03": "寂靜秋夜 (胡蘿蔔/番茄/橙子)", "前調 柑橘 04": "氣泡水 (葡萄柚/橘子)",
    "前調 柑橘 05": "海邊漫步 (橙子/檸檬)", "前調 柑橘 06": "海灘 (佛手柑/檸檬/香橙)",
    "前調 柑橘 07": "純真 (橙子/茉莉/琥珀)", "前調 柑苔 01": "晨間森林 (無花果木/香根草)",
    "前調 柑苔 02": "信仰 (橘子/麝香/苦橙葉)", "前調 柑苔 03": "清新 (葡萄柚/橡木苔)",
    "前調 柑苔 04": "苔蘚 (苔蘚)",
    # 中調
    "中調 果香 01": "夏日莊園 (柑橘/無花果)", "中調 果香 02": "純粹 (香瓜/橘子/黃瓜)",
    "中調 果香 03": "甜美 (草莓/梨/蜜橘)", "中調 果香 04": "情竇初開 (紅漿果/糖)",
    "中調 果香 05": "撒丁島 (橙花油/檸檬)", "中調 果香 06": "仲夏花園 (紅蘋果/玫瑰)",
    "中調 花香 01": "白襯衫 (薰衣草/橙花)", "中調 花香 02": "優雅女人 (晚香玉/茉莉花)",
    "中調 花香 03": "雨後花園 (玫瑰/依蘭)", "中調 花香 04": "靜謐花園 (玫瑰/茉莉)",
    "中調 花香 19": "桂花 (桂花)",
    # 後調
    "後調 東方 01": "雨落幽然 (苦橙/琥珀)", "後調 東方 02": "烏龍茶 (茶葉/香根草)",
    "後調 東方 05": "西西里島 (杏仁/香草/麝香)", "後調 東方 09": "荷爾蒙 (花椒/廣藿香)",
    "後調 木質 01": "冬日松林 (雪松/麝香)", "後調 木質 02": "沉靜森林 (白松香/檀香)",
    "後調 木質 08": "寺廟 (黑胡椒/檀木)", "後調 木質 10": "故鄉 (沉香/廣藿香)",
    "後調 木質 13": "檀香 (檀香)"
}

# ==========================================
# 資料庫 B：星座與心理特徵描述
# ==========================================
zodiac_db = {
    "白羊座": "天生的開拓者，充滿勇氣與活力。", "金牛座": "感官美好的守護者，追求質感生活。",
    "雙子座": "靈動的思想傳播者，充滿好奇心。", "巨蟹座": "細膩的療癒者，重視歸屬與情感。",
    "獅子座": "自信的領導者，散發強大創造力。", "處女座": "追求完美的工匠，擁有極致觀察力。",
    "天秤座": "和諧的協調者，追求優雅與平衡。", "天蠍座": "深邃的洞察者，意志強大且神祕。",
    "射手座": "真理的追求者，熱愛自由與冒險。", "摩羯座": "踏實的攀登者，擁有耐心與責任。",
    "水瓶座": "獨立的革新者，思維超前且獨特。", "雙魚座": "靈性的藝術家，靈魂充滿共情能力。"
}

personality_traits = {
    "芳香": "展現冷靜知性，適合追求邏輯與秩序的你。",
    "柑橘": "象徵親和活力，詮釋你開朗具感染力的性格。",
    "柑苔": "代表獨立探求，符合你追求獨特的自由靈魂。",
    "果香": "充滿生活情趣，對應你熱情且好奇的特質。",
    "花香": "展現優雅感性，呼應你細膩且富共情的內在。",
    "東方": "散發神祕權威，適合意志強大且深邃的你。",
    "木質": "象徵務實穩定，展現值得信賴的執行者風範。"
}
# --- [新增] 生肖資料庫 ---
zodiac_animal_db = {
    "鼠": "機敏靈活，觀察力極強，具備開拓精神。", "牛": "勤奮踏實，意志堅定，值得信賴。",
    "虎": "勇猛果敢，具備領袖氣質與冒險精神。", "兔": "溫柔文雅，心思細膩，追求和諧生活。",
    "龍": "充滿活力，志向遠大，具備天生的影響力。", "蛇": "冷靜神祕，直覺敏銳，處事精明幹練。",
    "馬": "熱情奔放，嚮往自由，行動力與生命力十足。", "羊": "仁慈體貼，富有藝術氣息與同情心。",
    "猴": "聰明伶俐，應變力強，充滿創意與好奇心。", "雞": "勤奮負責，講求效率，擁有獨到的審美。",
    "狗": "忠誠可靠，正義感強，是值得交心的夥伴。", "豬": "真誠厚道，性情豁達，天生自帶福氣。"
}
# --- [新增] 生肖五行對應表 ---
zodiac_elements = {
    "鼠": "水", "豬": "水",
    "虎": "木", "兔": "木",
    "蛇": "火", "馬": "火",
    "猴": "金", "雞": "金",
    "牛": "土", "龍": "土", "羊": "土", "狗": "土"
}

element_traits = {
    "水": "代表靈性與智慧，流動且具備極強的適應力。",
    "木": "代表成長與生機，充滿仁慈之心與向上攀升的能量。",
    "火": "代表熱情與禮儀，散發著溫暖與照亮他人的光芒。",
    "金": "代表剛毅與果斷，擁有高尚的節操與精準的決策力。",
    "土": "代表厚重與信用，象徵著值得信賴的包容力與穩定感。"
}
# --- [強化] 生命靈數資料庫 ---
life_num_detail = {
    "1": "開創數：象徵獨立、自信與天生的領導力。", "2": "合作數：象徵和諧、體貼與優異的協調性。",
    "3": "創意數：象徵熱情、表達與無窮的想像力。", "4": "執行數：象徵穩定、秩序與紮實的實踐力。",
    "5": "冒險數：象徵自由、多變與勇於挑戰的靈魂。", "6": "奉獻數：象徵責任、愛心與對美好的執著。",
    "7": "探求數：象徵智慧、內省與對真理的追求。", "8": "權威數：象徵豐盛、決策與強大的掌控力。",
    "9": "博愛數：象徵慈悲、理想與跨越邊界的視野。"
}
# ==========================================
# 資料庫 C：16 型人格專業配對 (部分範例)
# ==========================================
mbti_db = {
    "INTJ (建築師)": {
        "title": "理性的戰略家",
        "top": ["前調 芳香 01", "前調 柑苔 01", "前調 芳香 05"],
        "mid": ["中調 花香 08", "中調 果香 09", "中調 花香 01"],
        "base": ["後調 木質 10", "後調 東方 02", "後調 木質 08"],
        "logic": "清冷茶香與沈穩木質，為深謀慮的思維提供留白空間。"
    },
    "INFP (調解者)": {
        "title": "溫柔理想主義者",
        "top": ["前調 柑橘 06", "前調 芳香 03", "前調 芳香 02"],
        "mid": ["中調 花香 03", "中調 花香 04", "中調 花香 19"],
        "base": ["後調 東方 05", "後調 木質 01", "後調 木質 02"],
        "logic": "柔軟的花香與包裹感強的後調，守護內心最純粹的理想。"
    },
    "INFJ (提倡者)": {
        "title": "寧靜的預言家",
        "top": ["前調 芳香 09", "前調 柑苔 04", "前調 芳香 05"],
        "mid": ["中調 花香 02", "中調 花香 06", "中調 花香 14"],
        "base": ["後調 木質 11", "後調 東方 04", "後調 木質 07"],
        "logic": "幽靜的綠茶與焚香，體現出深邃且具備靈性的洞察力。"
    },
    "ENFP (競選者)": {
        "title": "熱情的創意家",
        "top": ["前調 柑橘 04", "前調 柑橘 02", "前調 果香 03"],
        "mid": ["中調 果香 04", "中調 花香 07", "中調 果香 06"],
        "base": ["後調 東方 06", "後調 東方 11", "後調 木質 13"],
        "logic": "明亮跳躍的氣泡感與甜美果香，展現無窮的感染力。"
    },
    "ISTJ (物流師)": {
        "title": "務實的守護者",
        "top": ["前調 芳香 06", "前調 柑苔 02", "前調 芳香 08"],
        "mid": ["中調 花香 01", "中調 花香 08", "中調 果香 12"],
        "base": ["後調 木質 05", "後調 木質 03", "後調 木質 10"],
        "logic": "潔淨的草本與紮實的雪松，呼應嚴謹且可靠的職業風範。"
    },
    "ISFJ (守衛者)": {
        "title": "細膩的照顧者",
        "top": ["前調 柑橘 07", "前調 芳香 02", "前調 柑橘 01"],
        "mid": ["中調 花香 09", "中調 花香 12", "中調 花香 18"],
        "base": ["後調 木質 02", "後調 東方 08", "後調 木質 01"],
        "logic": "溫潤的花香與暖感木質，營造出如家一般安心的避風港。"
    },
    "ENTJ (指揮官)": {
        "title": "果斷的領導者",
        "top": ["前調 芳香 04", "前調 柑苔 01", "前調 柑橘 03"],
        "mid": ["中調 果香 05", "中調 花香 11", "中調 果香 01"],
        "base": ["後調 東方 09", "後調 木質 08", "後調 東方 10"],
        "logic": "強烈的辛香與廣藿香，奠定不容置疑的權威與執行氣場。"
    },
    "ENTP (辯論家)": {
        "title": "靈動的創新者",
        "top": ["前調 柑橘 04", "前調 芳香 07", "前調 柑苔 03"],
        "mid": ["中調 果香 08", "中調 果香 07", "中調 花香 17"],
        "base": ["後調 東方 03", "後調 東方 09", "後調 木質 11"],
        "logic": "充滿層次與反轉的冷熱調性，呼應其敏捷且具挑戰性的思維。"
    },
    "ENFJ (主人公)": {
        "title": "具感染力的領袖",
        "top": ["前調 柑橘 07", "前調 芳香 09", "前調 柑橘 05"],
        "mid": ["中調 花香 05", "中調 花香 09", "中調 果香 06"],
        "base": ["後調 木質 13", "後調 東方 08", "後調 木質 12"],
        "logic": "明亮陽光的花香調，傳遞溫暖且積極正向的領袖能量。"
    },
    "ESTJ (總經理)": {
        "title": "卓越的管理者",
        "top": ["前調 芳香 02", "前調 柑橘 05", "前調 芳香 08"],
        "mid": ["中調 花香 01", "中調 果香 11", "中調 果香 12"],
        "base": ["後調 木質 03", "後調 木質 08", "後調 木質 10"],
        "logic": "俐落的柑橘與沈穩檀木，體現高效能與秩序感。"
    },
    "ESFJ (執政官)": {
        "title": "熱心的社交家",
        "top": ["前調 果香 03", "前調 柑橘 02", "前調 柑橘 01"],
        "mid": ["中調 花香 14", "中調 花香 16", "中調 果香 10"],
        "base": ["後調 東方 06", "後調 木質 13", "後調 東方 11"],
        "logic": "親切甜美的花果香，讓社交場合充滿溫馨與和諧感。"
    },
    "ISTP (鑑賞家)": {
        "title": "冷靜的行動派",
        "top": ["前調 芳香 07", "前調 柑苔 03", "前調 芳香 06"],
        "mid": ["中調 果香 09", "中調 花香 08", "中調 果香 14"],
        "base": ["後調 木質 06", "後調 木質 12", "後調 東方 02"],
        "logic": "冷冽的薄荷與空靈的沉香，體現極簡且獨立的風格。"
    },
    "ISFP (探險家)": {
        "title": "感性的藝術家",
        "top": ["前調 柑橘 03", "前調 芳香 03", "前調 柑橘 06"],
        "mid": ["中調 花香 07", "中調 果香 02", "中調 花香 03"],
        "base": ["後調 木質 07", "後調 東方 05", "後調 木質 04"],
        "logic": "流動的自然氣息與感性木質，共鳴藝術性的感官體驗。"
    },
    "ESTP (企業家)": {
        "title": "大膽的開拓者",
        "top": ["前調 柑橘 04", "前調 柑苔 01", "前調 芳香 04"],
        "mid": ["中調 果香 07", "中調 果香 08", "中調 果香 13"],
        "base": ["後調 東方 07", "後調 東方 09", "後調 木質 12"],
        "logic": "能量爆發的柑橘與具有侵略性的東方調，展現冒險精神。"
    },
    "ESFP (表演者)": {
        "title": "閃耀的社交星",
        "top": ["前調 柑橘 02", "前調 柑橘 04", "前調 果香 04"],
        "mid": ["中調 花香 10", "中調 花香 13", "中調 果香 15"],
        "base": ["後調 東方 11", "後調 東方 06", "後調 東方 01"],
        "logic": "華麗奪目的花果香，讓每個瞬間都像是在舞台中央。"
    },
    "INTP (邏輯學家)": {
        "title": "冷靜的思考者",
        "top": ["前調 芳香 01", "前調 芳香 09", "前調 柑苔 04"],
        "mid": ["中調 果香 14", "中調 花香 06", "中調 果香 09"],
        "base": ["後調 木質 06", "後調 木質 11", "後調 東方 02"],
        "logic": "低調且神祕的沉香與茶香，支撐起無邊無際的思考海洋。"
    }
}

# ==========================================
# 核心邏輯處理函數
# ==========================================
def translate_scents(code_list):
    """
    優化後的翻譯函數：
    1. 隱藏「前調 芳香 01」等編號。
    2. 標題僅顯示「優雅女人」等名稱。
    3. 自動關聯心理映射描述。
    """
    html_snippets = []
    for i, code in enumerate(code_list):
        # 抓取完整的字典資訊
        full_info = scent_map.get(code, f"{code} (專屬配方)")
        
        # --- 核心邏輯：拆分「名稱」與「成分描述」 ---
        # 假設格式為：富家千金 (小豆蔻/烏龍茶)
        if " (" in full_info:
            display_name, ingredients = full_info.split(" (", 1)
            ingredients = "(" + ingredients # 補回括號
        else:
            display_name, ingredients = full_info, ""
        
        # 根據編號抓取心理映射描述
        trait_desc = "這款香氣能平衡能量，展現獨特氣場。"
        for key in personality_traits:
            if key in code:
                trait_desc = personality_traits[key]
                break

        # 組合精美 HTML 區塊
        snippet = f"""
        <div style='margin-bottom:12px; padding: 10px; border-radius: 10px; background: rgba(255,255,255,0.45); border: 0.5px solid #eee;'>
            <div style='color: #8B4513; font-weight: bold; font-size: 14px;'>⭐ 方案 {i+1}: {display_name}</div>
            <div style='font-size: 11px; color: #666; margin-top: 2px;'>{ingredients}</div>
            <div style='font-size: 10px; color: #9E7E6B; margin-top: 5px; border-top: 0.5px solid #E0D5C1; padding-top: 5px; line-height: 1.4;'>
                <i><b>心理映射：</b>{trait_desc}</i>
            </div>
        </div>
        """
        html_snippets.append(snippet)
    return "".join(html_snippets)

def get_life_num(bday):
    d = "".join(filter(str.isdigit, str(bday)))
    while len(d) > 1: d = str(sum(int(x) for x in d))
    return d

def get_zodiac(m, d):
    signs = [(1,20,"摩羯座"),(2,19,"水瓶座"),(3,21,"雙魚座"),(4,20,"白羊座"),(5,21,"金牛座"),(6,22,"雙子座"),(7,23,"巨蟹座"),(8,23,"獅子座"),(9,23,"處女座"),(10,24,"天秤座"),(11,23,"天蠍座"),(12,22,"射手座"),(12,31,"摩羯座")]
    for mm, dd, s in signs:
        if m < mm or (m == mm and d <= dd): return s
    return "摩羯座"
def get_chinese_zodiac(year):
    animals = ["猴", "雞", "狗", "豬", "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊"]
    return animals[year % 12]

# ==========================================
# 介面顯示區
# ==========================================
st.title("🧪 Aroma's Secret Lab")

c1, c2 = st.columns(2)
with c1:
    birthday = st.date_input("📅 出生年月日", value=date(2000, 1, 1))
    occasion = st.selectbox("🏙️ 使用場合", ["日常通勤", "約會派對", "商務正式", "運動休閒", "冥想睡眠"])
with c2:
    mbti_choice = st.selectbox("🧠 MBTI 人格", list(mbti_db.keys()))

perfume_logic = {
    "日常通勤": {"type": "EDT", "strength": "10%", "ratio": [3, 4, 3], "oil": 1.0},
    "約會派對": {"type": "EDP", "strength": "15%", "ratio": [2, 3, 5], "oil": 1.5},
    "商務正式": {"type": "EDP", "strength": "12%", "ratio": [2.5, 4.5, 3], "oil": 1.2},
    "運動休閒": {"type": "Cologne", "strength": "5%", "ratio": [5, 3, 2], "oil": 0.8},
    "冥想睡眠": {"type": "Mist", "strength": "5%", "ratio": [2, 5, 3], "oil": 0.8}
}

if st.button("🔮 啟動 AI 深度分析"):
    res = mbti_db[mbti_choice]
    occ = perfume_logic[occasion]
    l_num = get_life_num(birthday)
    z_name = get_zodiac(birthday.month, birthday.day)
    c_zodiac = get_chinese_zodiac(birthday.year) 
    
    # --- [新增] 獲取五行屬性 ---
    c_element = zodiac_elements[c_zodiac]
    element_desc = element_traits[c_element]
    
    st.balloons()

    # 更新後的卡片 HTML (加上五行標籤)
    card_html = f"""
    <div style="background-color: white; padding: 25px; border-radius: 20px; border: 2px solid #1a1a1a; box-shadow: 8px 8px 0px #F5F5F5; color: #333;">
        <h2 style="margin:0; color: #8B4513;">🧬 AI 全維度調香處方</h2>
        
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 15px;">
            <span style="background: #E8F0FE; padding: 4px 10px; border-radius: 12px; font-size: 11px;"><b>🌠 星座：</b>{z_name}</span>
            <span style="background: #FFF0F0; padding: 4px 10px; border-radius: 12px; font-size: 11px;"><b>🏮 生肖：</b>{c_zodiac}({c_element}行)</span>
            <span style="background: #F0FDF4; padding: 4px 10px; border-radius: 12px; font-size: 11px;"><b>🔢 靈數：</b>{l_num}號人</span>
        </div>

        <div style="font-size: 12px; color: #666; margin-top: 15px; line-height: 1.5; background: #FAFAFA; padding: 10px; border-radius: 10px;">
            • <b>{z_name}：</b>{zodiac_db[z_name]}<br>
            • <b>生肖{c_zodiac}({c_element})：</b>{zodiac_animal_db[c_zodiac]} {element_desc}<br>
            • <b>生命靈數：</b>{life_num_detail[l_num]}
        </div>

        <hr style="margin: 18px 0; border: 0.5px dashed #ccc;">
        
        <div style="background: #F0F4F8; padding: 10px; border-radius: 8px; margin-bottom: 12px;">
            <p style="font-size: 13px; margin:0;"><b>🎯 推薦濃度：{occ['type']} ({occ['strength']}) - 【{occasion}】</b></p>
        </div>

        <div style="margin-bottom: 8px; border-left: 5px solid #D4AF37; padding-left: 10px; background: #FFF9F0; padding-top: 6px; padding-bottom: 6px;">
            <p style="font-size: 13px; font-weight: bold; margin:0 0 5px 0;">【前調建議】(三選一)</p>
            {translate_scents(res['top'])}
        </div>
        <div style="margin-bottom: 8px; border-left: 5px solid #D4AF37; padding-left: 10px; background: #FFF9F0; padding-top: 6px; padding-bottom: 6px;">
            <p style="font-size: 13px; font-weight: bold; margin:0 0 5px 0;">【中調建議】(三選一)</p>
            {translate_scents(res['mid'])}
        </div>
        <div style="margin-bottom: 8px; border-left: 5px solid #D4AF37; padding-left: 10px; background: #FFF9F0; padding-top: 6px; padding-bottom: 6px;">
            <p style="font-size: 13px; font-weight: bold; margin:0 0 5px 0;">【後調建議】(三選一)</p>
            {translate_scents(res['base'])}
        </div>
        
        <p style="font-size: 11px; font-style: italic; color: #888; border-top: 1px dashed #ddd; padding-top: 8px; margin-top: 8px;">
            <b>💡 調香邏輯：</b>{res['logic']}
        </p>
    </div>
    """.replace("\n", "")

    st.markdown(card_html, unsafe_allow_html=True)


    # 配比顯示
    st.write(f"### 🧪 10ml 調製比例 ({occ['type']})")
    v1, v2, v3 = st.columns(3)
    v1.metric("前調 ml", f"{occ['ratio'][0]/10 * occ['oil']:.2f}")
    v2.metric("中調 ml", f"{occ['ratio'][1]/10 * occ['oil']:.2f}")
    v3.metric("後調 ml", f"{occ['ratio'][2]/10 * occ['oil']:.2f}")

