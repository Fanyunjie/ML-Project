from django.db import models


class all_data(models.Model):
    author = models.TextField(max_length=5000, verbose_name='作者', blank=True, null=True)
    content = models.TextField(max_length=5000, verbose_name='内容')
    date = models.TextField(max_length=100, verbose_name='日期')
    entities = models.TextField(max_length=5000, verbose_name='实体')
    title = models.TextField(max_length=5000, verbose_name='题目')
    type = models.CharField(max_length=100, verbose_name='种类标签')

    class Meta:
        verbose_name = '整合数据信息'
        verbose_name_plural = '整合数据信息'

    def __str__(self):
        return self.title


# class research_papers(models.Model):
#     date = models.CharField(max_length=100, verbose_name='发表时间')
#     authors = models.TextField(max_length=5000, verbose_name='作者')
#     title = models.TextField(max_length=5000, verbose_name='标题')
#     abstract = models.TextField(max_length=5000, verbose_name='摘要')
#     ents = models.TextField(max_length=5000, verbose_name='实体', blank=True, null=True)
#
#     class Meta:
#         verbose_name = '科研论文信息'
#         verbose_name_plural = '科研论文信息'
#
#     def __str__(self):
#         return self.title
#
#
# class news(models.Model):
#     date = models.CharField(max_length=100, verbose_name='发表时间')
#     title = models.TextField(max_length=5000, verbose_name='标题')
#     content = models.TextField(max_length=5000, verbose_name='内容')
#     source_url = models.TextField(max_length=5000, verbose_name='来源url')
#     ents = models.TextField(max_length=5000, verbose_name='实体', blank=True, null=True)
#
#     class Meta:
#         verbose_name = '新闻信息'
#         verbose_name_plural = '新闻信息'
#
#     def __str__(self):
#         return self.title
#
#
# class rumors(models.Model):
#     publish_date = models.CharField(max_length=100, verbose_name='发表时间')
#     rumor = models.TextField(max_length=5000, verbose_name='标题')
#     fact = models.TextField(max_length=5000, verbose_name='内容')
#     ents = models.TextField(max_length=5000, verbose_name='实体', blank=True, null=True)
#
#     class Meta:
#         verbose_name = '谣言信息'
#         verbose_name_plural = '谣言信息'
#
#     def __str__(self):
#         return self.rumor
# Create your models here.
