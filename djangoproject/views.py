from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .filter import UserFilter
from .filter2 import UserFilter2
import json
import markdown2
import bleach
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question,Answer
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/index.html', context)
def index(request):
    context_index = {}
    context_index['questions'] = Question.objects.all()
    return render(request, 'djangoproject/base.html', context_index)

def askquestion(request):
    if request.method == 'POST':
        try:
            title = request.POST.get('title')
            question = request.POST.get('question')
            posted_by = request.POST.get('posted_by')
            q = Question(question_title=title, question_text=question, posted_by=posted_by)
            q.save()
        except Exception as e:
            return render(request, 'ask_question.html', {'error': 'Something is wrong with the form!'})
    else:

        return render(request, 'djangoproject/ask_question.html', {})

def viewquestion(request, qid, qslug):
    context = {}
    question = Question.objects.get(qid=qid, slug=qslug)

    # assuming obj is a model instance
    question_json = json.loads(serializers.serialize('json', [ question ]))[0]['fields']
    question_json['date_posted'] = question.date_posted
    question_json['qid'] = question.qid
    question_json['question_text'] = bleach.clean(markdown2.markdown(question_json['question_text']), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
    context['question'] = question_json
    context['answers'] = []
    answers = Answer.objects.filter(qid=qid)
    for answer in answers:
        answer.answer_text = bleach.clean(markdown2.markdown(answer.answer_text), tags=['p', 'pre','code', 'sup', 'strong', 'hr', 'sub', 'a'])
        context['answers'].append(answer)
    return render(request, 'djangoproject/view-question.html', context)




def about(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/about.html', context)

def Skills(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'djangoproject/test_skills.html', context)

def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter2(request.GET, queryset=user_list)
    return render(request, 'djangoproject/search_box.html', {'filter': user_filter})


def search_review(request):
    context = {
        'posts': Post.objects.all()
    }
    user_filter = UserFilter(request.GET, queryset=context)
    return render(request, 'djangoproject/search_box_2.html', {'filter': user_filter})

def Team(request):
    context={
        'posts':Post.objects.all()

    }
    return render(request,'djangoproject/team.html',context)



class PostListView(ListView):
    model = Post
    template_name = 'djangoproject/index.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'djangoproject/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')





class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['instructor', 'rating','comments','institute','course','department','agree_condition']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['rating','comments']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def about(request):
    return render(request, 'djangoproject/about.html', {'title': 'About'})