#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import apache_log_parser_split


class TestApacheLogParser(unittest.TestCase):

    def setUp(self):
        pass

    def testCombinedExample(self):
        combined_log_entry = '127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700]' \
                             ' "GET /apache_pb.gif HTTP/1.0" 200' \
                             ' 2326 "http://www.example.com/start.html" ' \
                             '"Mozilla/4.08 [en] (Win98; I ;Nav)"'
        self.assertEqual(apache_log_parser_split.dictify_logline(combined_log_entry),
                         {'remote_host': '127.0.0.1', 'status_code': '200', 'bytes_sent': '2326'})

    def testCommonExample(self):
        combined_log_entry = '127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700]' \
                             ' "GET /apache_pb.gif HTTP/1.0" 200 2326'
        self.assertEqual(apache_log_parser_split.dictify_logline(combined_log_entry),
                         {'remote_host': '127.0.0.1', 'status_code': '200', 'bytes_sent': '2326'})

    def testExtraWhitespace(self):
        combined_log_entry = '127.0.0.1     -    frank [10/Oct/2000:13:55:36 -0700]' \
                             ' "GET     /apache_pb.gif HTTP/1.0" 200 2326'
        self.assertEqual(apache_log_parser_split.dictify_logline(combined_log_entry),
                         {'remote_host': '127.0.0.1', 'status_code': '200', 'bytes_sent': '2326'})

    def testMalformed(self):
        combined_log_entry = '127.0.0.1     -    frank [10/Oct/2000:13:55:36 -0700]' \
                             ' "GET     /apache_pb.gif/with white space.html HTTP/1.0" 200 2326'
        self.assertEqual(apache_log_parser_split.dictify_logline(combined_log_entry),
                         {'remote_host': '127.0.0.1', 'status_code': '200', 'bytes_sent': '2326'})

if __name__ == '__main__':
    unittest.main()
