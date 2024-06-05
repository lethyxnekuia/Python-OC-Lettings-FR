import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile
from django.test import TestCase


@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create_user(username='testuser', password='password123')

    profile = Profile.objects.create(user=user, favorite_city='Test City')

    assert profile.user.username == 'testuser'
    assert profile.favorite_city == 'Test City'


@pytest.mark.django_db
class ProfilePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.profile = Profile.objects.create(user=self.user, favorite_city='Test City')

    def test_profile_page_status_code(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    def test_profile_page_template(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertTemplateUsed(response, 'profiles/index.html')

    def test_profile_page_content(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, 'Profiles')
