from django.shortcuts import render
from django.http import JsonResponse


def start_chat(request):
    if request.method == "POST":
        reply = request.POST.get("reply", "empty")
        print("replies",reply)
        return JsonResponse({
            "message": f"Django received: {reply}" 
        })
   
    return render(request,"chat/chat.html")
