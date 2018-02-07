
# coding: utf-8

# In[2]:

# Packages 
import tesserocr
from PIL import Image
import pyscreenshot
from google import google


# In[ ]:

def screengrab():
    question_img = pyscreenshot.grab(bbox=(10,10,500,500))
    ans1_img = pyscreenshot.grab(bbox=(10,10,500,500))
    ans2_img = pyscreenshot.grab(bbox=(10,10,500,500))
    ans3_img = pyscreenshot.grab(bbox=(10,10,500,500))


# In[6]:

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

# print question_text


# In[18]:

def function():
    global dummyvar 
    dummyvar = "big meme"
    
function()

print dummyvar


# In[ ]:

# maybe use automator to take screenshot and then run script.


# In[ ]:

num_page = 1
search_results = google.search("location of the 2014 winter olympics", num_page)

# Search results is an object that is a list of lists. Each element corrosponds to one result.
# Each result is composed of attributes like "name" and "description" that are strings and
# can be counted. 

type(search_results)
print search_results[0].name

str1 = search_results[0].name
count = str1.count("Winter")
print count


# # Search function

# Take in a google results object and three answer choices. Initilize an empty list called counts that stores the number of occurences of each answer choice in the search results. For each answer choice we want to cycle through each search result's description and count occurences of that answer choice, then append that count to the counts list. Finally we return the correct answer according to the highest count. 

# In[ ]:

# Run Time test on an actual question

question = "In Charles Dickens' A Christmas Carol, what was Mr. Scrooge's first name?"
choice1 = "William"
choice2 = "George"
choice3 = "Ebenezer"

google_results = google.search(question, 1)

# Function Description / Plan: 
# Cycel thorugh each answer choice in the answer list. For each choice, cycle through the results list and assign each description to a converted desctription variable. Then count the occurences of the current answer choice in the converted description. Append counts with the number of occurences. If the current count is greater thean the greatest count so far we save it as the correct choice. Then return the correct answer as the index of this choice number. 

def final_answer(results, ans1, ans2, ans3):
    # Intilize empty list of counts
    counts = []
    # Place answer choices into an ordered list
    answers = [ans1, ans2, ans3]

    for i in answers:
        for j in results:
            converted_description = results[j].description
        counted_description = converted_description.count(i)
        if counted_description > max(counts):
            correct_choice = i 
            
    return "The correct answer is %s" % answers[i]
        
final_answer(google_results,choice1,choice2,choice3)


# In[ ]:

line = "--------------------------------"
print google_results
print line
print google_results[0]
print line
print google_results[0].name
print line
print google_results[0].name.count("Marley")

lister = []
lister.append(google_results[0].name.count("Marley"))
print lister

question = "In Charles Dickens' A Christmas Carol, what was Mr. Scrooge's first name?"
choice1 = "William"
choice2 = "George"
choice3 = "Ebenezer"

container = []
print container 
things = google.search(question, 1)
meme = things[0].name.count("Marley")
container.append(meme)
print container

container.append(things[1].description.count("Scrooge"))
print max(container)


# Notes:
# 
# If the question is structured "Which of these:...?" we should employ a different search method. Comparing the searched answeres with occurences of the characteristic presented in the question. For example: "Which of these is a hip hop artist: Kendrick, Gaga, Metallica" Search Kendrick Gaga and Metallica, store results, count occurences of "hip hop" in each result and output the correct answer as the result with the most occurences of "hip hop".
