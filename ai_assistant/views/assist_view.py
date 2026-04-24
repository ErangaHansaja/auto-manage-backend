from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.http import StreamingHttpResponse
from ai_assistant.ai_agents.gemini import Gemini
    
class AssistView(APIView):
    
    def post(self, request, *args, **kwargs):
        customer_request = request.data.get('customer_request')

        # return StreamingHttpResponse(
        #     self.ai_agent.stream_response(customer_request),
        #     content_type='text/event-stream'
        # )

        if not customer_request:
            return Response(
                {
                    "success":  False,
                    "message": "Please provide a valid customer request in the request body.",
                    "data": None
                },
                status=HTTP_400_BAD_REQUEST
            )
        ai_agent = Gemini()
        ai_response = ai_agent.get_response(customer_request)

        return Response(
            {
                "success": True,
                "message": "AI response generated successfully",
                "response": ai_response
            },
            status=HTTP_200_OK
        )
