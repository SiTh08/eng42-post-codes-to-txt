def write_to_file(file, postcode, city, country):
    try:
        with open(file, 'w') as opened_file:
            opened_file.write(f'My postcode is {postcode} \nI am based in {city}, which is in {country}.')
    except FileNotFoundError:
        print('File not found.')