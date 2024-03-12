from weather_check import get_weather
# Add your code here and remember to remove all unused comments


while True:
    city = input("Enter the city that you want to know: ")
    result = get_weather(city)

    

    print(f'City: {get_weather(city)['name']}')
    print(f'The condition right now: {result['description']}')
    print(f'The temperature: {result['temp']}')
    print(f'But feel like: {result['feel']}')
    con = input("Do you want to continue? (Y/N) ")
    if con.lower() == 'n':
        print("Good bye! Don't forget to drink water to stay hydrated")
        break

