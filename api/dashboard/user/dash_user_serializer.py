from rest_framework import serializers
from db.user import User, UserRoleLink, Role


class UserDashboardSerializer(serializers.ModelSerializer):
    total_karma = serializers.SerializerMethodField()

    def get_total_karma(self, obj):
        karma = obj.total_karma_user.karma if hasattr(obj, "total_karma_user") else 0
        return karma

    class Meta:
        model = User
        exclude = ("password",)
        extra_fields = ["total_karma"]
        read_only_fields = ["id", "created_at", "total_karma"]


class UserVerificationSerializer(serializers.ModelSerializer):
    
    first_name = serializers.ReadOnlyField(source="user.first_name")
    last_name = serializers.ReadOnlyField(source="user.last_name")
    user_id = serializers.ReadOnlyField(source="user.id")
    discord_id = serializers.ReadOnlyField(source="user.discord_id")
    mu_id = serializers.ReadOnlyField(source="user.mu_id")
    role_title = serializers.ReadOnlyField(source="role.title")

    class Meta:
        model = UserRoleLink
        fields = [
            "id",
            "user_id",
            "discord_id",
            "mu_id",
            "first_name",
            "last_name",
            "verified",
            "role_id",
            "role_title",
        ]
