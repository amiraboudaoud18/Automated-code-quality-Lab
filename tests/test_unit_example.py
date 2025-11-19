# our unit test will test the items list management 

from app import items


def test_items_list_operations():
    # reset list for test
    items.clear()

    # Simulate adding
    items.append("item1")
    items.append("item2")
    assert items == ["item1", "item2"]

    # Simulate update
    items[1] = "updated"
    assert items[1] == "updated"

    # Simulate delete
    items.pop(0)
    assert items == ["updated"]
