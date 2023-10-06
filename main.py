import streamlit as st

# Constants
XP_PER_COIN = 400
XP_PER_DICE_STRAT = 8000

# Define the level-to-XP mapping
level_to_xp = {
    10: 115400, 20: 447000, 30: 1336300, 40: 3722400,
    50: 10133300, 60: 10133300, 70: 73762700, 80: 198606800,
    90: 534633200, 100: 1439116000, 110: 3873766100, 120: 10427316700
}

# Page title and icon (set only once at the beginning)
st.set_page_config(
    page_title='CSGORoll XP Calculator',
    page_icon=":video_game:"
)

# Introduction
st.title('CSGO Roll XP Calculator')
st.write("""
Welcome to the CSGO Roll XP Calculator! 🎮 This handy tool helps you figure out the XP you need to reach a specific level on CSGORoll.
Just input your current XP and choose your desired level - we'll do the math for you!
""")

# Function to validate and parse input
def validate_and_parse_input(input_str):
    if input_str.strip().isdigit():
        return int(input_str)
    return 0

# User input for current XP
current_xp = st.text_input('What\'s your current CSGO Roll XP?', value='0', key="current_xp", disabled=False)
current_xp = validate_and_parse_input(current_xp)

# Dropdown to select the level to calculate to
selected_level = st.selectbox('Which level are you aiming for?', list(level_to_xp.keys()), key="selected_level", disabled=False)

# Calculate the XP needed to reach the selected level
xp_needed = level_to_xp[selected_level]

# Calculate the difference between required XP and your XP
xp_difference = xp_needed - current_xp

# Calculate Coins to wager and Est. Dice strat cost
coins_to_wager = int(xp_difference / XP_PER_COIN)
dice_strat_cost = int(xp_difference / XP_PER_DICE_STRAT)

# Create a two-column layout for displaying results
col1, col2 = st.columns(2)

# Display the results
with col1:
    st.subheader('Your Current XP')
    st.info(f"{current_xp}")

    st.subheader('XP to Reach the Desired Level')
    st.info(f"{xp_difference}")

    st.subheader('Est. Dice Strategy Cost')
    st.info(f"{dice_strat_cost:,}")

with col2:
    st.subheader('XP Needed for Your Goal')
    st.info(f"{xp_needed}")

    st.subheader('Coins to Wager')
    st.info(f"{coins_to_wager:,}")

# Stylish separator
st.markdown(
    """
    ******
    """
)

# Instructions
st.write("Here's how it works:")
st.write("1. Enter your current CSGO Roll XP.")
st.write("2. Select the next main level you're aiming for from the dropdown.")
st.write("3. See the calculated results for reaching that level.")

# Footer
st.write("Note: Coded with ❤️")


