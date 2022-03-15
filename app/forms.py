from django.forms import ModelForm
from .models import Project,Rating


class ProjectUploadForm(ModelForm):
    class Meta:
        model = Project
        fields ="__all__"

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields =['design_rate','usability_rate','content_rate']

