from app import home


def test_home():
    result = home()

    assert result["message"] == "Welcome to our DevSecOps project!"
    assert result["status"] == "success"
