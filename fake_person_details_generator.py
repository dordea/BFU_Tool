from faker import Faker

fake = Faker()

def generate_fake_person_details():
    name = fake.name()
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    zip = fake.postcode()
    city = fake.city()
    state = fake.state_abbr()
    country = fake.country()
    return name, email, phone_number, address, zip, city, state, country

if __name__ == "__main__":
    name, email, phone_number, address, zip, city, state, country = generate_fake_person_details()
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")
    print(f"Address: {address}")
    print(f"Zip: {zip}")
    print(f"City: {city}")
    print(f"State: {state}")
    print(f"Country: {country}")