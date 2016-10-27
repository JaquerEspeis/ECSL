from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class QuestionCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    emoji_alt = models.CharField(max_length=5, blank=True,
                                 verbose_name=_("Emoticon"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    @property
    def data_emoji_alt(self):
        if not self.emoji_alt:
            return ''
        return format_html('data-emoji-alt="{}"', self.emoji_alt)

    def get_absolute_url(self):
        return reverse('faq:list') + '#category-{}'.format(self.pk)


class Question(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("Question"))
    answer = models.TextField(blank=True, verbose_name=_("Answer"))
    category = models.ForeignKey(QuestionCategory, blank=True, null=True,
                                 verbose_name=_("Category"))
    published = models.BooleanField(default=False, verbose_name=_("Published"))
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name=_("Created"))

    def __str__(self):
        return self.question

    def has_answer(self):
        return bool(self.answer)

    def get_absolute_url(self):
        return reverse('faq:list') + '#question-{}'.format(self.pk)
