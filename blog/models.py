from django.db import models

# post 실제 포스트 할 클래스 DB 변수 설정
class Post(models.Model):
    title=models.CharField(max_length=100)
    # 100자 까지 담을 수 있는 문자 필드
    content = models.TextField()
    # 포스팅 내용 (content) 길이 제한이 없는 문자 필드
    photo = models.ImageField()
    # 사진 이미지 필드
    created_at=models.DateTimeField(auto_now_add=True)
    # 최초 생성 시간이 자동으로 올라감
    update_at = models.DateTimeField(auto_now=False)
    # 마지막 수정 시간도 자동으로 올라감

    # Post object (1),(2),(3)과 같은 정보를 타이틀 이름으로 바꿔줌
    def __str__(self):
        return self.title

# commit 클래스 모듈
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    #포스트와 코멘트는 1:N의 관계라서 ForeignKey를 사용하여 관계를 형성
    messages = models.TextField()
    #mmessages 는 길이 제한이 없는 텍스트 필드
