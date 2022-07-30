#!/usr/bin/env python3

import re

trollspeak = "ACDEFHILMNORSTUW"
trollregex = re.compile(f"({'|'.join(trollspeak)})+")
