from django.views import generic
from django.urls import reverse_lazy
from .models import Textbook, Uhmarketplace

class IndexView(generic.ListView):
    template_name = 'uhmarketplace/index.html'
    model = Uhmarketplace

class CreateView(generic.edit.CreateView):
    template_name = 'uhmarketplace/createtextbook.html'
    model = Textbook
    fields = ['book_title','book_author','course','content']
    success_url = reverse_lazy('uhmarketplace:textbook') # more robust than hardcoding to /uhmarketplace/; directs user to index view after creating a Uhmarketplace

class UpdateView(generic.edit.UpdateView):
    template_name = 'uhmarketplace/updatetextbook.html'
    model = Textbook
    fields = ['book_title','book_author','course','content']
    success_url = reverse_lazy('uhmarketplace:textbook')

class DeleteView(generic.edit.DeleteView):
    template_name = 'uhmarketplace/deletetextbook.html' # override default of uhmarketplace/uhmarketplace_confirm_delete.html
    model = Textbook
    success_url = reverse_lazy('uhmarketplace:textbook')

class TextbookView(generic.ListView):
    template_name = 'uhmarketplace/textbook.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return the all uhmarketplace."""
        return Textbook.objects.all()

class DormView(generic.ListView):
    template_name = 'uhmarketplace/dorm.html'
    model = Uhmarketplace

class ClassesView(generic.ListView):
    template_name = 'uhmarketplace/classes.html'
    model = Uhmarketplace

class FoodieView(generic.ListView):
    template_name = 'uhmarketplace/foodie.html'
    model = Uhmarketplace

class SuppliesView(generic.ListView):
    template_name = 'uhmarketplace/supplies.html'
    model = Uhmarketplace

class OrderDateView(generic.ListView):
    template_name = 'uhmarketplace/ordereddate.html'
    context_object_name = 'textbook_list'

    def get_queryset(self):
        """Return all the textbooks."""
        return Textbook.objects.order_by('-created_on')
