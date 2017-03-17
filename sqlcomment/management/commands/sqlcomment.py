import re

from django.core.management.base import AppCommand
from django.db.models.fields.related import (
    ManyToOneRel, ManyToManyRel, ManyToManyField, ForeignKey,
)


def fix(s):
    return re.sub(r'\s', ' ', s)


class Command(AppCommand):
    def handle_app_config(self, app_config, **options):
        for model in app_config.get_models(include_auto_created=True):
            print ('COMMENT ON TABLE "%s" IS \'%s\';' % (
                model._meta.db_table,
                fix(model._meta.verbose_name).replace("'", "''"),
            )).encode('UTF-8')
            for i, f in enumerate(p for p in model._meta.get_fields()
                                  if not isinstance(p, (ManyToOneRel,
                                                        ManyToManyField,
                                                        ManyToManyRel))):
                print ('COMMENT ON COLUMN "%s"."%s" IS \'%s\';' % (
                    model._meta.db_table,
                    f.name + ('_id' if isinstance(f, ForeignKey) else ''),
                    fix(getattr(f, 'verbose_name', '').replace("'", "''")),
                )).encode('UTF-8')
