from rest_framework import serializers
from .models import Student

class StudentSerialzer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name','roll','city']
        # read_only_fields = ['name','roll']
        # extra_kwargs = {'name':{'read_only':True}}





# class StudentSerialzer(serializers.Serializer):
#     name = serializers.CharField(max_length=25)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=20)

#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         # print(instance.name)
#         instance.name = validated_data.get('name',instance.name)
#         # print(instance.name)
#         instance.roll = validated_data.get('roll',instance.roll)
#         instance.city = validated_data.get('city',instance.city)
#         instance.save()
#         return instance