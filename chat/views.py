from django.shortcuts import render
from django.http import JsonResponse,StreamingHttpResponse
from markdown import markdown
from .agent import Agent
import time 
quick = [
    "The", "night", "was", "quiet", "until", "the", "lights", "across", "the",
    "city", "suddenly", "went", "dark", "one", "building", "after", "another",
    "until", "the", "entire", "skyline", "disappeared", "into", "the", "night",
    "air", "was", "cold", "and", "the", "streets", "were", "almost", "empty",
    "but", "somewhere", "in", "the", "distance", "a", "strange", "blue", "light",
    "appeared", "above", "the", "rooftops", "slowly", "growing", "brighter",
    "as", "if", "something", "was", "coming", "through", "the", "clouds",
    "nobody", "knew", "what", "it", "was", "and", "nobody", "wanted", "to",
    "find", "out", "but", "then", "a", "voice", "came", "through", "every",
    "radio", "every", "phone", "and", "every", "speaker", "in", "the", "city",
    "saying", "only", "one", "thing", "stay", "inside", "the", "clock", "has",
    "already", "started", "counting", "backwards", "and", "there", "is", "no",
    "way", "to", "stop", "it"
]
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