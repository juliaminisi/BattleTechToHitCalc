import streamlit as st
import random

# --- Mech Definitions ---
mechs = {
    "Stinger": {
        "weapons": {"Medium Laser": 5, "Machine Gun": 2},
        "armor": {"Center Torso": 22, "Left Torso": 16, "Right Torso": 16,
                  "Left Arm": 8, "Right Arm": 8, "Left Leg": 12, "Right Leg": 12,
                  "Head": 9}
    },
    "Wasp": {
        "weapons": {"Medium Laser": 5, "SRM-2": 2},
        "armor": {"Center Torso": 22, "Left Torso": 16, "Right Torso": 16,
                  "Left Arm": 8, "Right Arm": 8, "Left Leg": 12, "Right Leg": 12,
                  "Head": 9}
    },
    "Locust": {
        "weapons": {"Machine Gun": 2, "Medium Laser": 5},
        "armor": {"Center Torso": 18, "Left Torso": 14, "Right Torso": 14,
                  "Left Arm": 6, "Right Arm": 6, "Left Leg": 10, "Right Leg": 10,
                  "Head": 9}
    }
}

hit_table_front = {
    (2,): "Center Torso",
    (3,): "Right Arm",
    (4,): "Right Arm",
    (5,): "Right Leg",
    (6,): "Right Torso",
    (7,): "Center Torso",
    (8,): "Left Torso",
    (9,): "Left Leg",
    (10,): "Left Arm",
    (11,): "Right Arm",
    (12,): "Head"
}

# --- Functions ---
def get_hit_location(roll):
    for key, location in hit_table_front.items():
        if roll in key:
            return location
    return "Miss"

def apply_damage(armor, location, damage):
    if location in armor:
        armor[location] = max(0, armor[location] - damage)
    return armor

# --- Streamlit App ---
st.set_page_config(page_title="Battletech Hit Calculator", layout="centered")
st.title("🤖 Battletech Hit & Damage Calculator")
st.markdown("Track attacks, hit locations, and damage by mech")

st.header("1. Select Mechs")
attacker = st.selectbox("Attacking Mech", list(mechs.keys()), key="attacker")
target = st.selectbox("Target Mech", list(mechs.keys()), key="target")

st.header("2. Weapon & To-Hit Roll")
weapon = st.selectbox("Select Weapon", list(mechs[attacker]["weapons"].keys()))
to_hit = st.number_input("Enter 2D6 To-Hit Roll Result", min_value=2, max_value=12, step=1)

if st.button("Resolve Hit"):
    if to_hit >= 7:
        hit_roll = random.randint(2, 12)
        location = get_hit_location(hit_roll)
        damage = mechs[attacker]["weapons"][weapon]
        mechs[target]["armor"] = apply_damage(mechs[target]["armor"], location, damage)

        st.success(f"**Hit!** Rolled {hit_roll} → `{location}` for {damage} damage.")
        st.info(f"{target} updated armor: {mechs[target]['armor'][location]} left on {location}")
    else:
        st.warning("Missed the attack!")

st.header("3. Armor Status")
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"{attacker} Weapons")
    st.json(mechs[attacker]["weapons"])

with col2:
    st.subheader(f"{target} Armor")
    st.json(mechs[target]["armor"])
