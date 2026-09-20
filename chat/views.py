from django.shortcuts import render

def start_chat(request):
    return render(request,"chat/chat.html")
