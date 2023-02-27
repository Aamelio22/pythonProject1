# Setting language.
while True:
    lang = input("What is your language?\n言語を選んでください\n\nEnglish or 日本語？\n\n")
    lang = lang.lower()
    char = [sym for sym in lang]
    if "e" in char:
        lang = "en"
        break
    elif "日" in char or "に" in char:
        lang = "jp"
        break
    else:
        print("\nError, invalid input.\nエラー、入力が無効です。\n")
        print('''>--------------------------------------------------------------------<\n''')

print(''' ______ ______  ______  ______  ______  __  __  ______  ______    
/\__  _/\  == \/\  ___\/\  __ \/\  ___\/\ \/\ \/\  == \/\  ___\   
\/_/\ \\ \  __<\ \  __\\ \  __ \ \___  \ \ \_\ \ \  __<\ \  __\   
   \ \_\\ \_\ \_\ \_____\ \_\ \_\/\_____\ \_____\ \_\ \_\ \_____\ 
    \/_/ \/_/ /_/\/_____/\/_/\/_/\/_____/\/_____/\/_/ /_/\/_____/ 

       __  ______  __      ______  __   __  _____                 
      /\ \/\  ___\/\ \    /\  __ \/\ "-.\ \/\  __-.               
      \ \ \ \___  \ \ \___\ \  __ \ \ \-.  \ \ \/\ \              
       \ \_\/\_____\ \_____\ \_\ \_\ \_\\"\_\ \____-              
        \/_/\/_____/\/_____/\/_/\/_/\/_/ \/_/\/____/              
                                                                 ''')
print('''    ___ __ 
   (_  ( . ) )__                  '.    \   :   /    .'
     '(___(_____)      __           '.   \  :  /   .'
                     /. _\            '.  \ : /  .'
                .--.|/_/__      -----____   _  _____-----
_______________''.--o/___  \_______________(_)___________
       ~        /.'o|_o  '.|  ~                   ~   ~
  ~            |/    |_|  ~'         ~
               '  ~  |_|        ~       ~     ~     ~
      ~    ~          |_|O  ~                       ~
             ~     ___|_||_____     ~       ~    ~
   ~    ~      .'':. .|_|A:. ..::''.
             /:.  .:::|_|.\ .:.  :.:\   ~
  ~         :..:. .:. .::..:  .:  ..:.       ~   ~    ~
             \.: .:  :. .: ..: :. :./
    ~      ~      ~    ~    ~         ~
               ~           ~    ~   ~             ~
        ~         ~            ~   ~                 ~
   ~                  ~    ~ ~                 ~''')
if lang == "en":
    print("Welcome to Treasure Island!")
    print("Yer goal be to find the treasure.")
else:
    print("宝島へようこそ!")
    print("あなたの目的は宝物を見つけることです。")


# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

# Getting user name and date of birth for use in the story, as well as the secret code.

def get_info():
    global secret_code
    while True:
        if lang == "en":
            print("Nice to meet ye, my name be Marco.\n")
            while True:
                print('''>--------------------------------------------------------------------<''')
                first_name = input("\nWhat be yer first name?\n\n")
                if first_name.isalpha() == False:
                    print("Yarrrrgh! Letters only!\n")
                    continue
                elif not len(first_name) >= 1:
                    print("Please enter something.\n")
                    continue
                else:
                    first_name = first_name.capitalize()
                while True:
                    last_name = input("What be yer last name?\n\n")
                    if last_name.isalpha() == False:
                        print("Yarrrrgh! Letters only!\n")
                        continue
                    elif not len(last_name) >= 1:
                        print("Please enter something.\n")
                        continue
                    else:
                        last_name = last_name.capitalize()
                        print(f"\nPleasure to meet ye {first_name} {last_name}\n")
                        print('''>--------------------------------------------------------------------<\n''')
                        break
                while True:
                    dob = input("What be the day ye came out the womb?\n(Date of Birth)\n\n")
                    if len(dob) != 10:
                        print("Yarrrrgh! Ye need ta enter it in the right order!\nMM/DD/YYYY\n\n")
                        continue
                    elif "/" in dob:
                        secret_code = dob.split("/")
                        m = secret_code[0]
                        d = secret_code[1]
                        y = secret_code[2]
                        if len(m) != 2 or len(d) != 2 or len(y) != 4 or int(m) > 12 or int(d) > 31 or int(
                                y) not in range(1900, 2024):
                            print("Yarrrrgh! I think ye be lyin'!\nMM/DD/YYYY\n")
                            continue
                        else:
                            print("\nArggh! That there be a MEAN date if I 'ave e'er spied one.\n")
                            print(secret_code)
                            return (first_name, last_name, m, d, y)
        else:
            print("案内係であるマルコです。\nよろしくな。\n")
            print('''>--------------------------------------------------------------------<''')
            while True:
                last_name = input("\n名字は何ですか?\n\n")
                if not len(last_name) >= 1:
                    print("何か入力してください。\n")
                else:
                    break
            while True:
                first_name = input("\n下の名前は何ですか?\n\n")
                if not len(first_name) >= 1:
                    print("何かを入力してください。\n")
                else:
                    print(f"\nお会いできて嬉しいです、\n{last_name}{first_name}さん\n")
                    print('''>--------------------------------------------------------------------<\n''')
                    break
            while True:
                dob = input("お誕生日はいつ?\n\n")
                if len(dob) != 10:
                    print("順番が間違っている\nMM/DD/YYYY\n\n")
                elif "/" in dob:
                    secret_code = dob.split("/")
                    m = secret_code[0]
                    d = secret_code[1]
                    y = secret_code[2]
                    if len(m) != 2 or len(d) != 2 or len(y) != 4 or int(m) > 12 or int(d) > 31 or int(y) not in range(
                            1900, 2024):
                        print("嘘でしょ!\n")
                    else:
                        print("\n平均的な日付だな。\n")
                        return (last_name, first_name, m, d, y)


# Setting a code found by getting the mean of the dob entered to be used in the final level.

name = get_info()
secret_code = str((round((int(secret_code[0]) + int(secret_code[1]) + int(secret_code[2])) / int(len(secret_code)))))

# Setting variable to determine whether or not to continue running game.

game_status = "run"

# Telling the story.
if lang == "en":
    print('''\n>--------------------------------------------------------------------<\n''')
    print(
        "E'er since ye was a little child, ye've 'eard stories \no' a legendary gentleman o' fortune by the name o' \nGoldtooth an' 'ow much treasure 'e 'ad acquired.\n\nYe swore that there one day ye would set sail an' \nseek out the treasure an' the mystery behind it...\nMap in hand, ye set out on a perilous journey.\nAll been well until a jolly storm shivered ye timbers.\nYe see an island emerge through the pouring rain.\nAfter ye dock yer ship, ye notice that it looks like the land on the map ye acquired.\nYe might as well explore a bit.\n")
else:
    print('''>--------------------------------------------------------------------<\n''')
    print(
        "幼い頃から、「金歯」という伝説の海賊と重ねてきた宝物の話をいつも聞いていた。\nいつか必ず宝物とその背後にある謎を探ると誓った。\n地図を手に握りしめ、危険な冒険に出かける。\n航海中で嵐に襲われ怯えていたが、大雨の中から島が見えてくる！\n錨を下ろしてから地図を見ると、まさにこの島みたいだ！\n調べてみましょう。\n")
    print('''>--------------------------------------------------------------------<''')


# Defining functions for each level.

def level1():
    global game_status
    while game_status == "run":
        if lang == "en":
            print('''\n>--------------------------------------------------------------------<''')
            choice = input("\nYe be at a fork in the road, which way would ye like to go? \n\nLeft or Right?\n\n")
            print('''\n>--------------------------------------------------------------------<''')
            choice = choice.lower()
            if choice == "right":
                print('''     ___
     \_/
      |._
      |'."-._.-""--.-"-.__.-'/
      |  \       .-.        (
      |   |     (@.@)        )
      |   |   '=.|m|.='     /
      |  /    .='`"``=.    /
      |.'                 (
      |.-"-.__.-""-.__.-"-.)
      |
      |
      |
''')
                print("\nYe ran into a band of pirates!\nThey stole your map and fed you to the alligators. T-T\n.")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("Would ye like to try again? (y/n)\n\n")
                    if retry == "y":
                        return
                    elif retry == "n":
                        print("Goodbye!\nThanks fer playin'!")
                        game_status = "end"
                        break
                    else:
                        print("\nYarrrrgh! It be a yes or no question. (y/n)\n")
            elif choice != "left":
                print("\nYa don't know how to spell?\n")
            else:
                return ("complete")
        else:
            choice = input("\n道の分岐点に着く。\n\n左か右かどっちを選ぶ?\n\n")
            print('''\n>--------------------------------------------------------------------<''')
            if choice == "右":
                print('''     ___
     \_/
      |._
      |'."-._.-""--.-"-.__.-'/
      |  \       .-.        (
      |   |     (@.@)        )
      |   |   '=.|m|.='     /
      |  /    .='`"``=.    /
      |.'                 (
      |.-"-.__.-""-.__.-"-.)
      |
      |
      |
''')
                print("\nあなたは海賊団に出くわして、ワニの餌となった。T-T\n.")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
 ███     █    █  ▀███▀               █  █  ▀███▀     █   
        █    ▀                        █▐            ▀    
       ▀                              ▐                  \n''')
                print('''>--------------------------------------------------------------------<\n''')
                while True:

                    retry = input("やり直す? (はい/いいえ)\n\n")
                    print('''>--------------------------------------------------------------------<''')
                    ans = [hi for hi in retry]
                    if "は" or "い" in ans:
                        return
                    elif "い" or "え" in ans:
                        print("さようなら。\nプレイしてくれてありがとう！")
                        game_status = "end"
                        break
                    else:
                        print("イエスかノーを選んでください。\n(はい/いいえ)\n")
            elif choice == "左":
                print("\n無事に進んだ。\n")
                print('''>--------------------------------------------------------------------<''')
                return ("complete")
            else:
                print("\n入力が無効だ。")


def level2():
    global game_status
    if lang == "en":
        while game_status == "run":
            choice = input("\nYe come across a wide river. Will ye brave it and swim, or wait?\n\n")
            print('''\n>--------------------------------------------------------------------<\n''')
            choice = choice.lower()
            if choice == "swim":
                print('''
           .-._   _ _ _ _ _ _ _ _
.-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
                             (((-'\ .' /
                           _____..'  .'
                          '-._____.-' ''')
                print("\nYe got eaten by an alligator!\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("Would you like to try again? (y/n)\n\n")
                    if retry == "y":
                        return
                    elif retry == "n":
                        print("Goodbye!\nThanks fer playin'!")
                        game_status = "end"
                        break
                    else:
                        print("Error, please input proper answer (y/n)\n")
            elif choice != "wait":
                print("Ya don't know how to spell?\n")
            else:
                print("A piece o' ship wreckage floated by an' ye used it to get across. 'Ow fortunate!.")
                return ("complete")
    else:
        while game_status == "run":
            choice = input("\n広い川に出くわする。\n\n勇気を出して泳いで渡ろうとするか、待つか?\n\n")
            print('''\n>--------------------------------------------------------------------<''')
            char = [hi for hi in choice]
            if choice == "泳ぐ":
                print("\nワニに食われた!\n")
                print('''
           .-._   _ _ _ _ _ _ _ _
.-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
                             (((-'\ .' /
                           _____..'  .'
                          '-._____.-' ''')
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("やり直す? (はい/いいえ)\n\n")
                    ans = [hi for hi in retry]
                    if "は" or "い" in ans:
                        return
                    elif "い" or "え" in ans:
                        print("さようなら。\nプレイしてくれてありがとう！")
                        game_status = "end"
                        break
                    else:
                        print("イエスかノーを選んでください。\n(はい/いいえ)\n")
            elif choice == "待つ":
                print("\n船の漂流した残骸を使って渡った。助かった！")
                return ("complete")
            else:
                print("\n入力が無効だ。")


def level3():
    global game_status
    if lang == "en":
        while game_status == "run":
            choice = input(
                "\nYe find yerself close to where the x be on the treasure map.\nWon't be long now...\n\nThere be a jungle to yer left, a swamp ahead, an' a rickety bridge to yer right.\nChoose wisely...\n\n")
            print('''\n>--------------------------------------------------------------------<\n''')
            choice = choice.lower()
            if choice == "jungle":
                print('''                               
              (
               )  )
           ______(____
          (___________)
           /         \                                      
          /           \                                         
         |             |                                        
     ____\             /____
    ()____'.__     __.'____()
         .'` .'```'. `-.
        ().'`       `'.()''')
                print("\nYe run into a crew o' 'ungry cannibals an' become their dinner.\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                print('''>--------------------------------------------------------------------<\n''')
                while True:
                    retry = input("Would you like to try again? (y/n)\n\n")
                    if retry == "y":
                        return
                    elif retry == "n":
                        print("Goodbye!\nThanks fer playin'!")
                        game_status = "end"
                        break
                    else:
                        print("Error, please input proper answer (y/n)\n")
            elif choice == "swamp":
                print('''░░░░░░░░█████████░░░░░░░░░
░░░░░░░██░░░░░░░███░░░░░░░
░░░░░██░░░░░░░░░░░██░░░░░░
░░░███░░░█░░░░█░░░░██░░░░░
░███░░░░███░░███░░░░███░░░
██░░░█░░░█░░░░█░░░█░░████░
███████░░░░░░░░░░█████████
█░░░████████████████░░░░██
█░░░██░░███░░███░░██░░░███
███████░░█░░░░█░░████████░
███░░░░█░░░░░░░░█░░░░░███░
░░████░█████████░░░░████░░
░░░░████░░░░░░░██████░█░██
░░░░░░██░░░░░░░░░███░░░█░█
░░░░░░░█░░░░░░█░███░░░█░░█
░░░░░░░█▒██████░██░░░█░░██
░░░░░░██▒▒▒▒▒▒▒▒█░░░░█░░█░
░░░░░░█░░▒▒▒▒▒▒░█░░░░█░░█░
░░░░░██░██░░░░█░███░██░░█░
░░░░██░░▒██████▒▒░██░░░░█░
░░░██░░░░▒▒▒▒▒▒▒░░█░░░░██░
░░░█░░███░░░░░░█░░░░░██░░░
░░░██░▒▒▒███████▒▒░░░█░░░░
░░░░███░▒▒▒▒▒▒▒▒▒░████░░░░
░░░░░░███░░░░░█████░░░░░░░
░░░░░░░░███████░░░░░░░░░░░
''')
                print("\nYe get bitten by a poisonous snake an' succumb to its deadly venom\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  ''')
                while True:
                    print('''\n>--------------------------------------------------------------------<\n''')
                    retry = input("Would you like to try again? (y/n)\n\n")
                    if retry == "y":
                        return ("retry")
                    elif retry == "n":
                        print("Goodbye!\nThanks fer playin'!")
                        game_status = "end"
                        break
                    else:
                        print("Error, please input proper answer (y/n)\n")
            elif choice == "bridge":
                print("\nYe brave the bridge an' almost fall to yer death...\nbut ye make it out alive.\n")
                return ("complete")
            else:
                print("\nYa don't know how to spell?\n")
    else:
        while game_status == "run":
            print('''\n>--------------------------------------------------------------------<''')
            choice = input("\n宝の地図によると「X」印の近くにいる。\nあともう少しだ...\n\n左はジャングル、前方は沼地、右はガタガタの橋。\nよく考えて選びな。\n\n")
            print('''\n>--------------------------------------------------------------------<''')
            if choice == "ジャングル":
                print("\n空腹の人食い人種のグループに出くわし、彼らの夕食になる。\n")
                print('''                               
              (
               )  )
           ______(____
          (___________)
           /         \                                      
          /           \                                         
         |             |                                        
     ____\             /____
    ()____'.__     __.'____()
         .'` .'```'. `-.
        ().'`       `'.()''')
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("やり直す? (はい/いいえ)\n\n")
                    print('''>--------------------------------------------------------------------<''')
                    ans = [hi for hi in retry]
                    if "は" or "い" in ans:
                        return
                    elif "い" or "え" in ans:
                        print("さようなら。\nプレイしてくれてありがとう！")
                        game_status = "end"
                        break
                    else:
                        print("\n入力が無効だ。")
            elif choice == "沼地":
                print('''░░░░░░░░█████████░░░░░░░░░
░░░░░░░██░░░░░░░███░░░░░░░
░░░░░██░░░░░░░░░░░██░░░░░░
░░░███░░░█░░░░█░░░░██░░░░░
░███░░░░███░░███░░░░███░░░
██░░░█░░░█░░░░█░░░█░░████░
███████░░░░░░░░░░█████████
█░░░████████████████░░░░██
█░░░██░░███░░███░░██░░░███
███████░░█░░░░█░░████████░
███░░░░█░░░░░░░░█░░░░░███░
░░████░█████████░░░░████░░
░░░░████░░░░░░░██████░█░██
░░░░░░██░░░░░░░░░███░░░█░█
░░░░░░░█░░░░░░█░███░░░█░░█
░░░░░░░█▒██████░██░░░█░░██
░░░░░░██▒▒▒▒▒▒▒▒█░░░░█░░█░
░░░░░░█░░▒▒▒▒▒▒░█░░░░█░░█░
░░░░░██░██░░░░█░███░██░░█░
░░░░██░░▒██████▒▒░██░░░░█░
░░░██░░░░▒▒▒▒▒▒▒░░█░░░░██░
░░░█░░███░░░░░░█░░░░░██░░░
░░░██░▒▒▒███████▒▒░░░█░░░░
░░░░███░▒▒▒▒▒▒▒▒▒░████░░░░
░░░░░░███░░░░░█████░░░░░░░
░░░░░░░░███████░░░░░░░░░░░
''')
                print("\n毒蛇に噛まれ、その猛毒に屈する。\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("やり直す? (はい/いいえ)\n\n")
                    print('''\n>--------------------------------------------------------------------<''')
                    ans = [hi for hi in retry]
                    if "は" or "い" in ans:
                        return
                    elif "い" or "え" in ans:
                        print("さようなら。\nプレイしてくれてありがとう！")
                        game_status = "end"
                        break
                    else:
                        print("\n入力が無効だ。")
            elif choice == "橋":
                print("\n橋に勇敢に立ち向かい、死にそうになったが、\n生きて渡った。\n\n")
                print('''>--------------------------------------------------------------------<\n''')
                return ("complete")
            else:
                print("\n入力が無効だ。")


def level4():
    global game_status
    print('''                           o                    
                       _---|         _ _ _ _ _ 
                    o   ---|     o   ]-I-I-I-[ 
   _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
   ]-I-I-I-I-[   ---|      |  ---|    |.   | 
    \ `   '_/       |     / \    |    | /^\| 
     [*]  __|       ^    / ^ \   ^    | |*|| 
     |__   ,|      / \  /    `\ / \   | ===| 
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
   |.   | |' |___|_____I___|___I___|---------| 
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\
\n''')
    while game_status == "run":
        if lang == "en":
            print(
                '''>--------------------------------------------------------------------<\n\nAfter ye recover from a near death experience、ye see a castle in the distance.\nUpon arriving, ye notice there be three doors...\nWho designed this?!\nAhem…\n''')
            print('''>--------------------------------------------------------------------<\n''')
            choice = input("Which colored door do ye choose？\nred, yellow, or blue?\n\n")
            choice = choice.lower()
            print('''\n>--------------------------------------------------------------------<''')
            if choice == "red":
                print('''          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
         ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
         ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ''')
                print("\nDue to it bein' very dark inside, ye stumble into a spike pit。\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''\n>--------------------------------------------------------------------<''')
                    retry = input("\nWould you like to try again? (y/n)\n\n")
                    if retry == "y":
                        return ("retry")
                    elif retry == "n":
                        print("Goodbye!\nThanks fer playin'!")
                        game_status = "end"
                        break
                    else:
                        print("Error, please input proper answer (y/n)\n")
            elif choice == "yellow":
                print("\nAs you make yer way through the dimly lit hallway, ye see a treasure chest in the distance.\n")
                return ("complete")
            elif choice == "blue":
                print(
                    "\nThe door fell on ye and ye be crushed like a pancake 🥞！\nWait a second...\nHow does that even happen??\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                print('''\n>--------------------------------------------------------------------<\n''')
                retry = input("Would you like to try again? (y/n)\n\n")
                if retry == "y":
                    return ("retry")
                elif retry == "n":
                    print("Goodbye!\nThanks fer playin'!")
                    game_status = "end"
                    break
            else:
                print("\nError, please input proper answer (y/n)\n")
        else:
            print(
                '''>--------------------------------------------------------------------<\n\n臨死体験から回復すると、遠くに城が見える。\n城に着くと戸が三つある…\n誰が設計したこれ？！\nあへん…\n''')
            print('''>--------------------------------------------------------------------<\n''')
            choice = input("何色の戸を開く？\n赤, 黄, 又は　青?\n\n")
            print('''\n>--------------------------------------------------------------------<''')
            if choice == "赤":
                print('''          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
         ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
         ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ 
          ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ⋀ ''')
                print("\n中はとても暗いから、スパイクのある落とし穴に転んだ。\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
█ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
█   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
 ███     █    █  ▀███▀               █  █  ▀███▀     █   
        █    ▀                        █▐            ▀    
       ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("やり直す? (はい/いいえ)\n\n")
                    print('''>--------------------------------------------------------------------<''')
                    ans = [hi for hi in retry]
                    if "は" or "い" in ans:
                        return
                    elif "い" or "え" in ans:
                        print("さようなら。\nプレイしてくれてありがとう！")
                        game_status = "end"
                        break
                    else:
                        print("\n入力が無効だ。")
            elif choice == "黄":
                print("\n薄暗い廊下を通して宝箱が見えてくる。\n")
                return ("complete")
            elif choice == "青":
                print("\n戸が落ちて潰された！パンケーキになちゃった…🥞\n待て、一体どうしてそんなこと起こるんだ？？\n")
                print('''  ▄▀  ██   █▀▄▀█ ▄███▄       ████▄     ▄   ▄███▄   █▄▄▄▄ 
  ▄▀    █ █  █ █ █ █▀   ▀      █   █      █  █▀   ▀  █  ▄▀ 
  █ ▀▄  █▄▄█ █ ▄ █ ██▄▄        █   █ █     █ ██▄▄    █▀▀▌  
  █   █ █  █ █   █ █▄   ▄▀     ▀████  █    █ █▄   ▄▀ █  █  
   ███     █    █  ▀███▀               █  █  ▀███▀     █   
          █    ▀                        █▐            ▀    
         ▀                              ▐                  \n''')
                while True:
                    print('''>--------------------------------------------------------------------<\n''')
                    retry = input("やり直す? (はい/いいえ)\n\n")
                    print('''\n>--------------------------------------------------------------------<''')
                    ans = [hi for hi in retry]
                    if "は" or "い" in ans:
                        return
                    elif "い" or "え" in ans:
                        print("さようなら。\nプレイしてくれてありがとう！")
                        game_status = "end"
                        break
            else:
                print("\n入力が無効だ。")


def final_level():
    global game_status
    global secret_code
    attempts = 0
    while game_status == "run":
        if lang == "en":
            attempts += 1
            if attempts == 1:
                print('''\n>--------------------------------------------------------------------<''')
                choice = input(
                    "\nThe chest appears to 'ave a three digit combination lock on it...\n\nI wonder what the combination be\n(Enter combination)\n\n")
            elif attempts == 2:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input("Was there any numbers in this here adventure?\n\n")
                print('''\n>--------------------------------------------------------------------<\n''')
            elif attempts == 3:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input('"That there be a MEAN date" ring any bells???\n\n')
            elif attempts == 4:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input(
                    "Blimey!! Be ye a chowder 'ead?\nMEAN be a mathematical term for the average of a GROUP OF NUMBERS.\n\n")
            elif attempts == 5:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input("Oh fer the love o' Pete!! Take the numbers in yer birth date and find the average!\n\n")
                ('''>--------------------------------------------------------------------<\n''')
            elif attempts < 10:
                print('''\n>--------------------------------------------------------------------<\n''')
                choice = input("*Silence*\n\n")
                ('''\n>--------------------------------------------------------------------<\n''')
            else:
                if attempts == 10:
                    print('''\n>--------------------------------------------------------------------<''')
                    choice = input(
                        f"\nJust add {name[2]}, {name[3]}, and {name[4]} together and divide that number by {len(secret_code)} to get the combination。\nYa got it？ Combination = ({name[2]} + {name[3]} + {name[4]}) / {len(secret_code)}\n")
            nums = [num for num in choice]
            if len(nums) != 3 and attempts < 5 and attempts <= 5:
                print('''\n>--------------------------------------------------------------------<''')
                print("\nOh come on!! I said THREE DIGIT didn't I?!\n*Mutters under breath*\n")
            elif choice.isdigit() == False and attempts < 5:
                print("Numbers only!!\n")
            if choice == secret_code:
                print('''>--------------------------------------------------------------------<''')
                print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
                print(
                    f'\nIt opened!! The treasure is all yers.\nBut wait...there be a note.\n"Dear {name[0]}:\nIf you are reading this, then I am probably gone from this earth.\nI know that I was never really there for you\nand although I followed my love of adventure and the sea,\nI still regret not being a part of your life.\nI hope you can take this treasure and make a good life for yourself.\n*A photo falls from the letter*\n*You pick it up*\n...Its a photo of you as a young child.\nYou are standing in between your mom and...\nGoldtooth???\nThe End')
                return "complete"
            elif attempts == 10:
                print("Yer still here?! Just start over an' hopefully ye can get it right.")
                game_status = "end"
                break
            elif attempts <= 5:
                print("That be the wrong answer.\nTry again\n")
        else:
            attempts += 1
            if attempts == 1:
                print('''>--------------------------------------------------------------------<''')
                choice = input("\n3桁のコンビネーションロックがかかっているようだ。\n\n何のコンビネーションだろう。\n(コンビネーションを入力)\n\n")
                print('''>--------------------------------------------------------------------<''')
            elif attempts == 2:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input("この冒険に数字はあったかな。\n\n")
            elif attempts == 3:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input("「平均的な日付だな。」と言う台詞覚えてる？？\n\n")
            elif attempts == 4:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input("バカなの？数学的なことをしないと。\n\n")
            elif attempts == 5:
                print('''>--------------------------------------------------------------------<\n''')
                choice = input("もうやってらんないわ！誕生日の数字を使って平均を見つけるべきだ。\n\n")
            elif attempts < 10:
                print('''\n>--------------------------------------------------------------------<\n''')
                choice = input("*沈黙*\n\n")
            else:
                if attempts == 10:
                    choice = input(
                        f"\nほら{name[2]}と{name[3]}と{name[4]}を全然たすしてから、その数字×{len(secret_code)}が\nコンビネーションになる。\n分かる？コンビネーション = ({name[2]} たす {name[3]} たす {name[4]}) わる {len(secret_code)}\n")
                    print('''\n\n>--------------------------------------------------------------------<\n''')
            nums = [num for num in choice]
            if len(nums) != 3 and attempts <= 5:
                print('''>--------------------------------------------------------------------<''')
                print("\nおいおい！数字三つって言っただろうが!\n*怒ってつぶやく*\n")
            elif choice.isdigit() == False and attempts <= 5:
                print("数字だけ!!\n")
                print('''>--------------------------------------------------------------------<''')
            if choice == secret_code:
                print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
                print(
                    f'\n開いたぞ!! 宝はやっと手に入れた。\nちょっと...手紙が黄金の上に置いてる。\n"{name[1]}へ:\nこの手紙を読んでるとしたら、俺はもう亡くなったかもしれない。\n俺は冒険と海への愛に導かされた。\nそのせいで君の成長していた瞬間を\n経験できなくて後悔してる.\nこの宝物を取って良い人生を味わうがいい。\n*手紙から写真が落ちた*\n*拾い上げる*\n...幼い頃の写真だ。\n母と逞しそうな男の中に立ってる...\nまさか金歯なのか???\n')
                return "complete"
            elif attempts > 10:
                print('''>--------------------------------------------------------------------<''')
                print("まだいるの?! もうやり直しな。今度こそ上手く成し遂げる。")
                game_status = "end"
                break
            elif attempts <= 5:
                print("\n入力が無効だ。\n")

            # Establishing while loop to proceed through each "level" function so long as "complete" condition is met.


while game_status == "run":
    l1 = level1()
    if l1 == "complete":
        l2 = level2()
        if l2 == "complete":
            l3 = level3()
            if l3 == "complete":
                l4 = level4()
                if l4 == "complete":
                    fl = final_level()
                    if fl == "complete":
                        if lang == "en":
                            print('''>--------------------------------------------------------------------<''')
                            print("\nYe have found the treasure!!!\nThanks fer playin'!\n")
                            print('''>--------------------------------------------------------------------<''')
                        else:
                            print('''>--------------------------------------------------------------------<''')
                            print("\n宝を発見!!!\nプレイしてくれてありがとう!\n")
                            print('''>--------------------------------------------------------------------<''')
                        print(''' _________ __              
|  _   _  [  |             
|_/ | | \_|| |--. .---.    
    | |    | .-. / /__\\   
   _| |_   | | | | \__.,   
  |_____| [___]|__'.__.'   

 ________              __  
|_   __  |            |  ] 
  | |_ \_|_ .--.  .--.| |  
  |  _| _[ `.-. / /'`\' |  
 _| |__/ || | | | \__/  |  
|________[___||__'.__.;__]\n''')
                        print('''>--------------------------------------------------------------------<''')
                        game_status = "end"
    else:
        continue