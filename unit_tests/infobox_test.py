import os
import re
import sys
import unittest

BASE_DIR = os.path.realpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '..'))

sys.path.append(BASE_DIR)
from patterns import REGEX  # pylint: disable=C0413

INFOBOX = REGEX[0]


def readfile(filename):
    with open(os.path.join(BASE_DIR, 'unit_tests/file/infobox/{0}.txt'.format(filename)), encoding='utf-8') as f:
        result = f.read()
    return result


class TestInfoboxMethods(unittest.TestCase):

    def test_all(self):
        test_cnt = 3
        imagename = 'Example image.png'
        imagename_new = 'Example image new.png'
        imageregex = "[" + imagename[0].upper() + \
            imagename[0].lower() + "]" + re.escape(imagename[1:])
        imageregex = imageregex.replace("\\ ", "[ _]")
        regex = INFOBOX['pattern'].format(imageregex)

        for fid in range(1, test_cnt + 1):
            with self.subTest(fid=fid):
                text = readfile('{0}_in'.format(fid))

                # existother = 'en'
                existothername = '英文維基百科'

                # comment_other
                replace = INFOBOX['replace']['comment_other'].format(
                    existothername)
                output1 = re.sub(regex, replace, text, flags=re.M)
                output2 = readfile('{0}_comment_other'.format(fid))
                self.assertEqual(output1, output2)

                # moved
                replace = INFOBOX['replace']['moved'].format(imagename_new)
                output1 = re.sub(regex, replace, text, flags=re.M)
                output2 = readfile('{0}_moved'.format(fid))
                self.assertEqual(output1, output2)

                # deleted_comment
                replace = INFOBOX['replace']['deleted_comment']
                output1 = re.sub(regex, replace, text, flags=re.M)
                output2 = readfile('{0}_deleted_comment'.format(fid))
                self.assertEqual(output1, output2)

                # deleted
                replace = INFOBOX['replace']['deleted']
                output1 = re.sub(regex, replace, text, flags=re.M)
                output2 = readfile('{0}_deleted'.format(fid))
                self.assertEqual(output1, output2)

                # comment
                replace = INFOBOX['replace']['comment']
                output1 = re.sub(regex, replace, text, flags=re.M)
                output2 = readfile('{0}_comment'.format(fid))
                self.assertEqual(output1, output2)


if __name__ == '__main__':
    unittest.main()
