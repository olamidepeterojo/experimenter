# Generated by Django 2.1.11 on 2019-08-26 19:40

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("experiments", "0068_experiment_related_to")]

    def format_to_new_changelog(apps, schema_editor):
        ExperimentChangeLog = apps.get_model("experiments", "ExperimentChangeLog")
        for changeLog in ExperimentChangeLog.objects.all():
            changed_values = {}
            # ensure change log has new_values
            if changeLog.new_values:
                for key in changeLog.new_values:
                    old_val = changeLog.old_values[key]
                    new_val = changeLog.new_values[key]
                    changed_values[key] = {
                        "display_name": key.replace("_", " ").title(),
                        "old_value": old_val,
                        "new_value": new_val,
                    }
            changeLog.changed_values = changed_values
            changeLog.save()

    operations = [
        migrations.AddField(
            model_name="experimentchangelog",
            name="changed_values",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                encoder=django.core.serializers.json.DjangoJSONEncoder,
                null=True,
            ),
        ),
        migrations.RunPython(format_to_new_changelog),
        migrations.RemoveField(model_name="experimentchangelog", name="new_values"),
        migrations.RemoveField(model_name="experimentchangelog", name="old_values"),
    ]
