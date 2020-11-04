from django.db import models ##  Im Allgemeinen wird jedes Modell einer einzelnen Datenbanktabelle zugeordnet.
from django.utils import timezone ## import der Zeitzone die django zur verfügung stellt
from django.contrib.auth.models import User ## Dieses Dokument enthält API-Referenzmaterial 
                                            ## für die Komponenten des Django-Authentifizierungssystems
# Create your models here.

class Post(models.Model): ## eine Tabelle in der Datenbank wird übergeben
    title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now) ## timezone.now zeitstempelfeld
    author = models.ForeignKey(User, on_delete=models.CASCADE) ## Wenn das referenzierte Objekt gelöscht wird, löschen Sie auch die Objekte, auf die verwiesen wird
## ForeignKey ein User kann mehrere Posts haben aber ein Post nur einen User
    def __str__(self):
        return self.title
