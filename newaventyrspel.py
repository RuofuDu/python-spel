import random as rand
import sys
        
class Item:
    def __init__(self):
        self.name = rand.choice(['kniv','svärd','kanon'])
        self.strength_bonus = rand.randint(100,200)
 
class Inventory:
    def __init__(self):
        self.tools = list()
    def display(self): 
        if self.tools == []: #tomt list
            print ("\nDin inventory är tomt just nu!\n")
        else:
            for tool in self.tools: #tool representera allting som finns i listan.
                print (f"Ditt hittade föremål är: {tool.name}, föremålet har styrkan: {tool.strength_bonus}")
    def append_tool(self, tool):
        self.tools.append(tool) #För att lägga till ett föremål och styrkan till listan som heter self.tools.(tool)betyder alla information i class Tool().
    def throw_away_tool(self, tool_number):
        self.tools.pop(tool_number)       #för att ta bort det här föremål från listan "self.tools"
 
class Spelaren:
    def __init__(self, name, HP=100, strength=100, level=1):
        self.name = name
        self.HP = HP
        self.strength = strength
        self.level = level
        self.inventory = Inventory() #för att kalla "class" Item
        self.inquiry = "\nEller du kan titta på dina egenskaper genom att ange[e]:\nDu kan itta på din inventory genom att ange[i]:\nOch du kan avsluta programmet/spelet genom att ange[q]:\n"
        
    def add_tool(self):
        tool = Item()  #för att kalla "class" Tool
        self.inventory.append_tool(tool) #För att lägga till listsn som har olika föremål och styrkaorna i din inventory. (tool)är argument vilket betyder allting som finns i class Tool()
        self.strength += tool.strength_bonus 
        print (f"Du hittar en {tool.name} i kistan")
        print (f"{tool.name} har styrkan: {tool.strength_bonus}")
 
    def remove_tool(self, tool_number):   #(tool_number) är lika som int(answer) i funktion change_tool, det är både funktionernas argument. Det betyder föremålens ording i listan self.tools i inventory. Det finns totalt 5 föremål, därför är tool_number mellan 0 och 4. 
        print (f"Du väljer att byta ut {self.inventory.tools[tool_number].name}, som har styrkan {self.inventory.tools[tool_number].strength_bonus}") #skriva ut vilket föremål vill du byta ut och dess styrkan.
        self.strength -= self.inventory.tools[tool_number].strength_bonus
        self.inventory.throw_away_tool(tool_number)    #self.inventory.throw_away_tool betyder att kalla funktionen som ligger i class inventory()
        
    def process_door(self):
        door = "\nDu kan välja 3 dörrar som är mellan nummer 1--3:"
        while True:
            user_choice = input(door + self.inquiry)
            if user_choice.lower() in ('e', 'i', 'q'):
                self.display_or_quit(user_choice)
                continue
            elif user_choice in ('1', '2', '3'):
                encounter = rand.choice(['monster','fälla','kista'])
                if encounter == 'monster':
                    self.meet_monster()
                elif encounter == 'fälla':
                    self.meet_falla()
                else:
                    self.meet_kista()
            else:
                print ("\nOförväntad svar, försök igen!")
 
    def display_or_quit(self, choice): #user choice skicka till function "display_or_quit" med en argument som är e eller i eller q.
        if choice in ('e', 'E'): #choice som en argument i funktion "display_or_quit" ska vara e, i eller q beror på vad är "user_choice".
            self.display_egenskaper()
        elif choice in ('i', 'I'):
            self.inventory.display()
        else: 
            print ("avsluta programmet")
            sys.exit()
            
    def meet_monster(self):
        print ("\nDu träffar en monster")
        monster_strength = rand.randint(500, 1000)
        if self.strength > monster_strength:
            self.level += 1
            if self.level < 10:
                print (f"Monstern har lägre styrkan än dig, du har vunnit stridan. Din nivå öka till {self.level}\n")
            else:
                print(f"Monstern har lägre styrkan än dig, du har vunnit stridan. Din nivå öka till {self.level}, du har vunnit spelet.\n")    
                sys.exit()
        elif self.strength < monster_strength:
            self.HP -= 1
            if self.HP > 0:
                print (f"Monstern har högre styrkan än dig, du har förlårat stridan. Du kommer att förlora 1 HP, din ny HP är {self.HP}\n")
            else: 
                print ("Monstern har högre styrkan än dig, du har förlårat stridan. Du kommer att förlora 1 HP, din HP har sänkt till 0, du har förlorat spelet\n")
                sys.exit()
        else:
            print("\nNi både har samma styrkor, spelet fortsätta.")
 
 
    def meet_falla(self):
        reduced_HP = rand.randint(1, 10)
        self.HP -= reduced_HP
        if self.HP > 0:
            print (f"\nDu faller i en fälla, du kommer att förlora {reduced_HP} hp, din ny HP {self.HP}\n")
        else: 
            print (f"\nDu faller i en fälla, du kommer att förlora {reduced_HP} hp, din HP har sänkt till 0, du har förlorat spelet.\n")
            sys.exit()


       
    def meet_kista(self):
        print("\nDu träffar en kista")
        if len(self.inventory.tools) < 5: #om element(föremålen) som finns i inventory(listan) är mindre än 5.
            self.add_tool()
        else:
            self.change_tool_or_not()
    
    def change_tool_or_not(self):
        while True:
            user_choice = input("\nDin inventory är full, du kan inte lägga till något föremål till din inventory. Vill du byta ett föremål, svara [ja] eller [nej]:\n" + self.inquiry).lower()
            if user_choice == 'nej': 
                break
            elif user_choice == 'ja':
                self.change_tool()
                break
            elif user_choice in ('e', 'i', 'q'):
                self.display_or_quit(user_choice) #(user choice) ska vara en argument och skicka till funktion "display_or_quit"
                continue    
            else:
                print ("\nOförväntad svar, försök igen!")  
                continue
 
  

    def change_tool(self): 
        while True:           
            answer = input("\nVilket föremål vill du byta? Ange [0,1,2,3 eller 4]:\n" + self.inquiry) 
            if answer in ('0', '1', '2', '3', '4'): # 0 till 4 representera föremålens ordning.
                self.remove_tool(int(answer)) #answer är lika som tool_number i funktion remove_tool
                self.add_tool()
                break
            elif answer in ('e', 'E', 'i', 'I', 'q', 'Q'):
                self.display_or_quit(answer)
                continue
            else:
                print ("\nOförväntad svar, försök igen!")
                continue
            
        
    def display_egenskaper(self):  #funktionen kallas när spelaren vill titta på sina egna egenskaper.
        print("\nDitt namn är", self.name)
        print("Ditt HP är",self.HP)
        print("Dina totala styrkor är", self.strength) #Totala styrkor som spelaren har fått
        print("Din nivå är",self.level,"\n")
 
def play_game():
    name = input ("Ange ditt namn:\n")
    if name in ("q", "Q"):   
        sys.exit()
    else:
        s1 = Spelaren(name)
        print("\nVälkommen till spelet.")
        s1.process_door() #s1 betyder att gå till funktionen som ligger i klass spelaren()
            
play_game()
 