from django.db import models

class englishWords(models.Model): 
    lang_code = models.CharField(max_length=10, null=False, default='en')
    words = models.CharField(max_length=100, null=False)
    
    class Meta:
        verbose_name = 'english_words'
    def __str__(self):
        return self.words
    
class hindiWords(models.Model): 
    lang_code = models.CharField(max_length=10, null=False, default='hi')
    words = models.CharField(max_length=100, null=False)
    
    class Meta:
        verbose_name = 'hindi_words'
    def __str__(self):
        return self.words
    
class russianWords(models.Model): 
    lang_code = models.CharField(max_length=10, null=False, default='ru')
    words = models.CharField(max_length=100, null=False)
    
    class Meta:
        verbose_name = 'russian_words'
    def __str__(self):
        return self.words
    
class japaneseWords(models.Model): 
    lang_code = models.CharField(max_length=10, null=False, default='ja')
    words = models.CharField(max_length=100, null=False)
    
    class Meta:
        verbose_name = 'japanese_words'
    def __str__(self):
        return self.words