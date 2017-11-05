#pickandshowRev1_LScroggs.py
#this program allows user to pick and display a pre-selected image
#10/19/2017
#JES

print("Image Select\n")
prompt = raw_input("Would you like to select an image?  ")
prompt = prompt.lower()
if prompt == "yes":
  print("please select")
else:
  sys.exit()
  
def main():
  
  file = get_file()
  image = make_image(file)
  show_image(image)

def get_file():
  file = pickAFile()
  return file

def make_image(file):
  image = makePicture(file)
  return image
  
def show_image(image):
  show(image)



main()
