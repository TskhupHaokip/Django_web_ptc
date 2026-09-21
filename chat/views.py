from django.shortcuts import render
from django.http import JsonResponse,StreamingHttpResponse
from markdown import markdown
from .agent import Agent

agent = Agent()

def start_chat(request):
    if request.method == "POST":
        reply = request.POST.get("reply", "")

        if not reply:
            return StreamingHttpResponse([b"Error: empty message"], status=400)
    
        def stream()  :
            for item in agent.stream(reply):
                if item is not None:
                    # Convert string to bytes
                    yield str(item).encode("utf-8")
            
        return StreamingHttpResponse(
            stream(),
            content_type="text/plain"
        )

    return render(request, "chat/chat.html")