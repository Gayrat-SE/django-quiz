
from django.db import models
from quizes.models import Quiz
from ckeditor_uploader.fields import RichTextUploadingField #import this


# Create your models here.
class Question(models.Model):
    
    text = RichTextUploadingField()
    
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions",
    )
    
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):
        """
        How the Question is displayed in the Admin page
        """
        return f"{self.pk} - {str(self.text)[:10]}"

    @property
    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    """
    The answer options to the Question model.
    It can be true or false.
    """
  
    text = RichTextUploadingField()
    
    date = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    correct = models.BooleanField(default=False)
 
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="answers"
    )

    def __str__(self):
        return f"Question: {str(self.question.text)[:15]}, Ans: {str(self.text)[:10]}, Correct: {self.correct}"
    