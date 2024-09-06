import requests
#import pip
#pip.main(['install','pyqt6']) 

def shorten_url(url):
    api_url = 'https://is.gd/create.php?format=simple&url='
    response = requests.get(api_url + url)
    return response.text
