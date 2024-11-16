from rest_framework import serializers
from .models import student

class Student_serializer(serializers.ModelSerializer):
    result = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = student
        fields = [
            "s_id",
            "name",
            "dept",
            "subject",
            "marks",
            "result",
        ]

    def get_result(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, student):
            return None
        return obj.get_pass_or_fail()