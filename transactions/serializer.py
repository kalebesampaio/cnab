from rest_framework import serializers
from .models import Transactions


class TransactionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        fields = ["id", "type", "value", "cpf", "card", "date_and_hour", "owner", "name"]
