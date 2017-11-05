#pickandshowRev2_LScroggs.py
#this program allows user to pick and display a pre-selected image
#10/19/2017
#JES
def main():
  print("Image Select\n")
  info()
  prompt()
  file = get_file()
  image = make_image(file)
  showImage(image)
  closing()
def info():
  print("This program allows you to select an image and display it to the screen.")  
  print("By selecting *yes* the program will open a file select this is where you select the image you want displayed to the screen.")
def prompt():
  prompt = raw_input("Would you like to select an image?  ")
  prompt = prompt.lower()
  if prompt == "yes":
    print("please select")
  else:
    sys.exit()
def get_file():
  file = pickAFile()
  return file

def make_image(file):
  image = makePicture(file)
  return image
  
def show_image(image):
  show(image)
def closing():
  print("Thank you for using the program.")
  print("I hope you will think of this program when selecting files in the future.")
  


main()
