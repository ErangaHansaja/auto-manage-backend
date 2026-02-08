from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.http import StreamingHttpResponse
from utils import Gemini

class AssistView(generics.GenericAPIView):
    ai_agent = Gemini
    
    def post(self, request, *args, **kwargs):
        # Placeholder for POST method logic
        customer_id = request.data.get('customer_id')
        vehicle_id = request.data.get('vehicle_id')
        issue_description = request.data.get('issue_description')

        return StreamingHttpResponse(
            self.ai_agent.stream_response(customer_id, vehicle_id, issue_description),
            content_type='text/event-stream'
        )
