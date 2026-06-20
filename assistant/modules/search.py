import webbrowser

def search_google(query):
    url=(
        "https://google.com/search?q="
        +
        query
    )

    webbrowser.open(

        url
    )

    return True