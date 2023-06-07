from .models import Jobs,JobDetail,JobFunctions,Location,Type,Industries,JbImage
from rest_framework import serializers

class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobDetail
        fields='__all__'
        
class JobFunctionSerializer(serializers.ModelSerializer):   
    class Meta:
        model=JobFunctions
        fields='__all__'
class JobLocationSerializer(serializers.ModelSerializer):   
    class Meta:
        model=Location
        fields='__all__'
class JobTimeSerializer(serializers.ModelSerializer):   
    class Meta:
        model=Type
        fields='__all__'
class JbImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=JbImage
        fields='__all__'
class IndustriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Industries
        fields='__all__'
class JobSerializer(serializers.ModelSerializer):
    job_function = JobFunctionSerializer()
    industries = IndustriesSerializer()
    location= JobLocationSerializer()
    job_type = JobTimeSerializer()
    jb_images = JbImageSerializer()
    job_details = JobDetailSerializer(many=True)

    class Meta:
        model = Jobs
        fields = ['id', 'title', 'link', 'date_posted', 'job_payment', 'location', 'job_type', 'jb_images', 'job_function', 'industries', 'job_details']