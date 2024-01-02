import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import mariadb


def custom_404(request, exception):
    return render(request, '404.html', status=404)
def index(request):
    return render(request, '403.html', status=403)
@csrf_exempt
def upload(request): #API POST
    if request.method == 'POST':

        try:
            conn = mariadb.connect(
                user="root",
                password="toor",
                host="127.0.0.1",
                port=3306,
                database="datas"

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")


        # Get Cursor
        cur = conn.cursor()
        data = request.POST #dict

        return JsonResponse({'status': '201', 'message': "Created!"}, status=201)

    return render(request, '403.html', status=403)

@csrf_exempt
def update(request): #API PUT
    if request.method == 'PUT':
        return JsonResponse({'status': '200', 'message': "Updated!"}, status=200)

def delete(request): #API DELETE

    return JsonResponse({'status': '204', 'message': "Deleted!"}, status=204)
