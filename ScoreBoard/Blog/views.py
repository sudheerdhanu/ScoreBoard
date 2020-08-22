from django.http import HttpResponse
from django.shortcuts import render, redirect
from Blog.form import PlayersForm, TeamForm, MatchFixForm, ScoreBoardForm

# Create your views here.
from Blog.models import Team, Player


def get_player_id():
    count=Player.objects.all().count()
    return count+1

def get_team_id():
    count=Team.objects.all().count()
    return count+1
# get points of team



def main_page(request):
    return render(request,'home.html')
# create Team

def create_team(request):
    form=TeamForm()
    if request.method=="POST":
        form=TeamForm(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            identifier=get_team_id()
            obj.identifier=identifier+1
            obj.save()
            return redirect('get_team_list')
    return render(request,'create_team.html',{'form':form})


# get team list

def get_team_list(request):
    list_team=Team.objects.all()
    return render(request,'total_team_list.html',{'list':list_team})


# get deatiled team with players

def team_detail(request,id):
    # list_team = Team.objects.filter(identifier=id).select_related('team')
    players=Player.objects.filter(team_id=id).select_related('team')

    return render(request, 'players_list.html', {'players': players})

#creating players

def create_player(request):
    form=PlayersForm()
    if request.method=="POST":
        form=PlayersForm(request.POST, request.FILES)
        print(request.POST)
        try:
            if form.is_valid():
                obj=form.save(commit=False)
                identifier = get_player_id()
                obj.identifier = identifier + 1
                obj.save()
                return redirect('get_team_list')
                # return HttpResponse('ok')
        except Exception as e:
            return HttpResponse(e)


    return render(request,'create_player.html',{'form':form})

def fix_match(request):
    form=MatchFixForm()
    if request.method=='POST':
        form=MatchFixForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('score')
    return render(request,'fix_match.html',{'form':form})

def score(request):
    form=ScoreBoardForm()
    if request.method=="POST":
        form=ScoreBoardForm(request.POST,request.FILES)
        if form.is_valid():
            won=form.save(commit=True)
            t=Team.objects.get(name=won)
            p=t.points
            if p is None:
                t.points=1
            else:
                t.points=p+1
            t.save()

            list=Team.objects.all()
            return redirect('get_team_list')



    return render(request,'score.html',{'form':form})