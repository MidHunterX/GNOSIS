from django import forms
from .models import Question , Profile , Comment , Replies
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email'
                  ,'password','confirm_password']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('Password Mismatch')
        else:
            return confirm_password


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['DOB','photo']


class QuestionAskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title' , 'body', 'department', 'language', 'restrict_comments']


class QuesUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title' , 'body', 'department', 'language', 'restrict_comments']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'video', 'audio']
        labels = {'content': '' }
        widgets = {
            'audio': forms.FileInput(attrs={'accept': 'audio/*'}),
            'video': forms.FileInput(attrs={'accept': 'video/*'}),
        }

    def clean_video(self):
        video = self.cleaned_data.get('video')
        if video:
            if not video.name.endswith(('.mp4', '.avi', '.mov')):
                raise forms.ValidationError('Invalid video file format. Supported formats: .mp4, .avi, .mov')
        return video

    def clean_audio(self):
        audio = self.cleaned_data.get('audio')
        if audio:
            if not audio.name.endswith(('.mp3', '.wav', '.ogg')):
                raise forms.ValidationError('Invalid audio file format. Supported formats: .mp3, .wav, .ogg')
        return audio
