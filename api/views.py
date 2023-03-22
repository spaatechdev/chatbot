from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot
import asyncio

# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create your views here.
def get_ai_message(request):
    if request.method == "POST":    
        # Give a name to the chatbot “corona bot”
        # and assign a trainer component.
        chatbot=ChatBot('corona bot')
        
        # Create a new trainer for the chatbot
        trainer = ChatterBotCorpusTrainer(chatbot)
        
        # Now let us train our bot with multiple corpus
        trainer.train("chatterbot.corpus.english.greetings",
                    "chatterbot.corpus.english.conversations" )
        # await asyncio.sleep(5)
        response = chatbot.get_response(request.POST['message'])
        print(response)
        # exit()
        return HttpResponse(response)
    else:
        return JsonResponse({
            'code': 501,
            'status': "ERROR",
            'message': "There should be ajax method."
        })