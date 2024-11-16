"""
No more context managers.

Logfire instrument.
"""

from datetime import datetime

import logfire

from ch4_instrument_db import permissions, users


def get_user(user_id: int) -> dict | None:
    user = users.get(user_id)
    if not user:
        max_user = max(users.keys())
        logfire.error("User not found", user_id=user_id, max_user_id=max_user)
        raise ValueError("User not found")
    return user


def get_permissions(role: str) -> list[str]:
    permissions_list = permissions.get(role)
    if not permissions_list:
        logfire.error("Permissions not found", role=role)
        raise ValueError("Permissions not found")
    return permissions_list


def calculate_age(dob: str) -> int:
    current_year = datetime.now().year
    dob_year = int(dob.split("-")[0])
    age = current_year - dob_year
    return age


def compose_user_info(user_id: int) -> dict | None:
    if user := get_user(user_id):
        role = user.get("role")
    permissions_list = get_permissions(role)
    user_info = {
        "user": user,
        "permissions": permissions_list,
        "age": calculate_age(user.get("dob")),
    }
    return user_info


def main() -> None:
    try:
        for user_id in range(1, 4):
            user_info = compose_user_info(user_id)
            logfire.info("User info {user_info}", user_info=user_info)
    except ValueError as e:
        logfire.error("Error occurred", error=e)
        raise e


if __name__ == "__main__":
    service_name = "logfire_instrument_show"
    logfire.configure(service_name=service_name)
    main()
