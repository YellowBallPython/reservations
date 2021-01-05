from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reservation
from .forms import CreateReservationForm
import datetime


def reservations_list(request):
    reservations = Reservation.objects.all()

    context = {
        'reservations': reservations,
    }
    return render(request, 'reservations/list.html', context)


@login_required(redirect_field_name='/users/login')
def make(request):
    form = CreateReservationForm()
    if request.method == 'POST':
        form = CreateReservationForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            form_ci = form.cleaned_data.get('ci')
            form_co = form.cleaned_data.get('co')
            res_by_day = Reservation.objects.filter(date=date)

            if date < datetime.date.today():
                messages.error(
                    request, f'Ingrese una fecha adecuada')
                context = {
                    'form': form,
                }
                return render(request, 'reservations/make.html', context)

            elif form_ci > form_co:
                messages.error(
                    request, f'Ingrese una hora correcta')
                context = {
                    'form': form,
                }
                return render(request, 'reservations/make.html', context)

            elif len(res_by_day) == 0:
                form.save()
                return redirect('reservations:success')
            elif len(res_by_day) == 1:
                if form_ci >= res_by_day[0].co or form_co <= res_by_day[0].ci:
                    form.save()
                    return redirect('reservations:success')
                else:
                    messages.error(
                        request, f'Alguien ya reservó ese espacio :(')
                    context = {
                        'form': form,
                    }
                    return render(request, 'reservations/make.html', context)
            else:
                for i in range(1, len(res_by_day)):
                    j = 0
                    while j <= i:
                        if res_by_day[i].ci >= form_co and res_by_day[i - 1].co <= form_ci:
                            form.save()
                            return redirect('reservations:success')
                        j += 1
                if j == len(res_by_day):
                    messages.error(
                        request, f'Alguien ya reservó ese espacio :(')
                    context = {
                        'form': form,
                    }
                    return render(request, 'reservations/make.html', context)

    context = {
        'form': form,
    }
    return render(request, 'reservations/make.html', context)
