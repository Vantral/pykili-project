import time
import random
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
import colorama
from colorama import Fore, Back, Style
colorama.init()
with open('important.txt', 'w', encoding = 'utf-8') as file:
    file.write('100\n0\n0\n4')
prob_scared = 0.3
questions = {
    '4 + 5 = ?': '9',
    '10 * 45 = ?': '450',
    'Столица Аргентины?': 'Буэнос-Айрес',
    'Является ли французский одним из домашних языков Канады?': 'Да',
    '5 + 6 = ?': '11',
    'Как зовут героя, за которого Вы играете (его имя без фамилии)?': 'Майкл',
    'Напишите год первого полёта человека в космос': '1961',
    'Является ли кортеж в питоне неизменяемым аналогом списка?': 'Да',
    'Сколько президентов было в США (включая текущего)?': '45',
    'Назовите последнего на данный момент музыканта, включённого в Клуб 27 (на английском языке, неполное имя и фамилию)': 'Amy Winehouse',
    'Назовите фамилию (в единственном числе) создателей мессенджера Telegram': 'Дуров',
}
info = {
    'health': 100,
    'body_count': 0,
    'lost': 0,
    'flashbang': 4,
}

def Michael(text):
    print(Fore.BLUE + Back.WHITE + 'Майкл:' + ' ' + text + Style.RESET_ALL)

def Lloyd(text):
    print(Fore.BLACK + Back.WHITE + 'Ллойд:' + ' ' + text + Style.RESET_ALL)

def Tom(text):
    print(Fore.CYAN + Back.BLACK + 'Том:' + ' ' + text + Style.RESET_ALL)

def Connor(text):
    print(Fore.GREEN + Back.BLACK + 'Коннор:' + ' ' + text + Style.RESET_ALL)

def further():
    further = input('Для продолжения нажмите ENTER')
    why = 0
    while further != '':
        if why > 5:
            further = input('Нужно нажать только ENTER, не надо пытаться ломать программу, пожалуйста :)')
        else:
            further = input('Для продолжения нажмите ENTER')
        why += 1
    print('\n')
    pass

def health_check():
    print('У Вас', info['health'], 'очков здоровья')

def flashbang_used():
    if info['flashbang'] == 0:
        print('В инвентаре больше нет оглушающих гранат')
    else:
        info['flashbang'] -= 1
        if info['flashbang'] == 1:
            print('Осталась одна оглушающая граната')
        
def tutorial_shooting_scene():
    print('Данный текст создан специально для того, чтобы научить Вас ориентироваться в перестрелках.\nКак будет идти перестрелка?')
    time.sleep(2)
    print('1. Необходимо выбрать цель для выстрела - рука, тело и голова.')
    print('Выстрел в руку обезоруживает противника, выстрел в тело может как обезоружить, так и убить противника, выстрел в голову убивает противника.\nПри условии, что Вы попадёте!')
    time.sleep(2)
    print('2. Вам будут выпадать вопросы, на которых нужно будет ответить максимально коротко, с большой буквы, если ответ требует букв.')
    print('Например, на вопрос "4 + 9 = ?" необходимо ответить "13" без кавычек, а на вопрос "Является ли Лондон столицей Англии?" нужно ответить "Да" (опять же, без кавычек).')
    time.sleep(2)
    print('Вы будете ограничены 5 секундами на ответ - за это время нужно будет ответить на как можно большее количество вопросов!')
    time.sleep(2)
    print('3. В результате Вы сформируете вероятность своего попадания. После этого Вам нужно будет только сидеть и смотреть на результаты.')
    print('Всё довольно просто! Желаю удачи и приятной игры!')
    further()
    
def shooting_scene():
    print('1 - Стрелять в руку;\n2 - Стрелять в тело;\n3 - Стрелять в голову.')
    shooting_choice = input('Напишите цифру действия и нажмите ENTER:')
    counter = 0
    while not shooting_choice:
        if counter >= 6:
            fail = 1
            break
        if counter == 5:
            print('Если Вы сейчас не сделаете выбор, Вы погибнете в перестрелке!')
            shooting_choice = input('Напишите цифру действия и нажмите ENTER:')
            counter += 1
        else:
            shooting_choice = input('Напишите цифру действия и нажмите ENTER:')
            counter += 1
    try:
        fail
    except NameError:
        fail = None
    if fail != None:
        health = 0
    else:
        prob = 0.5
        start_time = time.time()
        limit = 5
        while True:
            quest, answ = random.choice(list(questions.items()))
            print(quest)
            answer = input('Ваш ответ:')
            if answer != answ:
                print('Неправильно!')
                prob -= 0.1
            elif answer == answ:
                print('Правильно!')
                prob += 0.1
            if time.time() > start_time + limit:
                break
        print('Вы сделали выстрел')
        shot = random.random() < prob
        time.sleep(1)
        print('...')
        time.sleep(1)
        if shot == True:
            print('Вы попали!')
            if shooting_choice == '1':
                print('Враг обезврежен!')
            elif shooting_choice == '2':
                state = random.random() < prob
                if state == True:
                    info['body_count'] += 1
                    print('Враг убит!')
                if state == False:
                    print('Враг обезврежен!')
            elif shooting_choice == '3':
                info['body_count'] += 1
                print('Враг убит!')
        elif shot == False:
            if shooting_choice == '1':
                print('Вы не попали. Стреляет противник')
                prob = 0.4
                shot = random.random() < prob
                time.sleep(1)
                print('...')
                time.sleep(1)
                if shot == True:
                    info['health'] -= 20
                    info['lost'] += 1
                    print('Враг попал в Вас и убежал! Вы потеряли 20 ед. здоровья!')
                elif shot == False:
                    info['lost'] += 1
                    print('Враг не попал в Вас, но сумел скрыться!')
            elif shooting_choice == '2':
                print('Вы не попали. Вы стреляете ещё раз')
                shot = random.random() < prob
                if shot == True:
                    print('Вы попали')
                    state = random.random() < prob
                    if state == True:
                        info['body_count'] += 1
                        print('Враг убит!')
                    if state == False:
                        print('Враг обезврежен!')
                if shot == False:
                    print('Вы не попали. Стреляет противник')
                    prob = 0.4
                    shot = random.random() < prob
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    if shot == True:
                        info['health'] -= 20
                        info['lost'] += 1
                        print('Враг попал в Вас и убежал! Вы потеряли 20 ед. здоровья!')
                    elif shot == False:
                        info['lost'] += 1
                        print('Враг не попал в Вас, но сумел скрыться!')
            elif shooting_choice == '3':
                scared = random.random() < prob_scared
                if scared == True:
                    info['lost'] += 1
                    print('Вы не попали. Враг испугался и убежал')
                else:
                    print('Вы не попали. Стреляет противник')
                    prob = 0.4
                    shot = random.random() < prob
                    time.sleep(1)
                    print('...')
                    time.sleep(1)
                    if shot == True:
                        info['health'] -= 20
                        info['lost'] += 1
                        print('Враг попал в Вас и убежал! Вы потеряли 20 ед. здоровья!')
                    elif shot == False:
                        info['lost'] += 1
                        print('Враг не попал в Вас, но сумел скрыться!')
    if info['health'] == 0:
        print('Вы погибли!')
    

def first_choice():
    print('1 - Бесшумно открыли дверь и осторожно вошли в дом;\n2 - Выломали дверь ногой и ворвались в дом с Кольтом наперевес;\n3 - Заглянули в окно дома, чтобы разведать обстановку;\n4 - Внимательно прислушались.')
    choice = input('Напишите цифру действия и нажмите ENTER:')
    if choice == '1':
        print('Вы увидели человека с револьвером в одной руке и с сумкой в другой. Он смотрел в стену и не заметил, как Вы вошли. Что Вы будете делать?')
        print('1 - Броситься на него; \n2 - Подкрасться к нему и повалить на пол; \n3 - Наставить на него Кольт и приказать бросить оружие; \n4 - Спрятаться за стеной и ждать.')
        choice_1 = input('Напишите цифру действия и нажмите ENTER:')
        if choice_1 == '1':
            print('Вы бесстрашно бросились на преступника. Только через пару минут он понял, что произошло, но было слишком поздно - Вы уже успели надеть на него наручники и погрузить в свою машину.')
        elif choice_1 == '2':
            print('Вы тихо подкрались к преступнику, ловким движением выбили у него револьвер из рук и силовым приёмом повалили на пол. Вы надели на него наручники и погрузили в свою машину.')
        elif choice_1 == '3':
            print('Преступник настолько сильно испугался, что выронил револьвер и сумку из рук. Вы безо всякого труда надели на него наручники и погрузили его в машину.')
        elif choice_1 == '4':
            print('Вы спрятались за стеной, но преступник услышал Вас. Вы слышите, как он направляется к Вам. Что Вы будете делать?')
            print('1 - Резко выйти из-за стены и выстрелить в преступника; \n2 - Кинуть оглушающую гранату(количество гранат в инвентаре -', info['flashbang'], '); \n3 - Наставить Кольт на преступника и приказать сдаться; \n4 - Накинуться на преступника с кулаками.')
            choice_1_4 = input('Напишите цифру действия и нажмите ENTER:')
            if choice_1_4 == '1':
                print('Хотите ли Вы узнать, как работает перестрелка?')
                answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
                if answer == '1':
                    tutorial_shooting_scene()
                shooting_scene()
                health_check()
                if info['body_count'] == 1:
                    print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
                elif info['lost'] == 1:
                    print('Вы упустили преступника. Вы отряхнулись, посмотрели на свою рану, обработали её и сели в свой автомобиль.')
                else:
                    print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')
            elif choice_1_4 == '2':
                flashbang_used()
                print('Вы оглушили преступника и быстро скрутили его. От оглушающей гранаты он оправился уже будучи в полицеской машине.')
            elif choice_1_4 == '3':
                Michael('Положи оружие и сумку на землю! Быстро!')
                time.sleep(1)
                print('Преступник послушался Вашего приказа и быстро положил всё, что он держал в руках, на землю. Вы без труда смогли надеть на него наручники и посадить в свою машину.')
            elif choice_1_4 == '4':
                print('Удивительно, но во время драки Вас не зацепила ни единая пуля, выпущенная преступником. Возможно, впредь следует быть поосторожнее - некоторые люди имеют стальные нервы и смогут попасть в Вас даже в разгаре драки.')
                print('Вы смогли победить в драке и отправить оппонента в нокаут. Вы надели на него наручники и посадили в машину.')
            elif not choice_1_4:
                print('Вы продолжили стоять за стеной. Внезапно вы услышали грохот и выстрел. Вы резко выглянули из-за угла и обнаружили, что преступник... споткнулся и упал прямо на свой револьвер. Пуля попала прямо в сердце, так что не было смысла пытаться его спасти. \nВы оставили труп и сели в свою машину.')
                info['body_count'] += 1
        elif not choice_1:
            print('Вы просто остались на месте. Вы не двигались и ждали, что произойдёт дальше...')
            time.sleep(3)
            print('...стояли и ждали...')
            time.sleep(3)
            print('Внезапно преступник развернулся и увидел Вас! У Вас не было выбора, кроме как достать Кольт и начать стрелять!')
            time.sleep(1)
            print('Хотите ли Вы узнать, как работает перестрелка?')
            answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
            if answer == '1':
                tutorial_shooting_scene()
            shooting_scene()
            health_check()
            if info['body_count'] == 1:
                print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
            elif info['lost'] == 1:
                print('Вы упустили преступника. Вы отряхнулись и сели в свой автомобиль.')
            else:
                print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')
    elif choice == '2':
        print('Вы увидели человека и наставили на него свой Кольт. От испуга и неожиданности он уронил револьвер.\n Когда он понял, что произошло, Вы уже скрутили и заковали его в наручники.')
    elif choice == '3':
        print('Посмотрев в окно, Вы увидели фигуру человека с револьвером в одной руке и с сумкой в другой. Вы не могли понять, в какую сторону он смотрит и видит ли он Вас. Что Вы будете делать?')
        print('1 - Резко зайти в дом и приказать преступнику сдаться; \n2 - Выстрелить в преступника; \n3 - Бесшумно подкрасться к преступнику и вырубить его; \n4 - Спрятаться под окном и ждать.')
        choice_3 = input('Напишите цифру действия и нажмите ENTER:')
        if choice_3 == '1':
            print('Вы ворвались в дом.')
            time.sleep(1)
            Michael('Положи оружие и сумку на пол! Быстро!')
            time.sleep(1)
            print('Преступник явно не ожидал того, что кто-то найдет его. К тому же, он точно не ожидал, что кто-то резко закричит на него, так что он повиновался и сдался. \nВы надели на него наручники и посадили в автомобиль.')
        elif choice_3 == '2':
            print('Хотите ли Вы узнать, как работает перестрелка?')
            answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
            if answer == '1':
                tutorial_shooting_scene()
            shooting_scene()
            health_check()
            if info['body_count'] == 1:
                print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
            elif info['lost'] == 1:
                print('Вы упустили преступника. Вы отряхнулись и сели в свой автомобиль.')
            else:
                print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')
        elif choice_3 == '3':
            print('Все прошло как по маслу - уже через несколько секунд Вы успешно вырубили преступника, надели на него наручники и посадили в машину.')
        elif choice_3 == '4':
            print('Вы спрятались и начали ждать преступника.')
            time.sleep(2)
            print('Вы ждали...')
            time.sleep(2)
            print('...и ждали...')
            time.sleep(1)
            print('В конце концов Вы решили проверить дом. Оказалось, что он пуст - преступник успел убежать.')
            info['lost'] += 1
            time.sleep(1)
            print('Мысленно отругав себя, Вы сели в машину и поехали к полицейскому участку.')
        elif not choice_3:
            print('Вы просто стали смотреть на преступника через окно.')
            time.sleep(1)
            print('Внезапно он увидел Вас и достал револьвер! У Вас не было выбора, кроме как достать Кольт и начать стрелять!')
            time.sleep(1)
            print('Хотите ли Вы узнать, как работает перестрелка?')
            answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
            if answer == '1':
                tutorial_shooting_scene()
            shooting_scene()
            health_check()
            if info['body_count'] == 1:
                print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
            elif info['lost'] == 1:
                print('Вы упустили преступника. Вы отряхнулись и сели в свой автомобиль.')
            else:
                print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')
    elif choice == '4':
        print('Вы прислонились ухом к двери. Вы услышали шаги в доме, довольно далеко от Вас. Что Вы будете делать?')
        print('1 - Резко открыть дверь и наставить на преступника Кольт; \n2 - Отойти в сторону от двери и схватить преступника, когда тот будет выходить; \n3 - Кинуть оглушающую гранату через дверь (количество гранат в инвентаре -', info['flashbang'], '); \n4 - Открыть дверь и начать стрелять в преступника.')
        choice_4 = input('Напишите цифру действия и нажмите ENTER:')
        if choice_4 == '1':
            print('Как только преступник открыл дверь, он сразу же замер в оцепенении. Он смог осознать ситуацию только тогда, когда он уже сидел в полицейской машине в наручниках.')
        elif choice_4 == '2':
            print('Как только преступник вышел из дома, Вы сразу же набросились на него, надели на него наручники и посадили его в свой автомобиль.')
        elif choice_4 == '3':
            flashbang_used()
            print('Вы оглушили преступника и быстро скрутили его. От оглушающей гранаты он оправился уже будучи в полицеской машине.')
        elif choice_4 == '4':
            print('Хотите ли Вы узнать, как работает перестрелка?')
            answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
            if answer == '1':
                tutorial_shooting_scene()
            shooting_scene()
            print('У Вас', info['health'], 'очков здоровья')
            if info['body_count'] == 1:
                print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
            elif info['lost'] == 1:
                print('Вы упустили преступника. Вы отряхнулись и сели в свой автомобиль.')
            else:
                print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')
        elif not choice_4:
            info['lost'] += 1
            info['health'] -= 10
            print('Сложно сказать, что произошло. Судя по всему, когда преступник выходил из дома, он слишком сильно ударил Вас дверью по голове, поэтому Вы и упали без сознания. \nУдивительно, что он ещё и не убил Вас, а просто сбежал.')
            print('Вы потеряли 10 единиц здоровья!')
            health_check()
    elif not choice:
        print('Вам показалось, что лучшим решением в данной ситуации будет просто ждать. Внезапно вы услышали, что кто-то приближается ко входной двери изнутри дома. Что Вы будете делать?')
        print('1 - Спрятаться у двери; \n2 - Подойти к двери с Кольтом в руках; \n3 - Ворваться в дом и выстрелить в преступника; \n4 - Ворваться в дом и прыгнуть на преступника.')
        choice_none = input('Напишите цифру действия и нажмите ENTER:')
        if choice_none == '1':
            print('Как только преступник вышел из дома, Вы тут же скрутили его и надели на него наручники. Через несколько мгновений Вы уже везли преступника в участок.')
        elif choice_none == '2':
            print('Вы подошли к двери и приготовились ко встрече с преступником. Однако тут Вы перестали слышать шум за дверью. Что Вы будете делать?')
            print('1 - Стоять и ждать; \n2 - Аккуратно заглянуть в замочную скважину двери; \n3 - Выбить дверь; \n4 - Тихо обойти дом и ждать преступника со стороны задней двери.')
            choice_none_2 = input('Напишите цифру действия и нажмите ENTER:')
            if choice_none_2 == '1':
                info['lost'] += 1
                print('Прождав 10 минут, Вы всё-таки решили проверить дом. Но было уже поздно - преступник скрылся через заднюю дверь.')
                time.sleep(1)
                print('Вы сели обратно в машину и поехали в полицейский участок.')
            elif choice_none_2 == '2':
                info['lost'] += 1
                info['health'] -= 10
                print('Вы заглянули в замочную скважину, а затем Вы... упали без сознания. Видимо, преступник в тот момент открывал дверь и сильно ударил Вас. \nОсознав своё положение, Вы встали с земли и сели в автомобиль.')
                print('Вы потеряли 10 единиц здоровья!')
                health_check()
            elif choice_none_2 == '3':
                info['health'] -= 5
                print('Вы выбили дверь. Она придавила ногу преступника, который теперь лежал на полу, корчась от боли. Вам тоже было больно - не каждый день Вы выбиваете двери. \nНо преступник пойман - это главное.')
                print('Вы потеряли 10 единиц здоровья!')
                health_check()
            elif choice_none_2 == '4':
                print('Вы решили, что будет разумным проверить заднюю дверь. Вы оказались правы - как только Вы обошли дом, Вы увидели, как преступник открывает дверь. \nВы тут же на него набросились, надели на него наручники и посадили в свою машину.')
        elif choice_none == '3':
            print('Хотите ли Вы узнать, как работает перестрелка?')
            answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
            if answer == '1':
                tutorial_shooting_scene()
            shooting_scene()
            print('У Вас', info['health'], 'очков здоровья')
            if info['body_count'] == 1:
                print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
            elif info['lost'] == 1:
                print('Вы упустили преступника. Вы отряхнулись и сели в свой автомобиль.')
            else:
                print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')
        elif choice_none == '4':
            info['body_count'] += 1
            print('Вы ворвались в дом и прыгнули прямо на преступника. Каким-то образом вы умудрились приземлиться ему на шею. Дальше уже всё понятно, да?')
            time.sleep(1)
            print('Оставив бездыханное тело на полу в доме, Вы сели в полицейскую машину и поехали обратно в участок.')
        elif not choice_none:
            print('Судя по всему, Вы не особо любите действовать, так?')
            time.sleep(2)
            print('Внезапно преступник вышел из дома и, увидев Вас, достал револьвер.')
            time.sleep(2)
            print('Хотите ли Вы узнать, как работает перестрелка?')
            answer = input('1 - Да; \n2 - Нет.\nНапишите цифру и нажмите ENTER:')
            if answer == '1':
                tutorial_shooting_scene()
            shooting_scene()
            print('У Вас', info['health'], 'очков здоровья')
            if info['body_count'] == 1:
                print('Вы убили преступника. Вы оставили его тело в доме и сели в свой автомобиль.')
            elif info['lost'] == 1:
                print('Вы упустили преступника. Вы отряхнулись и сели в свой автомобиль.')
            else:
                print('Вы обезвредили противника. Вы надели на него наручники и посадили в машину.')

def talk1():
    time.sleep(3)
    if info['lost'] == 0:
        if info['body_count'] == 1:
            print('Вы приехали в полицейский участок. Оставив машину у дверей здания, Вы зашли внутрь. \nСразу же Вы увидели капитана полицейского участка, Тома Шонди.')
        else:
            print('Вместе с Ллойдом Вы приехали в полицейский участок. Оставив машину у дверей здания, Вы отдали преступника полицейским.')
            time.sleep(2)
            Lloyd('Я запомнил тебя, детектив. Я обязательно приду за тобой! Я обя...')
            time.sleep(1)
            print('Монолог Ллойда прервал удар капитана полиции Тома Шонди.')
            time.sleep(1)
            Tom('Да замолчи ты уже наконец!')
            time.sleep(0.5)
            print('Когда Ллойда увели, Вы остались один на один с капитаном')
            further()
        Tom('Добрый вечер, Майкл.')
        time.sleep(0.5)
        Michael('Здравствуйте, капитан.')
        time.sleep(0.5)
        Tom('Хотел обсудить с Вами ситуацию в городе.')
        time.sleep(0.5)
        Michael('Слушаю.')
        time.sleep(0.5)
        Tom('Ни для кого не секрет, что Даунтаун нуждается в Вашем профессиональном содействии, Майкл. \nС тех пор, как Вы стали работать здесь, дела пошли на поправку, но…')
        time.sleep(1.5)
        Michael('Мне очень лестны ваши слова, капитан, однако давайте перейдём к сути.')
        further()
        Tom('Буду краток и ясен. В городе объявился новый убийца. Его нужно поймать. Как можно скорее, Майкл. \nЭто Ваша следующая задача. Я знаю, Вы не подведёте.')
        time.sleep(1.5)
        Michael('Спасибо за доверие, сделаю всё в лучшем виде. Достану его из-под земли.')
        time.sleep(0.5)
        Tom('Удачи, детектив!')
        time.sleep(0.5)
        Tom('И ещё кое-что...')
        further()
        if info['body_count'] == 1:
            Tom('Майкл, убийство любого преступника в городе – довольно серьёзный проступок. \nВы знаете, что имидж полиции в городе и без того оставляет желать лучшего.')
            time.sleep(1.5)
            Michael('Капитан, порой нет никакого другого выхода.')
            time.sleep(0.5)
            Tom('Понимаю, детектив, но впредь постарайтесь избегать подобных ситуаций. \nСейчас они как никогда не кстати. Всего доброго. Будьте на связи')
            time.sleep(0.5)
            Michael('До завтра, капитан Шонди')
            further()
        else:
            print('Внезапно Вы услышали громкий крик.')
            time.sleep(0.5)
            Lloyd('СЛЫШИШЬ МЕНЯ? Я ТЕБЯ ДОСТАНУ!')
            time.sleep(2)
            Tom('Да заткните вы его уже наконец!')
            time.sleep(2)
            Tom('Простите, Майкл. В любом случае, я хотел бы поздравить Вас с успешным задержанием!')
            time.sleep(1)
            Michael('Благодарю, капитан.')
            time.sleep(1)
            Tom('Если так будет продолжаться и дальше, дела Даунтауна пойдут в гору, а имидж полиции укрепится.')
            time.sleep(2)
            Michael('Я приложу все усилия для этого.')
            time.sleep(1)
            Tom('Надеюсь, детектив. Не расслабляйтесь и продолжайте в том же духе.')
            time.sleep(1)
            Michael('Конечно. Надеюсь, наше сотрудничество будет плодотворным.')
            time.sleep(1)
            Tom('Взаимно. Ещё раз спасибо за помощь полиции. На сегодня всё. До завтра и будьте на связи.')
            time.sleep(1)
            Michael('Всего доброго, капитан.')
            further()
    else:
        print('Вы приехали в полицейский участок. Оставив машину у дверей здания, Вы зашли внутрь. \nСразу же Вы увидели капитана полицейского участка, Тома Шонди.')
        time.sleep(1.5)
        Tom('Майкл! Я искал вас повсюду. Срочно пройдите ко мне в кабинет. Живо!')
        time.sleep(1)
        Michael('Да, капитан.')
        time.sleep(1)
        print('Вы зашли в кабинет, и капитан закрыл за собой дверь.')
        time.sleep(2)
        Tom('Слушай сюда. Если такое повторится ещё раз, я буду вынужден открыть вакансию детектива для нашего отделения. \nНа вас лежит огромная ответственность, положение Даунтауна ужасно, никакой преступник не может быть упущен.')
        time.sleep(2)
        Michael('Вас понял. Впредь это не повторится.')
        time.sleep(1)
        Tom('Я надеюсь, Майкл. Это ваш последний шанс. Надеюсь, вы понимаете всю серьёзность положения.')
        time.sleep(2)
        Tom('Это всё на сегодня. До завтра, будьте на связи.')
        time.sleep(1)
        Michael('До завтра, капитан.')
        further()
    print('Вы уже дошли до выхода, как вдруг Вас окликнул Коннор Дилайт - заносчивый и высокомерный тип, который, по совместительству, также являлся диспитчером участка.')
    choice = input('1 - Повернуться и поговорить с ним; \n2 - Молча поехать домой.')
    if choice == '1':
        if info['lost'] == 1:
            Connor('Майкл, здравствуй. Какая неожиданная встреча. Отличное время для прогулки, не правда ли?')
            time.sleep(2)
            Michael('Добрый вечер, диспетчер.')
            time.sleep(1)
            Connor('Как дела на службе? Слышал, ты провёл отличное задержание! Дать преступнику уйти в такое время – отличная работа, старина!')
            time.sleep(1.5)
            Michael('Я бы посмотрел на тебя, попади ты на моё место. Всё, что ты можешь – отвечать на телефон и рассказывать об услышанном.')
            time.sleep(1.5)
            Connor('Не кипятись, приятель, все мы когда-то ошибаемся. Кто-то чаще, кто-то реже, а кто-то вообще всё время.')
            further()
        elif info['body_count'] == 1:
            Connor('Майкл, здравствуй. Какая неожиданная встреча. Отличное время для прогулки, не правда ли?')
            time.sleep(2)
            Michael('Добрый вечер, диспетчер.')
            time.sleep(1)
            Connor('Как успехи на службе? Слышал, ты провёл отличное задержание! Убийство - это же так гуманно! Как тебе это удалось? Не думал, что ты на это способен.')
            time.sleep(1.5)
            Michael('Я выполняю свою работу.')
            time.sleep(1)
            Connor('Да уж, работы прибавилось с тех пор, как в нашей части города появились такие полицейские как ты.')
            time.sleep(2)
            Michael('Твои колкости неуместны, Коннор. Ты должен быть рад тому, то мы избавились от такого злостного преступника.')
            time.sleep(1.5)
            Connor('Я был бы очень рад и благодарен, если бы ты, старина, и такие как ты сделали бы что-то действительно стоящее, чтобы помочь Даунтауну. \nПрекрати тратить чужое время на расследование того, в чём виноват лишь ты и твой непрофессионализм.')
            further()
        else:
            Connor('Майкл, здравствуй. Какая неожиданная встреча. Отличное время для прогулки, не правда ли?')
            time.sleep(2)
            Michael('Добрый вечер, диспетчер.')
            time.sleep(1)
            Connor('Как дела на службе? Слышал, ты провёл отличное задержание! Как тебе это удалось? Не думал, что ты на это способен.')
            time.sleep(1.5)
            Michael('Спасибо, я всего лишь выполняю свою работу.')
            time.sleep(1)
            Connor('Удивительно, что даже в этом лёгком задании ты умудрился облажаться. Неужели тебе не кажется, что такие опасные преступники не заслуживают жизни? \nТебе следовало помочь следствию и городу, избавив его от мороки с очередным бесполезным человечком, учитывая сложившуюся ситуацию.')
            time.sleep(2)
            Michael('Благодарю, Коннор, но, думаю, я обойдусь и без твоих советов. Все мы знаем, насколько гуманным можешь быть ты и твои рекомендации.')
            further()
    print('Вы вышли из участка, сели в машину и поехали к себе домой. Вам хотелось отдохнуть и поспать. Это было кстати - следующие дни предвещали быть мрачными, полными тайн и перестрелок. Они требовали от Вас хладнокровности и проницательности.')
    time.sleep(3)

def new_game():
    print('\nВы - детектив Майкл Бёрд, один из немногих полицейских, в которых сочитаются сила, невероятный интеллект. хладнокровность и смелость.\n На улицах Нового Лос-Анджелеса, Вашего родного города, появился преступник, угрожающий и без того хрупкой безопасности всех жителей.\n Удастся ли Вам схватить злодея, пока не стало слишком поздно?')
    further()
    print('\n*****\n')
    print('24 ОКТЯБРЯ 2107 ГОДА, НОВЫЙ ЛОС-АНДЖЕЛЕС.')
    print('\n*****\n')
    time.sleep(2)
    print('В вечер понедельника Вы как всегда патрулировали улицы Даунтауна Лос-Анджелеса.\n Что такое Даунтаун и почему детектив патрулирует улицы? Одно вытекает из другого. Даунтаун - самая опасная часть Нового Лос-Анджелеса. Она попросту кишит преступниками разных сортов и нищими, у которых не хватает денег переехать в другой район.')
    time.sleep(2)
    print('Ситуация настолько удручающая, что более 10 лет никто не хотел заниматься раскрытием преступлений в Даунтауне - это было слишком затратно, как с точки зрения финансов, так и с точки зрения времени.\n Однако после открытия участка всё начало меняться, даже несмотря на нехватку персонала - мало кто хотел ставить под угрозу свою жизнь ради работы за копейки в худшем районе города')
    time.sleep(2)
    print('Несмотря на всё, Вы были готовы работать не покладая рук, чтобы освободить район, в котором Вы выросли, от преступности.\n Даже если для этого придется рискнуть всем, чем только можно.')
    print('\n*****\n')
    further()
    print('В данный момент Вы патрулировали улицы Даунтауна. Вы искали преступника - Ллойда Брайтона. \nБуквально 5 минут назад Вам доложили, что человека, похожего на него, недавно видели в этом квартале.')
    time.sleep(1)
    print('Ваше внимание захватила приоткрытая дверь заброшенного дома. Вы вышли из автомобиля. Из кармана своего тренча Вы достали свой Кольт, быстро и тихо подбежали к двери и...')
    first_choice()
    talk1()
    print('На этом заканчивается первая глава этой истории. Напишите мне о своих впечатлениях!')
    time.sleep(10)
    

