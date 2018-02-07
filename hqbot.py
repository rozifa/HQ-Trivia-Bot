# Packages 
import tesserocr
from PIL import Image
import pyscreenshot

def screengrab():
    question_img = pyscreenshot.grab(bbox=(10,10,500,500))
    ans1_img = pyscreenshot.grab(bbox=(10,10,500,500))
    ans2_img = pyscreenshot.grab(bbox=(10,10,500,500))
    ans3_img = pyscreenshot.grab(bbox=(10,10,500,500))

# Anatomy of the question
question_img = pyscreenshot.grab(bbox=(10,10,500,500))
ans1_img = pyscreenshot.grab(bbox=(10,10,500,500))
ans2_img = pyscreenshot.grab(bbox=(10,10,500,500))
ans3_img = pyscreenshot.grab(bbox=(10,10,500,500))

# screenshot.show()

# save to file
pyscreenshot.grab_to_file('question_img.png')
pyscreenshot.grab_to_file('ans1_img.png')
pyscreenshot.grab_to_file('ans2_img.png')
pyscreenshot.grab_to_file('ans3_img.png')

# Import and open screengrabs
op_question_img = Image.open('question_img.png')
op_ans1_img = Image.open('ans1_img.png')
op_ans2_img = Image.open('ans2_img.png')
op_ans3_img = Image.open('ans3_img.png')

# prints grabbed text from screenshot
question_text = tesserocr.image_to_text(op_question_img)
ans1_text = tesserocr.image_to_text(op_ans1_img)
ans2_text = tesserocr.image_to_text(op_ans2_img)
ans3_text = tesserocr.image_to_text(op_ans3_img)

def google_search():
