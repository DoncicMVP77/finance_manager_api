from django.shortcuts import get_object_or_404
from manager.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets, mixins

from accounts.models import Account
from accounts.serializers import AccountSerializer


class AccountViewSet(mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Account.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return Account.objects.all()
        account = get_object_or_404(Account, user=self.request.user)
        return account

