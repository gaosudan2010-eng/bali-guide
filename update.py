import os
import datetime
import json

def generate_html(data):
    # Itinerary Data Structure
    itinerary = [
        {
            "day": 1,
            "date": "2月11日",
            "title": "出发！飞往众神之岛",
            "hotel": "The Westin Resort Nusa Dua",
            "desc": """
                <b>✈️ 飞行计划：</b><br>
                • <b>第一程：</b>北京首都 (PEK) 07:30 ➔ 香港 (HKG) 11:05 (CX347)<br>
                • <b>第二程：</b>香港 (HKG) 12:35 ➔ 巴厘岛 (DPS) 17:35 (CX785)<br>
                <br>
                <b>🚕 交通接驳：</b><br>
                抵达巴厘岛机场 (Ngurah Rai) 后，完成入境及海关申报。由于带着三岁宝宝且行李较多，建议提前预订酒店接机或使用 Grab/Klook 专车。车程约 20-30 分钟。
                <br><br>
                <b>🍽️ 晚餐建议：</b><br>
                • <b>首选：Ikan Restaurant</b> (威斯汀酒店内)。在沙滩边吹海风享用印尼烧烤，宝宝可以直接在旁边的沙滩玩耍。<br>
                • <b>备选：Prego</b> (威斯汀内意大利餐厅)。有专门的儿童菜单和游戏区，三岁宝宝绝对坐得住。
            """,
            "pois": [
                {"name": "巴厘岛国际机场 (DPS)", "lat": -8.7482, "lon": 115.1675, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g294226-d2279188-Reviews-Ngurah_Rai_International_Airport-Kuta_Bali.html"},
                {"name": "The Westin Resort Nusa Dua", "lat": -8.7941, "lon": 115.2302, "type": "hotel", "link": "https://www.tripadvisor.cn/Hotel_Review-g297698-d302324-Reviews-The_Westin_Resort_Nusa_Dua_Bali-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"}
            ],
            "tips": """
                <b>🛡️ 专业导游提醒：</b><br>
                1. <b>香港转机：</b>1.5小时较紧凑，下飞机后请迅速寻找 'Transfer' 指引。<br>
                2. <b>入境：</b>购买 VOA ➔ 边检 ➔ 提行李 ➔ 扫海关码 (e-CD)。<br>
                3. <b>接机口：</b>走出玻璃门后，在密集的牌子中寻找写有您名字或 'Westin' 的接机员。
            """
        },
        {
            "day": 2,
            "date": "2月12日",
            "title": "努沙杜瓦：阳光、沙滩与童话",
            "hotel": "The Westin Resort Nusa Dua",
            "desc": """
                <b>🏖️ 全日安排：</b><br>
                • <b>上午：</b>威斯汀儿童俱乐部 (Westin Family Kids Club)。这是全岛顶尖的托管中心，有手工、乐高和户外游戏。<br>
                • <b>下午：</b>在努沙杜瓦宁静的海滩玩沙，或在酒店的亲子泳池嬉水。这里海浪极小，非常适合三岁宝宝。<br>
                <br>
                <b>🍽️ 午晚餐建议：</b><br>
                • <b>午餐：Seasonal Tastes</b> (酒店内)。提供丰富的国际自助和零点，环境通透。<br>
                • <b>晚餐：The Pirate's Bay</b> (步行或打车 5 分钟)。这是一个以海盗为主题的海滨餐厅，有一艘巨大的木制海盗船和许多树屋，宝宝可以变身“小海盗”。
            """,
            "pois": [
                {"name": "Westin Family Kids Club", "lat": -8.7945, "lon": 115.2310, "type": "kids", "link": "https://www.marriott.com/en-us/hotels/dpswi-the-westin-resort-nusa-dua-bali/overview/"},
                {"name": "The Pirate's Bay Bali", "lat": -8.7925, "lon": 115.2335, "type": "dining", "link": "https://www.tripadvisor.cn/Restaurant_Review-g297698-d3493863-Reviews-The_Pirate_s_Bay-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"}
            ],
            "tips": "💡 导游建议：威斯汀的 Kids Club 有些课程需要提前预约，建议早餐后先去前台领一份当天的活动表。"
        },
        {
            "day": 3,
            "date": "2月13日",
            "title": "悬崖日落与海上火舞",
            "hotel": "The Westin Resort Nusa Dua",
            "desc": """
                <b>📷 行程亮点：</b><br>
                • <b>上午：</b>Waterblow。观看巨大的浪花在礁石间喷涌而出的壮观场景。<br>
                • <b>下午：</b>包车前往乌鲁瓦图 (Uluwatu)。参观悬崖上的情人崖神庙。傍晚在悬崖剧场观看举世闻名的 Kecak 火舞表演 (18:00 开始)。<br>
                <br>
                <b>🍽️ 晚餐建议：</b><br>
                • <b>特色推荐：Jimbaran Seafood</b> (金巴兰海滩)。看完表演后回程经过，在沙滩上吃烛光海鲜。虽然有点游客化，但仪式感拉满。
            """,
            "pois": [
                {"name": "Waterblow", "lat": -8.8012, "lon": 115.2355, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297698-d3527715-Reviews-Water_Blow-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"},
                {"name": "Uluwatu Temple (情人崖)", "lat": -8.8291, "lon": 115.0849, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379333-Reviews-Uluwatu_Temple-Uluwatu_Bukit_Peninsula_Bali.html"}
            ],
            "tips": "🐒 避坑警报：乌鲁瓦图情人崖的猴子非常调皮，请务必藏好您的眼镜、帽子和车钥匙！"
        },
        {
            "day": 4,
            "date": "2月14日",
            "title": "逃离城市，潜入乌布丛林",
            "hotel": "Maya Ubud Resort & Spa",
            "desc": """
                <b>🌿 换宿之旅：</b><br>
                • <b>上午：</b>退房后包车前往乌布。中途停留 <b>Tegenungan Waterfall</b>。瀑布气势磅礴，可以在岸边拍照。<br>
                • <b>下午：</b>入住 Maya Ubud。这是一个被森林环抱的世外桃源。带宝宝在河畔无边泳池玩耍，听溪水声。<br>
                <br>
                <b>🍽️ 晚餐建议：</b><br>
                • <b>首选：Bebek Bengil (Dirty Duck Diner)</b>。巴厘岛最著名的脏鸭餐。餐厅后面有一大片稻田，宝宝可以跑来跑去，环境极佳。
            """,
            "pois": [
                {"name": "Tegenungan Waterfall", "lat": -8.5752, "lon": 115.2903, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d8525287-Reviews-Tegenungan_Waterfall-Ubud_Gianyar_Regency_Bali.html"},
                {"name": "Bebek Bengil (脏鸭餐)", "lat": -8.5147, "lon": 115.2647, "type": "dining", "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d786438-Reviews-Bebek_Bengil-Ubud_Gianyar_Regency_Bali.html"}
            ],
            "tips": "🧳 交通贴士：努沙杜瓦到乌布车程约 1.5 小时，路况可能拥堵，请给宝宝备好零食和水。"
        },
        {
            "day": 5,
            "date": "2月15日",
            "title": "丛林里的精灵与意式下午茶",
            "hotel": "Maya Ubud Resort & Spa",
            "desc": """
                <b>🐒 探索乌布：</b><br>
                • <b>上午：</b>圣猴森林 (Sacred Monkey Forest)。在古树参天的森林里看猴子嬉戏。这里的猴子相对礼貌，但仍建议保持距离。<br>
                • <b>下午：</b>前往 <b>Milk & Madu Ubud</b>。这是全乌布最推荐的亲子餐厅，有专门的儿童游戏室和极其好吃的披萨/下午茶。<br>
                <br>
                <b>🍽️ 晚餐建议：</b><br>
                • <b>亲子推荐：Clear Cafe</b>。极具设计感的餐厅，进门要脱鞋，宝宝可以在软垫上爬，食物新鲜且健康。
            """,
            "pois": [
                {"name": "Sacred Monkey Forest (圣猴林)", "lat": -8.5188, "lon": 115.2585, "type": "kids", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379334-Reviews-Sacred_Monkey_Forest_Sanctuary-Ubud_Gianyar_Regency_Bali.html"},
                {"name": "Milk & Madu Ubud", "lat": -8.5065, "lon": 115.2625, "type": "dining", "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d14144365-Reviews-Milk_Madu_Ubud-Ubud_Gianyar_Regency_Bali.html"}
            ],
            "tips": "👟 穿衣建议：乌布步行较多且路面不平，请给宝宝穿上防滑舒适的运动鞋。"
        },
        {
            "day": 6,
            "date": "2月16日",
            "title": "绿色梯田与圣泉洗礼",
            "hotel": "Maya Ubud Resort & Spa",
            "desc": """
                <b>🙏 文化沉浸：</b><br>
                • <b>上午：</b>德格拉朗梯田 (Tegalalang)。感受巴厘岛标志性的绿色波浪。随后前往圣泉寺 (Tirta Empul)，看信徒在泉水中祈福。<br>
                • <b>下午：</b>回到酒店享受 Spa 或继续在森林中放空。<br>
                <br>
                <b>🍽️ 晚餐建议：</b><br>
                • <b>告别晚宴：Sayan House</b>。俯瞰阿勇河谷的壮丽景色，主打日系和印尼融合菜，日落时分美得令人心碎。需要提前预约。
            """,
            "pois": [
                {"name": "Tegalalang Rice Terrace", "lat": -8.4312, "lon": 115.2800, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d2279188-Reviews-Tegalalang_Rice_Terrace-Ubud_Gianyar_Regency_Bali.html"},
                {"name": "Tirta Empul Temple (圣泉寺)", "lat": -8.4162, "lon": 115.2895, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379331-Reviews-Tirta_Empul_Temple-Ubud_Gianyar_Regency_Bali.html"}
            ],
            "tips": "📸 摄影建议：德格拉朗梯田建议 9 点前到达，光线最美且避开人群。"
        },
        {
            "day": 7,
            "date": "2月17日",
            "title": "带上回忆，启程回家",
            "hotel": "Regala Skycity Hotel (Hong Kong)",
            "desc": """
                <b>✈️ 飞行计划：</b><br>
                • <b>第一程：</b>巴厘岛 (DPS) 16:20 ➔ 香港 (HKG) 21:10 (CX784)<br>
                • <b>第二程：</b>香港 (HKG) 10:15 ➔ 北京 (PEK) 13:50 (次日 CX348)<br>
                <br>
                <b>🏨 中转安排：</b><br>
                落地香港后直接入住 Regala Skycity。酒店与 11 SKIES 航天城直连，如果您还有精力，可以去买点礼物。<br>
                <br>
                <b>🍽️ 早餐建议：</b><br>
                • 次日早餐可以在酒店享用，也可以在香港机场尝试著名的<b>何洪记</b>或<b>太兴</b>烧味，作为旅行圆满结束。
            """,
            "pois": [
                {"name": "Regala Skycity Hotel", "lat": 22.2985, "lon": 113.9360, "type": "hotel", "link": "https://www.tripadvisor.cn/Hotel_Review-g294217-d23821034-Reviews-Regala_Skycity_Hotel-Hong_Kong.html"},
                {"name": "11 SKIES 航天城", "lat": 22.3000, "lon": 113.9380, "type": "attraction", "link": "https://www.11skies.com/zh-hk"}
            ],
            "tips": "🛍️ 购物提示：巴厘岛出境前可以买一点椰子饼干或手工皂。回程行李在值机时务必确认是否直挂北京。"
        }
    ]

    html_template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>巴厘岛 7 日亲子行程 | songsong的小跟班</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

        :root {
            --primary: #00B4DB;
            --primary-dark: #0083B0;
            --accent: #FF9F43;
            --kids: #FF78B4;
            --dining: #4BC0C0;
            --bg-gradient: linear-gradient(180deg, #F0F9FF 0%, #FFFFFF 100%);
            --card-bg: rgba(255, 255, 255, 0.95);
            --text-main: #1E293B;
            --text-sub: #64748B;
            --medical-red: #EF4444;
            --glass-bg: rgba(255, 255, 255, 0.7);
            --glass-border: rgba(255, 255, 255, 0.3);
        }

        * { box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        
        body {
            font-family: 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', 'Outfit', sans-serif;
            background: var(--bg-gradient);
            color: var(--text-main);
            margin: 0;
            padding: 0;
            min-height: 100vh;
        }

        .app-container {
            max-width: 480px;
            margin: 0 auto;
            background: #fff;
            min-height: 100vh;
            position: relative;
            box-shadow: 0 0 40px rgba(0,0,0,0.05);
        }

        /* Hero Header */
        .hero {
            position: relative;
            height: 200px;
            background: url('https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=800&q=80') center/cover;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 30px 20px;
            color: white;
            border-bottom-left-radius: 40px;
            border-bottom-right-radius: 40px;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(to bottom, rgba(0,0,0,0) 40%, rgba(0,0,0,0.7) 100%);
        }

        .hero-content { position: relative; z-index: 1; }
        .hero h1 { margin: 0; font-size: 28px; font-weight: 700; letter-spacing: -0.5px; }
        .hero p { margin: 5px 0 0; opacity: 0.9; font-weight: 300; font-size: 13px; }

        .content-body { padding: 20px; }

        /* Dashboard Grid */
        .stats-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: -50px;
            position: relative;
            z-index: 10;
        }

        .stat-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            padding: 15px;
            border-radius: 20px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            border: 1px solid var(--glass-border);
            text-align: center;
        }

        .stat-card i { font-size: 20px; color: var(--primary); margin-bottom: 8px; }
        .stat-card span { display: block; font-size: 10px; color: var(--text-sub); text-transform: uppercase; letter-spacing: 0.5px; }
        .stat-card strong { display: block; font-size: 15px; margin-top: 4px; color: var(--text-main); }

        /* Day Tabs */
        .day-tabs {
            display: flex;
            overflow-x: auto;
            gap: 10px;
            margin: 25px 0 15px;
            padding-bottom: 10px;
            scrollbar-width: none; /* Firefox */
        }
        .day-tabs::-webkit-scrollbar { display: none; }
        .tab {
            flex: 0 0 auto;
            padding: 10px 20px;
            border-radius: 15px;
            background: #F1F5F9;
            color: var(--text-sub);
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s;
        }
        .tab.active {
            background: var(--primary);
            color: white;
            box-shadow: 0 4px 12px rgba(0, 180, 219, 0.3);
        }

        /* Itinerary Content */
        .itinerary-card {
            background: white;
            border-radius: 24px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            margin-bottom: 25px;
            border: 1px solid #F1F5F9;
        }
        .itinerary-card h2 { margin: 0 0 10px; font-size: 20px; color: var(--primary-dark); }
        .itinerary-card .hotel-badge {
            display: inline-block;
            background: #F0F9FF;
            color: var(--primary-dark);
            padding: 4px 12px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 600;
            margin-bottom: 15px;
        }
        .itinerary-card p { font-size: 14px; line-height: 1.6; color: var(--text-main); margin-bottom: 10px; }

        .poi-item {
            display: flex;
            align-items: center;
            padding: 12px;
            background: #F8FAFC;
            border-radius: 15px;
            margin-bottom: 10px;
            gap: 12px;
            text-decoration: none;
            color: inherit;
        }
        .poi-icon {
            width: 36px;
            height: 36px;
            background: white;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--primary);
        }
        .poi-info { flex: 1; }
        .poi-info strong { display: block; font-size: 14px; }
        .poi-info span { font-size: 11px; color: var(--text-sub); }

        /* Tips Card */
        .tips-card {
            background: #FFF7ED;
            padding: 15px;
            border-radius: 18px;
            border: 1px solid #FFEDD5;
            margin-bottom: 20px;
        }
        .tips-card p { margin: 0; font-size: 13px; color: #9A3412; line-height: 1.5; }

        /* Map Section */
        #map {
            height: 220px;
            border-radius: 24px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.05);
            border: 4px solid white;
            margin-bottom: 25px;
        }

        /* Medical Alert */
        .medical-alert {
            background: #FEF2F2;
            padding: 20px;
            border-radius: 24px;
            border: 1px dashed #FCA5A5;
        }
        .medical-alert h4 { margin: 0 0 10px; color: var(--medical-red); display: flex; align-items: center; gap: 8px; }
        .medical-alert p { margin: 0; font-size: 13px; color: #7F1D1D; }

        .footer {
            text-align: center;
            padding: 40px 20px;
            font-size: 12px;
            color: var(--text-sub);
            background: #F8FAFC;
        }

        .update-badge {
            background: rgba(255,255,255,0.2);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 10px;
            display: inline-block;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="app-container">
        <header class="hero">
            <div class="hero-content">
                <div class="update-badge">最后更新: {UPDATE_TIME}</div>
                <h1>巴厘岛 7 日游</h1>
                <p>你好 松松！为您定制的亲子行程已就绪。</p>
            </div>
        </header>
        
        <div class="content-body">
            <div class="stats-grid">
                <div class="stat-card">
                    <i class="fas fa-cloud-sun"></i>
                    <span>当地天气</span>
                    <strong>{WEATHER}</strong>
                </div>
                <div class="stat-card">
                    <i class="fas fa-coins"></i>
                    <span>人民币汇率</span>
                    <strong>{EXCHANGE}</strong>
                </div>
            </div>

            <div class="day-tabs" id="dayTabs">
                <!-- Tabs will be injected by JS -->
            </div>

            <div id="map"></div>

            <div id="dayContent">
                <!-- Itinerary content will be injected by JS -->
            </div>

            <div class="section-header">
                <h2>管家建议</h2>
            </div>
            <div class="medical-alert">
                <h4><i class="fas fa-hospital-user"></i> 紧急医疗 & 安全</h4>
                <p><strong>BIMC Nusa Dua:</strong> +62 361 3000 911<br><strong>备忘:</strong> 坚持使用瓶装水刷牙，备好 Norit 活性炭预防 Bali Belly。</p>
            </div>
        </div>
        
        <footer class="footer">
            <p>由 <strong>songsong的小跟班</strong> 为您精心打造</p>
            <p>V11.0 专业导游全流程版 | 专属 AI 助手</p>
        </footer>
    </div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        const itineraryData = {ITINERARY_JSON};
        let currentDay = 1;
        let map, markersGroup, polyline;

        function initMap() {
            map = L.map('map', {zoomControl: false}).setView([-8.7941, 115.2302], 12);
            L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
                attribution: '©OpenStreetMap'
            }).addTo(map);
            markersGroup = L.layerGroup().addTo(map);
        }

        function updateDay(day) {
            currentDay = day;
            const data = itineraryData.find(d => d.day === day);
            
            // Update Tabs
            const tabsHtml = itineraryData.map(d => `
                <div class="tab ${d.day === day ? 'active' : ''}" onclick="updateDay(${d.day})">
                    Day ${d.day}<br><span style="font-size: 10px; font-weight: normal;">${d.date}</span>
                </div>
            `).join('');
            document.getElementById('dayTabs').innerHTML = tabsHtml;

            // Update Content
            const poisHtml = data.pois.map(poi => `
                <a href="${poi.link}" class="poi-item" target="_blank">
                    <div class="poi-icon"><i class="fas fa-${poi.type === 'hotel' ? 'hotel' : (poi.type === 'dining' ? 'utensils' : (poi.type === 'kids' ? 'child' : 'map-marker-alt'))}"></i></div>
                    <div class="poi-info">
                        <strong>${poi.name}</strong>
                        <span>点击查看详情</span>
                    </div>
                    <i class="fas fa-external-link-alt" style="font-size: 12px; color: #cbd5e1;"></i>
                </a>
            `).join('');

            const tipsHtml = data.tips ? `<div class="tips-card"><p>${data.tips}</p></div>` : '';

            document.getElementById('dayContent').innerHTML = `
                <div class="itinerary-card">
                    <div class="hotel-badge"><i class="fas fa-bed"></i> 入住: ${data.hotel}</div>
                    <h2>${data.title}</h2>
                    <p>${data.desc}</p>
                    ${tipsHtml}
                    <h3 style="font-size: 14px; margin-bottom: 12px; color: var(--text-sub);">行程目的地:</h3>
                    ${poisHtml}
                </div>
            `;

            // Update Map
            markersGroup.clearLayers();
            if (polyline) polyline.remove();

            const latlngs = data.pois.map(p => [p.lat, p.lon]);
            data.pois.forEach(p => {
                L.marker([p.lat, p.lon]).addTo(markersGroup).bindPopup(p.name);
            });

            if (latlngs.length > 1) {
                polyline = L.polyline(latlngs, {color: 'var(--primary)', weight: 3, dashArray: '5, 10'}).addTo(map);
                map.fitBounds(polyline.getBounds(), {padding: [50, 50]});
            } else if (latlngs.length === 1) {
                map.setView(latlngs[0], 14);
            }
        }

        window.onload = () => {
            initMap();
            updateDay(1);
        };
    </script>
</body>
</html>
"""
    
    # Process itinerary data to JSON
    itinerary_json = json.dumps(itinerary, ensure_ascii=False)
    
    # Replace placeholders
    html_content = html_template.replace("{UPDATE_TIME}", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
    html_content = html_content.replace("{WEATHER}", data.get('weather', '28°C'))
    html_content = html_content.replace("{EXCHANGE}", data.get('exchange_rate', '2,215'))
    html_content = html_content.replace("{ITINERARY_JSON}", itinerary_json)
    
    return html_content

if __name__ == "__main__":
    # Get from env
    data = {
        'weather': os.getenv('WEATHER_INFO', '巴厘岛 27°C 晴'),
        'exchange_rate': os.getenv('EXCHANGE_RATE', '1 CNY ≈ 2,410 IDR')
    }
    
    html_content = generate_html(data)
    dashboard_path = '/Users/sudandan/.openclaw/workspace/bali-guide/index.html'
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Dashboard updated at {dashboard_path}")
