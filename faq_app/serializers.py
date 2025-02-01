from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    """
    Serializer for FAQ model.

    This serializer is responsible for:
    - Converting FAQ model instances into JSON format.
    - Handling multilingual support by dynamically selecting the language for question and answer.
    - Using SerializerMethodField to fetch translations based on the requested language.

    Assumptions:
    1. The FAQ model contains multilingual fields (question_hi, question_bn).
    2. The FAQ model has get_translated(field, lang) method that return the translated text based on the requested language.
    3. The API client can specify the preferred language using the lang context (passed from FAQViewSet ).
    """

    # fetch based on the requested language
    question = serializers.SerializerMethodField()
    
    # fetch translated answer based on the requested language
    answer = serializers.SerializerMethodField()

    class Meta:
        """
        Meta class defining the model and fields to be serialized.
        """
        model = FAQ
        fields = ['id', 'question', 'answer']

    def get_question(self, obj):
        """
        Returns the translated question based on the requested language.

        - Extracts lang from the serializer's context 
        - Calls get_translated('question', lang) on the FAQ object
        - Defaults to English if no language is specified.

        Argumenbs:
            obj FAQ: The FAQ instance being serialized.

        Returns:
            str translated question.
        """
        lang = self.context.get('lang', 'en')  # Default language is English
        return obj.get_translated('question', lang)

    def get_answer(self, obj):
        """
        Returns the translated answer based on the requested language.

        - Extracts lang from the serializer's context (provided by FAQViewSet).
        - Calls get_translated('answer', lang) on the FAQ object.
        - Defaults to English  if no language is specified.

        Arguments:
            obj FAQ: The FAQ instance being serialized.

        Returns:
            str translated answer.
        """
        lang = self.context.get('lang', 'en')  # Default language is English
        return obj.get_translated('answer', lang)
