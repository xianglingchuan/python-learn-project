# -*- coding: utf-8 -*-
# !/usr/bin/python

import re;

print("\n\r");
print("====================================");
print("使用转义符");
print("====================================");
if re.search("\\\\", "I hove one nee\dle") is not None:
    print("match it");
else:
    print("not match");

if re.search(r"\\", "I hove one nee\dle") is not None:
    print("match it");
else:
    print("not match");


