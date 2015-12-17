from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.views import generic

from .models import Recipient

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'recipient_list'

    def get_queryset(self):
        """Return a list of recipients."""
        return Recipient.objects.order_by('last_name')

class DetailView(generic.DetailView):
    model = Recipient
    template_name = 'cards/detail.html'

def index(request):
    recipient_list = Recipient.objects.order_by('last_name')
    context = {'recipient_list': recipient_list}
    return render(request, 'cards/index.html', context)

def detail(request, recipient_id):
    recipient = get_object_or_404(Recipient, pk=recipient_id)
    return render(request, 'cards/detail.html', {'recipient': recipient})
