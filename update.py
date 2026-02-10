import os
import datetime
import json

def generate_html(data):
    # Itinerary Data Structure
    itinerary = [
        {
            "day": 1,
            "date": "2月11日",
            "title": "启程：飞往众神之岛",
            "hotel": "The Westin Resort Nusa Dua",
            "desc": "✈️ 飞行计划：CX347 (07:30-11:05) & CX785 (12:35-17:35)。抵达后接机入住，开启假期！",
            "pois": [
                {
                    "name": "巴厘岛国际机场 (DPS)", 
                    "lat": -8.7482, "lon": 115.1675, "type": "attraction", 
                    "img": "https://images.unsplash.com/photo-1542296332-2e4473faf563?auto=format&fit=crop&w=400&q=80",
                    "info": "✈️ 入境大厅 | 耗时: 1.5h | 费用: VOA 50万印尼盾",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g294226-d2279188-Reviews-Ngurah_Rai_International_Airport-Kuta_Bali.html"
                },
                {
                    "name": "晚餐：Ikan Restaurant", 
                    "lat": -8.7941, "lon": 115.2302, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=400&q=80",
                    "info": "🍴 海滨烧烤 | 亮点: 沙滩用餐 | 人均: 30-50 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297698-d1066526-Reviews-Ikan_Restaurant_Bar-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"
                }
            ],
            "tips": "🛡️ 导游建议：由于转机紧凑，建议在香港机场快速解决午餐（如太兴烧味）。"
        },
        {
            "day": 2,
            "date": "2月12日",
            "title": "努沙杜瓦：亲子童话时光",
            "hotel": "The Westin Resort Nusa Dua",
            "desc": "全天在酒店及周边享受顶级亲子设施，让宝宝彻底玩嗨！",
            "pois": [
                {
                    "name": "Westin Kids Club", 
                    "lat": -8.7945, "lon": 115.2310, "type": "kids", 
                    "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=400&q=80",
                    "info": "🎨 托管中心 | 建议玩: 3h | 住客免费",
                    "link": "https://www.marriott.com/en-us/hotels/dpswi-the-westin-resort-nusa-dua-bali/overview/"
                },
                {
                    "name": "午餐：Seasonal Tastes", 
                    "lat": -8.7941, "lon": 115.2302, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=400&q=80",
                    "info": "🍱 国际自助 | 亮点: 现磨咖啡 | 人均: 25 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297698-d2151608-Reviews-Seasonal_Tastes-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"
                },
                {
                    "name": "晚餐：The Pirate's Bay", 
                    "lat": -8.7925, "lon": 115.2335, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=400&q=80",
                    "info": "🏴‍☠️ 海盗船主题 | 建议停留: 2h | 宝宝必选",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297698-d3493863-Reviews-The_Pirate_s_Bay-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"
                }
            ],
            "tips": "💡 导游建议：下午 4 点后沙滩光线最柔和，适合拍全家福。"
        },
        {
            "day": 3,
            "date": "2月13日",
            "title": "巨浪涌动与悬崖火舞",
            "hotel": "The Westin Resort Nusa Dua",
            "desc": "见证自然的磅礴，体验巴厘岛最具震撼力的传统演出。",
            "pois": [
                {
                    "name": "Waterblow", 
                    "lat": -8.8012, "lon": 115.2355, "type": "attraction", 
                    "img": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=400&q=80",
                    "info": "🌊 自然景观 | 建议玩: 1h | 门票: 约2.5万印尼盾",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g297698-d3527715-Reviews-Water_Blow-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"
                },
                {
                    "name": "午餐：Bebek Tepi Sawah", 
                    "lat": -8.7900, "lon": 115.2200, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?auto=format&fit=crop&w=400&q=80",
                    "info": "🦆 稻田鸭餐 | 亮点: 酥脆脏鸭 | 人均: 20 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297698-d1502447-Reviews-Bebek_Tepi_Sawah-Nusa_Dua_Nusa_Dua_Peninsula_Bali.html"
                },
                {
                    "name": "晚餐：Jimbaran Seafood", 
                    "lat": -8.7700, "lon": 115.1680, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=400&q=80",
                    "info": "🍤 沙滩晚餐 | 亮点: 看日落 | 约玩: 1.5h",
                    "link": "https://www.tripadvisor.cn/Restaurants-g297696-Jimbaran_South_Kuta_Bali.html"
                }
            ],
            "tips": "🐒 避坑：情人崖猴子多，手机一定要抓稳，眼镜摘下来放包里。"
        },
        {
            "day": 4,
            "date": "2月14日",
            "title": "换宿之旅：潜入乌布丛林",
            "hotel": "Maya Ubud Resort & Spa",
            "desc": "告别大海，走向森林。今天我们将穿越半个岛屿，入住绝美丛林酒店。",
            "pois": [
                {
                    "name": "Tegenungan Waterfall", 
                    "lat": -8.5752, "lon": 115.2903, "type": "attraction", 
                    "img": "https://images.unsplash.com/photo-1559628233-eb1b1a45564b?auto=format&fit=crop&w=400&q=80",
                    "info": "🌿 森林瀑布 | 建议玩: 1.5h | 门票: 2万印尼盾",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d8525287-Reviews-Tegenungan_Waterfall-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "午餐：D'Tukad River Club", 
                    "lat": -8.5750, "lon": 115.2900, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=400&q=80",
                    "info": "🌴 俱乐部午餐 | 亮点: 瀑布景观 | 人均: 20 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d14175373-Reviews-D_Tukad_River_Club-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "晚餐：Bebek Bengil", 
                    "lat": -8.5147, "lon": 115.2647, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?auto=format&fit=crop&w=400&q=80",
                    "info": "🦆 创始脏鸭餐 | 亮点: 后花园稻田 | 人均: 25 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d786438-Reviews-Bebek_Bengil-Ubud_Gianyar_Regency_Bali.html"
                }
            ],
            "tips": "🧳 导游提示：行李较多建议包整车，Maya Ubud 有很棒的无边泳池，记得给娃带泳衣。"
        },
        {
            "day": 5,
            "date": "2月15日",
            "title": "乌布：精灵森林与艺术生活",
            "hotel": "Maya Ubud Resort & Spa",
            "desc": "漫步在充满艺术气息的乌布小镇，和可爱的生灵们近距离接触。",
            "pois": [
                {
                    "name": "圣猴森林 (Sacred Monkey)", 
                    "lat": -8.5188, "lon": 115.2585, "type": "kids", 
                    "img": "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=400&q=80",
                    "info": "🐒 生态探索 | 建议玩: 2h | 费用: 8万印尼盾",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d379334-Reviews-Sacred_Monkey_Forest_Sanctuary-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "午餐：Clear Cafe", 
                    "lat": -8.5140, "lon": 115.2660, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=400&q=80",
                    "info": "🍹 森林风餐厅 | 亮点: 必喝奶昔 | 人均: 15 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d1956557-Reviews-Clear_Cafe-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "晚餐：Milk & Madu Ubud", 
                    "lat": -8.5065, "lon": 115.2625, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=400&q=80",
                    "info": "🍕 顶级亲子餐 | 亮点: 有游乐区 | 人均: 20 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d14144365-Reviews-Milk_Madu_Ubud-Ubud_Gianyar_Regency_Bali.html"
                }
            ],
            "tips": "👟 穿衣：乌布建议穿好走的运动鞋。晚餐 Milk & Madu 的熔岩蛋糕非常推荐！"
        },
        {
            "day": 6,
            "date": "2月16日",
            "title": "绿色梯田与圣水洗礼",
            "hotel": "Maya Ubud Resort & Spa",
            "desc": "在著名的秋千上俯瞰梯田，在圣泉寺感受古老信仰的力量。",
            "pois": [
                {
                    "name": "Tegalalang Rice Terrace", 
                    "lat": -8.4312, "lon": 115.2800, "type": "attraction", 
                    "img": "https://images.unsplash.com/photo-1558239250-13651912f20c?auto=format&fit=crop&w=400&q=80",
                    "info": "🌾 绿色浪潮 | 建议玩: 2h | 最佳拍照: 09:00",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d2279188-Reviews-Tegalalang_Rice_Terrace-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "午餐：Alas Harum Bali", 
                    "lat": -8.4280, "lon": 115.2850, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1559628233-eb1b1a45564b?auto=format&fit=crop&w=400&q=80",
                    "info": "☕ 梯田午餐 | 亮点: 网红秋千 | 人均: 25 USD",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d14175373-Reviews-Alas_Harum_Agro_Tourism-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "晚餐：The Sayan House", 
                    "lat": -8.5020, "lon": 115.2420, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1559628233-eb1b1a45564b?auto=format&fit=crop&w=400&q=80",
                    "info": "🍱 日系融合菜 | 亮点: 阿勇河谷日落 | 人均: 40 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d7253503-Reviews-The_Sayan_House-Ubud_Gianyar_Regency_Bali.html"
                }
            ],
            "tips": "📸 摄影：Sayan House 的靠窗位置非常火爆，建议提前 2-3 天预约。"
        },
        {
            "day": 7,
            "date": "2月17日",
            "title": "带着回忆，平安返程",
            "hotel": "Regala Skycity HK",
            "desc": "最后在乌布采购一番，随后前往机场。回程 CX784 (16:20-21:10)。",
            "pois": [
                {
                    "name": "乌布市场 (Ubud Market)", 
                    "lat": -8.5068, "lon": 115.2625, "type": "attraction", 
                    "img": "https://images.unsplash.com/photo-1540541338287-41700207dee6?auto=format&fit=crop&w=400&q=80",
                    "info": "🛍️ 伴手礼采购 | 建议玩: 1h | 记得砍价",
                    "link": "https://www.tripadvisor.cn/Attraction_Review-g297701-d2279188-Reviews-Ubud_Art_Market-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "午餐：Sun Sun Warung", 
                    "lat": -8.5080, "lon": 115.2630, "type": "dining", 
                    "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=400&q=80",
                    "info": "🍛 平价印尼菜 | 亮点: 家庭氛围 | 人均: 10 USD",
                    "link": "https://www.tripadvisor.cn/Restaurant_Review-g297701-d12903332-Reviews-Sun_Sun_Warung-Ubud_Gianyar_Regency_Bali.html"
                },
                {
                    "name": "香港丽豪航天城", 
                    "lat": 22.2985, "lon": 113.9360, "type": "hotel", 
                    "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=400&q=80",
                    "info": "✈️ 中转首选 | 亮点: 离机场极近 | 晚22:00入住",
                    "link": "https://www.tripadvisor.cn/Hotel_Review-g294217-d23821034-Reviews-Regala_Skycity_Hotel-Hong_Kong.html"
                }
            ],
            "tips": "🛍️ 提醒：回程行李请确认是否直挂。香港机场 11 SKIES 有很多亲子互动区。"
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
            scrollbar-width: none;
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
        .itinerary-card p { font-size: 14px; line-height: 1.6; color: var(--text-main); margin-bottom: 15px; }

        /* POI Item with Images */
        .poi-item {
            display: block;
            background: #F8FAFC;
            border-radius: 20px;
            margin-bottom: 15px;
            overflow: hidden;
            text-decoration: none;
            color: inherit;
            border: 1px solid #E2E8F0;
        }
        .poi-img {
            width: 100%;
            height: 160px;
            background-size: cover;
            background-position: center;
        }
        .poi-details { padding: 12px 15px; }
        .poi-details strong { display: block; font-size: 15px; color: var(--text-main); }
        .poi-details .poi-info-text { font-size: 12px; color: var(--text-sub); margin-top: 4px; display: block; }

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
            height: 200px;
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
                <h1>巴厘岛亲子游</h1>
                <p>你好 松松！专业导游全流程为您服务。</p>
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

            <div class="day-tabs" id="dayTabs"></div>

            <div id="map"></div>

            <div id="dayContent"></div>

            <div class="medical-alert">
                <h4><i class="fas fa-hospital-user"></i> 紧急医疗 & 安全</h4>
                <p><strong>BIMC Nusa Dua:</strong> +62 361 3000 911<br><strong>备忘:</strong> 坚持使用瓶装水刷牙，备好 Norit 活性炭预防 Bali Belly。</p>
            </div>
        </div>
        
        <footer class="footer">
            <p>由 <strong>songsong的小跟班</strong> 为您精心打造</p>
            <p>V13.0 全程餐厅图片版 | 专属 AI 助手</p>
        </footer>
    </div>

    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        const itineraryData = {ITINERARY_JSON};
        let currentDay = 1;
        let map, markersGroup, polyline;

        function initMap() {
            map = L.map('map', {zoomControl: false}).setView([-8.7941, 115.2302], 12);
            L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png').addTo(map);
            markersGroup = L.layerGroup().addTo(map);
        }

        function updateDay(day) {
            currentDay = day;
            const data = itineraryData.find(d => d.day === day);
            
            // Update Tabs
            document.getElementById('dayTabs').innerHTML = itineraryData.map(d => `
                <div class="tab ${d.day === day ? 'active' : ''}" onclick="updateDay(${d.day})">
                    Day ${d.day}<br><span style="font-size: 10px; font-weight: normal;">${d.date}</span>
                </div>
            `).join('');

            // Update Content
            const poisHtml = data.pois.map(poi => `
                <a href="${poi.link}" class="poi-item" target="_blank">
                    <div class="poi-img" style="background-image: url('${poi.img}')"></div>
                    <div class="poi-details">
                        <strong>${poi.name}</strong>
                        <span class="poi-info-text">${poi.info}</span>
                    </div>
                </a>
            `).join('');

            document.getElementById('dayContent').innerHTML = `
                <div class="itinerary-card">
                    <div class="hotel-badge"><i class="fas fa-bed"></i> 入住: ${data.hotel}</div>
                    <h2>${data.title}</h2>
                    <p style="margin-bottom: 15px;">${data.desc}</p>
                    ${data.tips ? `<div class="tips-card"><p>${data.tips}</p></div>` : ''}
                    <h3 style="font-size: 15px; margin-top: 20px; margin-bottom: 12px; color: var(--text-sub); border-left: 4px solid var(--primary); padding-left: 8px;">📍 今日详细行程:</h3>
                    ${poisHtml}
                </div>
            `;

            // Update Map
            markersGroup.clearLayers();
            if (polyline) polyline.remove();
            const latlngs = data.pois.filter(p => p.lat && p.lon).map(p => [p.lat, p.lon]);
            data.pois.filter(p => p.lat && p.lon).forEach(p => L.marker([p.lat, p.lon]).addTo(markersGroup).bindPopup(p.name));
            if (latlngs.length > 1) {
                polyline = L.polyline(latlngs, {color: 'var(--primary)', weight: 3, dashArray: '5, 10'}).addTo(map);
                map.fitBounds(polyline.getBounds(), {padding: [40, 40]});
            } else if (latlngs.length === 1) map.setView(latlngs[0], 14);
        }

        window.onload = () => { initMap(); updateDay(1); };
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
