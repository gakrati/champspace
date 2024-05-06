
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()
# Initialize Faker
fakegen = Faker()
topics = ['search', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    acc_records = []  # Initialize acc_records list
    try:
        for entry in range(N):
            top = add_topic()
            fake_url = fakegen.url()
            fake_date = fakegen.date()
            fake_name = fakegen.company()

            # Create Webpage and AccessRecord instances directly
            webpage = Webpage.objects.create(topic=top, url=fake_url, name=fake_name)
            acc_record = AccessRecord.objects.create(webpage=webpage, date=fake_date)
            acc_records.append(acc_record)

        # Bulk create outside the loop
        AccessRecord.objects.bulk_create(acc_records)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ =='__main__':
    print("Populating script:")
    populate(20)
    print("Populating completed")
