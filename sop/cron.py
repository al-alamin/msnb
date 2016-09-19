from common.models import Tag, Category


def my_scheduled_job():
    print("\n\n\n ******* printing from my scheduled job\n\n\n")
    Category.objects.create(name="new tag from job")