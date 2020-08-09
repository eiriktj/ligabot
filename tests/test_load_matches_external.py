from ligabot.framework.beautiful_soup_wrapper import SoupWrapper
from ligabot.framework.beautiful_soup_wrapper import TagWrapper
from ligabot.storage.storage_altomfotball import StorageAltomfotball

def test_get_table_data_text(
    example_altomfotball_matchweeks_html,
    example_altomfotball_match1_html
):
    matchweeks_soup = SoupWrapper(example_altomfotball_matchweeks_html)
    storage = StorageAltomfotball(matchweeks_soup)
    match1_soup = SoupWrapper(example_altomfotball_match1_html)
    match1_tag_soup = TagWrapper(match1_soup.soup)
    match1_date = storage.find_table_data_text_by_css_class(match1_tag_soup, 'date')
    match1_date_strip_newline = match1_date.strip('\n')

    assert match1_date_strip_newline == "01.01.2000"

def test_load_matches_altomfotball(example_altomfotball_matchweeks_html):
    matchweeks_soup = SoupWrapper(example_altomfotball_matchweeks_html)
    storage = StorageAltomfotball(matchweeks_soup)
    matches = storage.load_matches()

    assert len(matches) == 4

    match1 = matches[0]

    assert match1.date.strip('\n') == "01.01.2000"
    assert match1.round.strip('\n') == "1. runde"
    assert match1.tournament.strip('\n') == "Eksempelserien"
    assert match1.home.strip('\n') == "Lagen"
    #assert match1.score.strip('\n') == "1&nbsp;-&nbsp;4"
    assert match1.away.strip('\n') == "Lagto"
    assert match1.channels.strip('\n') == "Kanalen"
