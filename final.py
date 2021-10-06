import speech_recognition as sr
import os
import datetime 
import warnings
import wikipedia
import random
import wolframalpha
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from playsound import playsound
from gtts import gTTS
import random
import spacy
import time
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from googlesearchnew import search



nlp = spacy.load('en_core_web_sm')
num = 0

class Assistant():
    def __init__(self,name):
        self.name = name
        self.speak(f'Hello Human You can activate me by saying "Hello {self.name}"')

    # def greetings(self,voice_data):
       
    #     greet_responses = ['whats up' , 'howdy' , 'hey' , 'welcome']
    #     if voice_data in greet_words:
    #         self.speak(random.choice(greet_responses))

    #     return 

    def record_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            r.dynamic_energy_threshold = True 
            
            self.speak('Say something')
            user_voice = r.listen(source,timeout=3)
        voice_data = ''
        try:
            voice_data = r.recognize_google(user_voice)
            print(voice_data)
        except Exception:
            self.speak('Sorry I couldnt get that')

        return voice_data

    def speak(self,voice_data):
        global num
        num += 1
        print(voice_data)
        tts = gTTS(text=voice_data , lang='en-IN')
        audio_file = 'audio'+str(num)+'.mp3'
        tts.save(audio_file)
        playsound(audio_file)        
        os.remove(audio_file)
        return

    def surf_web(self,voice_data):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chromedriver = 'chromedriver.exe'
        
        driver = webdriver.Chrome(chromedriver , chrome_options=chrome_options)
        #driver.implicitly_wait(1)
        driver.maximize_window()

          
        if 'youtube' in voice_data:
            self.speak('Opening Youtube')
            wait = WebDriverWait(driver, 3)
            presence = EC.presence_of_element_located
            visible = EC.visibility_of_element_located
            index = voice_data.split().index('youtube')
            query = voice_data.split()[index+1:]
            driver.get("http://www.youtube.com/results?search_query=" + ' '.join(query))
            wait.until(visible((By.ID, "video-title")))
            driver.find_element_by_id("video-title").click()
            
            
            return 
        
        elif 'google' in voice_data:
            self.speak('Opening google')
            index = voice_data.split().index('google')
            query = voice_data.split()[index+1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))
            #driver.get("http://www.google.com/search?q=" + 'oxygen benefits')
            res = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div')
            # print(driver.find_element_by_class_name('hgKE1c'))
            ans = res.text.split('.')
            #print(ans)
            for i in range(2):
                print(ans[i],end='.')
            return 

        elif 'wikipedia' in voice_data:
            self.speak('Opening wikipedia')
            index = voice_data.split().index('wikipedia')
            query = voice_data.split()[index+1:]
            driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
            return 
        else:
           
           return 
        
    def calculate(self,voice_data):
        app_id = 'RG368L-GXQ8R3H6VQ'
        client = wolframalpha.Client(app_id)
        index = voice_data.split().index('calculate')
        query = voice_data.split()[index+1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        self.speak('The answer is ' + answer)
        return    



    def process_text(self,text):

        if 'youtube' in text or 'google' in text or 'wikipedia' in text:
            self.surf_web(text)
            return
         
        elif 'calculate' in text:
            self.calculate(text)
            return

        else:
            print('yes')
            chatbot = ChatBot('Bob',
                                logic_adapters=[
                                        "chatterbot.logic.BestMatch"
                                    ],
                                    
                                    )

            trainer = ListTrainer(chatbot)

            doc = open('chats.txt','r').readlines()


            trainer.train(doc)
            print('yes')

                
            response = str(chatbot.get_response(text))
            
            assistant.speak(response)
            return
            
          

    
assistant = Assistant('lucy')

   


sentence = assistant.record_audio().lower()
# sentence = nlp(text) 
# ner = {}
# ner_list = []
if f'hello {assistant.name}' in sentence:

    assistant.speak('Greetings')
    print('Assistant activated... You can now use various features like surfing the web or calculations or just a convo.')
    print('Say "help" to get deatiled info.')
    while True:
        #assistant.process_text('google oxygen benefits')
        text = assistant.record_audio().lower()
        if text == 'help':
            print('''        1. Say Search Youtube/Google/Wikipedia to surf the web.
            2. Say calculate to carry out various mathematical and scientific calculations.
            3. Chitchat all you want.
            4. Say exit/bye/quit to turn off''')
        elif 'exit' in text or 'quit' in text or 'bye' in text:
            
            break
        
        elif 'and' in text:
            queries = text.split('and')
            for query in queries:
                assistant.process_text(query)
        
        else:
            
            # for ent in sentence.ents:
        #     if ent.label_ == 'GPE' or ent.label_ == 'DATE':
        #         #ner[ent.label_] = ent.text
        #         ner_list.insert(0,ent.text)
            
            assistant.process_text(text)