from django.shortcuts import render
from models import Article
from models import Content, Image, Contributor 

# Create your views here.

def home(request): 
	texts = Article.objects.all() 
	info = {'texts': texts}
	return render(request, 'home.html', info)

def extra(request, articleid):
	random = get_object_or_404(Article, pk=articleid)
	info = {'random': random}
	return render(request, 'extra.html', info)
