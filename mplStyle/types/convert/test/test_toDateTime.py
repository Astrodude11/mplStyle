#===========================================================================
#
# Copyright (c) 2014, California Institute of Technology.
# U.S. Government Sponsorship under NASA Contract NAS7-03001 is
# acknowledged.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#===========================================================================

"The toDateTime unit test."

__version__ = "$Revision: #1 $"

#===========================================================================
# Reqmtypes.ed imports.  Do not modify these.
import unittest

#===========================================================================
# Place all imports after here.
#
import os
import datetime
import mplStyle.types.convert as cvt
#
# Place all imports before here.
#===========================================================================

#===========================================================================


class TesttoDateTime(unittest.TestCase):
    """toDateTime module."""

    #-----------------------------------------------------------------------
    def setUp(self):
        """This method is called before any tests are run."""

        # You may place initialization code here.

    #-----------------------------------------------------------------------
    def tearDown(self):
        """This method is called after all tests are run."""
        pass
    #=======================================================================
    # Add tests methods below.
    # Any method whose name begins with 'test' will be run by the framework.
    #=======================================================================

    def testtoDateTime(self):
        """Test the toDateTime converter."""
        converter = cvt.toDateTime

        s = "4-mar-2004 12:13:14.1234 ET"
        right = datetime.datetime(2004, 3, 4, 12, 13, 14, 123400)

        t = converter(right)
        self.assertEqual(right, t, "Incorrect conversion of an Epoch.")

        t = converter(right)
        self.assertEqual(right, t, "Incorrect conversion of a datetime.")

        right = datetime.datetime(2004, 3, 4)
        t = converter(datetime.date(2004, 3, 4))
        self.assertEqual(right, t, "Incorrect conversion of a date.")

        self.assertRaises(Exception, converter, None, name='value',
                          msg="None argument should be an error.")
        self.assertRaises(Exception, converter, "foo bar", name='value',
                          msg="String argument should be an error.")
        self.assertRaises(Exception, converter, [1, 2, 3], name='value',
                          msg="List argument should be an error.")

        # Try w/ allowNone
        t = converter(None, allowNone=True)
        self.assertEqual(None, t, "Incorrect conversion of None.")

#=======================================================================
