from django.shortcuts import render, redirect
from deep_translator import GoogleTranslator
from django.contrib import messages
import inflect
from .models import Measurement
from .forms import MeasurementTranslateForm
from .helpers import convert_denominator

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MeasurementTranslateForm(request.POST,
                                        instance=Measurement())
        if form.is_valid():
            messages.success(request, f'Translating your measurement!')
            e = inflect.engine()
            f = e.number_to_words(request.POST['feet'])
            u1 = e.plural('foot', request.POST['feet'])
            i = e.number_to_words(request.POST['inches'])
            n = e.number_to_words(request.POST['numerator'])
            d = request.POST['denominator']
            fraction = n
            if d != 1:
                fraction = convert_denominator(fraction,request.POST['numerator'],d)

            u2 = 'inches'
            ut_s = f'{f} {u1}, {i} and {fraction} {u2}'
            es_s = GoogleTranslator(source='en', target='es').translate(ut_s)
            uk_s = GoogleTranslator(source='en', target='uk').translate(ut_s)
            messages.success(request, f'English: {ut_s}')
            messages.success(request, f'Spanish: {es_s}')
            messages.success(request, f'Ukranian: {uk_s}')
            return redirect('measurement:home')
    else:
        form = MeasurementTranslateForm(instance=Measurement())

    context = {
    'form': form
    }

    return render(request, 'measurement/home.html', context)

