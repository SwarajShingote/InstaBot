#!/usr/bin/env python
# coding: utf-8

# # Project : Instabot-II

# ## Importing required libraries

# In[2123]:


import pandas as pd
import matplotlib.pyplot as plt
import time 
import numpy as np
import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


# ## Initialize chrome webdriver and visit on Instagram

# In[2124]:


# location where the chrome driver is
driver = webdriver.Chrome(executable_path ="C:/Users/Win 10/Desktop/chromedriver.exe")
# visit on instagram and maximize the window 
driver.get('https://www.instagram.com/')
driver.maximize_window()


# ## Log-In to Instagram 

# In[2125]:


# Defined a function for login having username and password as argument
def log_in(a,b) :
        
        time.sleep(2)
        username = driver.find_elements_by_css_selector('form input')[0]
        password = driver.find_elements_by_css_selector('form input')[1]
        
        
        username.send_keys(a)
        password.send_keys(b)
        password.send_keys(Keys.ENTER)


# In[2126]:


# SAMPLE NAME : Swaraj Shingote
# SAMPLE Password : qwerty@123

log_in(SAMPLE NAME,SAMPLE Password)


# In[2127]:


time.sleep(2)
save = driver.find_elements_by_css_selector('button')[0].click()


# In[2128]:


time.sleep(2)
notify = driver.find_element_by_class_name('mt3GC').click()      


# In[2129]:


# searching for the keyword "food" and get the href of first 10 handles

search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys("food")
time.sleep(2)
href = []
names = []
count = 0
for i in driver.find_elements_by_class_name('yCE8d  '):
    
    if i.text[0] != "#":
        
        names.append(i.text.split()[0])
        href.append(i.get_attribute("href"))
        count+=1
    if count == 10:
            break
# print(len(href))


# ## Extracting Count of Followers

# In[2130]:


# Extracting the exact no. of followers and here repalcing the , with '' and converting string into int (e.g=> 93,526 --> 93526)
followers = []
for i in href:
    driver.get(i)
    driver.find_element_by_class_name("g47SY ").get_attribute("title")
    a = (driver.find_elements_by_class_name("g47SY ")[1].get_attribute("title"))
    a = int(a.replace(',',''))
    followers.append(a)
    time.sleep(3)


# In[1995]:


# followers


# In[1996]:


# names


# ## Que 1.1 : Top 5 handles with highest number of followers

# In[2133]:


# Craeting a dataframe with two columns "Names" and "followers" 
d = {'Names': names, 'followers': followers}
df = pd.DataFrame(data = d)
df.reset_index(drop =True,inplace = True)
df = df.sort_values("followers",ascending = False)

# Creating two lists and appending the first 5 handles and their count of followers
x = []
y = []
print("Top 5 handles having highest number of followers:")
print("--------------------------------------------------")
for i in zip(df.Names[:5],df.followers[:5]):
#     print(i)
    x.append(i[0])
    y.append(i[1])
    print(i[0],"with followers : ",i[1])
    
# Plotting bar graph between count of followers of and handles

plt.title('Top 5 handles having highest number of followers',fontsize = 12)
plt.xlabel('Handles>>>>>>>',fontsize = 12)
plt.ylabel('Followers>>>>>>>',fontsize = 12)

plt.bar(x,y,color = 'c',edgecolor = 'black')
plt.xticks(rotation = 10)
plt.show()


# ## Que 1.2 ,1.3 : Number of posts these handles have done in the previous 3 days.

# In[2136]:


# Creating a list named count_post and counting the posts upto 3 days 
# appending the counts in count_post list

count_post = []
for i in x[:5]:
    time.sleep(2)
    driver.get("https://www.instagram.com/"+i+"/")
    time.sleep(2)
    driver.find_element_by_class_name("v1Nh3 ").click()
    time.sleep(2)  

    i = 0
    while True:
        a = driver.find_element_by_class_name('_1o9PC').text.split()

        try :
            a1 = int(a[0])
            if a[1] == "DAY" or a[1] == "HOUR" or a[1] == "HOURS":
                i = i + 1
                driver.find_element_by_class_name("_65Bje ").click()
                time.sleep(2)

            elif a[1] == "DAYS" :
                driver.find_element_by_class_name("_65Bje ").click()
                time.sleep(2)                 
                
                if a1 > 3 :
                    break
                i = i + 1
                    
        except :
            print(0)
            break
    count_post.append(i)
 


# In[2137]:


## Plotting the bar graph between count of post in previous 3 days vs handles

for i in range(len(x)):
    print(x[i], "posts",count_post[i],"post in previous 3 days")
print("---------------------------------------------------------")
plt.title('Number of posts these handles have done in the previous 3 days',fontsize = 12)
plt.xlabel('Handles>>>>>>>',fontsize = 12)
plt.ylabel('Followers>>>>>>>',fontsize = 12)

plt.bar(x,count_post,color = 'red',edgecolor = 'black')
plt.xticks(rotation = 10)
plt.show()


# ## Que 2.1 :Scraping the content of the first 10 posts of each handle

# In[2144]:


# Here I am using Beautifulsoup to extract the content of post
# Creating a list named "content" and appending the scraped content in it
# Defined a specific function for scarping the content of each post 
content = []
def scrape():
    soup = BeautifulSoup(driver.page_source,'html')
    cont = soup.find_all('div',attrs={'class':'C4VMK'})
    soup_2 = BeautifulSoup(str(cont),'html')
    spans = soup_2.find_all('span')[1].get_text()
    if spans == "Verified":
        spans = soup_2.find_all('span')[2].get_text()
    print(spans)
    content.append(spans) 


# In[2145]:


for i in x[:5]:
    driver.get("https://www.instagram.com/"+i+"/")
    time.sleep(2)
    print(i,">>>>>>>") 
    print("----------------------------------------------------------------------------")
    driver.find_element_by_class_name("v1Nh3 ").click()
    time.sleep(1)  
    scrape()
    print("----------------------------------------------------------------------------")
    try :
        for j in range(9) :
            time.sleep(2)
            driver.find_element_by_class_name("_65Bje").click()
            time.sleep(2)
            scrape()
            print("----------------------------------------------------------------------------")
    except :
        pass 


# In[2180]:


# len(content)


# ## Que 2.2 : List of all words that are used in scraped posts

# In[2181]:


# Creating the list named "list_words" where i am appending all the words extracted from the scrape content
contents = []
for i in content:
    contents.append(i.split())
list2d = [i for i in contents]
list_words = list(itertools.chain(*list2d))
print("list of all words used in all the scraped posts")
print(list_words)


# ## Frequency of each word

# In[2182]:


# print(len(list_words))
# value_counts() method gives the dictionary with words and their frequency
# Creating a dataframe with two columns "words" and "frequency"
d = {"words" : list_words}
df = pd.DataFrame(data=d)
words_count = df.value_counts()
print("Words and their frequecies")
word = []
for i in words_count.keys():
    word.append(i[0])
df = pd.DataFrame({"words":word,"frequency" :words_count.values})
df.reset_index(drop= True,inplace = True)
print(df)


# ## Que 2.3 : CSV file with two columns :  word and frequency

# In[2150]:


df.to_csv("Instabot.csv",index = False)

## Uncomment below code to read the csv file
# Instabot = pd.read_csv("Instabot.csv")
# Instabot


# ## Que 2.4 : Most popular hashtags 

# In[2183]:


# Considering first 10 hashtags as most popular ones
df = df[df.words.str.startswith("#") ]
print('Most popular hashtags')
print('---------------------')
for i in df.words[0:10]:
    print(i) 


# ## Que 2.5 : Pie Chart for Top five hashtags

# In[2184]:


explode =(0,0.1,0,0.1,0)
colors = ['lightskyblue', 'red', 'blue', 'green', 'gold']
plt.pie(x=df[:5].frequency ,explode = explode,colors = colors,labels = df[:5].words,autopct='%.1f%%',startangle=90,shadow = True)
plt.title("Top five hashtags", fontsize = 18)
plt.legend(loc='upper right',bbox_to_anchor=(1.8, 1.0))
plt.show()


# ## Que 3.1 : Likes of the top 10 posts

# In[2153]:


# Creating two lists one which appends no of followers and other appends count of likes
# Extarcting the exact no of followers 
# counting the likes of first 10 posts (ignoring the posts which has video content (where views are there))

followers_no = []
like_count = []
for i in x[:5]:
    time.sleep(2)
    driver.get("https://www.instagram.com/"+i+"/")
    time.sleep(2)
    foll = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title').replace(',','')
    time.sleep(2)
    followers_no.append(foll)
    driver.find_element_by_class_name("v1Nh3 ").click()
    time.sleep(1)  
    i = 0
    try :
        a = driver.find_element_by_class_name("Nm9Fw").text.split()[0].replace(',','')
        like_count.append(int(a))
        i = i + 1
    except:
        pass
     
    while True :
        driver.find_element_by_class_name("_65Bje ").click()
        time.sleep(2)
        try :
            a = driver.find_element_by_class_name("Nm9Fw").text.split()[0].replace(',','')
            like_count.append(int(a))
            i = i + 1
            if i == 10:
                break
        except:
            pass
        


# In[2116]:


# like_count


# In[2162]:


# followers_no


# In[2193]:


print("Likes of the top 10 posts")
print("-------------------------")
for i in range(5):
    print(x[i],'first 10 posts likes :',(like_count[10*i:10*(i+1)]))


# ## Que 3.2 : Average likes for a handle 

# In[2187]:


# Finding the average likes by dividing sum of total likes by 10 
# Plotting the bar graph of handles and average likes
print("Average likes :")
print("-------------------------")

handle = []
for i in range(5):
    print(x[i],'=',sum(like_count[10*i:10*(i+1)])/10)
    handle.append(sum(like_count[10*i:10*(i+1)])/10)
print("--------------------------------------------------------")
plt.bar(x,handle,color = 'c',edgecolor = "black")
plt.title("Average likes for a handle",fontsize = 15)
plt.xlabel("Handles>>>>>",fontsize = 15)
plt.ylabel("Average likes>>>>>",fontsize = 15)
    
plt.xticks(rotation = 15)
plt.show()


# ## Que 3.3 : Average followers:like ratio of each handle

# In[2189]:


# Finding the Average followers by like ratio by dividing total followers by average likes of handle
# Plotting the bar graph between Handles and Average followers: like ratio 

ratio = []
for i in range(5):
    print("Followers/Avg.likes for",x[i],":",round(int(followers_no[i])/handle[i],2))
    ratio.append(round(int(followers_no[i])/handle[i],2))
print("--------------------------------------------------------")
plt.bar(x,ratio,color = 'm',edgecolor = "black")
plt.title("Followers/Avg.likes",fontsize = 15)
plt.xlabel("Handles>>>>>",fontsize = 15)
plt.ylabel("Ratio>>>>>",fontsize = 15)

plt.xticks(rotation = 15)
plt.show()

