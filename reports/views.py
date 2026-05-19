from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Complaint
from .serializers import ComplaintSerializer
from .ai_engine import analyze_complaint
from .permissions import IsOfficer


class ComplaintCreateView(generics.CreateAPIView):

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):

        description = self.request.data.get('description')
        ai_result = analyze_complaint(description)

        serializer.save(
            user=self.request.user,
            category=ai_result['category'],
            department=ai_result['department'],
            priority=ai_result['priority']
        )


class ComplaintListView(generics.ListAPIView):

    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Complaint.objects.filter(user=self.request.user)


class ComplaintStatusUpdateView(generics.UpdateAPIView):

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]


class OfficerComplaintListView(generics.ListAPIView):

    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer
    permission_classes = [IsAuthenticated]


class AnalyticsView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total = Complaint.objects.count()
        submitted = Complaint.objects.filter(status='submitted').count()
        completed = Complaint.objects.filter(status='completed').count()
        high_priority = Complaint.objects.filter(priority='high').count()

        return Response({
            "total_complaints": total,
            "submitted": submitted,
            "completed": completed,
            "high_priority": high_priority
        })