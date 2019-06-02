

import re

no_space = re.compile('[^\s]+')

quotation = re.compile('\"[^\s][^"]+[^\s]\"')

two_number = re.compile('(-?[0-9]+(\.[0-9]+)?)(,|, | )(-?[0-9]+(\.[0-9]+)?)')

likely_name = re.compile('([A-Z][a-z|\.]+)( )([A-Z][a-z]+)(( )([A-Z][a-z]*))?')

# I looked at the cheat sheet thing on pythex so i used \s instead of \n for the white space part
