from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from django.urls import reverse

from .models import Article, Comment
from users.models import CustomUser


def index(request):
	latest_articles_list = Article.objects.order_by('-pub_date')[:5]

	return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		raise Http404("Статья не найдена !")



	latest_comment_list = a.comment_set.order_by('-id')[:10]

	return render(request, 'articles/detail.html', {'article': a, 'latest_comment_list': latest_comment_list})

def leave_comment(request, article_id):
	
	if not request.user.is_authenticated:

		return redirect('login')
		
	else:
		try:
			a = Article.objects.get( id = article_id )
		except:
			raise Http404("Статья не найдена !")

		a.comment_set.create(author_name = request.user, comment_text = request.POST['text'])	

		return HttpResponseRedirect( reverse('articles:detail', args =(a.id, )) )



# class LeaveComment (LoginRequiredMixin, CreateView):
# 	model = Comment
# 	template_name = 'articles/detail.html'
# 	fields = ('comment_text', 'article')
# 	login_url = 'login' 
# _____________________________________________________________________________
# def form_valid(form):
# 	form.instance.author = request.user
# 	return super().form_valid(form)

# ________________________________________________________________________
