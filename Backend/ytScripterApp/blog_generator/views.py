from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import json
from pytube import YouTube
import os
# import assemblyai as aai
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import re
from .models import BlogPost




# Create your views here.


@login_required
def index(request):
    return render(request, 'index.html')
    # pass


@csrf_exempt
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['link']
            # print(yt_link)
            # return JsonResponse({'content':yt_link})
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data sent'}, status=400)

        # get yt title
        id = yt_id(yt_link)
        

        # get transcript
        transcription = get_transcription(id)
        if not transcription:
            return JsonResponse({'error': 'failed to get transcript'})

        # use Gemini to generate the blog
        title, blog_content = generate_blog_from_transcription(transcription)
        if not blog_content:
            return JsonResponse({'error': "Failed to generate blog article"}, status=500)
        # save blog article
        new_blog_article = BlogPost.objects.create(
            user= request.user,
            youtube_title= title,
            youtube_link= yt_link,
            generated_content = blog_content,            
        )
        # return blog article as response
        return JsonResponse({'content': blog_content})
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)


def yt_id(link):
    video_id = re.search(r'v=([a-zA-Z0-9_-]+)', link).group(1)
    return video_id


def get_transcription(ID):
    scri = YouTubeTranscriptApi.get_transcript(ID)
    transcribed_text = " ".join([item['text'] for item in scri])
    return transcribed_text


def generate_blog_from_transcription(transcription):
    genai.configure(api_key="AIzaSyA7IaGbDNXhVh2QGB37xB0A_q9pPCw8eKU")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Based on the following transcript from a YouTube video, write a comprehensive blog article, write it based on the transcript, but dont make it look like a youtube video, make it look like a proper blog article within 100 words:\n\n{transcription}\n\nArticle:")
    parts = response.text.split('\n', 1)  # Split into two parts at the first newline
    title = parts[0].strip(' *')  # Remove any surrounding '*' and whitespace from the title
    passage = parts[1].strip() if len(parts) > 1 else ""  # Handle cases where passage may be absent
    return title, passage


def blog_list(request):
    blog_articles = BlogPost.objects.filter(user = request.user) 
    return render(request,'allblogs.html', {'blog_articles':blog_articles})


def blog_details(request,pk):
    blog_article_detail = BlogPost.objects.get(id=pk)
    if request.user == blog_article_detail.user:
        return render(request, 'blogdetails.html', {'blog_article_detail': blog_article_detail})
    else:
        redirect('/')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = "Invalid Password or Username"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')


def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repeatPassword = request.POST['repeatPassword']

        if password == repeatPassword:
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
                login(request, user)
                return redirect('/')
            except:
                error_message = "Error creating account"
                return (request, 'signup.html', {'error_message': error_message})

        else:
            error_message = "Passwords Dont Match"
            return (request, 'signup.html', {'error_message': error_message})

    return render(request, 'signup.html')


def user_logout(request):
    logout(request)
    return redirect('/')
