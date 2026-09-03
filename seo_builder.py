# -*- coding: utf-8 -*-
"""
EchoGram Advanced Programmatic SEO Generator
Builds 31 Province Landing Pages with Internal Mesh Linking and Rich Schemas.
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime

# ========================================================
# ⚙️ تنظیمات اصلی - این دو متغیر را با اطلاعات خودت پر کن:
DOMAIN = "https://sepehrmamouri-bot.github.io/EchoGram_bot/"  # آدرس لندینگ پیج شما در گیت‌هاب
BOT_USERNAME = "echogrammmbot"                    # یوزرنیم ربات بدون @
# ========================================================

PROVINCES = [
    ("tehran", "تهران", "پایتخت و شلوغ‌ترین چت‌روم ناشناس"),
    ("isfahan", "اصفهان", "گفتگو با همشهریان اصفهانی، کاشان و نجف‌آباد"),
    ("fars", "فارس و شیراز", "چت ناشناس و دوستیابی در شیراز، مرودشت و جهرم"),
    ("khorasan-razavi", "خراسان رضوی و مشهد", "بزرگترین کامیونیتی چت ناشناس مشهد و نیشابور"),
    ("east-azerbaijan", "آذربایجان شرقی و تبریز", "چت ناشناس ترک‌زبانان در تبریز و مراغه"),
    ("khuzestan", "خوزستان و اهواز", "گفتگو با بچه‌های خونگرم اهواز، آبادان و دزفول"),
    ("mazandaran", "مازندران", "چت ناشناس شمال، ساری، بابل و آمل"),
    ("gilan", "گیلان و رشت", "دوستیابی و چت آزاد در رشت، انزلی و لاهیجان"),
    ("alborz", "البرز و کرج", "چت ناشناس کرج، فردیس و هشتگرد"),
    ("qom", "قم", "چت آنلاین و دوستیابی ناشناس در قم"),
    ("yazd", "یزد", "چت‌روم ناشناس یزد، میبد و اردکان"),
    ("kerman", "کرمان", "گفتگوی ناشناس در کرمان، رفسنجان و سیرجان"),
    ("hormozgan", "هرمزگان و بندرعباس", "چت بندری‌ها در بندرعباس و قشم"),
    ("bushehr", "بوشهر", "چت ناشناس جنوب در بوشهر و برازجان"),
    ("lorestan", "لرستان", "چت همشهریان در خرم‌آباد و بروجرد"),
    ("kermanshah", "کرمانشاه", "چت ناشناس غرب کشور در کرمانشاه"),
    ("hamedan", "همدان", "گفتگوی آنلاین در همدان و ملایر"),
    ("golestan", "گلستان و گرگان", "چت ناشناس در گرگان و گنبد کاووس"),
    ("kurdistan", "کردستان و سنندج", "چت ناشناس سنندج، مریوان و سقز"),
    ("markazi", "مرکزی و اراک", "چت همشهریان اراک و ساوه"),
    ("zanjan", "زنجان", "چت ناشناس در زنجان و ابهر"),
    ("ardabil", "اردبیل", "چت ناشناس اردبیل، سرعین و مشگین‌شهر"),
    ("qazvin", "قزوین", "چت‌روم ناشناس قزوین و تاکستان"),
    ("semnan", "سمنان", "گفتگو در سمنان، شاهرود و دامغان"),
    ("chaharmahal", "چهارمحال و بختیاری", "چت شهرکرد و بروجن"),
    ("kohgiluyeh", "کهگیلویه و بویراحمد", "چت یاسوج و گچساران"),
    ("ilam", "ایلام", "چت ناشناس در ایلام و دهلران"),
    ("north-khorasan", "خراسان شمالی", "چت بجنورد و شیروان"),
    ("south-khorasan", "خراسان جنوبی", "چت بیرجند و قائن"),
    ("sistan", "سیستان و بلوچستان", "چت زاهدان و چابهار"),
    ("west-azerbaijan", "آذربایجان غربی", "چت ارومیه و خوی")
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>چت ناشناس {name} | ربات تلگرام اکوگرام</title>
  <meta name="description" content="ربات چت ناشناس {name}؛ اتصال هوشمند به افراد نزدیک و همشهری‌ها در استان {name} با فیلتر جنسیت و سرعت بالا بدون فیلتر.">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
  <link rel="canonical" href="{domain}/provinces/{slug}.html">
  
  <link rel="preconnect" href="https://t.me">
  <link rel="dns-prefetch" href="https://t.me">

  <!-- Breadcrumb + FAQ Schema -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type": "ListItem", "position": 1, "name": "صفحه اصلی", "item": "{domain}/"}},
          {{"@type": "ListItem", "position": 2, "name": "چت ناشناس {name}", "item": "{domain}/provinces/{slug}.html"}}
        ]
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": [
          {{
            "@type": "Question",
            "name": "چگونه در {name} چت ناشناس پیدا کنم؟",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "کافی است وارد ربات اکوگرام شوید، استان {name} را انتخاب کنید تا بلافاصله به یک هم‌صحبت آنلاین متصل شوید."
            }}
          }},
          {{
            "@type": "Question",
            "name": "آیا هویت من در چت ناشناس {name} مخفی می‌ماند؟",
            "acceptedAnswer": {{
              "@type": "Answer",
              "text": "بله، تمام اطلاعات کاربری شامل شماره تلفن و آیدی تلگرام کاملاً مخفی و ناشناس هستند."
            }}
          }}
        ]
      }}
    ]
  }}
  </script>

  <style>
    :root {{ --bg: #0d1117; --card: #161b22; --accent: #0088cc; --text: #c9d1d9; --title: #58a6ff; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, -apple-system, sans-serif; }}
    body {{ background: var(--bg); color: var(--text); direction: rtl; padding: 1.5rem; line-height: 1.7; }}
    .container {{ max-width: 750px; margin: 0 auto; }}
    .box {{ background: var(--card); border: 1px solid #30363d; border-radius: 14px; padding: 2rem; margin-bottom: 1.5rem; }}
    h1 {{ color: var(--title); font-size: 1.8rem; margin-bottom: 0.8rem; }}
    h2 {{ color: #f0f6fc; font-size: 1.3rem; margin: 1.2rem 0 0.6rem 0; }}
    p {{ color: #8b949e; margin-bottom: 1rem; }}
    .cta {{ display: block; background: var(--accent); color: #fff; text-align: center; text-decoration: none; padding: 1rem; font-size: 1.2rem; font-weight: bold; border-radius: 50px; margin: 1.5rem 0; box-shadow: 0 4px 12px rgba(0, 136, 204, 0.4); }}
    .cta:hover {{ background: #0077b5; }}
    .mesh-links {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem; }}
    .mesh-links a {{ background: #21262d; color: #58a6ff; text-decoration: none; padding: 0.4rem 0.8rem; border-radius: 6px; font-size: 0.9rem; border: 1px solid #30363d; }}
    .mesh-links a:hover {{ background: #30363d; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="box">
      <h1>چت ناشناس {name}</h1>
      <p>{desc}. همین حالا مکالمه‌ای جدید، امن و کاملاً ناشناس با کاربران استان {name} را تجربه کنید.</p>
      
      <a href="https://t.me/{bot}?start=prov_{slug}" class="cta">
        💬 ورود به چت ناشناس {name}
      </a>

      <h2>امکانات چت در استان {name}</h2>
      <p>در اکوگرام می‌توانید بر اساس موقعیت جغرافیایی GPS، افراد نزدیک به خود را بیابید یا با انتخاب فیلتر جنسیت (دختر یا پسر) مکالمه را آغاز کنید.</p>
    </div>

    <!-- لینک‌سازی داخلی برای افزایش رتبه در گوگل -->
    <div class="box">
      <h2>چت ناشناس در سایر استان‌ها</h2>
      <div class="mesh-links">
        {internal_links}
      </div>
    </div>
  </div>
</body>
</html>
"""

def generate_seo_network():
    os.makedirs("provinces", exist_ok=True)
    urls = [{"loc": f"{DOMAIN}/", "priority": "1.0"}]
    total = len(PROVINCES)

    for idx, (slug, name, desc) in enumerate(PROVINCES):
        # ساخت لینک داخلی به ۳ استان قبلی و ۳ استان بعدی
        neighbor_links = []
        for offset in [-3, -2, -1, 1, 2, 3]:
            n_idx = (idx + offset) % total
            n_slug, n_name, _ = PROVINCES[n_idx]
            neighbor_links.append(f'<a href="{DOMAIN}/provinces/{n_slug}.html">چت {n_name}</a>')

        html_content = HTML_TEMPLATE.format(
            name=name,
            desc=desc,
            slug=slug,
            domain=DOMAIN,
            bot=BOT_USERNAME,
            internal_links="\n        ".join(neighbor_links)
        )

        with open(f"provinces/{slug}.html", "w", encoding="utf-8") as f:
            f.write(html_content)

        urls.append({"loc": f"{DOMAIN}/provinces/{slug}.html", "priority": "0.8"})

    # تولید sitemap.xml استاندارد
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    today = datetime.now().strftime("%Y-%m-%d")
    for u in urls:
        url_elem = ET.SubElement(urlset, "url")
        ET.SubElement(url_elem, "loc").text = u["loc"]
        ET.SubElement(url_elem, "lastmod").text = today
        ET.SubElement(url_elem, "priority").text = u["priority"]

    tree = ET.ElementTree(urlset)
    ET.indent(tree, space="  ")
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print("🚀 ۳۱ صفحه استانی، شبکه لینک‌سازی داخلی و sitemap.xml ساخته شد!")

if __name__ == "__main__":
    generate_seo_network()
