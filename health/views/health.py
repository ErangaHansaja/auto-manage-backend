from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from health.serializers import HealthSerializer

class HealthView(APIView):

    def get(self, request):
        data = {"status": "working"}
        serializer = HealthSerializer(data)

        return Response({
            "success": True,
            "message": "api testing.",
            "data": serializer.data
        }, status=HTTP_200_OK)
