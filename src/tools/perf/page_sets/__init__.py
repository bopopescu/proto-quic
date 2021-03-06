# Copyright 2014 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import inspect
import os
import sys

from telemetry.core import discover
from telemetry import story
from telemetry.story import expectations


# Import all submodules' PageSet classes.
start_dir = os.path.dirname(os.path.abspath(__file__))
top_level_dir = os.path.dirname(start_dir)
base_classes = [story.StorySet, expectations.StoryExpectations]

for base_class in base_classes:
  for cls in discover.DiscoverClasses(
      start_dir, top_level_dir, base_class).values():
    setattr(sys.modules[__name__], cls.__name__, cls)
