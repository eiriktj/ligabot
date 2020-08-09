from ligabot.data.storage_interface import StorageInterface
from ligabot.domain.match import Match

class StorageAltomfotball(StorageInterface):

    def __init__(self, matchweeks_soup):
        self.matchweeks_soup = matchweeks_soup

    def get_match_rows_soup(self):
        match_rows_soup = self.matchweeks_soup.get_tag_soups('tr')
        return match_rows_soup

    def find_table_data_text_by_css_class(self, match_row_soup, css_class_type):
        tag = 'td'
        css_class_base = 'sd_fixtures_'
        css_class = 'sd_fixtures_' + css_class_type
        table_data_soup = match_row_soup.find_tag_soup_with_class(tag, css_class)
        return table_data_soup.get_text()


    def load_matches(self):

        matches = []

        match_rows_soup = self.get_match_rows_soup()
        for match_row_soup in match_rows_soup:

            match = Match()

            match.date = self.find_table_data_text_by_css_class(match_row_soup, 'date')
            match.round = self.find_table_data_text_by_css_class(match_row_soup, 'round')
            match.tournament = self.find_table_data_text_by_css_class(match_row_soup, 'tournament')
            match.home = self.find_table_data_text_by_css_class(match_row_soup, 'home')
            match.score = self.find_table_data_text_by_css_class(match_row_soup, 'score')
            match.away = self.find_table_data_text_by_css_class(match_row_soup, 'away')
            match.channels = self.find_table_data_text_by_css_class(match_row_soup, 'channels')

            matches.append(match)

        return matches
