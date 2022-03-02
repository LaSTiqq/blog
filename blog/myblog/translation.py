from modeltranslation.translator import translator, TranslationOptions
from .models import Blog

class TestTranslationOptions(TranslationOptions):
    fields = ('title', 'preview_text', 'content')

translator.register(Blog, TestTranslationOptions)