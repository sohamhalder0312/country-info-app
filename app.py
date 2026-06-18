import requests
import streamlit as st

def get_country_info(country):
    api_key = "rc_live_5d3e242565bf43bc90ed91fdbe35ebf9"
    url = f"https://api.restcountries.com/countries/v5?q={country}"
    headers = {'Authorization':f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        country_data = data["data"]["objects"][0]
        if country_data:
            return country_data
        else:
            return {"error": "Country not found."}
    else:
        return {"error": f"API request failed with status code {response.status_code}."}


st.title("Country Information App")
st.warning("This app may give inaccurate results for countries with similar names. Please enter the full country name for better accuracy.")
c = st.text_input("Enter a country name")
if st.button("Process"):
    if c.strip() == "":
        st.warning("Please enter a country name.")
    try:    
        st.text("_"*40)
        info = get_country_info(c)
        st.write("Country:", info.get("names", {}).get("common", "N/A"))
        st.write("Official Name:", info.get("names", {}).get("official", "N/A"))
        st.write("Capital:", info.get("capitals", [{}])[0].get("name", "N/A"))
        st.write("Region:", info.get("region", "N/A"))
        st.write("Subregion:", info.get("subregion", "N/A"))
        st.write("Population:", info.get("population", "N/A"))
        st.write("Currency:", info.get("currencies", [{}])[0].get("name", "N/A"))
        st.write("Language:", info.get("languages", [{}])[0].get("name", "N/A"))
        st.write("Timezone:", info.get("timezones", ['N/A'])[0])
        st.write("Flag:", info.get("flag", {}).get("emoji", "N/A"))
        
    except:
        st.write("An error occurred while processing the request.")
    finally:
        st.text("_"*40)