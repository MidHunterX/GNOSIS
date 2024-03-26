from django.shortcuts import render, redirect, get_object_or_404, Http404
from .models import Question , Profile , Comment , Replies
from .forms import (LoginForm ,
                    QuestionAskForm ,
                    UserRegistrationForm ,
                    ProfileUpdateForm ,
                    UserUpdateForm ,
                    QuesUpdateForm,
                    CommentForm,
                    )
from django.contrib.auth import authenticate ,logout ,login
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Google Generative AI POST Request
import requests
# Markdown Renderer
import markdown
# Fuzzy Search Logic
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# =========================== For Initial Testing =========================== #


def fuzzy_search(request):
    query = request.GET.get('q', '')
    threshold = 60

    if query:
        # Perform fuzzy search on the title field
        questions = Question.objects.all()
        results = process.extract(query, questions, scorer=fuzz.token_sort_ratio)
        fuzzy_results = [result[0] for result in results if result[1] >= threshold]
    else:
        fuzzy_results = []

    context = {
        # 'query': query,
        'ques': fuzzy_results,
    }

    return render(request , 'gnosis/ques_list.html' , context = context)


def test(request):
    return HttpResponse("Henlo you are in de APP")


def greetings(request):
    return render(request, "greetings.html", {"name": "User"})

def goodbye(request):
    username = request.GET.get('username')
    if not username:
        username = 'User'
    return render(request, 'goodbye.html', {'username': username})


# =========================== End Initial Testing =========================== #

def info(request):
    return render(request,"gnosis/info.html")

def ques_list(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        if input_text:
            # Query Database for Questions (Fuzzy Logic)
            threshold = 60
            questions = Question.objects.all()
            results = process.extract(input_text, questions, scorer=fuzz.token_sort_ratio)
            ques = [result[0] for result in results if result[1] >= threshold]

            # Query Generative AI for Answer
            # api_key = os.getenv('GOOGLE_API_KEY')
            api_key = 'AIzaSyBo_13250kxL6U9C3O5pjVa9CI0FDjLDGM'
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
            headers = {
                'Content-Type': 'application/json'
            }
            data = {
                "contents": [ { "parts": [ { "text": input_text } ] } ]
            }
            # Sending POST request
            try:
                response = requests.post(url, headers=headers, json=data)
            except requests.exceptions.RequestException:
                output_text = "You seem to be offline. To generate answers, you need internet access"
                context = {'input_text': input_text, 'output_text': output_text, 'ques': ques}
                return render(request, 'gnosis/ques_generated.html', context = context)

            # Recieve POST response
            if response.status_code == 200:
                response_json = response.json()
                output_text = response_json['candidates'][0]['content']['parts'][0]['text']
                # Markdown to HTML Convertion
                output_text = markdown.markdown(output_text)
            else:
                output_text = f"Oops, there was an Error: {response.status_code}, {response.text}"

            context = {'input_text': input_text, 'output_text': output_text, 'ques': ques}
            return render(request, 'gnosis/ques_generated.html', context = context)

    # Community Generated Question List
    ques = Question.objects.all().order_by('-id')
    context = {
        'ques' : ques
    }

    return render(request , 'gnosis/ques_list.html' , context = context)



def ques_detail(request,id):

    ques = get_object_or_404(Question,id=id)

    replies = Replies.objects.all().filter(ques = ques).order_by('-id')

    is_liked = False
    if ques.likes.filter(id = request.user.id).exists():
        is_liked = True

    is_favourite = False
    if ques.favourite_ques.filter(id=request.user.id).exists():
        is_favourite = True

    comments =  Comment.objects.all().filter(ques = ques).order_by('-id')

    if request.method == 'POST':

        if ques.restrict_comments:
            messages.success('Commenting on this post is restricted')
            return HttpResponseRedirect(reverse('gnosis:ques_detail',args = (id,)))

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('gnosis:user_login'))

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            cmnt = comment_form.save(commit=False)
            cmnt.user = request.user
            cmnt.ques = ques
            cmnt.save()
            return HttpResponseRedirect(reverse('gnosis:ques_detail',args = (id,)))
    else:
        comment_form  = CommentForm()

    context = {
        'q': ques,
        'is_liked' : is_liked,
        'is_favourite' : is_favourite,
        'likes_count' : ques.likes.count() ,
        'comments' : comments,
        'comment_form' : comment_form ,
        'replies' : replies,
    }

    return render(request, 'gnosis/ques_detail.html', context=context)



def ques_likes(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    ques = get_object_or_404(Question,id = request.POST.get('q_id'))

    if ques.likes.filter(id = request.user.id).exists():
        ques.likes.remove(request.user)
    else:
        ques.likes.add(request.user)

    return HttpResponseRedirect(reverse('gnosis:ques_detail',args=(request.POST.get('q_id'),)))



def ques_fav(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    ques = get_object_or_404(Question,id = request.POST.get('q_id'))

    if ques.favourite_ques.filter(id = request.user.id).exists():
        ques.favourite_ques.remove(request.user)
    else:
        ques.favourite_ques.add(request.user)

    return HttpResponseRedirect(reverse('gnosis:ques_detail',args=(request.POST.get('q_id'),)))



def show_fav_ques(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    questions = request.user.favourite_ques.all().order_by('-id')
    context = {
        'questions' : questions,
    }
    return render(request,'gnosis/favourites.html',context)

def comment_reply(request,id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    text = request.POST.get('text')

    if len(text)==0:
        messages.success(request,'TextField is empty')
        return HttpResponseRedirect(reverse('gnosis:ques_detail', args=(id,)))

    ques = get_object_or_404(Question, id=id)

    comment_id = request.POST.get('comment_id')
    comment = Comment.objects.filter(id=comment_id).first()
    Replies.objects.create(ques = ques,comment=comment,user = request.user,content =text)

    return HttpResponseRedirect(reverse('gnosis:ques_detail',args=(id,)))



def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:ques_list'))

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user:

                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('gnosis:ques_list'))
                else:
                    return HttpResponse('User is not Active')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()

    context = {
        'form' : form
    }

    return render(request ,'gnosis/login.html' ,context )



@login_required()
def user_logout(request):
    username = request.user.first_name + " " + request.user.last_name
    logout(request)
    return HttpResponseRedirect(reverse('gnosis:goodbye') + f'?username={username}')
    # return HttpResponseRedirect(reverse('gnosis:ques_list'))



def register(request):

    if request.user.is_authenticated:
        return HttpResponse('First logout')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user = user)
            return HttpResponseRedirect(reverse('gnosis:user_login'))
    else:
        form = UserRegistrationForm()

    context = {
        'form' : form
    }

    return render(request , 'gnosis/register.html',context)



def edit_profile(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST , instance=request.user )
        profile_form = ProfileUpdateForm(request.POST ,
                            instance=request.user.profile,files =request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return HttpResponseRedirect(reverse('gnosis:profilepage',args=(request.user.username,)))

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form' : user_form,
        'profile_form' : profile_form,
    }

    return render(request,'gnosis/edit_profile.html',context)



def profilepage(request,username):
    user = User.objects.get(username=username)
    questions = Question.objects.filter(author=user)
    profile = Profile.objects.all()
    context = {
        'questions': questions,
        'profile' : profile,
        'user':user,
    }

    return render(request,'gnosis/profilepage.html',context)



@login_required()
def ask_question(request):

    if request.method == 'POST':
        form = QuestionAskForm(request.POST)

        if form.is_valid():
            ques = form.save(commit=False)
            ques.author = request.user
            ques.save()

            return HttpResponseRedirect(reverse('gnosis:ques_list'))
    else:
        form = QuestionAskForm()

    context = {
        'form' : form
    }

    return render(request , 'gnosis/ask_question.html',context)



@login_required()
def update_ques(request,id):

    ques = get_object_or_404(Question,id=id)
    print(ques.author)

    if ques.author != request.user:
        return Http404()

    if request.method == 'POST':
        form = QuesUpdateForm(request.POST,instance=ques)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('gnosis:ques_detail',args=(id,)))
    else:
        form = QuesUpdateForm(instance=ques)

    context = {
        'form' : form ,
        'ques' : ques ,
    }

    return render(request ,'gnosis/update_ques.html',context)



def delete_ques(request,id):

    ques = get_object_or_404(Question,id=id)

    if ques.author != request.user:
        return Http404()

    if request.method =='POST':
        ques.delete()
        return HttpResponseRedirect(reverse('gnosis:ques_list'))

    context = {
        'ques' : ques
    }



def delete_comment(request,id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    cmnt_id = request.POST.get('comment_id')
    cmnt = get_object_or_404(Comment,id=cmnt_id)

    if cmnt.user != request.user:
        return Http404()
    cmnt.delete()
    return HttpResponseRedirect(reverse('gnosis:ques_detail', args=(id,)))



def delete_reply(request, id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('gnosis:user_login'))

    reply_id = request.POST.get('reply_id')
    reply = get_object_or_404(Replies, id=reply_id)

    if reply.user != request.user:
        return Http404()
    reply.delete()
    return HttpResponseRedirect(reverse('gnosis:ques_detail', args=(id,)))

