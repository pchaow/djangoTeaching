from .models import Activity, ActivityTimeline, Student
from rest_framework import serializers


class ActivityTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTimeline
        fields = ['id',
                  'activity_start',
                  'activity_stop',
                  'activity_plantitle']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'code', 'name']


class ActivitySerializer(serializers.ModelSerializer):
    participant = StudentSerializer(many=True,required=False)
    activitytimeline_set = ActivityTimelineSerializer(many=True,required=False)

    class Meta:
        model = Activity
        fields = ['id',
                  'activity_name',
                  'activity_type','activity_desc',
                  'activity_date','participant','activitytimeline_set']
