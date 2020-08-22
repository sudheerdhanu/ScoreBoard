from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from Blog.views import main_page,create_player,create_team,get_team_list,team_detail,fix_match,score
urlpatterns = [
    path('', main_page,name='main_page'),
    path('create_team/', create_team,name='create_team'),
    path('get_team_list/', get_team_list,name='get_team_list'),
    path('team_detail/(?P<id>\d+)/$',team_detail , name='team_detail'),
    path('create_player/', create_player,name='create_player'),
    path('fix_match/', fix_match,name='fix_match'),
    path('score/', score,name='score'),
]