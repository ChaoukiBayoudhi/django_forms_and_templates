from django.shortcuts import redirect, render

from player_app.forms import PlayerForm
from player_app.models import Player

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

#get one player via form
def player(request):
        context={}
    #if request.method == 'POST':
        form = PlayerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/players/list',{'players',Player.objects.all()})
    #else:
     #   form = PlayerForm()
        context['form'] = form
        return render(request, 'create.html', {'form': form})
#show all players
def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})

    # dictionary for initial data with
    # field names as keys
   #context ={}
    # add the dictionary during initialization
    #context["palyers"] = Player.objects.all()

    #return render(request, 'players.html', context)
    

#update player form
def edit(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'GET':
        form = PlayerForm(instance=player)
    else:
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
        return redirect('/list')
    return render(request, 'edit.html', {'form': form, 'player': player})

#delete player
def delete(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'POST':
        player.delete()
        return redirect('/players/list')
    return render(request, 'delete.html', {'player': player})