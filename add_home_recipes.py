import os, re

def get_recipe_section(lang):
    if lang == "az":
        badge = "SAVOR KULİNARİYA"
        h2 = "Mətbəxinizdə Savor Ləzzətləri"
        sub = "Təbii kərə yağlarımız və Ghee ilə hazırlanan ən dadlı milli təamlar və desertlər."
        btn_text = "Daha çox resept →"
        url = "/recipes/index.html"
        r1_tag = "MİLLİ TƏAM"
        r1_title = "Əsl Zəfəranlı Şah Plov"
        r1_meta = "⏱️ 120 dəq • 👨‍🍳 Orta • 🍽️ 6-8 nəfərlik"
        r1_desc = "Savor Ghee ilə hazırlanan, qazmağı xırtıldayan və düyüsü dən-dən tökülən möhtəşəm Şah plov resepti."
        r1_butter = "🧈 Savor Ghee (150q)"
        r2_tag = "ŞİRNİYYAT"
        r2_title = "Klassik Bakı Paxlavası"
        r2_meta = "⏱️ 90 dəq • 👨‍🍳 Usta • 🍽️ 12-15 nəfərlik"
        r2_desc = "Təbii Savor kərə yağı ilə qat-qat açılmış, qoz və zəfəran şərbəti ilə zənginləşdirilmiş əsl Bakı paxlavası."
        r2_butter = "🧈 Savor Kərə Yağı (300q)"
        view_btn = "Reseptə bax →"
        nav_text = "Reseptlər"
    elif lang == "ru":
        badge = "КУЛИНАРИЯ SAVOR"
        h2 = "Вкусы Savor на Вашей Кухне"
        sub = "Самые вкусные национальные блюда и десерты на натуральном сливочном масле и Гхи."
        btn_text = "Все рецепты →"
        url = "/recipes/ru.html"
        r1_tag = "НАЦИОНАЛЬНОЕ БЛЮДО"
        r1_title = "Шах Плов с Шафраном"
        r1_meta = "⏱️ 120 мин • 👨‍🍳 Средняя • 🍽️ 6-8 порций"
        r1_desc = "Королевский Шах плов с хрустящей корочкой и рассыпчатым рисом на ароматном масле Savor Ghee."
        r1_butter = "🧈 Savor Ghee (150г)"
        r2_tag = "СЛАДОСТИ"
        r2_title = "Бакинская Пахлава"
        r2_meta = "⏱️ 90 мин • 👨‍🍳 Мастер • 🍽️ 12-15 порций"
        r2_desc = "Традиционная пахлава на натуральном масле Savor с начинкой из грецких орехов и шафрановым сиропом."
        r2_butter = "🧈 Масло Savor (300г)"
        view_btn = "Смотреть рецепт →"
        nav_text = "Рецепты"
    else:
        badge = "SAVOR CULINARY"
        h2 = "Savor Flavors in Your Kitchen"
        sub = "Delicious traditional recipes and pastries made with 100% pure Savor butter & Ghee."
        btn_text = "View All Recipes →"
        url = "/recipes/en.html"
        r1_tag = "NATIONAL DISH"
        r1_title = "Royal Saffron Shah Plov"
        r1_meta = "⏱️ 120 mins • 👨‍🍳 Medium • 🍽️ 6-8 servings"
        r1_desc = "Magnificent crusty Shah Plov made with aromatic Savor Ghee and tender meat."
        r1_butter = "🧈 Savor Ghee (150g)"
        r2_tag = "SWEET PASTRY"
        r2_title = "Classic Baku Pakhlava"
        r2_meta = "⏱️ 90 mins • 👨‍🍳 Expert • 🍽️ 12-15 servings"
        r2_desc = "Layered traditional pakhlava made with pure Savor butter and fragrant spiced walnuts."
        r2_butter = "🧈 Savor Butter (300g)"
        view_btn = "View Recipe →"
        nav_text = "Recipes"

    section_html = f"""
  <!-- SAVOR RECIPES SHOWCASE SECTION -->
  <section class="home-recipes-section" style="padding: 70px 20px; background: #faf8f5; border-top: 1px solid #ddd7cd; border-bottom: 1px solid #ddd7cd;">
    <div style="max-width: 1200px; margin: 0 auto;">
      <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 35px; flex-wrap: wrap; gap: 20px;">
        <div>
          <span style="color: #8c6828; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; background: #f0e6d6; padding: 5px 12px; border-radius: 20px;">{badge}</span>
          <h2 style="font-family: 'Playfair Display', serif; font-size: 2.3rem; color: #1f1d1a; margin-top: 12px; line-height: 1.2;">{h2}</h2>
          <p style="color: #6b665f; font-size: 1.02rem; max-width: 580px; margin-top: 8px;">{sub}</p>
        </div>
        <div>
          <a href="{url}" style="background: #965627; color: #ffffff !important; padding: 11px 24px; border-radius: 30px; text-decoration: none; font-weight: 700; font-size: 0.92rem; display: inline-flex; align-items: center; gap: 8px; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(150, 86, 39, 0.25);">
            {btn_text}
          </a>
        </div>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;">
        <!-- 1. Şah Plov -->
        <div style="background: #ffffff; border-radius: 18px; overflow: hidden; border: 1px solid #ddd7cd; box-shadow: 0 10px 25px rgba(0,0,0,0.04); display: flex; flex-direction: column;">
          <div style="height: 240px; overflow: hidden; position: relative;">
            <img src="https://media.azersun.com/crystalex.az/files/receipt/393cbafb-8e30-43db-8974-b2efd58e8aed_CristalEx.jpeg" alt="{r1_title}" style="width: 100%; height: 100%; object-fit: cover;">
            <span style="position: absolute; top: 15px; left: 15px; background: rgba(31, 29, 26, 0.85); color: #f7e7ce; font-size: 0.76rem; font-weight: 700; padding: 4px 10px; border-radius: 15px; backdrop-filter: blur(4px);">{r1_tag}</span>
          </div>
          <div style="padding: 24px 20px; display: flex; flex-direction: column; flex-grow: 1;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.45rem; color: #1f1d1a; margin-bottom: 8px;">{r1_title}</h3>
            <div style="font-size: 0.84rem; color: #718096; margin-bottom: 12px;">{r1_meta}</div>
            <p style="color: #4a5568; font-size: 0.9rem; line-height: 1.5; margin-bottom: 16px;">{r1_desc}</p>
            <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1px dashed #e2e8f0;">
              <span style="color: #6b4d1b; font-size: 0.88rem; font-weight: 700;">{r1_butter}</span>
              <a href="{url}#sah-plov" style="color: #965627; font-weight: 700; font-size: 0.88rem; text-decoration: none;">{view_btn}</a>
            </div>
          </div>
        </div>

        <!-- 2. Bakı Paxlavası -->
        <div style="background: #ffffff; border-radius: 18px; overflow: hidden; border: 1px solid #ddd7cd; box-shadow: 0 10px 25px rgba(0,0,0,0.04); display: flex; flex-direction: column;">
          <div style="height: 240px; overflow: hidden; position: relative;">
            <a href="{url}#baki-paxlavasi"><img src="https://th.bing.com/th/id/R.3fe4ab8faeb256d59668b5c591bf3cc5?rik=IWUa2iTmC%2bukxA&riu=http%3a%2f%2fazerbejdzan.eu%2fwp-content%2fuploads%2f2021%2f06%2fBaki-paxlavasi-1.jpg&ehk=J8imnKUsapvDHE787gWD3X1v1QNA7nguN1LPnZHyELg%3d&risl=&pid=ImgRaw&r=0" alt="{r2_title}" style="width: 100%; height: 100%; object-fit: cover;">
            <span style="position: absolute; top: 15px; left: 15px; background: rgba(31, 29, 26, 0.85); color: #f7e7ce; font-size: 0.76rem; font-weight: 700; padding: 4px 10px; border-radius: 15px; backdrop-filter: blur(4px);">{r2_tag}</span>
          </div>
          <div style="padding: 24px 20px; display: flex; flex-direction: column; flex-grow: 1;">
            <h3 style="font-family: 'Playfair Display', serif; font-size: 1.45rem; color: #1f1d1a; margin-bottom: 8px;"><a href="{url}#baki-paxlavasi" style="color: inherit; text-decoration: none;">{r2_title}</a></h3>
            <div style="font-size: 0.84rem; color: #718096; margin-bottom: 12px;">{r2_meta}</div>
            <p style="color: #4a5568; font-size: 0.9rem; line-height: 1.5; margin-bottom: 16px;">{r2_desc}</p>
            <div style="margin-top: auto; display: flex; justify-content: space-between; align-items: center; padding-top: 14px; border-top: 1px dashed #e2e8f0;">
              <span style="color: #6b4d1b; font-size: 0.88rem; font-weight: 700;">{r2_butter}</span>
              <a href="{url}" style="color: #965627; font-weight: 700; font-size: 0.88rem; text-decoration: none;">{view_btn}</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    return section_html, nav_text, url

pages = [("index.html", "az"), ("ru.html", "ru"), ("en.html", "en")]

for fname, lang in pages:
    if not os.path.exists(fname):
        continue
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Köhnə resept bölməsi varsa təmizləyirik
    content = re.sub(r"<!-- SAVOR RECIPES SHOWCASE SECTION.*?<\/section>", "", content, flags=re.DOTALL)

    sec_html, nav_title, nav_url = get_recipe_section(lang)

    # Keyfiyyət sənədləri (Sertifikatlar) bölməsindən əvvələ əlavə edirik
    cert_pattern = re.compile(r"(<(?:section|div)[^>]+(?:certificate|sertifikat|cert)[^>]*>)", re.IGNORECASE)
    match = cert_pattern.search(content)

    if match:
        content = content[:match.start()] + sec_html + "\n  " + content[match.start():]
    else:
        content = content.replace("<footer", sec_html + "\n<footer", 1)

    # Naviqasiya menyusuna "Reseptlər" linkini əlavə edirik
    if nav_url not in content:
        nav_item = f'\n        <a href="{nav_url}">{nav_title}</a>'
        content = re.sub(r'(<a[^>]+href=[\"\x27][^\"\x27]*horeca[^\"\x27]*[\"\x27][^>]*>.*?<\/a>)', r'\1' + nav_item, content, flags=re.IGNORECASE)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✓ {fname} faylına Reseptlər bölməsi əlavə edildi!")
