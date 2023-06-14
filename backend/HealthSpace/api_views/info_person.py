from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from HealthSpace.models import tbPerson
from HealthSpace.serializer import PersonSerializer


class InfoPerson(APIView):
    def get(self, request, username):
        tabela_person = get_object_or_404(tbPerson, username=username)
        returno_dados = {
            'usuario': tabela_person.username.pk,
            'firstName':tabela_person.firstName,
            'lastName':tabela_person.lastName,
            'sex':tabela_person.sex,
            'birthDate':tabela_person.birthDate,
            'bloodType':tabela_person.bloodType,
            'organDonor':tabela_person.organDonor,
            'weight':tabela_person.weight,
            'height':tabela_person.height,
            'maritalStatus':tabela_person.maritalStatus,
            'color':tabela_person.color,
            'nationality':tabela_person.nationality,
            'occupation':tabela_person.occupation,
            'address':tabela_person.address,
            'phone':tabela_person.phone,
            'primaryLanguague':tabela_person.primaryLanguague
        }
        return Response(returno_dados, status=200)

    def post(self, request):
        print("request", request.data)
        if tbPerson.objects.filter(username=request.data["username"]):
            return Response({"error":"Já possui registro"}, status=400)
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)
    
    def put(self, request):
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer._errors, status=400)

        return Response(status=201)