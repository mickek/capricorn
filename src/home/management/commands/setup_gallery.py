#!/usr/bin/env python2.5
# -*- coding: utf-8 -*-
import os
import Image
from django.utils import simplejson
from django.core.management.base import BaseCommand

SIZE = (500, 500)

class Command(BaseCommand):    
    
    def handle(self, **options):

        src_path = "media/src_galery/"
        target_path = "media/galery/"

        IMAGES = []

        os.system("rm %s*" % target_path)

        for i,f in enumerate(os.listdir(src_path)):

            print 'processing', f

            img = Image.open(os.path.join(src_path, f))
            thumb = img.copy()
            thumb.thumbnail(SIZE, Image.ANTIALIAS)
            fname = os.path.join(target_path, "%s.jpg" % i)
            IMAGES.append("%s.jpg" % i)
            thumb.save(fname, "JPEG", quality=90)

        arr = simplejson.dumps(IMAGES)
        fp = open("home/gallery.py", "w")
        fp.write("GALLERY = %s" % arr)
        fp.close()

