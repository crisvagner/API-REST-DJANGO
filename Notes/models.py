from django.db import models


# Define uma classe Notes que estende a classe Model do Django
class Notes(models.Model):
    # Define o campo title como um campo CharField de tamanho máximo 50
    title = models.CharField(max_length=50)
    # Define o campo content como um campo TextField
    content = models.TextField()
    # Define o campo author como um campo IntegerField
    author_id = models.IntegerField()

    # Método para retornar o título da nota
    def __str__(self):
        return self.title
