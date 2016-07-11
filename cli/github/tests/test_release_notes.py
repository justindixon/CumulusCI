import unittest
from github.release_notes import BaseReleaseNotesGenerator
from github.release_notes import ReleaseNotesGenerator
from github.release_notes import ChangeNotesLinesParser


class DummyParser(object):

    def parse(self, change_note):
        pass

    def render(self):
        return 'dummy parser output'


class TestBaseReleaseNotesGenerator(unittest.TestCase):

    def test_render_no_parsers(self):
        release_notes = BaseReleaseNotesGenerator()
        content = release_notes.render()
        assert content == ''

    def test_render_dummy_parsers(self):
        release_notes = BaseReleaseNotesGenerator()
        release_notes.parsers.append(DummyParser())
        release_notes.parsers.append(DummyParser())
        content = release_notes.render()
        assert content == 'dummy parser output\r\ndummy parser output'


class TestReleaseNotesGenerator(unittest.TestCase):

    def test_init_parser(self):
        release_notes = ReleaseNotesGenerator()
        assert len(release_notes.parsers) == 3


class TestBaseChangeNotesParser(unittest.TestCase):
    pass


class TestChangeNotesLinesParser(unittest.TestCase):

    def test_init_empty_start_line(self):
        pass

    def test_parse_no_start_line(self):
        start_line = '# Start Line'
        change_note = 'foo\r\nbar\r\n'
        parser = ChangeNotesLinesParser(None, None, start_line)
        parser.parse(change_note)
        assert parser.content == []

    def test_parse_start_line_no_content(self):
        start_line = '# Start Line'
        change_note = '{}\r\n\r\n'.format(start_line)
        parser = ChangeNotesLinesParser(None, None, start_line)
        parser.parse(change_note)
        assert parser.content == []

    def test_parse_start_line_no_end_line(self):
        start_line = '# Start Line'
        change_note = '{}\r\nfoo\r\nbar'.format(start_line)
        parser = ChangeNotesLinesParser(None, None, start_line)
        parser.parse(change_note)
        assert parser.content == ['foo', 'bar']

    def test_parse_start_line_no_content_no_end_line(self):
        pass

    def test_parse_multiple_start_lines_without_end_lines(self):
        pass

    def test_parse_multiple_start_lines_with_end_lines(self):
        pass

    def test_render_no_content(self):
        pass

    def test_render_one_content(self):
        pass

    def test_render_multiple_content(self):
        pass


class TestGithubIssuesParser(unittest.TestCase):
    pass
