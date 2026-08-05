import webbrowser
import urllib.parse


sites = {
"google" : "https://google.com",
"youtube" : "https://youtube.com",
"linkden" : "https://www.linkedin.com/feed/",
"instagram" : "https://instagram.com",
"tiktok" : "https://tiktok.com",
"whatsapp" : "https://web.whatsapp.com/",
"chatgpt" : "https://chatgpt.com/",
"claude" : "https://claude.ai/new",
"gemini" : "https://gemini.google.com/app",
"github" : "https://github.com/",
"canva"  : "https://www.canva.com/"
}


def search_google(query):
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)
    return

def search_youtube(query):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote_plus(query)
    webbrowser.open(url)
    return


