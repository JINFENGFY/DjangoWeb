from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from learning_log.models import LearningContent


# Create your models here.
# 评论模型
class Comment (MPTTModel):
    comnum = models.AutoField (primary_key=True)
    commentcontent = RichTextField (verbose_name=u'评论内容')
    created = models.DateTimeField (auto_now_add=True, verbose_name=u'创建时间')
    owner = models.ForeignKey (User,
                               on_delete=models.CASCADE,
                               verbose_name=u'所有者',
                               related_name='comments'
                               )
    learning_log = models.ForeignKey (LearningContent,
                                      on_delete=models.CASCADE,
                                      verbose_name=u'所有贴',
                                      related_name='comments'
                                      )

    # mptt树形结构
    parent = TreeForeignKey ('self',
                             on_delete=models.CASCADE,
                             null=True, blank=True,
                             related_name='children',
                             verbose_name=u'父级评论'
                             )
    # 记录二级评论回复给谁
    reply_to = models.ForeignKey (User,
                                  null=True, blank=True,
                                  on_delete=models.CASCADE,
                                  related_name='replyers',
                                  verbose_name=u'依赖评论'
                                  )

    class MPTTMeta:
        order_insertion_by = ['created']

    def __str__(self):
        return self.commentcontent[:20]
