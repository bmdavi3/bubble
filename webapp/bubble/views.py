from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, 'charts.html', {})


def get_data(request):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                json_agg(foo)
            FROM (
                SELECT
                    count(*) AS y,
                    date_trunc('minute', created) AS x
                FROM
                    bubble
                WHERE
                    jug_id = %s
                GROUP BY
                    date_trunc('minute', created)
                ORDER BY
                    date_trunc('minute', created)
            ) AS foo
        """, [1])
        data = cursor.fetchone()[0]

    return JsonResponse(data, safe=False)
