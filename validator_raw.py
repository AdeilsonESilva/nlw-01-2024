from cerberus import Validator

body = {
    "data": {"element1": 123.98, "element2": "olaMundo", "element3": "123"},
}

# na mão
# if "name" in body["data"]
# if isinstance(body["data"]["name"], int)

body_validator = Validator(
    {
        "data": {
            "type": "dict",
            "schema": {
                "element1": {"type": "float", "required": True, "empty": False},
                "element2": {"type": "string", "required": True, "empty": True},
                "element3": {"type": "string", "required": False, "empty": False},
            },
        }
    }
)


respose = body_validator.validate(body)

if respose is False:
    print(body_validator.errors)
else:
    print("Body OK")

print(respose)
