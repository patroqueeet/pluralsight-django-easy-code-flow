#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf import settings


def version(request):
    """ make app version available in template """
    version = getattr(
        settings, "VERSION", 'error: version not configured')
    res = dict(
        VERSION=version,
    )
    return res
