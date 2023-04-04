from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import asyncio
import os
import openai
import requests
import json


# Create your views here.
def get_ai_message(request):
    if request.method == "POST":
        ## request.POST['message']
        url = 'https://api.openai.com/v1/completions'
        formData = {
            'model': 'text-davinci-003',
            'prompt': 'Write a poem of donkey',
            'max_tokens': 1000,
            'temperature': 0
        }
        x = requests.post(url, data=json.dumps(formData), headers={
                          "Content-Type": "application/json", "Authorization": "Bearer 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"})
        print(x.text)
        exit()
        return HttpResponse(response)
    else:
        return JsonResponse({
            'code': 501,
            'status': "ERROR",
            'message': "There should be ajax method."
        })
