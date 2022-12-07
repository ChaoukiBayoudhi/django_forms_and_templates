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
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/players')
    else:
        form = PlayerForm()
    return render(request, 'index.html', {'form': form})
#show all players
def players(request):
    players = Player.objects.all()
    return render(request, 'players.html', {'players': players})

#edit player form
def edit(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'GET':
        form = PlayerForm(instance=player)
    else:
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
        return redirect('/players')
    return render(request, 'edit.html', {'form': form, 'player': player})

#delete player
def delete(request, id):
    player = Player.objects.get(id=id)
    if request.method == 'POST':
        player.delete()
        return redirect('/players')
    return render(request, 'delete.html', {'player': player})