import random as rand
class Item:
    def __init__(self):
        self.kniv = 0
        self.sword = 0
        self.kanon = 0
        self.kniv_strength_bonus = rand.randint(100,200)
        self.sword_strength_bonus = rand.randint(100,200)
        self.kanon_strength_bonus = rand.randint(100,200)
    def add_kniv (self):
        self.kniv = self.kniv + 1 #när funktionen kallas ska det räkna till en kniv i din inventory.
    def add_sword (self):
        self.sword = self.sword + 1
    def add_kanon (self):
        self.kanon = self.kanon + 1    
        

class Spelaren:
    def __init__(self, HP, strength, level):
        self.HP = HP
        self.strength = strength
        self.level = level
        self.inventory = Item()#för att kalla "class" Item
        

    def display_egenskaper(self):  #funktionen kallas när spelaren vill titta på sina egna egenskaper.
        print("\nDin HP är",s1.HP)
        print("Dina styrkor är", 100 + s1.inventory.kniv*s1.inventory.kniv_strength_bonus + s1.inventory.sword*s1.inventory.sword_strength_bonus + s1.inventory.kanon*s1.inventory.kanon_strength_bonus) #Totala styrkor som spelaren har fått
        print("Din nivå är",s1.level,"\n")

#HP, styrkan och nivån börjar från:
s1 = Spelaren(100, 100, 1)


def add_tool():   #funktionen kallas när slumpad siffran "door" är lika med 2 alltså spelaren hittade en kista, eller när man ska byta in ett föremål.
    while True:
        if hittade_verktyg == "en kniv":
            s1.inventory.add_kniv()
            s1.strength += s1.inventory.kniv_strength_bonus
            print("Du har fått",hittade_verktyg,"i kistan.")
            break
        elif hittade_verktyg == "ett svärd":
            s1.inventory.add_sword()
            s1.strength += s1.inventory.sword_strength_bonus
            print("Du har fått",hittade_verktyg,"i kistan.")
            break
        else:
            s1.inventory.add_kanon()
            s1.strength += s1.inventory.kanon_strength_bonus
            print("Du har fått",hittade_verktyg,"i kistan.")
            break      
        

def byta_foremal_ja(): #funktionen kallas när spelaren välja att byta ut ett föremål.
    while True:
        which_tool = (input("\nvilket föremål vill du byta ut? svara [kniv], [svärd],eller [kanon]:"))
        if which_tool.lower() == "kniv":
            if s1.inventory.kniv > 0:
                change_tool_knive()
                break
            else:
                print("\nDet finns inte kniv i din inventory just nu. Du kan bara byta ett annat föremål.")
                continue
        elif which_tool.lower() == "svärd":
            if s1.inventory.sword > 0:
                change_tool_sword()
                break
            else:
                print("\nDet finns inte svärd i din inventory just nu. Du kan bara byta ett annat föremål.")
                continue
        elif which_tool.lower() == "kanon":
            if s1.inventory.kanon > 0:    
                change_tool_kanon()
                break
            else:
                print("\nDet finns inte kanon i din inventory just nu. Du kan bara byta ett annat föremål.")
                continue
        else:
            print("\nOförväntad svar")
            continue       


def change_tool_knive():
    s1.inventory.kniv = s1.inventory.kniv - 1
    print("\nDu väljer att byta ut en kniv.")


def change_tool_sword():        
    s1.inventory.sword = s1.inventory.sword - 1
    print("\nDu väljer att byta ut en svärd.")

def change_tool_kanon():
    s1.inventory.kanon = s1.inventory.kanon - 1
    print("\nDu väljer att byta ut en kanon.")


while True:
    choose = input("\nVälkommen till äventyrspelet. Om du vill titta på dina egenskaper, vilket innehåller din HP, dina styrkor och dina nivå, du kan ange [e]; Om du vill titta på din inventory, ange på [i]; Om du ska gå in i dörr 1, klicka på [a]; Om du ska gå in i dörr 2, klicka på [b]; Om du ska gå in i dörr 3, klicka på [c]; Om du vill avsluta programmet/spelet, klicka på [q]:")
    if choose.lower() == "e":
        s1.display_egenskaper()      #.lower(): det funkar för både små och stor bokstäver.
    elif choose.lower() in ("a","b","c"):
        door = rand.randint(1,3)
        monster_strength = rand.randint(500,1000)
        if door == 1:
            print("\nDu träffar en monster.")
            if s1.strength < monster_strength:
                s1.HP = s1.HP - 1
                if s1.HP > 0:
                    print("Monstern har högre styrka än dig, du kommer att förlora 1 HP. Din ny HP är",s1.HP,".")
                else: 
                    print("Monstern har högre styrka än dig, du kommer att förlora 1 HP. Din HP har sänkt till 0, Du har förlorat spelet.")
                    break
            elif s1.strength > monster_strength:
                s1.level = s1.level + 1
                if s1.level < 10:
                    print("Monstern har lägre styrka än dig, du har vunnit stridan, din nivå öka till",s1.level,".")
                else:
                    print("Monstern har lägre styrka än dig, du har vunnit stridan. Din nivå har nått 10, du har vunnit spelet.")
                    break
            else:
                print("ni både har samma styrkor, spelet fortsätta.")
        elif door == 2:
            print("\nDu hittar en kista som innehåller olika föremål.")
            tool = ["en kniv", "ett svärd","en kanon"]
            hittade_verktyg = rand.choice(tool)
            if s1.inventory.kniv + s1.inventory.sword + s1.inventory.kanon < 5: #Om det finns mindre än 5 föremål i din inventory:
                add_tool()
                continue
            elif s1.inventory.kniv + s1.inventory.sword + s1.inventory.kanon == 5: #Om din inventory är full:
                while True:
                    Change_tool = input("\nMen din inventory är full, du kan inte lägga till något föremål till din inventory. Vill du byta ett föremål, svara [ja] eller [nej]:")
                    if Change_tool.lower() == "nej":
                        break
                    elif Change_tool.lower() == "ja":
                        byta_foremal_ja()  #Spelaren kan välja att byta ut ett föremål som finns i din inventory först, 
                        add_tool()         #Sedan lägga till ett slumpad föremål i spelarens inventory.
                        break
                    else:
                        print("\nOförväntad svar\n")
                        continue
              
        elif door == 3:
            print("\nDu faller i en fälla.")
            reduced_HP = rand.randint(1,13) #när spelaren faller till en fälla, spelarens HP kommer sänkas splumpad mellan 1 och 13.
            s1.HP = s1.HP - reduced_HP
            if s1.HP > 0:
                print("Du kommer förlora",reduced_HP,"HP. Din ny HP är",s1.HP,".\n")    
            else:
                print("Ditt HP har sänkt till 0,du har förlorat spelet.")
                break
            
    elif choose.lower() == "i": #Visa spelarens alla antal föremål som finns i inventory och dessa föremålens styrkor.
        print("\nDet finns",s1.inventory.kniv,"kniv,",s1.inventory.sword,"svärd och",s1.inventory.kanon,"kanon i din inventory, alla föremål har respektive styrkorna",s1.inventory.kniv*s1.inventory.kniv_strength_bonus,",",s1.inventory.sword*s1.inventory.sword_strength_bonus,"och",s1.inventory.kanon*s1.inventory.kanon_strength_bonus) #räkna sätt: antal kniv gånger styrkorna för en kniv,  antal svärd gånger styrkorna för ett svärd, antal kanon gånger styrkorna för en kanon.
    elif choose.lower() == "q":
        print("\nspelet har avslutat.\n")
        break
    else:
        print("\nfelaktig val")
        continue    