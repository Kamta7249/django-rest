from rest_framework import serializers
from .models import Todo, TimingTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['user','uid','todo_title','slug','todo_description']
        # fields = '__all__'
        # exclude = ['created_at','updated_at']

    def get_slug(self, obj):

        return slugify(obj.todo_title)
        # return "Kamta Kumar"

    def validate_todo_title(self, data):
        if data:
            todo_title = data
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
            
            if len(todo_title) < 3:
                raise serializers.ValidationError("todo-title must be more than 3 Character.")

            if not regex.search(todo_title) == None:
                raise serializers.ValidationError("Todo-title does not contain any special character.")
            
            return data
            

class TimingTodoSerializer(serializers.ModelSerializer):
    todo = TodoSerializer()
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']
        depth = 1
        # fields = '__all__'
    
    # def validate(self, validated_data):
    #     if validated_data.get('todo_title'):
    #         todo_title = validated_data['todo_title']
    #         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
            
    #         if len(todo_title) < 3:
    #             raise serializers.ValidationError("todo-title must be more than 3 Character.")

    #         if not regex.search(todo_title) == None:
    #             raise serializers.ValidationError("Todo-title does not contain any special character.")
            
    #         return validated_data
               
     


