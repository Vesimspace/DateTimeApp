from django.shortcuts import render

def get_html_content(request):
    import requests
    country = request.GET.get('country')
    country = country.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_content = session.get(f'https://www.timeanddate.com/worldclock/{country}').text
    return html_content
   

def home(request):
    result = None
    if 'country' in request.GET:
        html_content = get_html_content(request)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        result = dict()
        result['region'] = soup.find("span", attrs={"id": "ct"}).text
        result['temp_now'] = soup.find("span", attrs={"id": "ctdat"}).text
        print(result)
    return render(request, 'main/home.html', {'result': result})

