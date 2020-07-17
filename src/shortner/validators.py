from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

# def validate_url(value):
#     url_validator = URLValidator()
#     try:
#         url_validator(value)
#     except:
#         raise ValidationError("Invalid URL -> Make sure to add http://")
#     return value



def validate_url(value):
    url_validator = URLValidator()
    value1_invalid = False
    value2_invalid = False

    try:
        url_validator(value)
    except:
        value1_invalid = True
    
    value_2_url = 'http://' + value

    try:
        url_validator(value_2_url)
    except:
        value2_invalid = True
    
    if value1_invalid == True and value2_invalid == True:
        raise ValidationError("Invalid URL")
    
    return value


#    def validate_url(value):
#     url_validator = URLValidator()
#     value1_invalid = False
#     value2_invalid = False

#     try:
#         url_validator(value)
#     except:
#         value1_invalid = True
    
#     value_2_url = 'http://' + value

#     try:
#         url_validator(value_2_url)
#     except:
#         value2_invalid = True
    
#     if value1_invalid == True and value2_invalid == True:
#         raise ValidationError("Invalid URL")
    
#     return value
    
