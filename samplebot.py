from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer

chatbot = ChatBot('Jim',
                    logic_adapters=[
                            "chatterbot.logic.BestMatch"
                        ],
                          storage_adapter="chatterbot.storage.SQLStorageAdapter"
                        )

trainer = ListTrainer(chatbot)

doc = open('chats.txt','r').readlines()


trainer.train(doc)
while True:

    question = input('You : ')
    
      
    response = chatbot.get_response(question)
    print(response)