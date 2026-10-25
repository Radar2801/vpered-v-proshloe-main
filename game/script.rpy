transform right:
    xalign 0.999
    yalign 0.001
transform left:
    xalign 0.001
    yalign 0.001
# Определение персонажей игры.
define gg = Character('Артём', color="#c8ffc8",image="artem",callback=name_callback,cb_name="artem")
image artem normala = At("artem normal",sprite_highlight("artem"))
define teach = Character('Марья Ивановна', color="#c8ffc8",image="teacher",callback=name_callback,cb_name="teacher")
image teacher normala = At("teacher normal",sprite_highlight("teacher"))
define slav = Character("Святослав",color="#c8ffc8",image="slav",callback=name_callback,cb_name="slav")
image voin slava = At("voin slav",sprite_highlight("slav"))
define rurik = Character("Рюрик",color="#c8ffc8",image="rurik",callback=name_callback,cb_name="rurik")
image rurika = At("rurik",sprite_highlight("rurik"))
define slav2 = Character("Ярослав",color="#c8ffc8",image="slav2",callback=name_callback,cb_name="slav2")
image voin slava2 = At("voin slav 2",sprite_highlight("slav2"))
define vladimir = Character("Владимир Красное Солнышко",color="#c8ffc8",image="vladimir",callback=name_callback,cb_name="vladimir")
image vladimir krasnoa = At("vladimir krasno",sprite_highlight("vladimir"))


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


# Игра начинается здесь:
label start:
    scene now time with dissolve
    pause(2)
    scene museum zal with dissolve

    show artem normala  at left with dissolve: 
        xzoom -1.0
    show teacher normala at right with dissolve

    teach "Артём, не отставай от группы и ничего не трогай руками."
    gg "Да ладно, Марь Иванна, я не маленький."
    teach"И никуда не отлучайся. Понял?"
    gg "(закатывает глаза) Понял-понял..."
    teach "ну смотри мне!"
    hide teacher normala with dissolve
    "И зачем я вообще согласился на эту поездку в музей?"
    "Ненавижу историю. Серьёзно, зачем она мне в жизни?"
    "Надеюсь, хотя бы тройку поставят за активность..."
    "Мог бы сейчас в «Мир танков» катать, а не по пыльным залам ходить."
    "А теперь..."
    "Я огляделся, но никого уже не было."
    gg "Ну прекрасно! Я теперь даже не знаю, куда идти."
    hide artem normala with dissolve
    pause(1)
    scene main zal with dissolve
    show artem normala with dissolve:
        xzoom -1.0
    gg "ну чтож если я остался один, то нужно чем то заняться."
    menu:
        gg "куда бы мне пойти?"
        "Зал(Древняя Русь)":
            jump old_rus 

        "Зал(Российская Империя)":
            jump rus_imperia 

        "Зал(СССР)":
            jump sssr
    return


label old_rus:  
    gg "Пойду в зал Древней Руси."
    pause(1)
    scene old rus zal with dissolve
    show artem normala  at left with dissolve: 
            xzoom -1.0
    pause(1)
    scene old rus zal portal 
    show artem normala  at left: 
            xzoom -1.0
    "Воу! Что это такое!?"
    "Что то похожее на..."
    "Портал!"
    "Но я видел такое только в фильмах"
    "Интересно а что будет если туда войти!?"
    #==============================862 год========================================#
    scene 862 with dissolve
    pause(2)
    scene old rus les with dissolve
    show artem normala  at left with dissolve: 
            xzoom -1.0
    "Я делаю шаг вперёд — и музейный зал исчезает. Вокруг лес, река, деревянные избы. Холодно."
    gg "Так, я так и знал. Только руку протянул — и сразу в прошлое. Хоть бы в лето переносило, а то вечно в холод..."
    "Ко мне подбегает мужик в меховой шапке и  тащит за руки."
    show voin slava at right with dissolve
    slav "Ой, братцы, гляньте — ещё один варяг приплыл! Сам к нам идёт!"
    gg "Мужики, отпустите, я не варяг. Я просто... отстал от группы."
    slav "Молчи, князь Рюрик ждёт!"
    "(закатывает глаза) Рюрик... Да знаю я, 862 год, призвание варягов, начало русской государственности. Учительница сто раз повторяла. Скучнотища."
    "Меня волокут к дворцу. Сидит бородатый мужик с мечом — Рюрик."
    hide artem normala with dissolve
    hide voin slava at right with dissolve
    scene tron zal with dissolve
    show artem normala  at left with dissolve: 
            xzoom -1.0
    show rurika at right with dissolve
    rurik "А, подкрепление! Садись, будешь дружинником. Завтра идём на хазар."
    "Хазары... Да, был такой народ, кочевники, разгромил их Святослав потом..."
    gg "А можно я просто понаблюдаю? Я вообще-то гуманитарий, мне бы потрогать всё..."
    rurik "Ты странный. Говоришь, что знаешь, а делать ничего не хочешь."
    gg "Да я просто... историю не люблю. Зачем она мне? Даты, имена... Всё равно ничего не изменится."
    rurik "Не изменится? Мальчик, я сегодня решаю, быть Руси или не быть. Это не даты. Это жизни."
    scene 3 days with dissolve
    pause(2)
    scene fire with dissolve
    show artem normala  at left with dissolve: 
            xzoom -1.0
    "Я провёл в дружине Рюрика три дня. Видил, как люди пашут землю, как дети бегают босиком, как старики рассказывают сказки у костра. Как Рюрик лично обходит дозоры ночью, не спит, думает о будущем."
    "Он же просто человек... Не «основатель государственности» из учебника. Просто мужик, который тащит на себе кучу проблем..."
    scene fire portal
    show artem normala  at left: 
        xzoom -1.0
    "О а вот и мой портал!"
    "Надо пойти попрощаться с Рюриком и идти в портал."
    show rurika at right with dissolve
    "А вот и Рюрик"
    gg "Вот и подошло время мне уходить."
    gg "Пока Рюрик"
    rurik "Странный ты парень. Много знаешь, но ничего не понимаешь. Возьми монету. Может, поймёшь потом."
    "Он протягивает мне какую-то странную монету,которую я сразу забрал."
    gg "Спасибо..."
    #==============================988 год========================================#
    scene 988 with dissolve
    pause(2)
    scene dnepr with dissolve
    show artem normala  at left with dissolve: 
            xzoom -1.0
    "Я попал на берег реки. Тысячи людей в воде. Громкий голос гремит с деревянной платформы."
    "Крещение Руси. 988 год. Владимир Красное Солнышко. Всё это я слышал на уроках, только зачем — непонятно."
    "Ко мне подходит дружинник в кольчуге."
    show voin slava2 at right with dissolve
    slav2 "Эй, отрок! Иди крестись, князь Владимир велел!"
    gg "Да я уже крещёный, у меня крестик есть."
    "Я достал из-под футболки цепочку с крестиком. Дружинник был в шоке."
    slav2 "Откуда у тебя крест?! Ты что, из будущего?!"
    gg "Ну да."
    slav2 "Чудо! Чудо! Князь, чудо!"
    hide voin slava2 with dissolve
    show vladimir krasnoa at right with dissolve
    vladimir "Говори, отрок, что видишь в будущем? Русь велика будет?"
    gg "Да. Очень. Только потом развалится. Потом опять соберётся. Потом опять... короче, сложно."
    vladimir "Значит, крестить всё равно надо."
    gg "Он же не из-за власти это делает. Он реально верит, что это спасёт людей... (вслух) Князь, а зачем вам это? Ну, крещение."
    vladimir "Посмотри на них. Раньше они друг друга в жертву приносили. А сегодня — братья. Разве это не стоит того?"
    "Я посмотрел на людей в реке. Видит, как обнимаются бывшие враги. Как плачут старики. Как дети смеются."
    gg "В учебнике было написано: «принятие христианства как государственной религии». Сухая фраза. А на самом деле... на самом деле это тысячи судеб."
    scene dnepr portal 
    show artem normala  at left: 
        xzoom -1.0
    show vladimir krasnoa at right
    gg "Пришло время мне идти дальше!"
    vladimir "Возьми рубаху. Носи и помни — история делается не датами, а людьми."
    vladimir "Прощай."
    gg "До свидание"


    return
label rus_imperia:
    gg "Пойду в зал Российской Империи."

    return
label sssr:
    gg "Пойду в зал СССР."

    return