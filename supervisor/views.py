from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import SupervisorForm,DriverForm,ConductorForm
from .models import Supervisor,Driver,Conductor
# Create your views here.


def home(request):
    return render(request, 'supervisor/dashboard/index.html')

def editSupervisor(request):
	'''
	Edit a created supervisor
	'''
	if request.method == 'POST':
		form = SupervisorForm(request.POST,instance = Supervisor.objects.get(id = request.user.supervisor.id))
		if form.is_valid():
			form.save()
			messages.success(request, f'Success! Your edit has been successful!')
			return redirect('sup:dashboard')
	
	else:
		form = SupervisorForm(instance = Supervisor.objects.get(id = request.user.supervisor.id))
		return render(request,'supervisor/dashboard/edit.html',{"form":form})


def createDriver(request):
	'''
	Create Driver crew member
	'''
	if request.method == 'POST':
		form = DriverForm(request.POST)
		if form.is_valid():
			driver = form.save(commit = False)
			driver.sacco = request.user.supervisor.sacco_base
			driver.save()
			messages.success(request,'Success! Driver Crew member succesfully created!')
			return redirect('sup:allDrivers')
	else:
		form = DriverForm()
		return render(request, 'supervisor/crew/createDriver.html',{"form":form})


def editDriver(request,driverId):
	'''
	Edit driver instance
	'''
	if request.method == 'POST':
		form = DriverForm(request.POST,instance = Driver.objects.get(id = driverId))
		if form.is_valid():
			form.save()
			messages.success(request,'Success! Driver Crew member succesfully edited!')
			return redirect('sup:allDrivers')
	else:
		form = DriverForm(instance = Driver.objects.get(id = driverId))
		driver = Driver.objects.get(pk = driverId)
		return render(request, 'supervisor/crew/editDriver.html',{"form":form,"driver":driver})

def allDrivers(request):
	'''
	View all Driver instances
	'''
	drivers = Driver.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request,'supervisor/crew/allDrivers.html',{"drivers":drivers})

def deleteDriver(request,driverId):
	'''
	Delete a driver instance
	'''
	Driver.objects.filter(pk = driverId).delete()
	messages.info(request,'Succesfully delete a driver')
	return redirect('sup:allDrivers')

def createConductor(request):
	'''
	Create conductor instance
	'''
	if request.method == 'POST':
		form = ConductorForm(request.POST)
		if form.is_valid():
			conductor = form.save(commit = False)
			conductor.sacco = request.user.supervisor.sacco_base
			conductor.save()
			messages.success(request,'Success! Created a conductor crew member')
			return redirect('sup:allDrivers')

	else:
		form = ConductorForm()
		return render(request,'supervisor/crew/createConductor.html',{"form":form})

def editConductor(request,conductorId):
	'''
	Edit conductor instance
	'''
	if request.method == 'POST':
		form = ConductorForm(request.POST,instance = Conductor.objects.get(pk = conductorId))
		if form.is_valid():
			form.save()
			messages.success(request,'Succesfully edited a conductor instance')
			return redirect('sup:allConductors')
	else:
		form = ConductorForm(instance = Conductor.objects.get(pk = conductorId))
		cond = Conductor.objects.get(pk = conductorId)
		return render(request,'supervisor/crew/editConductor.html',{"form":form,"cond":cond})

def allConductors(request):
	'''
	View all conductor instances
	'''
	conductors = Conductor.objects.filter(sacco = request.user.supervisor.sacco_base)
	return render(request,'supervisor/crew/allConductors.html',{"conductors":conductors})

def deleteConductor(request,conductorId):
	'''
	Delete a conductor instance
	'''
	Conductor.objects.filter(pk = conductorId).delete()
	messages.error(request,'Succesfully deleted a conductor')
	return redirect('sup:dashboard')