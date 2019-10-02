def write_to_file(file, postcode, country, city):
    try:
        with open(file, 'w') as opened_file:
            opened_file.write(f'My postcode is {postcode} \n I am based in {city}, which is in {country}.')
    except FileNotFoundError:
        print('File not found.')