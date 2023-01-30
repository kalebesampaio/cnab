from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ResumeForm
from transactions import models, serializer
import ipdb
from datetime import date, time, datetime, timedelta, timezone
from rest_framework.views import APIView, Request, Response, status
from .logic import PlainTextParser

# Create your views here.

def upload_resume(request):    
    return render(request, 'files/upload.html', {})

class CnabView(APIView):
    parser_classes = [PlainTextParser]
    def post(self, request: Request, format=None) -> Response: 
        cnab_txt = request.data.decode("utf-8")
        list_line = cnab_txt.split("\r\n")
        for linha in list_line:
            date = datetime(
                int(linha[1:5]),
                int(linha[5:7]),
                int(linha[7:9]),
                int(linha[42:44]),
                int(linha[44:46]),
                int(linha[46:48]),
            )
            serializer_data = serializer.TransactionsSerializer(data={
                "type": int(linha[0]) ,
                "date_and_hour": date,
                "value": int(linha[9:19]) / 100,
                "cpf": int(linha[19:30]),
                "card": linha[30:42],
                "owner": linha[48:62],
                "name": linha[62:81]
            })  
            if serializer_data.is_valid():
                serializer_data.save()
        return Response(status=status.HTTP_201_CREATED)   

    def get(self, request: Request) -> Response:

        transactions_data = models.Transactions.objects.all()

        transactions_serializer = serializer.TransactionsSerializer (transactions_data, many=True)

        return Response(transactions_serializer.data)        