from .operation import Operations
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def index(request):
    #creating new snippets
    if request.method == "POST":
        try:
            operator = request.data.get('operation_type')
            x = request.data.get('x')
            y = request.data.get('y')
        except Exception as e:
            message = {"message": "Invalid Request"}
            return Response(message, status=status.HTTP_400_BAD_REQUEST)

        result = Operations.operate(operator, x, y)
        json_form = {
            "slackUsername": "SerahN",
                     "result": int(result[0]),
                     "operation_type": result[1],
                     }

        return Response(json_form, status=status.HTTP_200_OK)
