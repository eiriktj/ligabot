import pytest

@pytest.fixture
def example_altomfotball_match1_html():
    return """
        <tr class="sd_odd">
            <td class="sd_fixtures_date">
                <span>01.01.2000</span>
            </td>
            <td class="sd_fixtures_round">
                <span>1. runde</span>
            </td>
            <td class="sd_fixtures_tournament">
                <a href="">Eksempelserien</a>
            </td>
            <td class="sd_fixtures_home">
                <a href="">Lagen</a>
            </td>
            <td class="sd_fixtures_score">
                <a href="" class="sd_fixtures_score">1&nbsp;-&nbsp;4</a>
            </td>
            <td class="sd_fixtures_away">
                <a href="">Lagto</a>
            </td>
            <td class="sd_fixtures_channels">
                <span>Kanalen</span>
            </td>
            <td class="sd_fixtures_sumo">
                &nbsp;
            </td>
        </tr>
    """

@pytest.fixture
def example_altomfotball_match2_html():
    return """
        <tr class="sd_even">
            <td class="sd_fixtures_date">
                <span>&nbsp;</span>
            </td>
            <td class="sd_fixtures_round">
                <span>1. runde</span>
            </td>
            <td class="sd_fixtures_tournament">
                <a href="">Eksempelserien</a>
            </td>
            <td class="sd_fixtures_home">
                <a href="">Lagtre</a>
            </td>
            <td class="sd_fixtures_score">
                <a href="" class="sd_fixtures_score">1&nbsp;-&nbsp;2</a>
            </td>
            <td class="sd_fixtures_away">
                <a href="">Lagfire</a>
            </td>
            <td class="sd_fixtures_channels">
                <span>Kanalto</span>
            </td>
            <td class="sd_fixtures_sumo">
                &nbsp;
            </td>
        </tr>
    """

@pytest.fixture
def example_altomfotball_match3_html():
    return """
        <tr class="sd_odd">
            <td class="sd_fixtures_date">
                <span>01.01.2050</span>
            </td>
            <td class="sd_fixtures_round">
                <span>2. runde</span>
            </td>
            <td class="sd_fixtures_tournament">
                <a href="">Eksempelserien</a>
            </td>
            <td class="sd_fixtures_home">
            <a href="">Lagto</a>
            </td>
            <td class="sd_fixtures_score">
                <a href="" class="sd_fixtures_score">(1&nbsp;-&nbsp;0)</a>
            </td>
            <td class="sd_fixtures_away">
                <a href="">Lagen</a>
            </td>
            <td class="sd_fixtures_channels">
                <span>Kanalen</span>
            </td>
            <td class="sd_fixtures_sumo">
                &nbsp;
            </td>
        </tr>
    """

@pytest.fixture
def example_altomfotball_match4_html():
    return """
        <tr class="sd_even">
            <td class="sd_fixtures_date">
                <span>01.01.2100</span>
            </td>
            <td class="sd_fixtures_round">
                <span>3. runde</span>
            </td>
            <td class="sd_fixtures_tournament">
                <a href="">Eksempelserien</a>
            </td>
            <td class="sd_fixtures_home">
                <a href="">Lagfire</a>
            </td>
            <td class="sd_fixtures_score">
            <a href="" class="sd_fixtures_score">20.00</a>
            </td>
            <td class="sd_fixtures_away">
                <a href="">Lagtre</a>
            </td>
            <td class="sd_fixtures_channels">
                <span>Kanalto</span>
            </td>
            <td class="sd_fixtures_sumo">
                &nbsp;
            </td>
        </tr>
    """

@pytest.fixture
def example_altomfotball_matchweeks_html(
    example_altomfotball_match1_html,
    example_altomfotball_match2_html,
    example_altomfotball_match3_html,
    example_altomfotball_match4_html,
):
    table_and_tbody_start_html = """
<table class="sd_fixtures" id="sd_fixtures_table" summary="Kamper">
    <tbody>
    """
    table_and_tbody_end_html = """
    </tbody>
</table>
    """

    return (
        table_and_tbody_start_html +
        example_altomfotball_match1_html +
        example_altomfotball_match2_html +
        example_altomfotball_match3_html +
        example_altomfotball_match4_html +
        table_and_tbody_end_html
    )
