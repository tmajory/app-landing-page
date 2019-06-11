from django.shortcuts import render

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
    return render(request, 'home/home.html', html)

def dados(request):
    html = {
        'headTitle': "Dados - Dual Junior",
        'bodyTitle': "Uma ferramenta para lhe ajudar a poupar tempo",
        'bodySubtitle': "Já imaginou quanto tempo você gasta com trabalhos operacionais? "+
        "Imagina se você tivesse uma ferramenta que fizesse todo o serviço para você, e que "+
        "estivesse no seu compultador do escritórioe na palma de sua mão, totalmente "+
        "personalizavel e fácil de usar? Ela existe e você pode conhecê-lahoje!",
        'aboutTitle': "...",
        'aboutSubtitle': "...",
    }
    return render(request, 'home/dados.html', html)
