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
        'headTitle': "Gestão de Dados - Dual Junior",
        'bodyTitle': "Uma ferramenta para lhe ajudar a poupar tempo",
        'bodySubtitle': "Acesse seus dados de maneira mais rápida sem uso de planilhas "+
        "e papéis que gastam seu tempo na hora de tomar suas decisões e utilize agora uma"+
        " ferramenta ERP (Planejamento de Recursos Empresariais) para solucionar seus problemas."+
        " Garanta de forma segura e automatizada a integração e realimentação do seu banco de dados"+
        " com uma única ferramenta acessível e personalizável, dando previsões para alavancar seu "+
        "crescimento!!",
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