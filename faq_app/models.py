from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

#Google Translator 
translator = Translator()

class FAQ(models.Model):
    """
    This model represents a Frequently Asked Question (FAQ) with multilingual support.
    
    Attributes:
        question (TextField): Stores the question in English,default language,.
        answer (RichTextField): Stores the answer in English with WYSIWYG editor support.
        question_hi (TextField): Stores the translated question in Hindi (auto).
        question_bn (TextField): Stores the translated question in Bengali (auto).
        answer_hi (RichTextField): Stores the translated answer in Hindi (auto).
        answer_bn (RichTextField): Stores the translated answer in Bengali (auto).
    """
    
    question = models.TextField(help_text="Question in English")
    answer = RichTextField(help_text="Answer in English (WYSIWYG enabled)")
    question_hi = models.TextField(blank=True, null=True, help_text="Question in Hindi")
    question_bn = models.TextField(blank=True, null=True, help_text="Question in Bengali")
    answer_hi = RichTextField(blank=True, null=True, help_text="Answer in Hindi")
    answer_bn = RichTextField(blank=True, null=True, help_text="Answer in Bengali")

    def save(self, *args, **kwargs):
        """
        Overrides the save method to automatically translate the English question and answer
        into Hindi and Bengali before saving the instance to the database.
        
        Assumptions:
        - Google Translate API is used for translations.
        - If translation fails, the English text is retained.
        - Translations are performed only if the fields are empty.
        """
        if not self.question_hi:
            try:
                translation = translator.translate(self.question, dest='hi')
                self.question_hi = translation.text
            except Exception:
                self.question_hi = self.question  #to English

        if not self.question_bn:
            try:
                translation = translator.translate(self.question, dest='bn')
                self.question_bn = translation.text
            except Exception:
                self.question_bn = self.question  # to English

        if not self.answer_hi:
            try:
                translation = translator.translate(self.answer, dest='hi')
                self.answer_hi = translation.text
            except Exception:
                self.answer_hi = self.answer  # to English

        if not self.answer_bn:
            try:
                translation = translator.translate(self.answer, dest='bn')
                self.answer_bn = translation.text
            except Exception:
                self.answer_bn = self.answer  #to English

        super().save(*args, **kwargs)

    def get_translated(self, field, lang='en'):
        """
        Returns the translation of a specified field (question or answer) in the requested language.
        
        Arguments:
            field: The field to retrieve ('question' or 'answer').
            lang: The language code ('en', 'hi', 'bn'). Default is English ('en').
        
        Returns:
            str: The translated text of the specified field in the requested language.
        
        Assumptions:
        - The translations are stored in separate fields (question_hi, answer_hi).
        - If the requested translation does not exist, it falls back to the English version.
        - Uses Django caching to improve performance and avoid redundant translations.
        """
        cache_key = f"faq_{self.id}_{field}_{lang}"
        cached_text = cache.get(cache_key)
        if cached_text:
            return cached_text

        if lang == 'en':
            text = getattr(self, field)
        elif lang in ('hi', 'bn'):
            text = getattr(self, f"{field}_{lang}")
        else:
            text = getattr(self, field)  # Default to English if an unsupported language

        # Cache the result for one hour
        cache.set(cache_key, text, timeout=3600)
        return text

    def __str__(self):
        """
        Returns a string FAQ object.
        Displays the English version of the question.
        """
        return self.question
