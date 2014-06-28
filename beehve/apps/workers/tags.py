from taggit.models import TagBase, GenericTaggedItemBase

class TechTag(TagBase):
    class Meta:
        verbose_name = _('Tech Tag')
        verbose_name_plural = _('Tech Tags')


class TaggedProject(GenericTaggedItemBase):
    tag = models.ForeignKey(
        TechTag,
        related_name="%(app_labels_%(class_items")
    pass

