import sqlite3

authors = ['А.С Пушкин', 'С.А Есенин', 'А.А Блок']
titles = ["Ex ungue leonem", "А в ненастные дни", "Адели", "Берёза", "Что это такое?", "Черемуха",
          "Ночь, улица, фонарь, аптека…", "Ветхая избушка", "Летний вечер"]
texts = ["Недавно я стихами как-то свистнул\nИ выдал их без подписи моей;\nЖурнальный шут о них статейку тиснул,"
         "\nБез подписи ж пустив ее, злодей.\nНо что ж? Ни мне, ни площадному шуту\nНе удалось прикрыть своих проказ:"
         "\nОн по когтям узнал меня в минуту,\nЯ по ушам узнал его как раз", "А в ненастные дни\nСобирались они"
         "\nЧасто.\nГнули, мать их ети!\nОт пятидесяти\nНа сто.\nИ выигрывали,\nИ отписывали\nМелом."
         "\nТак в ненастные дни\nЗанимались они\nДелом.", "Играй, Адель,\nНе знай печали;\nХариты, Лель\nТебя венчали"
         "\nИ колыбель\nТвою качали;\nТвоя весна\nТиха, ясна;\nДля наслажденья\nТы рождена;\nЧас упоенья\nЛови, лови!"
         "\nМладые лета\nОтдай любви,\nИ в шуме света\nЛюби, Адель,\nМою свирель.", "Белая береза\nПод моим окном"
         "\nПринакрылась снегом,\nТочно серебром.\nНа пушистых ветках\nСнежною каймой\nРаспустились кисти"
         "\nБелой бахромой.\nИ стоит береза\nВ сонной тишине,\nИ горят снежинки\nВ золотом огне.\nА заря, лениво"
         "\nОбходя кругом,\nОбсыпает ветки\nНовым серебром.", "В этот лес завороженный,\nПо пушинкам серебра,"
         "\nЯ с винтовкой заряженной\nНа охоту шел вчера.\nПо дорожке чистой, гладкой\nЯ прошел, не наследил…"
         "\nКто ж катался здесь украдкой?\nКто здесь падал и ходил?\nПодойду, взгляну поближе:"
         "\nХрупкий снег изломан весь.\nЗдесь вот когти, дальше — лыжи…\nКто-то странный бегал здесь."
         "\nКабы твердо знал я тайну\nЗаколдованным речам,\nЯ узнал бы хоть случайно,\nКто здесь бродит по ночам."
         "\nИз-за елки бы высокой\nПодсмотрел я на кругу:\nКто глубокий след далекий\nОставляет на снегу?..",
         "Черемуха душистая\nС весною расцвела\nИ ветки золотистые,\nЧто кудри, завила.\nКругом роса медвяная"
         "\nСползает по коре,\nПод нею зелень пряная\nСияет в серебре.\nА рядом, у проталинки,\nВ траве, между корней,"
         "\nБежит, струится маленький\nСеребряный ручей.\nЧеремуха душистая,\nРазвесившись, стоит,\nА зелень золотистая"
         "\nНа солнышке горит.\nчей волной гремучею\nВсе ветки обдает\nИ вкрадчиво под кручею\nЕй песенки поет.",
         "Ночь, улица, фонарь, аптека,\nБессмысленный и тусклый свет.\nЖиви еще хоть четверть века —"
         "\nВсе будет так. Исхода нет.\nУмрешь — начнешь опять сначала\nИ повторится все, как встарь:"
         "\nНочь, ледяная рябь канала,\nАптека, улица, фонарь.", "Ветхая избушка\nВся в снегу стоит.\nБабушка-старушка"
         "\nИз окна глядит.\nВнукам-шалунишкам\nПо колено снег.\nВесел ребятишкам\nБыстрых санок бег…\nБегают, смеются,"
         "\nЛепят снежный дом,\nЗвонко раздаются\nГолоса кругом…\nВ снежном доме будет\nРезвая игра…\nПальчики застудят, —"
         "\nПо домам пора!\nЗавтра выпьют чаю,\nГлянут из окна —\nАн уж дом растаял,\nНа дворе — весна!",
         "Последние лучи заката\nЛежат на поле сжатой ржи.\nДремотой розовой объята\nТрава некошеной межи."
         "\nНи ветерка, ни крика птицы,\nНад рощей — красный диск луны,\nИ замирает песня жницы\nСреди вечерней тишины."
         "\nЗабудь заботы и печали,\nУмчись без цели на коне\nВ туман и в луговые дали,\nНавстречу ночи и луне!"]

conn = sqlite3.connect('mysqlite.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE If NOT EXISTS library (name text, title text, strings text)''')

for i in range(len(authors)):
    for y in range(int(len(titles)/3)):
        c.execute(f'''INSERT INTO library VALUES('{authors[i]}', '{titles[y+i+2*i]}', '{texts[y+i+2*i]}')''')
conn.commit()
conn.close()