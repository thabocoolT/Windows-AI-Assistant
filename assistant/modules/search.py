import webbrowser

def search_google(query):
    url = "https://google.com/search?q=" + query.replace(" ", "+")
    webbrowser.open(url)
    return True

def open_youtube(query):
    url = "https://youtube.com/search?search_query=" + query.replace(" ", "+")
    webbrowser.open(url)
    return True