from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from acorta.models import Urls
from django.http import HttpResponseRedirect

# Create your views here.
FORMULARIO= """
<form action="" method="POST" target="_blank">
    Introduce una url para acortarla:
    <input type="text" name="url"/>
    <input type="submit" value="Enviar"/>
</form>"""

@csrf_exempt
def acortar(request):
    urls_list = Urls.objects.all()
    if request.method == 'GET':
        resp = "<h4>Programa para acortar las urls:</h4>"
        resp += FORMULARIO
        if len(urls_list) == 0:
            resp += "<br>En este momento, <b>no hay ninguna url</b>"
        else:
            resp += "<br><b>Las urls que tengo son:</b>"
            for url in urls_list:
                url_acortada = "http://localhost:8000/" + str(url.id)
                resp += ("<br>URL original:  <a href=" + url.url_original  + ">" + url.url_original + "</a>"
                         "<br> URL acortada :<a href=" + url_acortada + ">" + url_acortada + "</a>" + "<br>")                       
    elif request.method == 'POST':
        url_original = request.POST['url']
        if (url_original[0:8] != "https://" and url_original[0:7] != "http://"):
            url_original = "http://" + url_original
        try: #cuando ya tienes la url
            url_acortada = Urls.objects.get(url_original=url_original)
        except Urls.DoesNotExist: #cuando no tienes la url
            url = Urls(url_original=url_original)
            url.save()
            url_acortada = Urls.objects.get(url_original=url_original)
        url_acortada = "http://localhost:8000/" + str(url_acortada.id)
        resp = ("<a href=" + url_acortada + ">" + url_acortada + "</a>")
    else:
        resp = "Method Not Allowed"
    return HttpResponse(resp)

def redirigirse(request, id):
    try:
        url_original = Urls.objects.get(id=id).url_original
        return HttpResponseRedirect(url_original)
    except Urls.DoesNotExist:
        return HttpResponse("<p><h3>No existe esa url</h3></p>")

def error(request):
    return HttpResponse('<h3>La url que ha introducido es incorrecta<h3>')
