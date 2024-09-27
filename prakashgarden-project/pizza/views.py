from django.shortcuts import render
from .forms import PizzaForm

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST, request.FILES) # Files for uploaded files through browser.
        if filled_form.is_valid():
            note = 'Thanks for ordering. Your  %s %s %s pizza is on the way !' %(filled_form.cleaned_data['size'],filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'],)
            newform = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': newform, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form})