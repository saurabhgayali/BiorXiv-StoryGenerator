url='https://www.biorxiv.org/content/10.1101/840553v1'
import requests
import imgkit

g=requests.get(url)
text=str(g.content,'UTF-8',errors='replace')
def getheader(text):
    t=text.split('<h1 class="highwire-cite-title" id="page-title">')
    t=t[1]
    t=t.split('</h1>')
    t=t[0]
    return t
def getabstract(text):
    t=text.split('<div class="section abstract" id="abstract-1">')
    t=t[1]
    t=t.split('</div>')
    t=t[0]
    t=t.replace('<h2 class="">Abstract</h2>','')
    return t
def getauthors(text):
    t=text.split('<meta name="DC.Contributor" content="')
    #return t
    t=t[1:]
    tlist=[]
    for t1 in t:
        t1=t1.split('"')
        t1=t1[0]
        tlist.append(t1)
    return tlist
def getdoi(text):
    t=text.split('<span class="label">doi:</span>')
    t=t[1]
    t=t.split('</span>')
    return t[0]
header=getheader(text)
abstract=getabstract(text)
authors=','.join(getauthors(text))
doi=getdoi(text)

#print(','.join(authors))


html='<center><div style="width:600; text-align:justify"><center><img src="https://i.imgur.com/5bIKX2M.jpg"></center><h2>'+header+'</h2><hr><span>'+authors+'</span><hr><div><b>Abstract: </b><div style="padding:10">'+abstract+'</div></div><h4></b>'+doi+'</h4></div></center>'


html2=html.encode(encoding='UTF-8',errors='strict')
html2=html2.decode(encoding='UTF-8')
options = """{
    'format': 'png',
    'crop-h': '3',
    'crop-w': '3',
    'crop-x': '3',
    'crop-y': '3',
    'size': 600, 
    'disable-smart-width': '',
    'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ]
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}"""

#print (html)

imgkit.from_string(html2, 'story.png','')

print(html)
