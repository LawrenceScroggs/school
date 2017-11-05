#Whitepixel_Lscroggs
#This program will alter an image by changing 4 of the pixels to the color white
#11/03/17
#JES

print("White Pixel Program\n")
print("You will be asked for 4 pixel locations to change")
print("The values must be between 10 and 200")
prompt_onex = 0
prompt_oney = 0
prompt_twox = 0
prompt_twoy = 0
prompt_threex = 0
prompt_threey = 0
prompt_fourx = 0
prompt_foury = 0

def main():
  prompt_one()
  prompt_two()
  prompt_three()
  prompt_four()
  file = get_file()
  image = make_image(file)
  change_dots(image)
  show_image(image)
  
def prompt_one():
  global prompt_onex
  global prompt_oney
  print("Pixel number one")
  prompt_onex = int(raw_input("Please enter your X value and then hit enter.    "))
  prompt_oney = int(raw_input("Please enter your Y value and then hit enter.    "))
  if prompt_onex >= 10 and prompt_onex <=200:
    print("Thank you")
  elif prompt_oney >= 10 and prompt_oney <=200:
    print("Thank you")
  else:
    print("User Error")
    sys.exit()
  
def prompt_two():
  global prompt_twox
  global prompt_twoy
  print("Pixel number two")
  prompt_twox = int(input("Please enter your X value and then hit enter.    "))
  prompt_twoy = int(input("Please enter your Y value and then hit enter.    "))
  if prompt_twox >= 10 and prompt_twox <=200:
    print("Thank you")
  elif prompt_twoy >= 10 and prompt_twoy <= 200:
    print("Thank you") 
  else:
    print("User Error")
    sys.exit()  
  
def prompt_three():
  global prompt_threex
  global prompt_threey
  print("Pixel number three")
  prompt_threex = int(input("Please enter your X value and then hit enter.    "))
  prompt_threey = int(input("Please enter your Y value and then hit enter.    "))
  if prompt_threex >= 10 and prompt_threex <=200:
    print("Thank you")
  elif prompt_threey >= 10 and prompt_threey <= 200:
    print("Thank you") 
  else:
    print("User Error")
    sys.exit()    
def prompt_four():
  global prompt_fourx
  global prompt_foury
  print("Pixel number four")
  prompt_fourx = int(input("Please enter your X value and then hit enter.    "))
  prompt_foury = int(input("Please enter your Y value and then hit enter.    "))
  if prompt_fourx >= 10 and prompt_fourx <=200:
    print("Thank you")
  elif prompt_foury >= 10 and prompt_foury <= 200:
    print("Thank you")
  else:
    print("User Error")
    sys.exit()    
def change_dots(image):
  
  pixel_1 = getPixel(image, prompt_onex, prompt_oney)
  pixel_2 = getPixel(image, prompt_twox, prompt_twoy)
  pixel_3 = getPixel(image, prompt_threex, prompt_threey)
  pixel_4 = getPixel(image, prompt_fourx, prompt_foury)
  
  newColor = makeColor(255,255,255)
  
  setColor(pixel_1, newColor)
  setColor(pixel_2, newColor)
  setColor(pixel_3, newColor)
  setColor(pixel_4, newColor)

def get_file():
  file = pickAFile()
  return file
  
def make_image(file):
  image = makePicture(file)
  return image
  
def show_image(image):
  show(image)
main()  