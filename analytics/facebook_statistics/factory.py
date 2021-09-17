import factory
from faker import Faker
from django.utils import timezone

fake = Faker()


class PostFactory(factory.django.DjangoModelFactory):
    user_id = fake.pyint()
    post_id = fake.pyint()
    likes_count = fake.pyint()
    # created = factory.LazyFunction(lambda: faker.date_between_dates(
    #     start=timezone.now() - timedelta(days=40), end=timezone.now()
    # ))

    class Meta:
        model = 'facebook_statistics.Post'
