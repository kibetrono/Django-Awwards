from django.shortcuts import render,redirect
from .models import Profile,Project,Rating
from django.contrib .auth import authenticate,login,logout# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import  ProjectUploadForm,RatingForm

from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer
from .permissions import IsAdminOrReadOnly
from django.http import HttpResponse

# Create your views here.
@login_required(login_url='login')
def home(request):  # Home page
    project = Project.objects.all()
    recent_project = project[0]
    rating = Rating.objects.filter(project_id=recent_project.id).first()
    context={"projects": project, "project_home": recent_project, "rating": rating}
    return render(request, "app/index.html",context)


@login_required(login_url='login')
def my_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()  
    project = Project.objects.filter(user_id=current_user.id).all()  
    context={"profile": profile, "images": project}
    return render(request, "app/my_profile.html", context)


@login_required(login_url='login')
def uploadProject(request):

    form = ProjectUploadForm()
    if request.method == "POST":
        form_results = ProjectUploadForm(request.POST,request.FILES)
        if form_results.is_valid():

            form_results.save()
            return redirect('home')

    context = {"form": form}
    return render(request, 'app/upload_project.html', context)