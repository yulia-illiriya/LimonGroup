from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProductionSerializer
from .models import DailyWork



class ProductionView(APIView):
    def get(self, request):
        queryset = DailyWork.objects.all()
        date = request.query_params.get('date')
        if date:
            queryset = queryset.filter(date=date)
            serializer = ProductionSerializer(queryset, many=True)
            return Response(serializer.data)