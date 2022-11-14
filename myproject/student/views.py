

from django.views.generic import View, ListView
from django.shortcuts import render, redirect

from student.forms import ContactForm
from student.models import Contact

class ContactView(View):
    
    def get(self, request):
        form = ContactForm() 
        return render(request, "student/school.html", {"form": form})
    
    def post(self, request):
        form = ContactForm(request.POST) 
        if form.is_valid():
            instance = form.save()
            return render(request, "student/class.html", {"data": instance})
        else:
            return render(request, "student/school.html", {"form": form})

class ContactListView(ListView):
    template_name = "student/school-list.html"
    context_object_name = "records"
    queryset = Contact.objects.all()

class ContactUpdateView(View):

    def get(self, request, id):
        form = ContactForm(instance=Contact.objects.get(id=id))
        return render(request, "student/school.html", {"form": form})
    
    def post(self, request, id):
        form = ContactForm(request.POST, instance=Contact.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("list-contact")
        else:
            return render(request, "student/student.html", {"form": form})

