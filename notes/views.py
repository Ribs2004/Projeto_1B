from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title=title, content=content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})