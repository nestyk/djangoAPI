import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import mariadb
import config

def custom_404(request, exception):
    return render(request, '404.html', status=404)
def index(request):
    return render(request, '403.html', status=403)
@csrf_exempt
def upload(request): #API POST
    if request.method == 'POST':

        try:
            conn = mariadb.connect(
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                host=config.DB_HOST,
                port=config.DB_PORT,
                database=config.DB_NAME

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")


        # Get Cursor
        cur = conn.cursor()
        data = request.POST #dict
        try:
            mydict = dict(data)


            for key in mydict.keys():
                for value in mydict[key]:
                    cur.execute(
                        "INSERT INTO datas (`dev_name`, `value`) VALUES (?, ?);",
                        (key, value)
                    )
                    conn.commit()
        except Exception as e:
            print(e)

        return JsonResponse({'status': '201', 'message': "Created!"}, status=201)

    return render(request, '403.html', status=403)

@csrf_exempt
def update(request, id): #API PUT
    if request.method == 'PUT':
        data = request.POST

        try:
            mydict = dict(data)
            conn = mariadb.connect(
                user=config.DB_USER,
                password=config.DB_PASSWORD,
                host=config.DB_HOST,
                port=config.DB_PORT,
                database=config.DB_NAME

            )
            cur = conn.cursor()
            for key in mydict.keys():
                for value in mydict[key]:
                    cur.execute("UPDATE datas SET dev_name = ?, value = ? WHERE id = ?",
                              (key,value, id))
                    conn.commit()

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

        return JsonResponse({'status': '200', 'message': "Updated!"}, status=200)

def delete(request,id): #API DELETE

    try:
        conn = mariadb.connect(
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME

        )
        cur = conn.cursor()
        cur.execute("DELETE FROM datas WHERE id = ?", (id,))
        conn.commit()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    return JsonResponse({'status': '204', 'message': "Deleted!"}, status=204)
