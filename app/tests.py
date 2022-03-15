from django.test import TestCase
from .models import Profile,Project,Rating
from django.contrib.auth.models import User


# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        """Creating a new location and saving it"""
        user = User.objects.create(username='kibet',first_name='rono',last_name='David')

        self.profile=Profile.objects.create(user=user,profile_photo='lorem2.png',bio="New description",contact=1)
        self.profile.save_profile()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_method(self):
        """Testing Save Method"""
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) < 1)

    def tearDown(self):
        """tearDown method"""
        Profile.objects.all().delete()


class ProjectTestClass(TestCase):
    # Set up method
    def setUp(self):
        """Creating a new location and saving it"""
        user = User.objects.create(username='kibet',first_name='rono',last_name='David')

        self.project=Project.objects.create(user=user,title="project 1",description="Initial project",image='lorem2.png',url="https://ksms.or.ke/contact-us-3/",location="New description",date=None)
        self.project.save_project()

    def test_instance(self):
        """Testing instance"""
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        """Testing Save Method"""
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_delete_method(self):
        """Testing delete Method"""
        self.project.delete_project()
        project= Project.objects.all()
        self.assertTrue(len(project) < 1)

    def tearDown(self):
        """tearDown method"""
        Project.objects.all().delete()
