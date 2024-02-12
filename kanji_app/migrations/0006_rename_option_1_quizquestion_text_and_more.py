# Generated by Django 5.0.2 on 2024-02-12 01:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanji_app', '0005_studylist'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizquestion',
            old_name='option_1',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='kanji',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='option_2',
        ),
        migrations.RemoveField(
            model_name='quizquestion',
            name='option_3',
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='choices',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='matches',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='question_type',
            field=models.CharField(choices=[('multiple_choice', 'Multiple Choice'), ('fill_in_the_blank', 'Fill in the Blank'), ('matching', 'Matching')], default='multiple_choice', max_length=50),
        ),
        migrations.CreateModel(
            name='PremadeStudyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('kanjis', models.ManyToManyField(to='kanji_app.kanji')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('level', models.IntegerField()),
                ('kanjis', models.ManyToManyField(to='kanji_app.kanji')),
                ('study_list', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kanji_app.studylist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='kanji_app.quiz'),
        ),
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]