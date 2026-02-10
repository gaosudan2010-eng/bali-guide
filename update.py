import os
import datetime
import json

def generate_html(data):
    # Itinerary Data Structure
    itinerary = [
        {
            "day": 1,
            "date": "2月11日",
            "title": "抵达与休整",
            "hotel": "Westin Nusa Dua",
            "desc": "北京经香港抵达巴厘岛。办理入住威斯汀度假酒店，享受全岛顶级的亲子设施。第一天建议在酒店沙滩和泳池放松，缓解旅途劳累。",
            "pois": [
                {"name": "Westin Nusa Dua", "lat": -8.7941, "lon": 115.2302, "type": "hotel", "link": "https://www.tripadvisor.cn/Hotel_Review-g297698-d302324-Reviews-The_Westin_Resort_Nusa_Dua_Bali-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"},
                {"name": "威斯汀儿童俱乐部", "lat": -8.7945, "lon": 115.2310, "type": "kids", "link": "https://www.marriott.com/en-us/hotels/dpswi-the-westin-resort-nusa-dua-bali/overview/"}
            ]
        },
        {
            "day": 2,
            "date": "2月12日",
            "title": "努沙杜瓦亲子时光",
            "hotel": "Westin Nusa Dua",
            "desc": "上午参加威斯汀儿童俱乐部的活动。下午前往海盗湾餐厅，在巨大的海盗船和树屋上用餐，这是孩子们最喜欢的体验。",
            "pois": [
                {"name": "The Pirate's Bay Bali", "lat": -8.7925, "lon": 115.2335, "type": "dining", "link": "https://www.tripadvisor.cn/Restaurant_Review-g297698-d3493863-Reviews-The_Pirate_s_Bay-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"},
                {"name": "Nusa Dua Beach", "lat": -8.7960, "lon": 115.2320, "type": "beach", "link": "https://www.tripadvisor.cn/Attraction_Review-g297698-d1045931-Reviews-Nusa_Dua_Beach-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"}
            ]
        },
        {
            "day": 3,
            "date": "2月13日",
            "title": "壮丽悬崖与日落",
            "hotel": "Westin Nusa Dua",
            "desc": "参观南端的神奇喷泉 Waterblow。傍晚前往乌鲁瓦图情人崖，观看壮丽的海上日落和精彩的 Kecak 舞蹈表演。注意避开猴子！",
            "pois": [
                {"name": "Waterblow", "lat": -8.8012, "lon": 115.2355, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297698-d3527715-Reviews-Water_Blow-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"},
                {"name": "Uluwatu Temple", "lat": -8.8291, "lon": 115.0849, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379333-Reviews-Uluwatu_Temple-Uluwatu_Bukit_Peninsula_Bali.html"}
            ]
        },
        {
            "day": 4,
            "date": "2月14日",
            "title": "前往乌布丛林",
            "hotel": "Maya Ubud",
            "desc": "退房后前往乌布，中途可停留艺术村。入住玛雅乌布度假村，感受巴厘岛的森林气息。晚上在乌布皇宫附近享用地道脏鸭餐。",
            "pois": [
                {"name": "Maya Ubud Resort", "lat": -8.5081, "lon": 115.2758, "type": "hotel", "link": "https://www.tripadvisor.cn/Hotel_Review-g297701-d305615-Reviews-Maya_Ubud_Resort_Spa-Ubud_Gianyar_Regency_Bali.html"},
                {"name": "Bebek Bengil (脏鸭餐)", "lat": -8.5147, "lon": 115.2647, "type": "dining", "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d786438-Reviews-Bebek_Bengil-Ubud_Gianyar_Regency_Bali.html"}
            ]
        },
        {
            "day": 5,
            "date": "2月15日",
            "title": "猴子林与亲子咖啡",
            "hotel": "Maya Ubud",
            "desc": "步行探索乌布圣猴林。下午前往全巴厘岛最出名的亲子餐厅 Milk & Madu，那里有专门的儿童游戏室和美味的披萨。",
            "pois": [
                {"name": "Sacred Monkey Forest", "lat": -8.5188, "lon": 115.2585, "type": "kids", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379334-Reviews-Sacred_Monkey_Forest_Sanctuary-Ubud_Gianyar_Regency_Bali.html"},
                {"name": "Milk & Madu Ubud", "lat": -8.5065, "lon": 115.2625, "type": "dining", "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d14144365-Reviews-Milk_Madu_Ubud-Ubud_Gianyar_Regency_Bali.html"}
            ]
        },
        {
            "day": 6,
            "date": "2月16日",
            "title": "梯田与圣泉祈福",
            "hotel": "Maya Ubud",
            "desc": "早起避开人群前往德格拉朗梯田。随后参观圣泉寺，体验巴厘岛的宗教文化。下午回酒店享受玛雅乌布著名的无边泳池。",
            "pois": [
                {"name": "Tegalalang Rice Terrace", "lat": -8.4312, "lon": 115.2800, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d2279188-Reviews-Tegalalang_Rice_Terrace-Ubud_Gianyar_Regency_Bali.html"},
                {"name": "Tirta Empul Temple", "lat": -8.4162, "lon": 115.2895, "type": "attraction", "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379331-Reviews-Tirta_Empul_Temple-Ubud_Gianyar_Regency_Bali.html"}
            ]
        },
        {
            "day": 7,
            "date": "2月17日",
            "title": "启程转机香港",
            "hotel": "Regala Skycity HK",
            "desc": "告别巴厘岛，乘机飞往香港。入住机场附近的丽豪航天城酒店。晚上可以去 11 SKIES 购物中心补货或带娃在酒店休息。",
            "pois": [
                {"name": "Regala Skycity Hotel", "lat": 22.2985, "lon": 113.9360, "type": "hotel", "link": "https://www.tripadvisor.cn/Hotel_Review-g294217-d23821034-Reviews-Regala_Skycity_Hotel-Hong_Kong.html"}
            ]
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
        .itinerary-card p { font-size: 14px; line-height: 1.6; color: var(--text-main); margin-bottom: 20px; }

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
            <p>V8.0 全程路线版 | 专属 AI 助手</p>
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
                        <span>点击查看 TripAdvisor 详情</span>
                    </div>
                    <i class="fas fa-external-link-alt" style="font-size: 12px; color: #cbd5e1;"></i>
                </a>
            `).join('');

            document.getElementById('dayContent').innerHTML = `
                <div class="itinerary-card">
                    <div class="hotel-badge"><i class="fas fa-bed"></i> 入住: ${data.hotel}</div>
                    <h2>${data.title}</h2>
                    <p>${data.desc}</p>
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
    dashboard_path = '/Users/sudandan/.openclaw/bali_dashboard.html'
    with open(dashboard_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Dashboard updated at {dashboard_path}")
