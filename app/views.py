from django.shortcuts import render
from google import genai
from django.conf import settings
from .forms import ContentForm
import os
from dotenv import load_dotenv
load_dotenv()

def generate_content(request):
    generated_content = None
    
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['query']

            client = genai.Client(api_key=os.environ.get('API_KEY'))

            response = client.models.generate_content(model="gemini-2.0-flash",contents=prompt)

            generated_content = response.text
    
    else:
        form = ContentForm()
    
    return render(request, 'generator.html', {
        'form': form,
        'content': generated_content
    })



