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
            f = int(request.POST['feet'])
            f_s = ''
            if f != 0:
                f_s = e.number_to_words(f)
                u1 = e.plural('foot', request.POST['feet'])
                f_s = f'{f_s} {u1}, '
            i = int(request.POST['inches'])
            i_s = ''
            if i != 0:
                i_s = e.number_to_words(i)
            
            n = int(request.POST['numerator'])
            n_s = ''
            fraction = ''
            u2 = 'inch'
            if n != 0:
                n_s = e.number_to_words(n)
                u2_s = e. plural(u2, n)
                d = int(request.POST['denominator'])
                if i != 0:
                    fraction = f' and {n_s}'
                else:
                    fraction = n_s
                if d != 1:
                    fraction = convert_denominator(fraction,n,d)
            else:
                u2_s = e. plural(u2, i)
            ut_s = f'{f_s}{i_s}{fraction} {u2_s}'
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

