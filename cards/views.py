from .models import Card
from django.views.generic import DetailView,CreateView,ListView
from django.urls import reverse_lazy
from django.shortcuts import redirect


class CreateCardView(CreateView):
    model=Card
    template_name= 'cards/create_card.html'
    success_url = reverse_lazy('list_card')
    fields = '__all__'

class ListCardView(ListView):
    model=Card
    template_name='cards/list_cards.html'
    def get_context_data(self, **kwargs):
        cards = Card.objects.all()
        return {'cards_list': cards}