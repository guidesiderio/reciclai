from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Residue, Collection, Reward, Profile, UserReward
from .forms import CollectionStatusForm

def index(request):
    return render(request, 'core/index.html')

# Views do Cidadão

@login_required
def residue_create(request):
    # Lógica para criar resíduo
    return HttpResponse("<h1>Cidadão: Cadastrar Resíduo</h1>")

@login_required
def collection_request(request):
    # Lógica para solicitar coleta
    return HttpResponse("<h1>Cidadão: Solicitar Coleta</h1>")

@login_required
def collection_status(request):
    # Lógica para acompanhar o status da coleta
    return HttpResponse("<h1>Cidadão: Acompanhar Status da Coleta</h1>")

@login_required
def points_view(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'core/points_view.html', {'profile': profile})

@login_required
def rewards_list(request):
    rewards = Reward.objects.all()
    return render(request, 'core/rewards_list.html', {'rewards': rewards})

@login_required
def redeem_reward(request, reward_id):
    reward = get_object_or_404(Reward, id=reward_id)
    profile = Profile.objects.get(user=request.user)
    if profile.points >= reward.points_required:
        profile.points -= reward.points_required
        profile.save()
        UserReward.objects.create(user=request.user, reward=reward)
        return redirect('core:rewards_list')
    else:
        return HttpResponse("<h1>Você não tem pontos suficientes para resgatar esta recompensa.</h1>")

# Views do Coletor

@login_required
def available_collections(request):
    # Lógica para visualizar coletas disponíveis
    return HttpResponse("<h1>Coletor: Coletas Disponíveis</h1>")

@login_required
def accept_collection(request, collection_id):
    # Lógica para aceitar coleta
    return HttpResponse(f"<h1>Coletor: Aceitar Coleta {collection_id}</h1>")

@login_required
def update_collection_status(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    if request.method == 'POST':
        form = CollectionStatusForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect('core:available_collections')
    else:
        form = CollectionStatusForm(instance=collection)
    return render(request, 'core/update_collection_status.html', {'form': form, 'collection': collection})


# Views da Recicladora

@login_required
def recycler_received(request):
    # Lógica para visualizar resíduos recebidos
    return HttpResponse("<h1>Recicladora: Resíduos Recebidos</h1>")

@login_required
def recycler_process(request, residue_id):
    residue = get_object_or_404(Residue, id=residue_id)
    profile = Profile.objects.get(user=residue.citizen)
    profile.points += 10
    profile.save()
    residue.status = 'F'
    residue.save()
    return redirect('core:recycler_received')
