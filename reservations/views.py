from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation
from .forms import CreateReservationForm


def index(request):
    reservations = Reservation.objects.all()
    form = CreateReservationForm()
    if request.method == 'POST':
        form = CreateReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            form_ci = form.cleaned_data.get('ci')
            form_co = form.cleaned_data.get('co')
            res_by_day = Reservation.objects.filter(date=date)

            if len(res_by_day) == 0:
                form.save()
                return redirect('index')
            elif len(res_by_day) == 1:
                if form_ci >= res_by_day[0].co or form_co <= res_by_day[0].ci:
                    form.save()
                    return redirect('index')
                else:
                    messages.error(
                        request, f'Alguien ya reservó ese espacio :(')
                    return redirect('index')
            else:
                for i in range(1, len(res_by_day)):
                    j = 0
                    while j <= i:
                        if res_by_day[i].ci >= form_co and res_by_day[i - 1].co <= form_ci:
                            form.save()
                            return redirect('index')
                        j += 1
                if j == len(res_by_day):
                    messages.error(
                        request, f'Alguien ya reservó ese espacio :(')
                    return redirect('index')

    context = {
        'reservations': reservations,
        'form': form,
    }
    return render(request, 'reservations/index.html', context)
