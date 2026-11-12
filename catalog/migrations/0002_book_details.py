from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="book",
            name="year",
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name="book",
            name="categories",
            field=models.ManyToManyField(
                blank=True,
                related_name="books",
                to="catalog.category",
            ),
        ),
    ]
