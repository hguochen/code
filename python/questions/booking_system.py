class UserManager(models.Manager):
    def get_query_set(self):
        return AlbumQuerySet(self.model)

    def desc_user_age(self):
        return self.get_query_set().desc_user_age()
    # ...

class UserQuerySet(QuerySet):
    """docstring for UserQuerySet"""
    def desc_user_age(self):
        return self.filter(user_age__year=timezone.now().year()).order_by('-user_age')
    ...
        
        
class User(models.Model):
    """
    Model Fields for User.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    updated_at = models.DateTimeField('date published', default=timezone.now()) # saved in UTC timezone

    objects = UserManager()


