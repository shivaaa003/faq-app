from django.shortcuts import render
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

# API View - FAQ ViewSet
class FAQViewSet(viewsets.ModelViewSet):
    """
    API ViewSet for managing FAQs.

    Features:
    - Supports retrieving all FAQs.
    - Uses the FAQSerializer to convert model instances to JSON format.
    - Supports multilingual responses by determining the requested language from query parameters.

    Assumptions:
    1. The `FAQ` model contains multilingual fields (question_hi, question_bn).
    2. The serializer FAQSerializer is capable of handling language-based filtering.
    3. The API consumer can specify the preferred language using the lang query parameter ( ?lang=hi for Hindi).
    4. If no language is specified, English is used by default.
    """

    queryset = FAQ.objects.all()  # Fetch all FAQ objects
    serializer_class = FAQSerializer  # Use FAQSerializer for data conversion

    def get_serializer_context(self):
        """
        Passes additional context to the serializer.

        - Extracts the lang query parameter from the request.
        - Defaults to en if no language is specified.
        """
        context = super().get_serializer_context()
        context['lang'] = self.request.query_params.get('lang', 'en')
        return context


# View to handle the root URL '/'
def home(request):
    """
    Renders the home page.

    Assumptions:
    1.home.html template in the templates directory.
    2. No additional context is required for rendering this page.
    3. This function is for UI support and not affect the API.
    """

    return render(request, 'home.html')  
