

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_get_faqs_api():
    # Create a sample FAQ object
    faq = FAQ.objects.create(
        question="how do i open my account",
        answer="visit nearest branch or login online"
    )
    
    client = APIClient()
    url = reverse('faq-list')  # DefaultRouter 
    response = client.get(url, {'lang': 'en'})
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['question'] == "how do i open my account"
