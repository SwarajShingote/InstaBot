#!/usr/bin/env python
# coding: utf-8

# # Instabot

# ### Dependencies :

# In[ ]:


import sys
import time 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


# ### Visiting to Instagram.com :

# In[ ]:



# location where the chrome driver is
driver = webdriver.Chrome(executable_path ="C:/Users/Win 10/Desktop/chromedriver.exe")

# visit on instagram and maximize the window 
driver.get('https://www.instagram.com/')
driver.maximize_window()


# In[ ]:



class Instabot:

    def __init__(self,user_id,passcode):
        self.user_id = user_id
        self.passcode = passcode
    
    def log_in(self) :
        
        time.sleep(2)
        username = driver.find_elements_by_css_selector('form input')[0]
        password = driver.find_elements_by_css_selector('form input')[1]
        
        
        username.send_keys(self.user_id)
        password.send_keys(self.passcode)
        password.send_keys(Keys.ENTER)
    
        ## Save your password for future 
        time.sleep(3)
        save = driver.find_elements_by_css_selector('button')[0].click()
        ## Turn on Notifications
        time.sleep(2)
        notify = driver.find_element_by_class_name('mt3GC').click()    
    
            
    # Defined a function where we just want to pass the keyword we want as argument
    # and we will get list of all handles that are related to the keyword

    def searching(self,keyword):
        
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(keyword)
        time.sleep(2)
        for i in driver.find_elements_by_class_name('Ap253'):
            if i.text[0] != "#":
                print(i.text)
                
    def clear_box(self):
        
        search = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.clear()
    
    # Defined a function where we just want to pass the profile name we want to visit,as argument
    
    def visit_profile(self,profile_name):
        
        # searching for the profile_name using send_keys() and clicking on the search icon
        search_box=driver.find_element_by_class_name('XTCLo')
        search_box.send_keys(profile_name)
        waiter=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "yCE8d")))
        driver.find_element_by_class_name('yCE8d').click()
        waiter=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "_6VtSN")))
        
    # Defined function to follow the visited profile 

    def follow(self):
        
        
        followButton = driver.find_element_by_css_selector('button')
        if (followButton.text == 'Follow'):
            followButton.click()
            time.sleep(2)
            print("You are now following this handle!")
        elif (followButton.text == 'Message') :
            print("You are already following this handle!")
    
    # Defined function to follow the visited profile 
  
    def unfollow(self):
        
        # if there is message button then it will unfollow 
        # else,already unfollowed
        
        followButton = driver.find_element_by_css_selector('button')
        
        if (followButton.text== 'Message'):
            
            unfollow_butt= driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
            time.sleep(1)
            cnf_unfollow = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            time.sleep(2)
            print("You are now unfollowing this handle!",)
        else :
            print("You are already not following this handle!")
            

    # Defined function to like the 'n' number of posts of visited profile 
    
    def like(self,username,posts):
        
        driver.get('https://www.instagram.com/' + username + '/')
        
        # Clicking on the first post and liking it
        wait = WebDriverWait(driver, 10)
        first_post = wait.until(EC.presence_of_element_located((By.CLASS_NAME , '_9AhH0')))
        first_post.click()
        status =  wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class , "QBdPU")]/span'))).get_attribute('outerHTML').split(' ')[2].split('=')[1]
        
        # if the post is unlike then like it else print already likes
        if status == '"Like"':
            wait.until(EC.presence_of_element_located((By.XPATH , '//section[contains(@class , "ltpMr")]/span[1]/button'))).click()
        elif status == '"Unlike"' :
            print('Already Liked')

        #Running the loop for remaining 29 posts.
        for i in range(posts-1):
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,'coreSpriteRightPaginationArrow'))).click()         
            status =  wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class , "QBdPU")]/span'))).get_attribute('outerHTML').split(' ')[2].split('=')[1]          
            time.sleep(2)
        # if the post is unlike then like it else print already likes
            if status == '"Like"': 
                wait.until(EC.presence_of_element_located((By.XPATH,'//section[contains(@class , "ltpMr")]/span[1]/button'))).click()
            elif status == '"Unlike"' :
                print('Already Liked')
                
        print("Liked all ",posts," posts !")
        
        
    # Defined function to dislike the 'n' number of posts of visited profile 
    
    def dislike(self,username,posts):
        
        driver.get('https://www.instagram.com/' + username + '/')
        
        # Clicking on the first post and liking it.
        wait = WebDriverWait(driver, 10)
        first_post = wait.until(EC.presence_of_element_located((By.CLASS_NAME , '_9AhH0')))
        first_post.click()
        status =  wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class , "QBdPU")]/span'))).get_attribute('outerHTML').split(' ')[2].split('=')[1] 
        
        # if the post is unlike then like it else print already likes
        if status == '"Unlike"':
            wait.until(EC.presence_of_element_located((By.XPATH , '//section[contains(@class , "ltpMr")]/span[1]/button'))).click()
        elif status == '"Like"' :
            print('Already unliked')


        #Running the loop for remaining posts
        for i in range(posts-1):
            
            wait.until(EC.presence_of_element_located((By.CLASS_NAME,'coreSpriteRightPaginationArrow'))).click()         
            status =  wait.until(EC.presence_of_element_located((By.XPATH,'//div[contains(@class , "QBdPU")]/span'))).get_attribute('outerHTML').split(' ')[2].split('=')[1]          
            time.sleep(2)
            
            # if the post is unlike then like it else print already likes
            if status == '"Unlike"': 
                wait.until(EC.presence_of_element_located((By.XPATH,'//section[contains(@class , "ltpMr")]/span[1]/button'))).click()
            elif status == '"Like"' :
                print('Already unliked')
                
        print("Disliked all ",posts," posts !")
    
    # Defined function to extract the followers of visited profile 
        
    def extract_followers(self,username,no_of_followers):

        driver.get("https://www.instagram.com/"+username+"/")
        
        try:
            
            driver.execute_script('window.scrollTo(0, 0)')
            driver.find_element_by_xpath('//a[@class="-nal3 "]/span[@class="g47SY "]').click()
            
        except NoSuchElementException:
            
            driver.find_element_by_xpath('//a[@class=" _81NM2"]/span[contains(@class, "g47SY")]').click()
            waiter=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "notranslate")]')))
            
        time.sleep(2)
        
        while True:
            try:
                
                userlist=[]
                count=0
                
                while True:
                    
                    elements=driver.find_elements_by_xpath('//a[contains(@class, "notranslate")]')
                    if len(elements) < no_of_followers:
                        
                        waiter=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "jSC57")]')))
                        driver.execute_script('arguments[0].scrollIntoView(0, 100);', driver.find_element_by_xpath('//ul[contains(@class, "jSC57")]'))
                        time.sleep(0.8)
                        
                    i=elements[count]
                    userlist.append(i.get_attribute('innerHTML'))
                    if len(userlist)>= no_of_followers:
                        break
                    count+=1
                break
            except StaleElementReferenceException:
                continue

        print(userlist)
        
    # Defined function to see the story of visited profile 

    def story(self,username):
    
        driver.find_element_by_class_name('TqC_a').click()
        search_box=driver.find_element_by_class_name('XTCLo')
        search_box.send_keys(username)
        waiter=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "yCE8d")))
        time.sleep(1)
        driver.find_element_by_class_name('yCE8d').click()
        time.sleep(3)

        try:
            
            if int(driver.find_element_by_xpath('//div[contains(@class, "h5uC0")]/canvas').get_attribute('height')) == 210 :
                
                print('You have not seen the story yet!, The story of',username,'will be opened in the driver window, check now')
                driver.find_element_by_xpath('//div[contains(@class, "h5uC0")]').click()
            
            elif int(driver.find_element_by_xpath('//div[contains(@class, "h5uC0")]/canvas').get_attribute('height')) == 208 :
                
                print('You have already seen the story of' ,username,"!")
                
        except NoSuchElementException:
            print(username,' has no story!')    


# In[ ]:


# pass your Insta-Id and Password as arguments
# E.g ---> Instabot('instabot','123')

ibt = Instabot(YOUR INSTA_ID , YOUR PASS)


# ### Log-in to Instagram :

# In[ ]:


ibt.log_in()


# ### Searching a specific keyword :

# In[ ]:


# Pass the keyword you want, as an arguement
ibt.searching('sodelhi')


# ### Clear a search-box :

# In[ ]:


ibt.clear_box()


# ### Visit the profile :

# In[ ]:


# Pass the profile_name you want, as an arguement

ibt.visit_profile('dilsefoodie')


# ### Follow the visited handle :

# In[ ]:


ibt.follow()


# ### Unfollow the visited handle :

# In[ ]:


ibt.unfollow()


# ### Like  'n' posts of visited handle :

# In[ ]:


# Pass the profile_name and no of post you want to like, as an arguement

ibt.like("dilsefoodie",10)


# ### UnLike  'n' posts of visited handle :

# In[ ]:


# Pass the profile_name and no of post you want to Unlike, as an arguement

ibt.dislike("dilsefoodie",10)


# ### Extracting the followers :

# In[ ]:


# Pass the profile_name and no of followers you want to extract, as an arguement


ibt.extract_followers("foodtalkindia",100)


# In[ ]:


# Exit from following or followers
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()


# ### Checkout the story : 

# In[ ]:


# Pass the profile_name of handle you want to see the story of, as an arguement

ibt.story("python.hub")

