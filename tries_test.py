# File: tries_test.py_compile

from unittest import TestCase, main
from tries import Trie


class TestTries(TestCase):

    def test_len(self):
        t: Trie[int] = Trie()
        self.assertEqual(0, len(t))
        t.insert('bit', 0)
        self.assertEqual(1, len(t))
        t.insert('bicycle', 2)
        self.assertEqual(2, len(t))
        t.insert('bit', 1)
        self.assertEqual(2, len(t))
        t.insert('byte', 8)
        self.assertEqual(3, len(t))
        t.insert('byte', 16)
        self.assertEqual(3, len(t))
        self.assertTrue(t.remove('bit'))
        self.assertEqual(2, len(t))
        self.assertFalse(t.remove('bit'))
        self.assertEqual(2, len(t))
        self.assertTrue(t.remove('bicycle'))
        self.assertEqual(1, len(t))
        self.assertTrue(t.remove('byte'))
        self.assertEqual(0, len(t))
        self.assertFalse(t.remove('byte'))

    def test_items(self):
        t: Trie[int] = Trie()
        self.assertEqual([], t.items())
        t.insert('hello', 1)
        self.assertEqual([('hello', 1)], t.items())
        t.insert('a', 2)
        self.assertEqual([('a', 2), ('hello', 1)], t.items())
        t.insert('hellen', 3)
        self.assertEqual([('a', 2), ('hellen', 3), ('hello', 1)],
                         t.items())
        t.insert('an', 4)
        self.assertEqual([('a', 2), ('an', 4), ('hellen', 3),
                          ('hello', 1)],
                         t.items())
        t.insert('he', 5)
        self.assertEqual([('a', 2), ('an', 4), ('he', 5),
                          ('hellen', 3), ('hello', 1)],
                         t.items())
        t.insert('ant', 6)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('he', 5), ('hellen', 3), ('hello', 1)],
                         t.items())
        t.insert('help', 7)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('he', 5), ('hellen', 3), ('hello', 1),
                          ('help', 7)],
                         t.items())
        t.insert('antivirus', 8)
        self.assertEqual([('a', 2),  ('an', 4), ('ant', 6),
                          ('antivirus', 8), ('he', 5), ('hellen', 3),
                          ('hello', 1), ('help', 7)],
                         t.items())
        t.insert('at', 9)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('antivirus', 8), ('at', 9), ('he', 5),
                          ('hellen', 3), ('hello', 1), ('help', 7)],
                         t.items())
        t.insert('hell', 10)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('antivirus', 8), ('at', 9), ('he', 5),
                          ('hell', 10), ('hellen', 3), ('hello', 1),
                          ('help', 7)],
                         t.items())
        t.insert('antilope', 11)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('antilope', 11), ('antivirus', 8),
                          ('at', 9), ('he', 5), ('hell', 10),
                          ('hellen', 3), ('hello', 1), ('help', 7)],
                         t.items())
        t.insert('her', 12)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('antilope', 11), ('antivirus', 8),
                          ('at', 9), ('he', 5), ('hell', 10),
                          ('hellen', 3), ('hello', 1),
                          ('help', 7), ('her', 12)],
                         t.items())
        t.insert('antique', 13)
        self.assertEqual([('a', 2), ('an', 4), ('ant', 6),
                          ('antilope', 11), ('antique', 13),
                          ('antivirus', 8), ('at', 9), ('he', 5),
                          ('hell', 10), ('hellen', 3), ('hello', 1),
                          ('help', 7), ('her', 12)],
                         t.items())

    def test_prefixes(self):
        t: Trie[int] = Trie()
        self.assertEqual({}, t.prefixes())
        t.insert('hello', 1)
        self.assertEqual({}, t.prefixes())
        t.insert('a', 2)
        self.assertEqual({}, t.prefixes())
        t.insert('hellen', 3)
        self.assertEqual({}, t.prefixes())
        t.insert('an', 4)
        self.assertEqual({'a': {'an'}}, t.prefixes())
        t.insert('he', 5)
        self.assertEqual({'a': {'an'}, 'he': {'hellen', 'hello'}},
                         t.prefixes())
        t.insert('ant', 6)
        self.assertEqual({'an': {'ant'}, 'a': {'an', 'ant'},
                          'he': {'hellen', 'hello'}},
                         t.prefixes())
        t.insert('help', 7)
        self.assertEqual({'an': {'ant'}, 'a': {'ant', 'an'},
                          'he': {'hello', 'hellen', 'help'}},
                         t.prefixes())
        t.insert('antivirus', 8)
        self.assertEqual({'a': {'antivirus', 'ant', 'an'},
                          'an': {'antivirus', 'ant'},
                          'ant': {'antivirus'},
                          'he': {'hello', 'hellen', 'help'}},
                         t.prefixes())
        t.insert('at', 9)
        self.assertEqual({'a': {'at', 'antivirus', 'an', 'ant'},
                          'an': {'antivirus', 'ant'},
                          'ant': {'antivirus'},
                          'he': {'help', 'hello', 'hellen'}},
                         t.prefixes())
        t.insert('hell', 10)
        self.assertEqual({'a': {'an', 'at', 'antivirus', 'ant'},
                          'an': {'antivirus', 'ant'},
                          'ant': {'antivirus'},
                          'he': {'hello', 'hell', 'help', 'hellen'},
                          'hell': {'hello', 'hellen'}},
                         t.prefixes())
        t.insert('antilope', 11)
        self.assertEqual({'a': {'antilope', 'ant', 'antivirus',
                                'an', 'at'},
                          'an': {'antilope', 'ant', 'antivirus'},
                          'ant': {'antilope', 'antivirus'},
                          'he': {'hello', 'hellen', 'help', 'hell'},
                          'hell': {'hellen', 'hello'}},
                         t.prefixes())
        t.insert('her', 12)
        self.assertEqual({'a': {'an', 'at', 'antilope', 'ant',
                                'antivirus'},
                          'an': {'antivirus', 'antilope', 'ant'},
                          'ant': {'antivirus', 'antilope'},
                          'he': {'hellen', 'hello', 'hell', 'her',
                                 'help'},
                          'hell': {'hellen', 'hello'}},
                         t.prefixes())
        t.insert('antique', 13)
        self.assertEqual({'a': {'antilope', 'at', 'antique',
                                'antivirus', 'an', 'ant'},
                          'an': {'antilope', 'antique', 'antivirus',
                                 'ant'},
                          'ant': {'antilope', 'antique',
                                  'antivirus'},
                          'he': {'her', 'hello', 'hell', 'help',
                                 'hellen'},
                          'hell': {'hellen', 'hello'}},
                         t.prefixes())


if __name__ == '__main__':
    main()