import streamlit as st
import pandas as pd
import altair as alt
import hmac

# Set up the title for the page
st.title("HDB Resale Market Analysis Tool")

# Function to check password (same as in main.py)
def check_password():
    """Returns `True` if the user had the correct password."""
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False
            
    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True
    
    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
        
    return False

# Check password for this page
if not check_password():
    st.stop()  # Stop if password check fails

# Load the data from the CSV file
@st.cache_data  # Streamlit's caching for data
def load_data():
    # Adjust the path as necessary to point to your CSV file
    return pd.read_csv('data/hdb_data.csv')

# Fetch data from the CSV file
df = load_data()
df['resale_price'] = df['resale_price'].astype(float)  # Convert resale_price to float
df['month'] = pd.to_datetime(df['month'])  # Convert month to datetime

# User inputs for filtering
st.sidebar.header("Filter Options")
town = st.sidebar.selectbox("Select Town", ["ANY"] + list(df['town'].unique()))
flat_type = st.sidebar.selectbox("Select Flat Type", df['flat_type'].unique())

# Filter the DataFrame based on user selection
if town == "ANY":
    filtered_data = df[df['flat_type'] == flat_type]
else:
    filtered_data = df[(df['town'] == town) & (df['flat_type'] == flat_type)]

# Display filtered data with specified columns
st.subheader("Filtered Resale Data")
if not filtered_data.empty:
    filtered_columns = filtered_data[['town', 'flat_type', 'block', 'street_name', 'storey_range', 'remaining_lease', 'resale_price']]
    filtered_columns.columns = ["Town", "Flat Type", "Block", "Street Name", "Storey Range", "Remaining Lease", "Resale Price"]

    # Display the DataFrame using st.dataframe to prevent showing index
    st.dataframe(filtered_columns.reset_index(drop=True), use_container_width=True)
else:
    st.warning("No data available for the selected options.")

# Visualization of resale prices over time using Altair
st.subheader("Resale Price Trend")
if not filtered_data.empty:
    # Aggregate the data by month
    monthly_data = filtered_data.groupby('month').agg({'resale_price': 'mean'}).reset_index()

    # Display available year range in the dataset
    min_year = monthly_data['month'].dt.year.min()
    max_year = monthly_data['month'].dt.year.max()
    st.write(f"Data available from **{min_year}** to **{max_year}**.")

    # Create the Altair chart
    chart = alt.Chart(monthly_data).mark_line(point=True).encode(
        x='month:T',  # Use temporal encoding for month
        y='resale_price:Q',
        tooltip=['month:T', 'resale_price:Q']
    ).properties(
        title=f"Average Resale Price Trend for {flat_type} in {town}",
        width=700,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

    # If "ANY" is selected, show average resale price by town
    if town == "ANY":
        town_data = filtered_data.groupby('town').agg({'resale_price': 'mean'}).reset_index()
        
        # Create a bar chart for average resale price by town
        town_chart = alt.Chart(town_data).mark_bar().encode(
            x=alt.X('town:N', sort='-y'),  # Sort by average price
            y='resale_price:Q',
            tooltip=['town:N', 'resale_price:Q']
        ).properties(
            title="Average Resale Price by Town",
            width=700,
            height=400
        )

        st.altair_chart(town_chart, use_container_width=True)
else:
    st.warning("No data available for the selected options.")

# Insights based on the analysis
st.subheader("Insights")
if not filtered_data.empty:
    avg_resale_price = filtered_data['resale_price'].mean()
    min_resale_price = filtered_data['resale_price'].min()
    max_resale_price = filtered_data['resale_price'].max()
    
    st.write(f"The average resale price for the selected filters is **${avg_resale_price:,.2f}**.")
    st.write(f"The minimum resale price recorded is **${min_resale_price:,.2f}**.")
    st.write(f"The maximum resale price recorded is **${max_resale_price:,.2f}**.")
else:
    st.write("No data to generate insights based on the selected options.")
