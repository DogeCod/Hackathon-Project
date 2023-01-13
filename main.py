
import sys, os, signal, colorama
colorama.init() 



colors = {
  "info":     "35m",      #Orange for info messages
  "error":    "31m",      #Red for error messages
  "ok":       "32m",      #Green for success messages
  "menu2c":  "\033[46m",  #Light blue menu
  "menu1c":  "\033[44m",  #Blue menu
  "close":  "\033[0m"     #Color coding close
  }
cc = "\033[0m"
ct = "\033[101m"
cs = "\033[41m"
c1 = colors["menu1c"]
c2 = colors["menu2c"]



programtitle="Hackafon Menu"

# Fill the options as needed.
menu2_colors = {
  "ct":ct,
  "cs":cs,
  "opt":c2
}
menu2_options = {
  "title":  "Credits",
  "a":      "Port Scanner",
  "b":      "Matrix Screen",
  "c":      "Py Chat",

  "9":      "Main menu",
  "0":      "Quit (or use CNTRL+C)",
}
menu1_colors = {
  "ct":ct,
  "cs":cs,
  "opt":c1
}
menu1_options = {
  "title":  "Hackathon Project",
  "1":      "Port Scanner",
  "2":      "Matrix Screen",
  "3":      "Py Chat Server",
  "4":      "Py Chat Client",
  "9":      "Credits",
  "0":      "Quit (or use CNTRL+C)",
}


def printWithColor(color,string):
  print("\033["+colors[color]+" "+string+cc)
def printError():
  printWithColor("error","Error!!")
  return 1
def printSuccess():
  printWithColor("ok","Success!!")
  return 0

# Exit program
def exit():
  sys.exit()
  

def sigint_handler(signum, frame):
  print("CNTRL+C exit")
  import exit.py
  sys.exit(0)


class menu_template():

  def __init__(self,options,colors):
    self.menu_width = 50  
    self.options = options
    self.colors = colors

  def createMenuLine(self,letter,color,length,text):
    menu = color+" ["+letter+"] "+text
    line = " "*(length-len(menu))
    return  menu+line+cc

  def createMenu(self,size):
    line = self.colors["ct"] + " "+programtitle
    line += " "*(size-len(programtitle)-6)
    line += cc
    print (line)  # Title
    line = self.colors["cs"] + " "+self.options["title"]
    line += " "*(size-len(self.options["title"])-6)
    line += cc
    print (line) # Subtitle
    for key in self.options:
      if(key != "title"):
        print (self.createMenuLine(key,self.colors["opt"],size,self.options[key]))

  def printMenu(self):
    self.createMenu(self.menu_width)

  def action(self,ch):
    if   ch == '1':
      self.method_1()
      import port_scanner
    elif ch == '2':
      self.method_2()
      import matrix_screen
    elif ch == '3':
      self.method_3()
    elif ch == '4':
      self.method_4()
    elif ch == '5':
      self.method_5()
    elif ch == 'a':
      self.method_a()
    elif ch == 'b':
      self.method_s()
    elif ch == 'c':
      self.method_c()
    elif ch == 'd':
      self.method_e()
    elif ch == 'e':
      self.method_f()
    elif (ch==''):
      pass # Print menu again
    elif ch == '0':
      import exit.py
      sys.exit()
    else:
      printError()

  def method_1(self):
    pass
  def method_2(self):
    pass
  def method_3(self):
        #put py chat
        print("SERVER INSTRCIONZ")
        print("To Start PyChat Server, Go To Py Chat Folder (DO NOT RUN) Then in")
        print("Vscode Terminal Type 'py server.py <ur ipv4> <a free port>' To Start Server")
  
  def method_4(self):
    print("CLIENT INSTRCIONZ")
    print("To Start PyChat Client, Go To Py Chat Folder (DO NOT RUN) Then in")
    print("Vscode Terminal Type 'py client.py <server ipv4 > <server port>' To Connect To Server")
  def method_5(self):
    pass
  def method_a(self):
    print("Port Scanner:")
    print("Ben Hogety (My Class)")
    
  def method_b(self):
     print("Matrix:")
     print("Ben Hogety (My Class)")
  def method_c(self):
     print("Py Chat:")
     print("Krystian (DogeCod) And Github For Socket Example")
  def method_d(self):
    pass
  def method_e(self):
    pass


class menu1(menu_template):
  pass


class menu2(menu_template):
      pass


class menu_handler:

  def __init__ (self):
    self.current_menu="main"
    self.m1=menu1(menu1_options, menu1_colors)
    self.m2=menu2(menu2_options, menu2_colors)

  def menuExecution(self):
    if(self.current_menu=="main"):
      self.m1.printMenu()
    else:
      self.m2.printMenu()
    choice = input(" >> ")
    if(self.current_menu=="main"):
      if(choice=="9"):
        self.current_menu="second"
      else:
        self.actuator(0,choice)
    else:
      if(choice=='9'):
        self.current_menu="main"
      else:
        self.actuator(1,choice)
    print("\n")

  def actuator(self,type,ch):
    if type == 0:
      self.m1.action(ch)
    else:
      self.m2.action(ch)

# Main Program
if __name__ == "__main__":
  x = menu_handler()
  signal.signal(signal.SIGINT, sigint_handler)
  while True:
    x.menuExecution()