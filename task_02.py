#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

WRDLENGTH = len("Spanish")

STARTSLICE = inquisition.SPANISH.index("Spanish")

ENDSLICE = STARTSLICE + WRDLENGTH

FOUNDYOU = inquisition.SPANISH[STARTSLICE:ENDSLICE]

FLEMISH = inquisition.SPANISH.replace(FOUNDYOU, "Flemish")
