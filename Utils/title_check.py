def check_title(driver, expected_title):
    titulo = driver.find_element("css selector", "div.header_secondary_container .title").text
    assert titulo == expected_title, f"Título esperado '{expected_title}', pero fue '{titulo}'"
    print(f"Título OK → {titulo}")
