import pymash

site = pymash.html()
site.add_line("h1","hello world")

site.complile()

site.run('0.0.0.0')