from rest_framework import serializers
from app.models import Post, PostLike, Profile, Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="user.profile.username")
    post_title = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ("id", "post_title", "owner", "content", "created_time")

    @staticmethod
    def get_post_title(obj):
        return obj.post.title


class CommentCreateSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="user.profile.username")

    class Meta:
        model = Comment
        fields = (
            "id",
            "owner",
            "content",
        )


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    unlikes_count = serializers.SerializerMethodField()

    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "owner",
            "title",
            "content",
            "image",
            "comments",
            "likes_count",
            "unlikes_count",
            "created_time",
        )

    @staticmethod
    def get_likes_count(obj):
        return obj.postlikes.filter(status=PostLike.StatusChoices.LIKE).count()

    @staticmethod
    def get_unlikes_count(obj):
        return obj.postlikes.filter(status=PostLike.StatusChoices.UNLIKE).count()


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "image")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "image")


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ["status"]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        author = self.context["request"].user
        post = self.context.get("post")

        if PostLike.objects.filter(author=author, post=post).exists():
            raise serializers.ValidationError("You have already liked this post.")

        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "username",
            "city",
            "birth_date",
            "avatar",
            "posts",
            "followers_count",
        ]

    @staticmethod
    def get_followers_count(obj):
        return obj.followings.count()

    def get_is_following(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            user = request.user
            return obj.followings.filter(id=user.profile.id).exists()
        return False


class ProfileSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "username"]


class ProfileNoPostSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "username",
            "city",
            "birth_date",
            "avatar",
            "followers_count",
        ]

    @staticmethod
    def get_followers_count(obj):
        return obj.followings.count()

    def get_is_following(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            user = request.user
            return obj.followings.filter(id=user.profile.id).exists()
        return False


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("user", "username", "city", "birth_date", "avatar")


class ProfileFollowAddSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="id")
    is_following = serializers.SerializerMethodField()

    def get_username(self, obj):
        user = self.context.get("request").user
        if user.is_authenticated:
            return user.profile.username
        return None

    def get_is_following(self, obj):
        user = self.context["request"].user
        return obj.followings.filter(id=user.profile.id).exists()

    class Meta:
        model = Profile
        fields = ["profile_id", "username", "is_following"]


class LikedPostsSerializer(serializers.ModelSerializer):
    postlike = PostLikeSerializer(source="postlikes", many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("id", "owner", "title", "postlike")
