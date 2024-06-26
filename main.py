import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selection-box and sub-header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select number of forecast days")
option = st.selectbox("Select data to view",
                      ("Temperature C", "Temperature F", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    try:
        # Get temperature/sky data
        filtered_data = get_data(place=place, forcast_days=days)

        if option in ("Temperature C", "Temperature F"):
            dates = [dic["dt_txt"] for dic in filtered_data]

            if option[-1:] == "C":
                # update formula for to get degree celsius from kelvin
                temperature = [dic["main"]["temp"] - 273.15 for dic in filtered_data]
                # create a temperature plot
                figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (C)"})
            else:
                # update formula for to get degree celsius from kelvin
                temperature = [(dic["main"]["temp"] - 273.15) * 1.8 + 32 for dic in filtered_data]
                # create a temperature plot
                figure = px.line(x=dates, y=temperature, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "./images/clear.png", "Clouds": "./images/cloud.png", "Rain": "./images/rain.png",
                      "Snow": "./images/snow.png"}
            sky_conditions = [d["weather"][0]["main"] for d in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except TypeError:
        st.info(f"City name \"{place}\" is not valid")
