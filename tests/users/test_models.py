import pytest


def test_user_str(base_user):
    """Test the custom user model string representation"""
    assert base_user.__str__() == f"{base_user.first_name}"


def test_user_full_name(base_user):
    """Test that the user models get_full_name method works"""
    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name


def test_base_user_email_is_normalized(base_user):
    """Test that a new users email is normalized"""
    email = "admIn@GMAIL.COM"
    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(super_user):
    """Test that an admin users email is normalized"""
    email = "AdmIn@GmAIL.COM"
    assert super_user.email == email.lower()


def test_super_user_is_not_staff(user_factory):
    """Test that an error is raised when an admin user has is_staff set to false"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)
    assert str(err.value) == "Superusers must have is_staff=True"


def test_super_user_is_not_superuser(user_factory):
    """Test that an error is raised when an admin user has is_superuser set to False"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)
    assert str(err.value) == "Superusers must have is_superuser=True"


# def test_super_user_is_not_admin(user_factory):
#     """Test that an error is raised when an admin user has is_mainadmin set to False"""
#     with pytest.raises(ValueError) as err:
#         user_factory.create(is_mainadmin=False, is_staff=False)
#     assert str(err.value) == "User must set role_type True for admin employee account registration"


# def test_super_user_is_not_manager(user_factory):
#     """Test that an error is raised when an manager user has is_manager set to False"""
#     with pytest.raises(ValueError) as err:
#         user_factory.create(is_manager=False, is_staff=False)
#     assert str(err.value) == "User must set role_type True for manager employee account registration"


# def test_super_user_is_not_accountant(user_factory):
#     """Test that an error is raised when an accountant user has is_accountant set to False"""
#     with pytest.raises(ValueError) as err:
#         user_factory.create(is_accountant=False, is_staff=False)
#     assert str(err.value) == "User must set role_type True for accountant employee account registration"


# def test_super_user_is_not_salesman(user_factory):
#     """Test that an error is raised when an salesman user has is_salesman set to False"""
#     with pytest.raises(ValueError) as err:
#         user_factory.create(is_salesman=False, is_staff=False)
#     assert str(err.value) == "User must set role_type True for salesman employee account registration"


# def test_super_user_is_not_customer(user_factory):
#     """Test that an error is raised when an customer user has is_customer set to False"""
#     with pytest.raises(ValueError) as err:
#         user_factory.create(is_customer=False, is_staff=False)
#     assert str(err.value) == "User must set role_type True for customer account registration"




def test_create_user_with_no_email(user_factory):
    """Test that creating a new user with no email address raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)
    assert str(err.value) == "Base User Account: An email address is required"


def test_create_user_with_no_firstname(user_factory):
    """Test creating a new user without a firstname raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)
    assert str(err.value) == "Users must submit a first name"


def test_create_user_with_no_lastname(user_factory):
    """Test creating a new user without a lastname raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)
    assert str(err.value) == "Users must submit a last name"


def test_create_superuser_with_no_email(user_factory):
    """Test creating a superuser without an email address raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email=None, is_superuser=True, is_staff=True)
    assert str(err.value) == "Admin Account: An email address is required"


def test_create_superuser_with_no_password(user_factory):
    """Test creating a superuser without a password raises an error"""
    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=True, password=None)
    assert str(err.value) == "Superusers must have a password"


def test_user_email_incorrect(user_factory):
    """Test that an Error is raised when a non valid email is provided"""
    with pytest.raises(ValueError) as err:
        user_factory.create(email="realestate.com")
    assert str(err.value) == "You must provide a valid email address"