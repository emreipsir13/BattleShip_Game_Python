import random,time
print("Amiral Battı Oyununa Hoş Geldiniz")
time.sleep(1)
menu=True
language=5
calis=True
while (calis==True):
    language=int(input("Türkçe İçin Yazın (0) /// For english write (1) : "))
    if (language==0 or language==1):
        calis=False
while menu==True:
    if (language==0):
        print("(1) Tek Kişilik Oyun")
        print("(2) Bot a Karşı Bot")
        print("(3) Çıkış")
        tercih=input("Lütfen Bir Seçim Yapınız (1-2-3) : ")
    if (language==1):
        print("(1) Player VS Computer")
        print("(2) Computer VS Computer")
        print("(3) Exit")
        tercih=input("Please Make A Decision (1-2-3) : ")
    if tercih=="1":
        hedeftahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        gemitahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        for i in range(len(hedeftahtasi)):
            print(hedeftahtasi[i])
        for i in range(3):
            if (language==0):
                print(i+1,end="")
                ykor=input(". Geminin Dikey Koordinatını Giriniz (A-B-C-D-E) : ")
                print(i+1,end="")
                xkor=input(". Geminin Yatay Koordinatını Giriniz (1-2-3-4-5) : ")
            if (language==1):
                print(i+1,end="")
                ykor=input(". Please Enter Vertical Position Of The Ship (A-B-C-D-E) : ")
                print(i+1,end="")
                xkor=input(". Please Enter Horizontal Position Of The Ship (1-2-3-4-5) : ")
            if xkor=="1":
                xkor=1
            elif xkor=="2":
                xkor=2
            elif xkor=="3":
                xkor=3
            elif xkor=="4":
                xkor=4
            elif xkor=="5":
                xkor=5
            else:
                xkor=0
            if ykor=="a" or ykor=="A":
                ykor=1
            elif ykor=="b" or ykor=="B":
                ykor=2
            elif ykor=="c" or ykor=="C":
                ykor=3
            elif ykor=="d" or ykor=="D":
                ykor=4
            elif ykor=="e" or ykor=="E":
                ykor=5
            else:
                ykor=0
            #kontrol eger hata varsa dogru olana kadar tekrar tekrar sectiriyor
            while xkor==0 or ykor==0 or gemitahtasi[ykor][xkor]=="1":
                if (language==0):
                    print("Yanlış Bir Giriş Yaptınız Lütfen Tekrar Giriş Yapınız.")
                    print(i+1,end="")
                    ykor=input(". Geminin Dikey Koordinatını Giriniz (A-B-C-D-E) : ")
                    print(i+1,end="")
                    xkor=input(". Geminin Yatay Koordinatını Giriniz (1-2-3-4-5) : ")
                if (language==1):
                    print("You Entered Somethings Wrong. Please Enter Again.")
                    print(i+1,end="")
                    ykor=input(". Please Enter Vertical Position Of The Ship (A-B-C-D-E) : ")
                    print(i+1,end="")
                    xkor=input(". Please Enter Horizontal Position Of The Ship (1-2-3-4-5) : ")
                if xkor=="1":
                    xkor=1
                elif xkor=="2":
                    xkor=2
                elif xkor=="3":
                    xkor=3
                elif xkor=="4":
                    xkor=4
                elif xkor=="5":
                    xkor=5
                else:
                    xkor=0
                if ykor=="a" or ykor=="A":
                    ykor=1
                elif ykor=="b" or ykor=="B":
                    ykor=2
                elif ykor=="c" or ykor=="C":
                    ykor=3
                elif ykor=="d" or ykor=="D":
                    ykor=4
                elif ykor=="e" or ykor=="E":
                    ykor=5
                else:
                    ykor=0
            gemitahtasi[ykor][xkor]="1"
        if (language==0):    
            print("Gemilerinizin Konumları")
        if (language==1):
            print("Positions of Your Ships")
        for i in range(len(gemitahtasi)):
            print(gemitahtasi[i])
        #İkilik geminin konumlandırılması
        for i in range(1):
            if (language==0):
                ykor=input("2 Lik Geminin Dikey Koordinatını Giriniz (A-B-C-D-E) : ")
                xkor=input("2 Lik Geminin Yatay Koordinatını Giriniz (1-2-3-4-5) : ")
            if (language==1):
                ykor=input("Please Enter Vertical Position Of The 2-Length Ship (A-B-C-D-E) : ")
                xkor=input("Please Enter Horizontal Position Of The 2-Length Ship (1-2-3-4-5) : ")
            if xkor=="1":
                xkor=1
            elif xkor=="2":
                xkor=2
            elif xkor=="3":
                xkor=3
            elif xkor=="4":
                xkor=4
            elif xkor=="5":
                xkor=5
            else:
                xkor=0
            if ykor=="a" or ykor=="A":
                ykor=1
            elif ykor=="b" or ykor=="B":
                ykor=2
            elif ykor=="c" or ykor=="C":
                ykor=3
            elif ykor=="d" or ykor=="D":
                ykor=4
            elif ykor=="e" or ykor=="E":
                ykor=5
            else:
                ykor=0
            while xkor==0 or ykor==0 or gemitahtasi[ykor][xkor]=="1" or (xkor==5 and ykor==1 and gemitahtasi[1][4]=="1" and gemitahtasi[2][5]=="1") or (xkor==1 and ykor==1 and gemitahtasi[1][2]=="1" and gemitahtasi[2][1]=="1") or (xkor==1 and ykor==5 and gemitahtasi[4][1]=="1" and gemitahtasi[5][2]=="1") or (xkor==5 and ykor==5 and gemitahtasi[4][5]=="1" and gemitahtasi[5][4]=="1") or (ykor==1 and xkor!=1 and xkor!=5 and gemitahtasi[ykor][xkor-1]=="1" and gemitahtasi[ykor][xkor+1]=="1" and gemitahtasi[ykor+1][xkor]=="1") or (ykor==5 and xkor!=1 and xkor!=5 and gemitahtasi[ykor][xkor-1]=="1" and gemitahtasi[ykor][xkor+1]=="1" and gemitahtasi[ykor-1][xkor]=="1") or (xkor==5 and ykor!=1 and ykor!=5 and gemitahtasi[ykor-1][xkor]=="1" and gemitahtasi[ykor+1][xkor]=="1" and gemitahtasi[ykor][xkor-1]=="1") or (xkor==1 and ykor!=1 and ykor!=5 and gemitahtasi[ykor-1][xkor]=="1" and gemitahtasi[ykor+1][xkor]=="1" and gemitahtasi[ykor][xkor+1]=="1"):
                if (language==0):
                    print("Gemiyi Koymak İstediğiniz Yer Sıkışık Veya Orada Zaten Bir Gemi Var.")
                    ykor=input("2 Lik Geminin Dikey Koordinatını Giriniz (A-B-C-D-E) : ")
                    xkor=input("2 Lik Geminin Yatay Koordinatını Giriniz (1-2-3-4-5) : ")
                if (language==1):
                    print("The Place You Want to Put The Ship Is Blocking or There is Already A Ship in There.")
                    ykor=input("Please Enter Vertical Position Of The 2-Length Ship (A-B-C-D-E) : ")
                    xkor=input("Please Enter Horizontal Position Of The 2-Length Ship (1-2-3-4-5) : ")
                if xkor=="1":
                    xkor=1
                elif xkor=="2":
                    xkor=2
                elif xkor=="3":
                    xkor=3
                elif xkor=="4":
                    xkor=4
                elif xkor=="5":
                    xkor=5
                else:
                    xkor=0
                if ykor=="a" or ykor=="A":
                    ykor=1
                elif ykor=="b" or ykor=="B":
                    ykor=2
                elif ykor=="c" or ykor=="C":
                    ykor=3
                elif ykor=="d" or ykor=="D":
                    ykor=4
                elif ykor=="e" or ykor=="E":
                    ykor=5
                else:
                    ykor=0
            gemitahtasi[ykor][xkor]="1"
            dikyattt=True
            if ykor!=5:
                if gemitahtasi[ykor-1][xkor]=="1" and gemitahtasi[ykor+1][xkor]=="1":
                    if (language==0):
                        print("Sıkışıklıktan Dolayı Otomatikmen Yatay")
                    if(language==1):
                        print("Automatically Horizontal Due To Blocking.")
                    dikyat="Y"
                    dikyattt=False
            if gemitahtasi[ykor-1][xkor]=="1" and ykor==5:
                if (language==0):
                    print("Sıkışıklıktan Dolayı Otomatikmen Dikey")
                if (language==1):
                    print("Automatically Vertical Due To Blocking.")
                dikyat="Y"
                dikyattt=False 
            if xkor!=5:
                if gemitahtasi[ykor][xkor-1]=="1" and gemitahtasi[ykor][xkor+1]=="1":
                    if (language==0):
                        print("Sıkışıklıktan Dolayı Otomatikmen Dikey")
                    if (language==1):
                        print("Automatically Vertical Due To Blocking.")
                    dikyat="D"
                    dikyattt=False
            if gemitahtasi[ykor][xkor-1]=="1" and xkor==5:
                if (language==0):
                    print("Sıkışıklıktan Dolayı Otomatikmen Dikey")
                if (language==1):
                    print("Automatically Vertical Due To Blocking.")
                dikyat="D"
                dikyattt=False       
            while dikyattt==True:
                if (language==0):
                    dikyat=input("Geminizi Dikey mi Yatay mı Koymak İstiyorsunuz (D - Y) : ")
                if (language==1):
                    dikyat=input("Did You Want To Put Your Ship Vertical Or Horizontal (V - H) : ")
                    if (dikyat=="V" or dikyat=="v"):
                        dikyat="D"
                    if(dikyat=="H" or dikyat=="h"):
                        dikyat="Y"
                dikyattt=False
            vurdukmu=True
            if ykor!=1 and gemitahtasi[ykor-1][xkor]!="1":
                if dikyat=="D" or dikyat=="d":
                    gemitahtasi[ykor-1][xkor]="1"
                    vurdukmu=False
            if ykor!=5 and vurdukmu==True and gemitahtasi[ykor+1][xkor]!="1":
                if dikyat=="D" or dikyat=="d":
                    gemitahtasi[ykor+1][xkor]="1"
            if xkor!=5 and gemitahtasi[ykor][xkor+1]!="1":
                if dikyat=="Y" or dikyat=="y":
                    gemitahtasi[ykor][xkor+1]="1"
                    vurdukmu=False                   
            if xkor!=1 and vurdukmu==True and gemitahtasi[ykor][xkor-1]!="1":    
                if dikyat=="Y" or dikyat=="y":
                    gemitahtasi[ykor][xkor-1]="1"
        for i in range(len(gemitahtasi)):
            print(gemitahtasi[i])
        if (language==0):
            print("     Tahtanızın Son Hali\n")
        if (language==1):
            print("     Final Wersion Of Your Board\n")
        time.sleep(3)
            #BBOOOOTTTTELLLAAA
        bothedeftahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        botgemitahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        for i in range(3):
            ykor=random.randint(1,5)
            xkor=random.randint(1,5)
            while botgemitahtasi[ykor][xkor]=="1":
                ykor=random.randint(1,5)
                xkor=random.randint(1,5)
            botgemitahtasi[ykor][xkor]="1"
        for i in range(1):
                    ykor=random.randint(1,5)
                    xkor=random.randint(1,5)
                    while botgemitahtasi[ykor][xkor]=="1" or (xkor==5 and ykor==1 and botgemitahtasi[1][4]=="1" and botgemitahtasi[2][5]=="1") or (xkor==1 and ykor==1 and botgemitahtasi[1][2]=="1" and botgemitahtasi[2][1]=="1") or (xkor==1 and ykor==5 and botgemitahtasi[4][1]=="1" and botgemitahtasi[5][2]=="1") or (xkor==5 and ykor==5 and botgemitahtasi[4][5]=="1" and botgemitahtasi[5][4]=="1") or (ykor==1 and xkor!=1 and xkor!=5 and botgemitahtasi[ykor][xkor-1]=="1" and botgemitahtasi[ykor][xkor+1]=="1" and botgemitahtasi[ykor+1][xkor]=="1") or (ykor==5 and xkor!=1 and xkor!=5 and botgemitahtasi[ykor][xkor-1]=="1" and botgemitahtasi[ykor][xkor+1]=="1" and botgemitahtasi[ykor-1][xkor]=="1") or (xkor==5 and ykor!=1 and ykor!=5 and botgemitahtasi[ykor-1][xkor]=="1" and botgemitahtasi[ykor+1][xkor]=="1" and botgemitahtasi[ykor][xkor-1]=="1") or (xkor==1 and ykor!=1 and ykor!=5 and botgemitahtasi[ykor-1][xkor]=="1" and botgemitahtasi[ykor+1][xkor]=="1" and botgemitahtasi[ykor][xkor+1]=="1"):
                        ykor=random.randint(1,5)
                        xkor=random.randint(1,5)
                    botgemitahtasi[ykor][xkor]="1"
                    dikyattt=True
                    if ykor!=5:
                        if botgemitahtasi[ykor-1][xkor]=="1" and botgemitahtasi[ykor+1][xkor]=="1":
                            dikyat="Y"
                            dikyattt=False
                    if botgemitahtasi[ykor-1][xkor]=="1" and ykor==5:
                        dikyat="Y"
                        dikyattt=False 
                    if xkor!=5:
                        if botgemitahtasi[ykor][xkor-1]=="1" and botgemitahtasi[ykor][xkor+1]=="1":
                            dikyat="D"
                            dikyattt=False
                    if botgemitahtasi[ykor][xkor-1]=="1" and xkor==5:
                        dikyat="D"
                        dikyattt=False  
                    while dikyattt==True:
                        dikyat=random.randint(1,2)
                        if dikyat==1:
                            dikyat="D"
                            dikyattt=False
                        if dikyat==2:
                            dikyat="Y"
                            dikyattt=False
                    vurdukmu=True
                    if ykor!=1 and botgemitahtasi[ykor-1][xkor]!="1":
                        if dikyat=="D" or dikyat=="d":
                            botgemitahtasi[ykor-1][xkor]="1"
                            vurdukmu=False
                    if ykor!=5 and vurdukmu==True and botgemitahtasi[ykor+1][xkor]!="1":
                        if dikyat=="D" or dikyat=="d":
                            botgemitahtasi[ykor+1][xkor]="1"
                    if xkor!=5 and botgemitahtasi[ykor][xkor+1]!="1":
                        if dikyat=="Y" or dikyat=="y":
                            botgemitahtasi[ykor][xkor+1]="1"
                            vurdukmu=False                   
                    if xkor!=1 and vurdukmu==True and botgemitahtasi[ykor][xkor-1]!="1":    
                        if dikyat=="Y" or dikyat=="y":
                            botgemitahtasi[ykor][xkor-1]="1"
        for i in range(len(gemitahtasi)):
            print(hedeftahtasi[i],"          ",bothedeftahtasi[i])
        if (language==0):
            print("       Sizin Tahtanız                             Botun Tahtası\n")
        if (language==1):
            print("         Your Board                               Computers Board\n")
        #ATEŞ ETMEEE
        botskor=0
        oyuncuskor=0
        dongu=True
        while dongu==True:
            oyuncuvurdu=True
            botvurdu=True
            while oyuncuvurdu==True and botskor!=5 and oyuncuskor!=5:
                if (language==0):
                    ykor=input("Ateş Etmek İstediğiniz Koorditanı Giriniz (A-B-C-D-E) : ")
                    xkor=input("Ateş Etmek İstediğiniz Koorditanı Giriniz (1-2-3-4-5) : ")
                if (language==1):
                    ykor=input("Please Enter The Vertical Coordinates of Where You Want To Shoot (A-B-C-D-E) : ")
                    xkor=input("Please Enter The Horizontal Coordinates of Where You Want To Shoot (1-2-3-4-5) : ")
                if xkor=="1":
                    xkor=1
                elif xkor=="2":
                    xkor=2
                elif xkor=="3":
                    xkor=3
                elif xkor=="4":
                    xkor=4
                elif xkor=="5":
                    xkor=5
                else:
                    xkor=0
                if ykor=="a" or ykor=="A":
                    ykor=1
                elif ykor=="b" or ykor=="B":
                    ykor=2
                elif ykor=="c" or ykor=="C":
                    ykor=3
                elif ykor=="d" or ykor=="D":
                    ykor=4
                elif ykor=="e" or ykor=="E":
                    ykor=5
                else:
                    ykor=0
                while xkor==0 or ykor==0 or bothedeftahtasi[ykor][xkor]=="X" or bothedeftahtasi[ykor][xkor]=="O":
                    if (language==0):
                        print("Yanlış Bir Seçim Yaptınız Lütfen Tekrar Giriş Yapınız.")
                        ykor=input("Ateş Etmek İstediğiniz Koorditanı Giriniz (A-B-C-D-E) : ")
                        xkor=input("Ateş Etmek İstediğiniz Koorditanı Giriniz (1-2-3-4-5) : ")
                    if (language==1):
                        print("You Entered Somethings Wrong. Please Enter Again.")
                        ykor=input("Please Enter The Vertical Coordinates of Where You Want To Shoot (A-B-C-D-E) : ")
                        xkor=input("Please Enter The Horizontal Coordinates of Where You Want To Shoot (1-2-3-4-5) : ")
                    if xkor=="1":
                        xkor=1
                    elif xkor=="2":
                        xkor=2
                    elif xkor=="3":
                        xkor=3
                    elif xkor=="4":
                        xkor=4
                    elif xkor=="5":
                        xkor=5
                    else:
                        xkor=0
                    if ykor=="a" or ykor=="A":
                        ykor=1
                    elif ykor=="b" or ykor=="B":
                        ykor=2
                    elif ykor=="c" or ykor=="C":
                        ykor=3
                    elif ykor=="d" or ykor=="D":
                        ykor=4
                    elif ykor=="e" or ykor=="E":
                        ykor=5
                    else:
                        ykor=0
                if botgemitahtasi[ykor][xkor]=="1":
                    if (language==0):
                        print("Vurdunuz!!!")
                    if (language==1):
                        print("Hit!!!")
                    bothedeftahtasi[ykor][xkor]="X"
                    oyuncuskor+=1
                else:
                    if (language==0):
                        print("Iska")
                    if (language==1):
                        print("Miss")
                    bothedeftahtasi[ykor][xkor]="O"
                    oyuncuvurdu=False
                for i in range(len(gemitahtasi)):
                    print(hedeftahtasi[i],"          ",bothedeftahtasi[i])
                if (language==0):
                    print("       Sizin Tahtanız                             Botun Tahtası\n")
                if (language==1):
                    print("         Your Board                               Computers Board\n")
            while botvurdu==True and botskor!=5 and oyuncuskor!=5:
                ykor=random.randint(1,5)
                xkor=random.randint(1,5)
                while hedeftahtasi[ykor][xkor]=="X" or hedeftahtasi[ykor][xkor]=="O":
                    ykor=random.randint(1,5)
                    xkor=random.randint(1,5)
                if gemitahtasi[ykor][xkor]=="1":
                    hedeftahtasi[ykor][xkor]="X"
                    botskor+=1
                else:
                    hedeftahtasi[ykor][xkor]="O"
                    botvurdu=False
                for i in range(len(gemitahtasi)):
                    print(hedeftahtasi[i],"          ",bothedeftahtasi[i])
                if (language==0):
                    print("       Sizin Tahtanız                             Botun Tahtası\n")
                if (language==1):
                    print("         Your Board                               Computers Board\n")
            if oyuncuskor==5:
                if (language==0):
                    print("============================================================")
                    print(" Tebrikler Düşmanın Tüm Gemilerini Batırdınız Ve Kazandınız ")
                    print("============================================================")
                if (language==1):
                    print("=================================================================")
                    print(" Congratulations You Have Sunk All The Enemy's Ships And You Won ")
                    print("=================================================================")
                dongu=False
            if botskor==5:
                if (language==0):
                    print("====================================================")
                    print(" Düşmanınız Tüm Gemilerinizi Batırdı Ve Kaybettiniz ")
                    print("====================================================")
                if (language==1):
                    print("===============================================")
                    print(" Your Enemy Sinked All Your Ships And You Lost ")
                    print("===============================================")
                dongu=False
    elif tercih=="2":
        birincibothedeftahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        birincibotgemitahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        for i in range(3):
            ykor=random.randint(1,5)
            xkor=random.randint(1,5)
            while birincibotgemitahtasi[ykor][xkor]=="1":
                ykor=random.randint(1,5)
                xkor=random.randint(1,5)
            birincibotgemitahtasi[ykor][xkor]="1"
        for i in range(1):
                    ykor=random.randint(1,5)
                    xkor=random.randint(1,5)
                    while birincibotgemitahtasi[ykor][xkor]=="1" or (xkor==5 and ykor==1 and birincibotgemitahtasi[1][4]=="1" and birincibotgemitahtasi[2][5]=="1") or (xkor==1 and ykor==1 and birincibotgemitahtasi[1][2]=="1" and birincibotgemitahtasi[2][1]=="1") or (xkor==1 and ykor==5 and birincibotgemitahtasi[4][1]=="1" and birincibotgemitahtasi[5][2]=="1") or (xkor==5 and ykor==5 and birincibotgemitahtasi[4][5]=="1" and birincibotgemitahtasi[5][4]=="1") or (ykor==1 and xkor!=1 and xkor!=5 and birincibotgemitahtasi[ykor][xkor-1]=="1" and birincibotgemitahtasi[ykor][xkor+1]=="1" and birincibotgemitahtasi[ykor+1][xkor]=="1") or (ykor==5 and xkor!=1 and xkor!=5 and birincibotgemitahtasi[ykor][xkor-1]=="1" and birincibotgemitahtasi[ykor][xkor+1]=="1" and birincibotgemitahtasi[ykor-1][xkor]=="1") or (xkor==5 and ykor!=1 and ykor!=5 and birincibotgemitahtasi[ykor-1][xkor]=="1" and birincibotgemitahtasi[ykor+1][xkor]=="1" and birincibotgemitahtasi[ykor][xkor-1]=="1") or (xkor==1 and ykor!=1 and ykor!=5 and birincibotgemitahtasi[ykor-1][xkor]=="1" and birincibotgemitahtasi[ykor+1][xkor]=="1" and birincibotgemitahtasi[ykor][xkor+1]=="1"):
                        ykor=random.randint(1,5)
                        xkor=random.randint(1,5)
                    birincibotgemitahtasi[ykor][xkor]="1"
                    dikyattt=True
                    if ykor!=5:
                        if birincibotgemitahtasi[ykor-1][xkor]=="1" and birincibotgemitahtasi[ykor+1][xkor]=="1":
                            dikyat="Y"
                            dikyattt=False
                    if birincibotgemitahtasi[ykor-1][xkor]=="1" and ykor==5:
                        dikyat="Y"
                        dikyattt=False 
                    if xkor!=5:
                        if birincibotgemitahtasi[ykor][xkor-1]=="1" and birincibotgemitahtasi[ykor][xkor+1]=="1":
                            dikyat="D"
                            dikyattt=False
                    if birincibotgemitahtasi[ykor][xkor-1]=="1" and xkor==5:
                        dikyat="D"
                        dikyattt=False  
                    while dikyattt==True:
                        dikyat=random.randint(1,2)
                        if dikyat==1:
                            dikyat="D"
                            dikyattt=False
                        if dikyat==2:
                            dikyat="Y"
                            dikyattt=False
                    vurdukmu=True
                    if ykor!=1 and birincibotgemitahtasi[ykor-1][xkor]!="1":
                        if dikyat=="D" or dikyat=="d":
                            birincibotgemitahtasi[ykor-1][xkor]="1"
                            vurdukmu=False
                    if ykor!=5 and vurdukmu==True and birincibotgemitahtasi[ykor+1][xkor]!="1":
                        if dikyat=="D" or dikyat=="d":
                            birincibotgemitahtasi[ykor+1][xkor]="1"
                    if xkor!=5 and birincibotgemitahtasi[ykor][xkor+1]!="1":
                        if dikyat=="Y" or dikyat=="y":
                            birincibotgemitahtasi[ykor][xkor+1]="1"
                            vurdukmu=False                   
                    if xkor!=1 and vurdukmu==True and birincibotgemitahtasi[ykor][xkor-1]!="1":    
                        if dikyat=="Y" or dikyat=="y":
                            birincibotgemitahtasi[ykor][xkor-1]="1"
        ikincibothedeftahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        ikincibotgemitahtasi=[["/","1","2","3","4","5"],["A"," "," "," "," "," "],["B"," "," "," "," "," "],["C"," "," "," "," "," "],["D"," "," "," "," "," "],["E"," "," "," "," "," "]]
        for i in range(3):
            ykor=random.randint(1,5)
            xkor=random.randint(1,5)
            while ikincibotgemitahtasi[ykor][xkor]=="1":
                ykor=random.randint(1,5)
                xkor=random.randint(1,5)
            ikincibotgemitahtasi[ykor][xkor]="1"
        for i in range(1):
                    ykor=random.randint(1,5)
                    xkor=random.randint(1,5)
                    while ikincibotgemitahtasi[ykor][xkor]=="1" or (xkor==5 and ykor==1 and ikincibotgemitahtasi[1][4]=="1" and ikincibotgemitahtasi[2][5]=="1") or (xkor==1 and ykor==1 and ikincibotgemitahtasi[1][2]=="1" and ikincibotgemitahtasi[2][1]=="1") or (xkor==1 and ykor==5 and ikincibotgemitahtasi[4][1]=="1" and ikincibotgemitahtasi[5][2]=="1") or (xkor==5 and ykor==5 and ikincibotgemitahtasi[4][5]=="1" and ikincibotgemitahtasi[5][4]=="1") or (ykor==1 and xkor!=1 and xkor!=5 and ikincibotgemitahtasi[ykor][xkor-1]=="1" and ikincibotgemitahtasi[ykor][xkor+1]=="1" and ikincibotgemitahtasi[ykor+1][xkor]=="1") or (ykor==5 and xkor!=1 and xkor!=5 and ikincibotgemitahtasi[ykor][xkor-1]=="1" and ikincibotgemitahtasi[ykor][xkor+1]=="1" and ikincibotgemitahtasi[ykor-1][xkor]=="1") or (xkor==5 and ykor!=1 and ykor!=5 and ikincibotgemitahtasi[ykor-1][xkor]=="1" and ikincibotgemitahtasi[ykor+1][xkor]=="1" and ikincibotgemitahtasi[ykor][xkor-1]=="1") or (xkor==1 and ykor!=1 and ykor!=5 and ikincibotgemitahtasi[ykor-1][xkor]=="1" and ikincibotgemitahtasi[ykor+1][xkor]=="1" and ikincibotgemitahtasi[ykor][xkor+1]=="1"):
                        ykor=random.randint(1,5)
                        xkor=random.randint(1,5)
                    ikincibotgemitahtasi[ykor][xkor]="1"
                    dikyattt=True
                    if ykor!=5:
                        if ikincibotgemitahtasi[ykor-1][xkor]=="1" and ikincibotgemitahtasi[ykor+1][xkor]=="1":
                            dikyat="Y"
                            dikyattt=False
                    if ikincibotgemitahtasi[ykor-1][xkor]=="1" and ykor==5:
                        dikyat="Y"
                        dikyattt=False 
                    if xkor!=5:
                        if ikincibotgemitahtasi[ykor][xkor-1]=="1" and ikincibotgemitahtasi[ykor][xkor+1]=="1":
                            dikyat="D"
                            dikyattt=False
                    if ikincibotgemitahtasi[ykor][xkor-1]=="1" and xkor==5:
                        dikyat="D"
                        dikyattt=False  
                    while dikyattt==True:
                        dikyat=random.randint(1,2)
                        if dikyat==1:
                            dikyat="D"
                            dikyattt=False
                        if dikyat==2:
                            dikyat="Y"
                            dikyattt=False
                    vurdukmu=True
                    if ykor!=1 and ikincibotgemitahtasi[ykor-1][xkor]!="1":
                        if dikyat=="D" or dikyat=="d":
                            ikincibotgemitahtasi[ykor-1][xkor]="1"
                            vurdukmu=False
                    if ykor!=5 and vurdukmu==True and ikincibotgemitahtasi[ykor+1][xkor]!="1":
                        if dikyat=="D" or dikyat=="d":
                            ikincibotgemitahtasi[ykor+1][xkor]="1"
                    if xkor!=5 and ikincibotgemitahtasi[ykor][xkor+1]!="1":
                        if dikyat=="Y" or dikyat=="y":
                            ikincibotgemitahtasi[ykor][xkor+1]="1"
                            vurdukmu=False                   
                    if xkor!=1 and vurdukmu==True and ikincibotgemitahtasi[ykor][xkor-1]!="1":    
                        if dikyat=="Y" or dikyat=="y":
                            ikincibotgemitahtasi[ykor][xkor-1]="1"
        for i in range(len(birincibothedeftahtasi)):
            print(birincibotgemitahtasi[i],"          ",ikincibotgemitahtasi[i])
        if (language==0):
            print("    Birinci Botun Tahtası                       İkinci Botun Tahtası\n")
        if (language==1):
            print("      First Bot's Board                            Second Bot's\n")
        time.sleep(1)
        if (language==0):
            print("Maç Başlıyor.")
        if (language==1):
            print("Match Starting.")
        time.sleep(1)
        if (language==0):
            print("Maç Başlıyor..")
        if (language==1):
            print("Match Starting..")
        time.sleep(1)
        if (language==0):
            print("Maç Başlıyor...")
        if (language==1):
            print("Match Starting...")
        birskor=0
        ikiskor=0
        tur=1
        dongu=True
        while dongu==True:
            birvurdu=True
            ikivurdu=True
            while birvurdu==True and birskor!=5 and ikiskor!=5:
                ykor=random.randint(1,5)
                xkor=random.randint(1,5)
                while ikincibothedeftahtasi[ykor][xkor]=="X" or ikincibothedeftahtasi[ykor][xkor]=="O":
                    ykor=random.randint(1,5)
                    xkor=random.randint(1,5)
                if ikincibotgemitahtasi[ykor][xkor]=="1":
                    ikincibothedeftahtasi[ykor][xkor]="X"
                    birskor+=1
                else:
                    ikincibothedeftahtasi[ykor][xkor]="O"
                    birvurdu=False
            while ikivurdu==True and birskor!=5 and ikiskor!=5:
                ykor=random.randint(1,5)
                xkor=random.randint(1,5)
                while birincibothedeftahtasi[ykor][xkor]=="X" or birincibothedeftahtasi[ykor][xkor]=="O":
                    ykor=random.randint(1,5)
                    xkor=random.randint(1,5)
                if birincibotgemitahtasi[ykor][xkor]=="1":
                    birincibothedeftahtasi[ykor][xkor]="X"
                    ikiskor+=1
                else:
                    birincibothedeftahtasi[ykor][xkor]="O"
                    ikivurdu=False
            for i in range(10):
                print("\n")
            print("                               ",tur,". Tur")
            tur+=1
            for i in range(len(birincibothedeftahtasi)):
                print(birincibothedeftahtasi[i],"          ",ikincibothedeftahtasi[i])
            if (language==0):
                print("    Birinci Botun Tahtası                       İkinci Botun Tahtası\n")
            if (language==1):
                print("      First Bot's Board                            Second Bot's\n")
            time.sleep(1)
            if birskor==5:
                if (language==0):
                    print("=========================")
                    print(" Birinci Bot Kazandı !!! ")
                    print("=========================")
                if (language==1):
                    print("===================")
                    print(" First Bot Won !!! ")
                    print("===================")
                dongu=False
            if ikiskor==5:
                if (language==0):
                    print("========================")
                    print(" İkinci Bot Kazandı !!! ")
                    print("========================")
                if (language==1):
                    print("====================")
                    print(" Second Bot Won !!! ")
                    print("====================")
                dongu=False
    elif tercih=="3":
        if (language==0):
            print("Çıkış Yapılıyor.")
        if (language==1):
            print("Exitting.")
        time.sleep(0.5)
        if (language==0):
            print("Çıkış Yapılıyor..")
        if (language==1):
            print("Exitting..")
        time.sleep(0.5)
        if (language==0):
            print("Çıkış Yapılıyor...")
        if (language==1):
            print("Exitting...")
        time.sleep(0.5)
        menu=False
    else:
        if (language==0):
            print("Yanlış Bir Seçim Yaptınız.")
        if (language==1):
            print("You Maked a Wrong Decision.")