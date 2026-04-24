from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.http import StreamingHttpResponse
from ai_assistant.ai_agents.gemini import Gemini
    
class AssistView(APIView):
    ai_agent = Gemini()
    
    def get(self, request, *args, **kwargs):
        customer_request = request.query_params.get('customer_request')

        # return StreamingHttpResponse(
        #     self.ai_agent.stream_response(customer_request),
        #     content_type='text/event-stream'
        # )

        if not customer_request:
            return Response(
                {"error": "customer_request query parameter is required."},
                status=HTTP_400_BAD_REQUEST
            )
        
        ai_response = self.ai_agent.get_response(customer_request)

        return Response(
            {"response": ai_response},
            status=HTTP_200_OK
        )
