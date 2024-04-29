from django import forms
from .models import Question , Profile , Comment , Replies
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Row, Column, Submit, Reset
from crispy_forms.bootstrap import PrependedText


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label = "Password" , widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    DOB = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    photo = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'DOB', 'photo']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password': 'Password',
            'confirm_password': 'Confirm Password',
            'DOB': 'Date of Birth',
            'photo': 'Profile Picture'
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            PrependedText('username', '@', placeholder='user_name'),
            Row(
                Column('password', css_class='form-group col'),
                Column('confirm_password', css_class='form-group col'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col'),
                Column('last_name', css_class='form-group col'),
                css_class='form-row'
            ),
            'email',
            'DOB',
            'photo',
            Submit('submit', 'Register', css_class='btn btn-primary'),
            Reset('reset', 'Reset', css_class='btn btn-secondary'),
        )

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
    DOB = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Profile
        fields = ['DOB','photo']


class QuestionAskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'department', 'language', 'preferred_ans', 'restrict_comments']
        labels = {
            'title': 'Title',
            'body': 'Body',
            'department': 'Department',
            'language': 'Preferred Language',
            'preferred_ans': 'Preferred Answer Type',
            'restrict_comments': 'Restrict Comments',
        }


class QuesUpdateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'department', 'language', 'preferred_ans', 'restrict_comments']
        labels = {
            'title': 'Title',
            'body': 'Body',
            'department': 'Department',
            'language': 'Preferred Language',
            'preferred_ans': 'Preferred Answer Type',
            'restrict_comments': 'Restrict Comments',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'photo', 'video', 'audio']
        labels = {'content': '' }
        widgets = {
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
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
