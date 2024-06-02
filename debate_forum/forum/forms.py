from django import forms
from django.shortcuts import redirect, render
from .models import DebateTopic, ForumPost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm


@login_required # type: ignore
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('debate_list')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'forum/edit_profile.html', {'form': form})
class DebateTopicForm(forms.ModelForm):
    class Meta:
        model = DebateTopic
        fields = ['title', 'description']

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['message']

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']