from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . forms import *
from . models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic



# create youur views here
def home(request):
	return render(request, 'index.html')
def about(request):
	return render(request, 'about.html')
def contact(request):
	return render(request, 'contact.html')
def services(request):
	return render(request, 'services.html')
def	transaction(request):
	user=request.user
	records=Record.objects.filter(user=user)
	# records = Record.objects.all()
	return	render(request,	'transaction.html',	{'records':	records})
	
def profile(request):
	return render(request, 'single-member.html')
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# profile
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # load the profile instance created by the signal
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.location = form.cleaned_data.get('location')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('index')
	else:
		form = SignUpForm()
	return render(request, 'registration/signup.html', {'form': form})

def record(request):
	if request.method=='POST':
		form=RecordForm(request.POST)
		if form.is_valid(): 
				instance=form.save(commit=False)
				print(form.cleaned_data.get("bank_name") )
				print(form.cleaned_data.get("branch") )
				print(form.cleaned_data.get("account_name") )
				print(form.cleaned_data.get("account_number") )
				print(form.cleaned_data.get("depositors_name") )
				print(form.cleaned_data.get("amount") )
				print(form.cleaned_data.get("comment") )
				instance.user = request.user
				instance.save()
			# queen=form.cleaned_data['title']
			# esty=form.cleaned_data['content']
			# Ijas.objects.create(title=queen,content=esty)
			
		return HttpResponseRedirect('/')
	else:
		recordform=RecordForm()
		return render(request,"record/create.html", {"recordform":recordform})
	
  
def recorddelete(request,id):
	'''c=id
	return  render(request,'record/delete.html',{'c':id})'''
	Record.objects.filter(id=id).delete()
	return HttpResponseRedirect('/')

def recordview(request,id):
	Es=id
	display=Record.objects.get(id=Es)
	return render(request,'record/view.html',{'segun':id,'display':display})


def recordedit(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = RecordForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance= form.save(commit=False)
		instance.user = request.user
		instance.save()
		
		messages.success(request, "item saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "item not saved")
	context = {
		"form": form,
		"instance":instance,
		
	}

	return render(request, 'record/edit.html', context)