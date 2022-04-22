from django.shortcuts import render
from rest_framework import views

from address.forms import AddressSearch

from .coordinates_radius import required_database_objects
from .dadata import request_use_api


class AddressFromApiList(views.APIView):
    def get(self, request):
        form = AddressSearch()
        return render(request, 'address/index.html', {'form': form})

    def post(self, request):
        form = AddressSearch(request.POST)

        if form.is_valid():
            answer = request_use_api(form.data['search'])
            if not answer['result']:
                return render(request, 'address/not_found_page.html')

            radius = abs(float(form.data['radius']) * 1000)
            obj_list = required_database_objects(answer, radius)

            return render(request, 'address/index.html', {
                'form': form,
                'answer': answer,
                'obj_list': obj_list
            })
