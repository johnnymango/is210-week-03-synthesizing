#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

WRDLENGTH = len("Spanish")

STARTSLICE = inquisition.SPANISH.index("Spanish")

ENDSLICE = STARTSLICE + WRDLENGTH

FIRSTPART = inquisition.SPANISH[:STARTSLICE]

LASTPART = inquisition.SPANISH[ENDSLICE:]

FLEMISH = FIRSTPART + 'Flemish' + LASTPART