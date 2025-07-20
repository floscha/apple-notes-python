import pytest

from apple_notes import api, model


TEST_FOLDER_NAME = "__test__"


def test_create_folder():
    api.create_folder(TEST_FOLDER_NAME)

def test_created_folder_is_empty():
    notes_in_folder = api.get_notes_in_folder(TEST_FOLDER_NAME)

    assert notes_in_folder == []

def test_create_note():
    api.create_note("test_note", "test text", TEST_FOLDER_NAME)

def test_created_folder_contains_one_note():
    notes_in_folder = api.get_notes_in_folder(TEST_FOLDER_NAME)

    assert notes_in_folder == [model.Note("test_note")]
    
def test_delete_note():
    api.delete_note("test_note")

def test_delete_folder():
    api.delete_folder(TEST_FOLDER_NAME)

def test_delete_non_existing_folder_raises_exception():
    with pytest.raises(Exception) as excinfo:
        api.delete_folder(TEST_FOLDER_NAME)
    assert "Notes got an error: Can’t get folder \"__test__\" of account \"iCloud\"." in str(excinfo.value)