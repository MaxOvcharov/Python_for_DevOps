# -*- coding: utf-8 -*-

import docutils.core

# All information about reStructeredText is here
# http://docutils.sourceforge.net/docs/user/rst/quickref.html

rest = '''
=======
Heading
=======
SubHeading
----------
This is just a simple
little subsection. Now,
we'll show a bulleted list:

- item one
- item two
- item three
'''

html = docutils.core.publish_string(source=rest, writer_name='html')
print html[html.find('<body>') + 6:html.find('</body>')]
