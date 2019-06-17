from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import PlusOne


def home(request):
    html = {
        'headTitle': "Home - Dual Junior",
        'bodyTitle': "Minimizando custos, Maximizando Lucros",
        'bodySubtitle': "O que desejamos para nossos clientes é que tenham a "+
        "possibilidade de alavancar seus negócios com a redução dos desperdícios "+
        "de recursos e tempo.",
        'aboutTitle': "Nós temos exatamente o que você precisa.",
        'aboutSubtitle': "Disponibilizamos de embasamento matemático e ajuda dos "+
        "professores da UFC para trazer aos nossos clientes o melhor produto que ele "+
        "pode encontrar no mercado!",
    }
    return render(request, 'home.html', html)

def dados(request):
    html = {
        'headTitle': "Dados - Dual Junior",
        'bodyTitle': "Uma ferramenta para lhe ajudar a poupar tempo",
        'bodySubtitle': "Já imaginou quanto tempo você gasta com trabalhos operacionais? "+
        "Imagina se você tivesse uma ferramenta que fizesse todo o serviço para você, e que "+
        "estivesse no seu compultador do escritórioe na palma de sua mão, totalmente "+
        "personalizavel e fácil de usar? Ela existe e você pode conhecê-lahoje!",
        'aboutTitle': "Deu certo",
        'aboutSubtitle': "Tais a ver como é facil...",
        'respondido': request.COOKIES.get("respondido")
    }
    return render(request, 'dados.html', html)

def submit(request):
    
    response = HttpResponseRedirect("/dados/#about")
    print(request.POST)

    one = PlusOne(
        choice=request.POST['choice'], 
        email=request.POST['email'], 
        feedback=request.POST['feedback']
    )
    one.save()
    response.set_cookie("respondido", True)
    return response