def get_hello_from_country(input_data: dict) -> str:
    try:
        country_name = input_data.get('country_name', None)
        
        if country_name == "India":
            return "Welcome to India"
        return f"hello {country_name}"
        
    except Exception as e:
        print("api.package.temp error:", e)
        return "error"
