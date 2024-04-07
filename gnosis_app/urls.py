from django.urls import path
from . import responses

# Namespace
app_name = 'gnosis'

# URL Patterns
urlpatterns = [
    path("test/", responses.test),
    path("", responses.greetings, name="greetings"),
    path('goodbye/',responses.goodbye,name = 'goodbye'),
    path('info/',responses.info,name = 'info'),

    path('home/',responses.ques_list,name = 'ques_list'),
    path('ques/<int:id>/',responses.ques_detail,name='ques_detail'),
    path('login/',responses.user_login,name = 'user_login'),
    path('logout/',responses.user_logout ,name = 'user_logout'),
    path('register/',responses.register,name = 'register'),
    path('edit_profile/',responses.edit_profile , name = 'edit_profile'),
    path("uploader_form/", responses.uploader_form, name = 'uploader_form'),
    path('ask_question/',responses.ask_question,name = 'ask_question'),
    path('update_ques/<int:id>/',responses.update_ques ,name = 'update_ques'),
    path('delete_ques/<int:id>/', responses.delete_ques, name='delete_ques'),
    path('likes/',responses.ques_likes,name ='ques_likes'),
    path('comment_reply/<int:id>',responses.comment_reply,name = 'comment_reply'),
    path('profilepage/<str:username>/',responses.profilepage,name='profilepage'),
    path('delete_comment/<int:id>',responses.delete_comment,name='delete_comment'),
    path('delete_reply/<int:id>', responses.delete_reply, name='delete_reply'),
    path('ques_fav/',responses.ques_fav,name='ques_fav'),
    path('show_fav_ques/',responses.show_fav_ques,name='show_fav_ques'),
]
