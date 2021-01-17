from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from dadata_api.services import DadataService


class GetLegalEntityInfoByInnView(APIView):
    permission_classes = (permissions.AllowAny,)

    def __init__(self):
        super().__init__()
        self.client = DadataService()

    def post(self, request):
        inn = request.data.get('inn')
        data = self.client.get_legal_entity_info_by_inn(inn)
        return Response(data, status=status.HTTP_200_OK)

class GetBankInfoByBikView(APIView):
    permission_classes = (permissions.AllowAny,)

    def __init__(self):
        super().__init__()
        self.client = DadataService()

    def post(self, request):
        bik = request.data.get('bik')
        data = self.client.get_bank_info_by_bik(bik)
        return Response(data, status=status.HTTP_200_OK)
