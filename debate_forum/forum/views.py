from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import DebateTopic, ForumPost
from .forms import DebateTopicForm, ForumPostForm, SignUpForm # type: ignore

def debate_list(request):
    topics = DebateTopic.objects.all()
    return render(request, 'forum/debate_list.html', {'topics': topics})

def debate_detail(request, pk):
    topic = get_object_or_404(DebateTopic, pk=pk)
    posts = ForumPost.objects.filter(topic=topic)
    return render(request, 'forum/debate_detail.html', {'topic': topic, 'posts': posts})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('debate_list')
    else:
        form = SignUpForm()
    return render(request, 'forum/signup.html', {'form': form})

@login_required
def create_debate(request):
    if request.method == 'POST':
        form = DebateTopicForm(request.POST)
        if form.is_valid():
            debate = form.save(commit=False)
            debate.created_by = request.user
            debate.save()
            return redirect('debate_list')
    else:
        form = DebateTopicForm()
    return render(request, 'forum/create_debate.html', {'form': form})

@login_required
def create_post(request, pk):
    topic = get_object_or_404(DebateTopic, pk=pk)
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('debate_detail', pk=topic.pk)
    else:
        form = ForumPostForm()
    return render(request, 'forum/create_post.html', {'form': form})
