import os

images_map = {
    1: ["https://media.azersun.com/crystalex.az/files/receipt/393cbafb-8e30-43db-8974-b2efd58e8aed_CristalEx.jpeg", "https://b7x9kq.arazmarket.az/storage/blog/sah-plov-2-edited.png", "../images/savor21.jpeg", "https://tse1.mm.bing.net/th/id/OIP.12ML-y5wGvq2iqNEZG33cgHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", "https://i.pinimg.com/736x/e5/0f/79/e50f79edb5624b37b0202337d80517d5.jpg", "https://www.rttotravel.com/templates/yootheme/cache/12/Maqluba-121dbb80.jpeg", "https://i1.wp.com/ashleyparamore.com/wp-content/uploads/2021/07/IMG_3673.jpg?w=2048&ssl=1", "https://i.pinimg.com/736x/f3/59/8a/f3598a9d64c8ba8671b3a4e3b64857f4.jpg"],
    2: ["https://evdar.az/wp-content/uploads/Vitaminl%C9%99-Z%C9%99ngin-S%C9%99bzi-Qovurma-Plov6-1170x650.jpg", "https://thumbs.dreamstime.com/b/pilau-green-plate-beef-pilaf-traditional-asian-dish-plov-also-known-as-polow-pilav-pallao-pulao-palaw-azerbaijanian-rice-365793055.jpg?w=992", "../images/savor22.jpeg", "https://i.ytimg.com/vi/lMxDAstrUtA/maxresdefault.jpg", "https://sultanbasmati.az/images/receipt/2t4zbpoq.23m.jpg", "https://blog.wego.com/wp-content/uploads/shutterstock_1165362130.jpg"],
    3: ["https://tse4.mm.bing.net/th/id/OIP.d-ySK5XCpMNioVi8TtGLBwHaGK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", "https://i.pinimg.com/originals/3a/31/1b/3a311be0acebf94557b1a3f02a2f7062.jpg", "../images/savor23.jpeg", "https://thespanishradish.com/wp-content/uploads/2022/03/pisto-square-v2-2k.jpg", "https://i.pinimg.com/736x/b8/e8/4b/b8e84b3efa8c828a2746106a4635f708.jpg", "https://i.ytimg.com/vi/kKbLU7lWQiw/maxresdefault.jpg"],
    4: ["https://th.bing.com/th/id/R.3fe4ab8faeb256d59668b5c591bf3cc5?rik=IWUa2iTmC%2bukxA&riu=http%3a%2f%2fazerbejdzan.eu%2fwp-content%2fuploads%2f2021%2f06%2fBaki-paxlavasi-1.jpg&ehk=J8imnKUsapvDHE787gWD3X1v1QNA7nguN1LPnZHyELg%3d&risl=&pid=ImgRaw&r=0", "https://i.pinimg.com/736x/08/db/9e/08db9ede7c216b41a5f2d97f9cdd6159.jpg", "../images/savor24.jpeg", "https://tse3.mm.bing.net/th/id/OIP.PVAMgkaBLfda_9eWwX_Q7gHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", "https://i.pinimg.com/originals/b3/86/29/b3862943d0ebe30b1f56ae21620570e9.jpg", "https://i.ytimg.com/vi/yrRYQ0y_D5o/hqdefault.jpg"],
    5: ["https://tse4.mm.bing.net/th/id/OIP.dzTksqIsZrDk4ET_1uw3UAHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", "https://i.ytimg.com/vi/nUjHcgsjQk4/maxresdefault.jpg", "../images/savor25.jpeg", "https://lh3.googleusercontent.com/3ZjwLmvMeDJu57eQUtqvoIodzrxh_DlQImTo8UEXYOMHoxT9mgxZasPxYr7Z3HFshnz7gTKineY21l2AgtyM-EvArpmh6x4egX2AH60=w900", "https://i.ytimg.com/vi/cOlUh0kV2iw/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgYShUMA8=&rs=AOn4CLBsrrqmpj77hEoM61QDzgY08CNeNQ", "https://tse2.mm.bing.net/th/id/OIP._iIigXmYUCvgeq10X5Rb-gHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"],
    6: ["https://tse2.mm.bing.net/th/id/OIP.YfkofR3kybLsKAZtvd0prAHaEO?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", "https://i.ytimg.com/vi/U8pu1tb64Zc/maxresdefault.jpg", "../images/savor26.jpeg", "https://evdar.az/wp-content/uploads/%C6%8Fsl-Qaraba%C4%9F-K%C9%99t%C9%99si1-1170x650.jpg", "https://media.istockphoto.com/id/1430987681/photo/traditional-turkish-pastries-pogaca-on-rustic-table-famous-bakery-product.jpg?s=170667a&w=0&k=20&c=rpEcFqVYH2sQid_wdTzG8sXg2VQlP5TsWiciXEpzDBw=", "https://i.ytimg.com/vi/bhJ9Sn4QBFQ/maxresdefault.jpg"],
    7: ["https://lent.az/storage/news/2025/november/06/big/690c5f471e90d690c5f471e90e1762418503690c5f471e90b690c5f471e90c.webp", "../images/savor27.jpeg", "https://th.bing.com/th/id/OIP.ManLUJUf4Q_Bxh9E4GpSHgHaE8?r=0&o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3", "https://tse3.mm.bing.net/th/id/OIP.DxFjfCOQ4FH3ws5bh8abOwHaFu?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", "https://i.pinimg.com/originals/6b/63/b0/6b63b0078d3060fea68be6308d9be151.jpg", "https://i.pinimg.com/originals/e1/9f/b6/e19fb60d5ce25a159e8de909277aad4a.png", "https://i.pinimg.com/originals/cc/09/56/cc0956e454cf2efc9f38f8a695663ecf.jpg"],
    8: ["https://azza.az/wp-content/uploads/2026/06/12766d698a30f3aa2edcb2baa6ce8ec6_9e4374b0-78d8-4ba4-95f0-7dd5bca8f761.jpg", "../images/savor28.jpeg", "https://i.ytimg.com/vi/0HA0Ok3nT6c/maxresdefault.jpg", "https://i.ytimg.com/vi/4xASXBlb8Js/hqdefault.jpg", "https://i.ytimg.com/vi/0WoPvSWzMOA/maxresdefault.jpg", "https://i.ytimg.com/vi/yOMzBOnVmCE/maxresdefault.jpg", "https://i.ytimg.com/vi/tRd8dK9fAvw/maxresdefault.jpg"],
    9: ["https://evdar.az/wp-content/uploads/Desertl%C9%99rin-%C6%8Fn-Goz%C9%99li_-Narli-Brauni-Brownie-1170x650.jpg", "../images/savor29.jpeg", "https://evdar.az/wp-content/uploads/Sokolad-Sev%C9%99nl%C9%99r-Ucun-Oreo-Pecenyeli-Brauni-Brownie-1170x650.jpg"]
}

def make_slides(recipe_id):
    slides = ""
    for url in images_map[recipe_id]:
        slides += f'\n          <div class="swiper-slide"><img src="{url}" alt="Savor Recipe {recipe_id}"></div>'
    return slides

def generate_html(lang):
    if lang == "az":
        title = "Kulinariya & Reseptlər | Savor Kərə Yağları & Ghee"
        desc = "Savor kərə yağı və Ghee ilə hazırlanan ən dadlı Azərbaycan milli mətbəxi və şirniyyat reseptləri."
        back_text = "← Ana Səhifə"
        home_link = "/index.html"
        contact_link = "/contact.php?lang=az.html"
        order_btn = "Sifariş et"
        h1 = "Savor Kulinariya Reseptləri"
        subtitle = "100% təbii Savor kərə yağları və ətirli Ghee ilə hazırlanan, süfrənizin bəzəyi olacaq ən dadlı milli yeməklər, şirniyyatlar və incə desertlər."
        btn_all, btn_milli, btn_seher, btn_sirniyyat, btn_tort = "Bütün Reseptlər (9)", "Milli Yeməklər", "Səhər Təamları", "Milli Şirniyyatlar", "Tortlar & Desertlər"
        prod_btn = "Məhsula bax →"
        ing_title = "🛒 Tərkibi:"
        prep_title = "👨‍🍳 Hazırlanması:"
        
        r1 = ("Milli Təamlar", "Əsl Zəfəranlı Şah Plov", "⏱️ 120 dəq", "👨‍🍳 Çətinlik: Orta", "🍽️ 6-8 nəfərlik", "Savor Ghee (150q)", "/product.php?slug=ghee-600g&lang=az.html",
              ["150q Savor Ghee (əridilmiş kərə yağı)", "3 stəkan basmati düyü", "600q quzu əti, qaysı və şabalıd", "Lavaş və təbii zəfəran dəmləməsi"],
              ["Düyü süzülür, ət soğan və Savor Ghee ilə qovrulur.", "Qazan Savor Ghee ilə yağlanır, lavaş düzülüb düyü və ət qat-qat yığılır.", "180°C sobada 60 dəqiqə qızılı rəng alana qədər dəmə qoyulur."])
              
        r2 = ("Milli Təamlar", "Səbzi Qovurma Plovu", "⏱️ 90 dəq", "👨‍🍳 Çətinlik: Orta", "🍽️ 5-6 nəfərlik", "Savor Kərə Yağı (180q)", "/products.php?lang=az.html",
              ["180q Savor Kərə Yağı", "500q quzu əti və 2 baş soğan", "Kəvər, keşniş, şüyüd, ispanaq, quzuqulağı", "Limon suyu və ya abqora"],
              ["Ət qaynadılıb soğanla Savor kərə yağında qızardılır.", "Göyərtilər iri doğranıb bol Savor kərə yağında zəif odda pörtlədilir.", "Ət və göyərti birləşdirilib abqora əlavə olunur və zəfəranlı düyü ilə verilir."])

        r3 = ("Səhər Təamı", "Kərə Yağlı Pomidor-Yumurta", "⏱️ 20 dəq", "👨‍🍳 Çətinlik: Asan", "🍽️ 2-3 nəfərlik", "Savor Kərə Yağı (80q)", "/products.php?lang=az.html",
              ["80q təbii Savor Kərə Yağı", "4 ədəd sulu Zirə pomidoru", "4 ədəd kənd yumurtası", "Duz və təzə çəkilmiş istiot"],
              ["Pomidorlar xırda doğranıb tavada öz suyunu çəkənə qədər bişirilir.", "Bol Savor kərə yağı əlavə olunub qızardılır, yumurtalar vurulub qaynar təndir çörəyi ilə təqdim edilir."])

        r4 = ("Milli Şirniyyat", "Klassik Bakı Paxlavası", "⏱️ 90 dəq", "👨‍🍳 Çətinlik: Usta", "🍽️ 12-15 nəfərlik", "Savor Kərə Yağı (300q)", "/products.php?lang=az.html",
              ["300q əridilmiş Savor Kərə Yağı", "1 kq əla növ un və 3 yumurta", "500q qoz ləpəsi və 500q şəkər tozu", "Hil və zəfəran şərbəti"],
              ["Xəmir nazik yayılır, aralarına bol Savor kərə yağı çəkilir və içlik səpilir.", "Romb kəsilib 180°C sobada qızardılır və qaynar şərbət tökülür."])

        r5 = ("Milli Şirniyyat", "Zərif Qat-qat Badambura", "⏱️ 80 dəq", "👨‍🍳 Çətinlik: Usta", "🍽️ 10-12 nəfərlik", "Savor Kərə Yağı (250q)", "/products.php?lang=az.html",
              ["250q ilıq Savor Kərə Yağı (qatlar üçün)", "700q un, 200ml süd və 1 yumurta", "300q üyüdülmüş təmiz badam və şəkər", "Üyüdülmüş hil və vanil"],
              ["Xəmirlər nazik yayılıb aralarına Savor kərə yağı sürtülərək üst-üstə yığılır və rulet bükülür.", "Rulet kəsilib içi açılır, badam içliyi qoyulub bükülür və 160°C sobada ağappaq bişirilir."])

        r6 = ("Milli Şirniyyat", "Əsl Qarabağ Kətəsi", "⏱️ 60 dəq", "👨‍🍳 Çətinlik: Orta", "🍽️ 8 nəfərlik", "Savor Kərə Yağı (200q)", "/products.php?lang=az.html",
              ["200q soyudulmuş Savor Kərə Yağı (İçlik üçün)", "500q un, 150q şəkər tozu və vanil", "Xəmir üçün: 400q un, 150q xama və maya"],
              ["İçlik (xoruz): Savor kərə yağı un və şəkərlə ovulub qum halına gətirilir.", "Xəmir yayılır, içinə bol kərə yağlı içlik qoyulub dairəvi bükülür, çəngəllə naxış vurulub 180°C sobada qızardılır."])

        r7 = ("Tort & Desert", "Xırtıldayan Napoleon Tortu", "⏱️ 80 dəq", "👨‍🍳 Çətinlik: Orta", "🍽️ 8-10 nəfərlik", "Savor Kərə Yağı (350q)", "/products.php?lang=az.html",
              ["350q dondurulmuş Savor Kərə Yağı", "450q un, buzlu su və sirkə", "Krem: 200q Savor yağı və qatılaşdırılmış süd"],
              ["Kərə yağı unla sürtgəcdən keçirilir, yoğrulub 10 korj şəklində bişirilir.", "Kərə yağı kremi ilə korjlar yağlanıb xırdalanmış qırıntılarla örtülür."])

        r8 = ("Tort & Desert", "Klassik Ballı Tort (Medovik)", "⏱️ 75 dəq", "👨‍🍳 Çətinlik: Orta", "🍽️ 10-12 nəfərlik", "Savor Kərə Yağı (200q)", "/products.php?lang=az.html",
              ["100q Savor Kərə Yağı (xəmir) + 150q (krem)", "3 x.q. təbii bal və 1 st şəkər tozu", "3 yumurta, 1 ç.q. soda və 400q un", "Krem: Bişmiş qatılaşdırılmış süd və xama"],
              ["Bal, şəkər və Savor yağı buxar vannasında əridilib soda əlavə edilir və xəmir yoğrulur.", "8 nazik qat bişirilir və zərif Savor kərə yağlı kremlə birləşdirilir."])

        r9 = ("Desert", "Zəngin Şokoladlı Brauni", "⏱️ 35 dəq", "👨‍🍳 Çətinlik: Asan", "🍽️ 6-8 nəfərlik", "Savor Kərə Yağı (180q)", "/products.php?lang=az.html",
              ["180q keyfiyyətli Savor Kərə Yağı", "200q tünd qara şokolad (70%)", "3 yumurta və 150q qəhvəyi şəkər", "100q un və 30q kakao tozu"],
              ["Savor kərə yağı şokoladla birlikdə əridilir və ilıdılır.", "Yumurta və şəkər çalınır, şokoladlı kərə yağı qarışığı və un əlavə olunub 175°C sobada 22-25 dəqiqə bişirilir."])
              
        footer_sub = "Təbii xammaldan premium yağ məhsulları.<br>Pərakəndə və HORECA üçün istehsal."
        f_c1, f_c2, f_c3 = "ƏLAQƏ", "MƏHSULLAR", "SERTİFİKATLAR"
        f_p1, f_p2, f_p3 = "SAVOR Ghee 600 q", "SAVOR HORECA 20 kq", "İstehsal"
        f_s1, f_s2, f_s3 = "Bütün sənədlər", "Bütün məqalələr", "Topdan sifariş"
        f_p1_link, f_p2_link, f_p3_link = "/product.php?slug=ghee-600g&lang=az.html", "/product.php?slug=horeca-20kg&lang=az.html", "/production.php?lang=az.html"
        f_s1_link, f_s2_link, f_s3_link = "/certificates.php?lang=az.html", "/blog.php?lang=az.html", "/horeca.php?lang=az.html"
        copy_text = "© 2026 SAVOR. Bütün hüquqlar qorunur."
        motto_text = "Keyfiyyət • Şəffaflıq • Stabil təchizat"

    elif lang == "ru":
        title = "Кулинария & Рецепты | Сливочное Масло & Гхи Savor"
        desc = "Самые вкусные рецепты азербайджанской и мировой кухни со сливочным маслом и Гхи Savor."
        back_text = "← Главная Страница"
        home_link = "/ru.html"
        contact_link = "/contact.php?lang=ru.html"
        order_btn = "Заказать"
        h1 = "Кулинарные Рецепты Savor"
        subtitle = "Вкуснейшие национальные блюда, выпечка и изысканные десерты, приготовленные на 100% натуральном масле и ароматном Гхи Savor."
        btn_all, btn_milli, btn_seher, btn_sirniyyat, btn_tort = "Все Рецепты (9)", "Национальные Блюда", "Завтраки", "Восточные Сладости", "Торты & Десерты"
        prod_btn = "О продукте →"
        ing_title = "🛒 Ингредиенты:"
        prep_title = "👨‍🍳 Приготовление:"

        r1 = ("Национальные Блюда", "Шах Плов с Шафраном", "⏱️ 120 мин", "👨‍🍳 Сложность: Средняя", "🍽️ 6-8 порций", "Savor Ghee (150г)", "/product.php?slug=ghee-600g&lang=ru.html",
              ["150г топленого масла Savor Ghee", "3 стакана риса басмати", "600г баранины, курага и каштаны", "Лаваш и настой натурального шафрана"],
              ["Рис отваривается до полуготовности. Мясо обжаривается с луком на масле Savor Ghee.", "Казан смазывается маслом Savor Ghee, выстилается лавашом, слоями выкладывается рис с мясом.", "Запекается в духовке при 180°C около 60 минут до золотистой корочки."])

        r2 = ("Национальные Блюда", "Сябзи Говурма Плов", "⏱️ 90 мин", "👨‍🍳 Сложность: Средняя", "🍽️ 5-6 порций", "Масло Savor (180г)", "/products.php?lang=ru.html",
              ["180г сливочного масла Savor", "500г мяса баранины и 2 луковицы", "Праздничная зелень: кявяр, кинза, укроп, шпинат, щавель", "Лимонный сок или абгора"],
              ["Мясо отваривается и обжаривается с луком на сливочном масле Savor.", "Зелень тушится на слабом огне в обильном количестве масла Savor.", "Мясо соединяется с зеленью, заправляется абгорой и подается с шафрановым рисом."])

        r3 = ("Завтрак", "Помидор-Юмурта на Масле", "⏱️ 20 мин", "👨‍🍳 Сложность: Легко", "🍽️ 2-3 порции", "Масло Savor (80г)", "/products.php?lang=ru.html",
              ["80г натурального сливочного масла Savor", "4 сочных помидора Зиря", "4 деревенских яйца", "Соль и свежемолотый перец"],
              ["Помидоры нарезаются и тушатся в сковороде до испарения влаги.", "Добавляется щедрая порция масла Savor, вбиваются яйца и подается с горячим хлебом."])

        r4 = ("Сладости", "Бакинская Пахлава", "⏱️ 90 мин", "👨‍🍳 Сложность: Мастер", "🍽️ 12-15 порций", "Масло Savor (300г)", "/products.php?lang=ru.html",
              ["300г растопленного сливочного масла Savor", "1 кг муки высшего сорта и 3 яйца", "500г грецких орехов и 500г сахара", "Кардамон и шафрановый сироп"],
              ["Тесто раскатывается тончайшими слоями, смазывается маслом Savor и посыпается начинкой.", "Нарезается ромбиками, выпекается при 180°C и заливается горячим сиропом."])

        r5 = ("Сладости", "Нежная Слоеная Бадамбура", "⏱️ 80 мин", "👨‍🍳 Сложность: Мастер", "🍽️ 10-12 порций", "Масло Savor (250г)", "/products.php?lang=ru.html",
              ["250г теплого масла Savor (для слоев)", "700г муки, 200мл молока и 1 яйцо", "300г очищенного молотого миндаля и сахар", "Молотый кардамон и ваниль"],
              ["Слои теста обильно смазываются маслом Savor, сворачиваются в рулет.", "Формируются бадамбура с миндальной начинкой и выпекаются при 160°C до белоснежного цвета."])

        r6 = ("Сладости", "Карабахская Кята", "⏱️ 60 мин", "👨‍🍳 Сложность: Средняя", "🍽️ 8 порций", "Масло Savor (200г)", "/products.php?lang=ru.html",
              ["200г охлажденного сливочного масла Savor (для начинки)", "500г муки, 150г сахарной пудры и ваниль", "Тесто: 400г муки, 150г сметаны и дрожжи"],
              ["Начинка: масло Savor перетирается с мукой и сахаром в нежную крошку.", "Тесто раскатывается, начиняется, формуется круг с узором вилкой и выпекается до румянца."])

        r7 = ("Торты & Десерты", "Хрустящий Торт Наполеон", "⏱️ 80 мин", "👨‍🍳 Сложность: Средняя", "🍽️ 8-10 порций", "Масло Savor (350г)", "/products.php?lang=ru.html",
              ["350г замороженного сливочного масла Savor", "450г муки, ледяная вода и уксус", "Крем: 200г сливочного масла Savor и сгущенное молоко"],
              ["Масло натирается с мукой, замешивается слоеное тесто и выпекаются 10 коржей.", "Коржи промазываются пышным кремом из масла Savor и посыпаются крошкой."])

        r8 = ("Торты & Десерты", "Классический Медовик", "⏱️ 75 мин", "👨‍🍳 Сложность: Средняя", "🍽️ 10-12 порций", "Масло Savor (200г)", "/products.php?lang=ru.html",
              ["100г масла Savor (тесто) + 150г (крем)", "3 ст.л. натурального меда и 1 стакан сахара", "3 яйца, 1 ч.л. соды и 400г муки", "Крем: Вареная сгущенка и сметана"],
              ["Мед, сахар и масло Savor прогреваются на водяной бане с содой.", "Выпекаются 8 коржей и пропитываются нежнейшим кремом."])

        r9 = ("Десерты", "Насыщенный Шоколадный Брауни", "⏱️ 35 мин", "👨‍🍳 Сложность: Легко", "🍽️ 6-8 порций", "Масло Savor (180г)", "/products.php?lang=ru.html",
              ["180г премиального масла Savor", "200г темного шоколада (70%)", "3 яйца и 150г тростникового сахара", "100г муки и 30г какао-порошка"],
              ["Масло Savor растапливается вместе с шоколадом.", "Яйца взбиваются с сахаром, смешиваются с шоколадным маслом и выпекаются при 175°C 22-25 минут."])

        footer_sub = "Премиальная масляная продукция из натурального сырья.<br>Производство для розницы и HORECA."
        f_c1, f_c2, f_c3 = "КОНТАКТЫ", "ПРОДУКЦИЯ", "СЕРТИФИКАТЫ"
        f_p1, f_p2, f_p3 = "SAVOR Ghee 600 г", "SAVOR HORECA 20 кг", "Производство"
        f_s1, f_s2, f_s3 = "Все документы", "Все статьи", "Оптовый заказ"
        f_p1_link, f_p2_link, f_p3_link = "/product.php?slug=ghee-600g&lang=ru.html", "/product.php?slug=horeca-20kg&lang=ru.html", "/production.php?lang=ru.html"
        f_s1_link, f_s2_link, f_s3_link = "/certificates.php?lang=ru.html", "/blog.php?lang=ru.html", "/horeca.php?lang=ru.html"
        copy_text = "© 2026 SAVOR. Все права защищены."
        motto_text = "Качество • Прозрачность • Стабильные поставки"

    else: # English
        title = "Culinary & Recipes | Savor Butter & Ghee"
        desc = "Delicious traditional Azerbaijani and gourmet recipes made with 100% natural Savor butter and Ghee."
        back_text = "← Home Page"
        home_link = "/en.html"
        contact_link = "/contact.php?lang=en.html"
        order_btn = "Order Now"
        h1 = "Savor Culinary Recipes"
        subtitle = "Authentic Azerbaijani dishes, traditional pastries and delicate desserts made with 100% pure Savor butter and aromatic Ghee."
        btn_all, btn_milli, btn_seher, btn_sirniyyat, btn_tort = "All Recipes (9)", "National Dishes", "Breakfast", "Sweet Pastries", "Cakes & Desserts"
        prod_btn = "View Product →"
        ing_title = "🛒 Ingredients:"
        prep_title = "👨‍🍳 Instructions:"

        r1 = ("National Dishes", "Royal Saffron Shah Plov", "⏱️ 120 mins", "👨‍🍳 Difficulty: Medium", "🍽️ 6-8 servings", "Savor Ghee (150g)", "/product.php?slug=ghee-600g&lang=en.html",
              ["150g pure Savor Ghee", "3 cups basmati rice", "600g lamb or veal, apricots and chestnuts", "Lavash flatbread and saffron infusion"],
              ["Rice is parboiled. Meat is sautéed with onions in rich Savor Ghee.", "The pot is greased with Savor Ghee, lined with lavash, and layered with rice and meat.", "Baked at 180°C for 60 minutes until golden and crusty."])

        r2 = ("National Dishes", "Sabzi Govurma Plov", "⏱️ 90 mins", "👨‍🍳 Difficulty: Medium", "🍽️ 5-6 servings", "Savor Butter (180g)", "/products.php?lang=en.html",
              ["180g pure Savor Butter", "500g lamb meat and 2 onions", "Fresh herbs: cilantro, dill, spinach, sorrel, leeks", "Lemon juice or verjuice"],
              ["Meat is braised and browned with onions in Savor butter.", "Herbs are chopped and sautéed gently in plenty of Savor butter.", "Meat and herbs are combined and served over fragrant saffron rice."])

        r3 = ("Breakfast", "Butter Tomato-Egg Scramble", "⏱️ 20 mins", "👨‍🍳 Difficulty: Easy", "🍽️ 2-3 servings", "Savor Butter (80g)", "/products.php?lang=en.html",
              ["80g natural Savor Butter", "4 ripe juicy tomatoes", "4 farm eggs", "Salt and freshly ground black pepper"],
              ["Tomatoes are simmered in a skillet until their juices reduce.", "A generous knob of Savor butter is melted in, eggs are stirred in, and served sizzling with hot bread."])

        r4 = ("Pastries", "Classic Baku Pakhlava", "⏱️ 90 mins", "👨‍🍳 Difficulty: Expert", "🍽️ 12-15 servings", "Savor Butter (300g)", "/products.php?lang=en.html",
              ["300g melted Savor Butter", "1 kg premium flour and 3 eggs", "500g ground walnuts and 500g sugar", "Cardamom and saffron syrup"],
              ["Dough is rolled into paper-thin layers, brushed with Savor butter and filled with spiced walnuts.", "Cut into diamond shapes, baked at 180°C and drenched in hot saffron syrup."])

        r5 = ("Pastries", "Delicate Layered Badambura", "⏱️ 80 mins", "👨‍🍳 Difficulty: Expert", "🍽️ 10-12 servings", "Savor Butter (250g)", "/products.php?lang=en.html",
              ["250g warm Savor Butter (for laminating)", "700g flour, 200ml milk and 1 egg", "300g peeled ground almonds and sugar", "Cardamom and vanilla"],
              ["Laminated dough is generously buttered with Savor butter, rolled into spirals.", "Filled with almond stuffing and baked at 160°C until delicate and ivory white."])

        r6 = ("Pastries", "Authentic Karabakh Kyata", "⏱️ 60 mins", "👨‍🍳 Difficulty: Medium", "🍽️ 8 servings", "Savor Butter (200g)", "/products.php?lang=en.html",
              ["200g chilled Savor Butter (for crumb filling)", "500g flour, 150g powdered sugar and vanilla", "Dough: 400g flour, 150g sour cream and yeast"],
              ["Filling: Savor butter is rubbed with flour and sugar into rich buttery crumbs.", "Dough is rolled, stuffed, shaped into a round pastry with fork patterns and baked until golden."])

        r7 = ("Cakes & Desserts", "Crispy Napoleon Cake", "⏱️ 80 mins", "👨‍🍳 Difficulty: Medium", "🍽️ 8-10 servings", "Savor Butter (350g)", "/products.php?lang=en.html",
              ["350g chilled Savor Butter", "450g flour, iced water and vinegar", "Cream: 200g Savor butter and condensed milk"],
              ["Flaky puff pastry layers are rolled thin and baked until crispy.", "Layered with velvety Savor butter cream and coated in crispy crumbs."])

        r8 = ("Cakes & Desserts", "Classic Honey Cake (Medovik)", "⏱️ 75 mins", "👨‍🍳 Difficulty: Medium", "🍽️ 10-12 servings", "Savor Butter (200g)", "/products.php?lang=en.html",
              ["100g Savor Butter (dough) + 150g (cream)", "3 tbsp natural honey and 1 cup sugar", "3 eggs, 1 tsp baking soda and 400g flour", "Cream: Dulce de leche and sour cream"],
              ["Honey, sugar and Savor butter are gently heated, forming an aromatic dough.", "8 golden layers are baked and infused with luscious buttercream."])

        r9 = ("Desserts", "Rich Chocolate Brownie", "⏱️ 35 mins", "👨‍🍳 Difficulty: Easy", "🍽️ 6-8 servings", "Savor Butter (180g)", "/products.php?lang=en.html",
              ["180g premium Savor Butter", "200g dark chocolate (70%)", "3 eggs and 150g brown sugar", "100g flour and 30g cocoa powder"],
              ["Savor butter and dark chocolate are melted together smoothly.", "Eggs and sugar are whipped, folded with chocolate butter, and baked at 175°C for 22-25 mins."])

        footer_sub = "Premium dairy and butter products from natural raw materials.<br>Production for Retail and HORECA."
        f_c1, f_c2, f_c3 = "CONTACT", "PRODUCTS", "CERTIFICATES"
        f_p1, f_p2, f_p3 = "SAVOR Ghee 600 g", "SAVOR HORECA 20 kg", "Production"
        f_s1, f_s2, f_s3 = "All Documents", "All Articles", "Wholesale Order"
        f_p1_link, f_p2_link, f_p3_link = "/product.php?slug=ghee-600g&lang=en.html", "/product.php?slug=horeca-20kg&lang=en.html", "/production.php?lang=en.html"
        f_s1_link, f_s2_link, f_s3_link = "/certificates.php?lang=en.html", "/blog.php?lang=en.html", "/horeca.php?lang=en.html"
        copy_text = "© 2026 SAVOR. All rights reserved."
        motto_text = "Quality • Transparency • Reliable Supply"

    recipes_data = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
    cat_keys = ["milli", "milli", "seher", "sirniyyat", "sirniyyat", "sirniyyat", "tort", "tort", "tort"]

    cards_html = ""
    for idx, (r, c_key) in enumerate(zip(recipes_data, cat_keys), start=1):
        badge, name, time_str, diff_str, yield_str, rec_butter, prod_url, ings, steps = r
        slides = make_slides(idx)
        ing_items = "".join([f"<li><label><input type=\"checkbox\"> <span>{item}</span></label></li>" for item in ings])
        step_items = "".join([f"<li>{step}</li>" for step in steps])
        
        cards_html += f"""
    <!-- Recipe {idx} -->
    <article class="recipe-card" data-category="{c_key}">
      <div class="swiper mySwiper">
        <div class="swiper-wrapper">{slides}
        </div>
        <div class="swiper-pagination"></div>
        <div class="swiper-button-next"></div>
        <div class="swiper-button-prev"></div>
      </div>
      <div class="recipe-body">
        <span class="badge-category">{badge}</span>
        <h2 class="recipe-title">{name}</h2>
        <div class="meta-tags"><span>{time_str}</span><span>{diff_str}</span><span>{yield_str}</span></div>
        <div class="savor-highlight">
          <span>🧈 {rec_butter}</span>
          <a href="{prod_url}">{prod_btn}</a>
        </div>
        <div class="section-subtitle">{ing_title}</div>
        <ul class="ingredients-list">
          {ing_items}
        </ul>
        <div class="section-subtitle">{prep_title}</div>
        <ol class="steps-list">
          {step_items}
        </ol>
      </div>
    </article>"""

    active_az = 'class="active"' if lang == "az" else ''
    active_ru = 'class="active"' if lang == "ru" else ''
    active_en = 'class="active"' if lang == "en" else ''

    html_content = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  
  <!-- Swiper.js CSS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <link rel="stylesheet" href="../assets/css/style.css">
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,600&display=swap" rel="stylesheet">

  <style>
    :root {
      --primary-gold: #c59d5f;
      --primary-dark: #1f1d1a;
      --accent-brown: #965627;
      --bg-cream: #ece7e1;
      --card-bg: #faf8f5;
      --text-main: #1f1d1a;
      --text-muted: #6b665f;
      --border-soft: #ddd7cd;
    }

    *, *::before, *::after {
      box-sizing: border-box !important;
      margin: 0;
      padding: 0;
    }
    
    html, body {
      overflow-x: hidden !important;
      width: 100% !important;
      max-width: 100vw !important;
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-cream);
      color: var(--text-main);
    }

    .nav-bar-top {
      width: 100%;
      padding: 14px 25px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #171411;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }

    .nav-back {
      color: #e5ded6;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.92rem;
      transition: color 0.2s;
    }

    .nav-back:hover {
      color: var(--primary-gold);
    }

    .nav-brand {
      color: var(--primary-gold);
      font-weight: 800;
      letter-spacing: 2px;
      font-size: 1.1rem;
    }

    .nav-right {
      display: flex;
      align-items: center;
      gap: 15px;
    }

    .lang-switch {
      display: flex;
      gap: 10px;
      font-size: 0.88rem;
      font-weight: 700;
    }

    .lang-switch a {
      color: #8c8275;
      text-decoration: none;
      transition: color 0.2s;
    }

    .lang-switch a.active, .lang-switch a:hover {
      color: var(--primary-gold);
    }

    .btn-order {
      background-color: var(--accent-brown);
      color: white !important;
      padding: 7px 16px;
      border-radius: 20px;
      text-decoration: none;
      font-size: 0.86rem;
      font-weight: 700;
      transition: all 0.2s;
    }

    .btn-order:hover {
      background-color: #7a3e18;
      transform: translateY(-2px);
    }

    .recipe-header {
      width: 100%;
      background: linear-gradient(rgba(23, 20, 17, 0.88), rgba(23, 20, 17, 0.95)), url('https://media.azersun.com/crystalex.az/files/receipt/393cbafb-8e30-43db-8974-b2efd58e8aed_CristalEx.jpeg') center/cover;
      color: white;
      padding: 65px 20px 40px;
      text-align: center;
    }

    .recipe-header h1 {
      font-family: 'Playfair Display', serif;
      font-size: 2.6rem;
      margin-bottom: 12px;
      color: #f7e7ce;
    }

    .recipe-header p {
      font-size: 1.08rem;
      max-width: 680px;
      margin: 0 auto 24px;
      color: #d1d5db;
      line-height: 1.6;
    }

    .filter-container {
      display: flex;
      justify-content: center;
      gap: 8px;
      flex-wrap: wrap;
      max-width: 800px;
      margin: 0 auto;
    }

    .filter-btn {
      background: rgba(255,255,255,0.1);
      color: white;
      border: 1px solid rgba(255,255,255,0.25);
      padding: 8px 16px;
      border-radius: 25px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.88rem;
      transition: all 0.3s ease;
    }

    .filter-btn.active, .filter-btn:hover {
      background: var(--primary-gold);
      color: #122017;
      border-color: var(--primary-gold);
    }

    /* MƏRKƏZLƏŞDİRİLMİŞ QUTU */
    .recipes-container {
      width: 100%;
      max-width: 1200px;
      margin: 35px auto 60px;
      padding: 0 20px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
      gap: 30px;
    }

    .recipe-card {
      width: 100%;
      max-width: 100%;
      background: var(--card-bg);
      border-radius: 18px;
      overflow: hidden;
      box-shadow: 0 10px 25px rgba(0,0,0,0.05);
      border: 1px solid var(--border-soft);
      display: flex;
      flex-direction: column;
      transition: transform 0.3s ease;
    }

    .recipe-card:hover {
      transform: translateY(-5px);
    }

    .swiper {
      width: 100% !important;
      max-width: 100% !important;
      height: 250px;
      overflow: hidden;
    }

    .swiper-slide {
      width: 100% !important;
    }

    .swiper-slide img {
      width: 100% !important;
      height: 100% !important;
      object-fit: cover !important;
      display: block;
    }

    .recipe-body {
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }

    .badge-category {
      align-self: flex-start;
      background: #f0e6d6;
      color: #8c6828;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      padding: 4px 10px;
      border-radius: 15px;
      margin-bottom: 10px;
    }

    .recipe-title {
      font-family: 'Playfair Display', serif;
      font-size: 1.5rem;
      margin: 0 0 10px;
      color: var(--primary-dark);
      line-height: 1.3;
    }

    .meta-tags {
      display: flex;
      gap: 12px;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 15px;
      padding-bottom: 12px;
      border-bottom: 1px dashed #e2e8f0;
      flex-wrap: wrap;
    }

    .savor-highlight {
      background: #fbf6ee;
      border-left: 4px solid var(--primary-gold);
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      margin-bottom: 16px;
      font-size: 0.88rem;
      font-weight: 600;
      color: #6b4d1b;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .savor-highlight a {
      color: #8c6828;
      text-decoration: underline;
      font-weight: 700;
      font-size: 0.82rem;
    }

    .section-subtitle {
      font-size: 0.94rem;
      font-weight: 700;
      color: var(--primary-dark);
      margin: 10px 0 6px;
    }

    .ingredients-list {
      list-style: none;
      padding: 0;
      margin: 0 0 14px;
    }

    .ingredients-list li {
      padding: 4px 0;
      font-size: 0.88rem;
      color: #4a5568;
    }

    .ingredients-list label {
      display: flex;
      align-items: center;
      gap: 8px;
      cursor: pointer;
    }

    .ingredients-list input[type="checkbox"] {
      accent-color: var(--primary-gold);
      width: 16px;
      height: 16px;
    }

    .ingredients-list input[type="checkbox"]:checked + span {
      text-decoration: line-through;
      color: #a0aec0;
    }

    .steps-list {
      padding-left: 16px;
      margin: 0 0 10px;
      font-size: 0.86rem;
      color: #4a5568;
      line-height: 1.5;
    }

    .steps-list li {
      margin-bottom: 5px;
    }

    /* MOBİL DƏQİQ MƏRKƏZLƏŞDİRMƏ */
    @media (max-width: 768px) {
      .recipe-header {
        padding: 45px 16px 30px;
      }
      .recipe-header h1 {
        font-size: 2rem;
      }
      .recipe-header p {
        font-size: 0.95rem;
        margin-bottom: 18px;
      }
      .filter-btn {
        padding: 6px 12px;
        font-size: 0.8rem;
      }
      .recipes-container {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        padding: 0 16px !important;
        margin: 20px auto 45px !important;
        gap: 20px !important;
        width: 100% !important;
      }
      .recipe-card {
        width: 100% !important;
        max-width: 100% !important;
        border-radius: 16px;
      }
      .swiper {
        height: 220px !important;
      }
      .recipe-body {
        padding: 18px 14px !important;
      }
    }

    /* Savor Footer */
    .savor-footer {
      width: 100%;
      background-color: #120e0b;
      color: #d1c7bc;
      padding: 55px 20px 25px;
      font-family: 'Plus Jakarta Sans', sans-serif;
      margin-top: 50px;
    }

    .footer-top {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 1.4fr 1fr 1fr 1fr;
      gap: 35px;
      padding-bottom: 35px;
    }

    @media (max-width: 820px) {
      .footer-top {
        grid-template-columns: 1fr;
        gap: 25px;
      }
      .nav-bar-top {
        padding: 12px 16px;
      }
      .nav-brand {
        display: none;
      }
    }

    .footer-logo {
      font-size: 2.4rem;
      font-weight: 800;
      color: #c57b2e;
      letter-spacing: 2px;
      margin-bottom: 12px;
    }

    .brand-col p {
      color: #8f8579;
      font-size: 0.92rem;
      line-height: 1.5;
    }

    .footer-col h4 {
      color: #c57b2e;
      font-size: 0.8rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      margin: 0 0 15px;
      text-transform: uppercase;
    }

    .footer-col ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    .footer-col ul li {
      margin-bottom: 10px;
      font-size: 0.92rem;
    }

    .footer-col ul li a, .footer-col ul li span {
      color: #e5ded6;
      text-decoration: none;
      transition: color 0.2s ease;
    }

    .footer-col ul li a:hover {
      color: #c57b2e;
    }

    .footer-bottom {
      max-width: 1200px;
      margin: 0 auto;
      padding-top: 20px;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.82rem;
      color: #7d7367;
      flex-wrap: wrap;
      gap: 12px;
    }

    /* Floating WhatsApp Button */
    .floating-wa {
      position: fixed !important;
      bottom: 25px !important;
      right: 25px !important;
      width: 54px !important;
      height: 54px !important;
      background-color: #25d366 !important;
      color: #ffffff !important;
      border-radius: 50% !important;
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
      box-shadow: 0 4px 15px rgba(0,0,0,0.35) !important;
      text-decoration: none !important;
      z-index: 999999 !important;
      transition: transform 0.3s ease, box-shadow 0.3s ease !important;
    }

    .floating-wa:hover {
      transform: scale(1.1) !important;
      box-shadow: 0 6px 20px rgba(37, 211, 102, 0.6) !important;
    }

    .floating-wa svg {
      width: 30px !important;
      height: 30px !important;
      fill: #ffffff !important;
      display: block !important;
    }
  </style>
</head>
<body>

  <!-- Dəqiq Reseptlərarası Dil Keçidi -->
  <header class="nav-bar-top">
    <a href="{home_link}" class="nav-back">{back_text}</a>
    <span class="nav-brand">SAVOR</span>
    <div class="nav-right">
      <div class="lang-switch">
        <a href="/recipes/index.html" {active_az}>AZ</a>
        <a href="/recipes/ru.html" {active_ru}>RU</a>
        <a href="/recipes/en.html" {active_en}>EN</a>
      </div>
      <a href="{contact_link}" class="btn-order">{order_btn}</a>
    </div>
  </header>

  <!-- Başlıq və Filterlər -->
  <section class="recipe-header">
    <h1>{h1}</h1>
    <p>{subtitle}</p>
    
    <div class="filter-container">
      <button class="filter-btn active" onclick="filterRecipes('all')">{btn_all}</button>
      <button class="filter-btn" onclick="filterRecipes('milli')">{btn_milli}</button>
      <button class="filter-btn" onclick="filterRecipes('seher')">{btn_seher}</button>
      <button class="filter-btn" onclick="filterRecipes('sirniyyat')">{btn_sirniyyat}</button>
      <button class="filter-btn" onclick="filterRecipes('tort')">{btn_tort}</button>
    </div>
  </section>

  <!-- Reseptlər Grid -->
  <main class="recipes-container">
    {cards_html}
  </main>

  <!-- SAVOR FOOTER -->
  <footer class="savor-footer">
    <div class="footer-top">
      <div class="footer-col brand-col">
        <div class="footer-logo">SAVOR</div>
        <p>{footer_sub}</p>
      </div>
      <div class="footer-col">
        <h4>{f_c1}</h4>
        <ul>
          <li><a href="tel:+994775759555">+994 77 575 95 55</a></li>
          <li><a href="tel:+994517225511">+994 51 722 55 11</a></li>
          <li><a href="mailto:sales@savor.az">sales@savor.az</a></li>
          <li><span>Bakı, Azərbaycan</span></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{f_c2}</h4>
        <ul>
          <li><a href="{f_p1_link}">{f_p1}</a></li>
          <li><a href="{f_p2_link}">{f_p2}</a></li>
          <li><a href="{f_p3_link}">{f_p3}</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>{f_c3}</h4>
        <ul>
          <li><a href="{f_s1_link}">{f_s1}</a></li>
          <li><a href="{f_s2_link}">{f_s2}</a></li>
          <li><a href="{f_s3_link}">{f_s3}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-copy">{copy_text}</div>
      <div class="footer-motto">{motto_text}</div>
    </div>
  </footer>

  <!-- Official Floating WhatsApp Button -->
  <a href="https://wa.me/994775759555" target="_blank" rel="noopener noreferrer" class="floating-wa" title="WhatsApp">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
      <path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/>
    </svg>
  </a>

  <!-- Swiper.js Script & Filter -->
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script>
    const swiper = new Swiper('.mySwiper', {{
      loop: true,
      pagination: {{ el: '.swiper-pagination', clickable: true }},
      navigation: {{ nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' }},
      autoplay: {{ delay: 3500, disableOnInteraction: false }},
    }});

    function filterRecipes(category) {{
      const buttons = document.querySelectorAll('.filter-btn');
      buttons.forEach(btn => btn.classList.remove('active'));
      event.target.classList.add('active');

      const cards = document.querySelectorAll('.recipe-card');
      cards.forEach(card => {{
        if (category === 'all' || card.getAttribute('data-category') === category) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}
  </script>

</body>
</html>"""
    return html_content

# Faylları generasiya edirik
with open("recipes/index.html", "w", encoding="utf-8") as f:
    f.write(generate_html("az"))

with open("recipes/ru.html", "w", encoding="utf-8") as f:
    f.write(generate_html("ru"))

with open("recipes/en.html", "w", encoding="utf-8") as f:
    f.write(generate_html("en"))

print("✓ Dəqiq dil keçidləri və WhatsApp loqoları uğurla yeniləndi!")
