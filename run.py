from API_get_call import *
from write_function import *

postcode = post_code_dict['result']['postcode']
country = post_code_dict['result']['country']
city = post_code_dict['result']['nhs_ha']

write_to_file('postcode.txt', postcode, city, country)


