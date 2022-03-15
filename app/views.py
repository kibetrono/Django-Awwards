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

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

class ProjectList(APIView): # get all projects
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

@login_required(login_url='login')
def vote_details(request, project_id):
    project = Project.objects.get(id=project_id)
    # get project rating
    rating = Rating.objects.filter(id=project_id)
    context={"project": project, "rating": rating}
    return render(request, "app/voting.html", context)

@login_required(login_url='login')
def rate(request,id):
    form = RatingForm()
    # rating= Rating.objects.get(id=id)
    project = Project.objects.get(id=id)

    # rating= Rating.objects.filter(project=project)

    if request.method == "POST":

        form_results = RatingForm(request.POST)
        if form_results.is_valid():
            design_rate = request.POST["design_rate"]
            usability_rate = request.POST["usability_rate"]
            content_rate = request.POST["content_rate"]

            avg_rating = (int(design_rate) + int(usability_rate) + int(content_rate)) / 3

            project.rate = avg_rating
            project.update_project()
            form_results.save()
            return redirect('home')

    context = {"form": form,'rating':Rating.objects.all()}
    return render(request,'app/rate.html',context)

@login_required(login_url='login')
def search(request):
    if 'query' in request.GET and request.GET["query"]:
        search_term = request.GET.get("query")
        searched_projects = Project.objects.filter(title__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "app/search.html", {"message": message, "results": searched_projects})
    else:
        message = "You haven't searched for any term"
        return render(request, "app/search.html", {"message": message})