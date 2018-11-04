from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.edit import *
from django.http import Http404
from .models import Person, Contact
from .forms import ContactForm
from .mixins import OnlyStaffMixin


def home(request):
    person = Person.objects.all()
    return render(request, 'home.html', {'person': person})


def person_detail(request, personid):
    try:
        person = Person.objects.get(personid=personid)
    except Person.DoesNotExist:
        raise Http404('Person not found')
    return render(request, 'person_detail.html', {'person': person})


class ContactUpdate(UpdateView):
    model = Contact
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        kwargs = super(ContactUpdate, self).get_context_data(**kwargs)
#        kwargs.update({'form2':AnotherForm()})
        return kwargs


class ContactNew(OnlyStaffMixin, CreateView):
    model = Contact
    form_class = ContactForm

class ReservationView(View):
        reservation = 0
        reservname = 'name'

        def get_reservation(self):
            return JsonResponse({'reservation': self.reservation})

        def get_resvname(self):
            return JsonResponse({'resv name': self.reservname})

