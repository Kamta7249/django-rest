from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=25)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=25)
#     roll = forms.IntegerField()
#     city = forms.CharField(max_length=20)
