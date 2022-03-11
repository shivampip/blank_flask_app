

def missing(entity):
    return {
        "success": False,
        "message": "{} is missing".format(entity),
        "data": {}
    }, 404


def not_found(entity):
    return {
        "success": False,
        "message": "{} not found".format(entity),
        "data": {}
    }


def error(message, data={}):
    return {
        "success": False,
        "message": message,
        "data": data
    }
