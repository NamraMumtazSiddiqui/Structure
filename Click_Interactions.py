from POM.ClickInteractions import ClickBtnsInteractions

def test_item_group_clicks(driver):
    click_page = ClickBtnsInteractions(driver)
    click_page.item_group_actions(driver)

    assert click_page.disabledbutton() is False, "Disabled button should not be enabled"

    # Click original text button
    click_page.originaltext()
