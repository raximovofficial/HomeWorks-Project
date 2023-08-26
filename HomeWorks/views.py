# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def WeekdaysUzView(request):
#     weekdaysuz = ['Dushanba','Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
#     return HttpResponse(" ".join(weekdaysuz))
        
# def WeekdaysEnView(request):
#     weekdaysen = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#     return HttpResponse(' '.join(weekdaysen))

# def WeekdaysRuView(request):
#     weekdaysru = ['понедельник', 'вторник', 'среда', 'четверг', ' пятница', 'суббота', 'воскресенье']
#     return HttpResponse(' '.join(weekdaysru))

from django.shortcuts import render

def weekdays_view(request, language):
    weekdays = {
        'uz': ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba'],
        'en': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'ru': ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'],
    }
    
    selected_weekdays = weekdays.get(language, [])  # Get weekdays list based on language
    
    return render(request, 'weekdays.html', {'weekdays': selected_weekdays, 'language': language})


