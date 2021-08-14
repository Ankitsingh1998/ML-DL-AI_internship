#Day010 - Postal_codes_Germany
import re
cities_file = open("largest_cities_germany.txt", encoding=('utf-8'))
cities_list = cities_file.readlines()
city_pattern = r"\s[\w\s]+\s"

Germany_cities_list = []
for city_list in cities_list:
    city_name = re.findall(city_pattern, city_list)[0]
    Germany_cities_list.append(city_name.strip()) 
#.strip() - removes extra whitespace in the beginning or at the end.
    
postal_code_dict = {}
postal_code_file = open("postal_codes_germany.txt", encoding=('utf-8'))
postal_code_data = postal_code_file.read()


for city in Germany_cities_list:
    postal_pattern = '\s'+city+'\s[\d]+\s'
#To obtain first n postal addressess, we can use list slicing here
    Matching_cities = re.findall(postal_pattern, postal_code_data)[0:]
#Each Matching cities converted into string to furthur apply regex to fing postal codes.
    Matching_cities_string_conversion = "".join(Matching_cities)
#Then, again re.findall is applied to extract postal codes for each cities respectively.
    postal_codes_list = re.findall(r"[\d]+",Matching_cities_string_conversion)
#Then, each city is provided with their corresponding postal codes using dictionary.
    postal_code_dict[city] = postal_codes_list
    
print(Germany_cities_list)
print('Hamburg all postal code list: ',postal_code_dict['Hamburg'])
print('Hamburg four postal code list: ',postal_code_dict['Hamburg'][0:4])



