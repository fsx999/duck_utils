# coding=utf-8
from django.apps import AppConfig


class DuckUtils(AppConfig):
    name = "duck_utils"
    label = "duck_utils"

    collapse_settings = [{
        "group_label": "Duck_Utils",
        "icon": 'fa-fw fa fa-circle-o',
        "entries": [{
            "label": 'Etapes settings  ',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/duck_utils/etapesettings/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Salles',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/duck_utils/salle/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }, {
            "label": 'Propertys',
            "icon": 'fa-fw fa fa-circle-o',
            "url": '/duck_utils/property/',  # name or url
            "groups_permissions": [],  # facultatif
            "permissions": [],  # facultatif
        }],

        "groups_permissions": [],  # facultatif
        "permissions": [],  # facultatif
    }, ]