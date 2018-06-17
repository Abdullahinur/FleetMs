from django.contrib import messages
from django.http import (Http404, HttpResponse, HttpResponseRedirect,
                         JsonResponse)
from django.shortcuts import redirect, render

from .forms import EditProfile, EditSupervisor, SaccoForm, Super_listForm
from .models import Sacco, Super_list

# Create your views here.


def dashboard(request):
    '''
    View function to display all that a user will be interacting with fromm the onset of the app.
    '''
    supervisor = Super_list.objects.filter(
        sacco=Sacco.objects.get(pk=request.user.sacco.id))
    return render(request, 'sacco/all/dashboard.html', {"supervisor": supervisor})

# Supervisor section


def superlist(request):
    '''
    View function to add a new supervisor
    '''
    if request.method == 'POST':
        form = Super_listForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.sacco = Sacco.objects.get(user=request.user)
            '''
            above line of code displays a supervisor registered in a specific sacco
            '''
            user.save()
            messages.success(
                request, 'Congratulations! You have succesfully Added a new Supervisor!')
            return redirect('sacco:sacco_home')
    else:
        form = Super_listForm()
    return render(request, 'sacco/all/supervisor.html', {"form": form})


def edit_superlist(request, supervisor_id):
    '''
    View function to edit an instance of a supervisor already created
    '''
    supervisor = Super_list.objects.get(pk=supervisor_id)
    if request.method == 'POST':
        form = EditSupervisor(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Success! Your edit has been successful!')
            return redirect('sacco:sacco_home')
    else:
        form = EditSupervisor(instance=supervisor)
    return render(request, 'sacco/all/editsupervisor.html', {"form": form, "supervisor": supervisor})


def delete_supervisor(request, supervisorID):
    '''
    View function that enables one delete a given supervisor in a sacco
    '''

    Super_list.objects.filter(pk=supervisorID).delete()
    messages.error(
        request, 'Supervisor deleted!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Sacco section

def profile(request):
    profile = Sacco.objects.get(user=request.user)
    return render(request, "sacco/all/profile.html", {"profile": profile})


def edit_profile(request, sacco_id):
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES,
                           instance=Sacco.objects.get(pk=sacco_id))
        if form.is_valid():
            form.save()
            return redirect('sacco:profile')
    else:
        form = EditProfile(instance=Sacco.objects.get(pk=sacco_id))
    return render(request, 'sacco/all/editprofile.html', {"form": form})


def delete_sacco(request, saccoID):
    '''
    View function that enables one delete a given sacco
    '''
    Sacco.objects.filter(pk=saccoID).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
