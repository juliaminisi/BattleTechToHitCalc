import streamlit as st
from PIL import Image

# -----------------------------
# Modifier Dictionaries
# -----------------------------

attacker_movement_modifiers = {
    "None": 0,
    "Attacker did not move": 0,
    "Attacker walked": 1,
    "Attacker ran": 2,
    "Attacker jumped": 3,
    "Attacker made a lateral shift (VTOL/Aircraft)": 1,
    "Attacker is airborne VTOL/Conventional": 1,
    "Attacker performed DFA (Death From Above)": 3,
    "Attacker used WiGE movement": 1,
    "Attacker in depth 1 water (leg movement only)": 1,
}

target_movement_modifiers = {
    "None": 0,
    "Target moved 0–2 hexes": 1,
    "Target moved 3–4 hexes": 2,
    "Target moved 5–6 hexes": 3,
    "Target moved 7–9 hexes": 4,
    "Target moved 10+ hexes": 5,
    "Target made lateral shift (VTOL/Aircraft)": 1,
    "Target is jumping": 1,
}

terrain_modifiers = {
    "None": 0,
    "Target in light woods (1 hex)": 1,
    "Target in heavy woods (1 hex)": 2,
    "Target in light woods (2+ hexes)": 2,
    "Target in heavy woods (2+ hexes)": 3,
    "Firing through light woods (1 hex)": 1,
    "Firing through heavy woods (1 hex)": 2,
    "Firing through light woods (2+ hexes)": 2,
    "Firing through heavy woods (2+ hexes)": 3,
    "Target in light smoke": 1,
    "Target in heavy smoke": 2,
    "Attacker in depth 1+ water (torso twist or turret fire)": 1,
}

target_status_modifiers = {
    "None": 0,
    "Target is prone": -2,
    "Target is prone and adjacent": 0,
    "Target is hull down": 1,
    "Target is immobile": -4,
    "Target is in a building (partial cover)": 1,
    "Target is shutdown": -4,
    "Target is unconscious": -4,
    "Target is on a higher elevation": 1,
    "Target is in depth 1+ water (LOS issues)": 1,
}

attacker_status_modifiers = {
    "None": 0,
    "Attacker is prone": 0,
    "Attacker is in depth 1+ water": 1,
    "Attacker is in woods": 1,
    "Firing indirect LRM": 1,
    "Firing after torso twist": 1,
    "Fire control hit": 2,
    "Multiple weapon attacks": 1,
    "Attacker has fire control critical hit": 2,
    "Firing at target in rear arc": -1,
}

heat_modifiers = {
    "None": 0,
    "Heat Level 8–11": 1,
    "Heat Level 12–14": 2,
    "Heat Level 15–17": 3,
    "Heat Level 18–20": 4,
    "Heat Level 21–23": 5,
    "Heat Level 24+": 6,
}

range_modifiers = {
    "None": 0,
    "Short Range": 0,
    "Medium Range": 2,
    "Long Range": 4,
    "Extreme Range": 6,
}

visibility_modifiers = {
    "None": 0,
    "Dusk/Dawn (no searchlight)": 1,
    "Dusk/Dawn (with searchlight)": 0,
    "Night (no NV/IR)": 2,
    "Night (with NV/IR or searchlight)": 1,
    "Heavy fog/rain/snow": 1,
    "Pitch black + weather": 3,
}

ew_modifiers = {
    "None": 0,
    "Target has ECM affecting attacker": 1,
    "Attacker has BAP targeting enemy in woods": -1,
    "Attacker has targeting computer": -1,
    "Target has stealth armor": 1,
    "Attacker affected by ECM/ECCM": 1,
}

pilot_skill_base = {
    "Gunnery 0 (Elite)": 0,
    "Gunnery 1": 1,
    "Gunnery 2": 2,
    "Gunnery 3": 3,
    "Gunnery 4 (Average)": 4,
    "Gunnery 5": 5,
    "Gunnery 6+": 6,
}

special_modifiers = {
    "None": 0,
    "Firing at airborne VTOL (non-flak)": 3,
    "Firing from moving vehicle": 1,
    "Target airborne (high altitude)": 4,
    "Firing while evading": 2,
    "Using indirect fire (spotter)": 1,
    "Firing underwater": 2,
    "Target behind wall or rubble": 1,
}

# -----------------------------
# Streamlit UI
# -----------------------------

st.set_page_config(page_title="🤖 BattleTech Modifier Calculator", layout="centered")
st.title("🤖 BattleTech To-Hit Modifier Calculator")
st.caption("Created by Julia Minisi")

# Function to create a select box and return the value

def modifier_select(label, options):
    return st.selectbox(label, options, index=0)

# Layout the dropdowns in two columns
col1, col2 = st.columns(2)
with col1:
    gunnery = modifier_select("Pilot Gunnery Skill", list(pilot_skill_base.keys()))
    attacker_movement = modifier_select("Attacker Movement", list(attacker_movement_modifiers.keys()))
    target_movement = modifier_select("Target Movement", list(target_movement_modifiers.keys()))
    terrain = modifier_select("Terrain", list(terrain_modifiers.keys()))
    visibility = modifier_select("Visibility", list(visibility_modifiers.keys()))
    range_val = modifier_select("Range", list(range_modifiers.keys()))

with col2:
    attacker_status = modifier_select("Attacker Status", list(attacker_status_modifiers.keys()))
    target_status = modifier_select("Target Status", list(target_status_modifiers.keys()))
    heat = modifier_select("Heat", list(heat_modifiers.keys()))
    ew = modifier_select("Electronic Warfare", list(ew_modifiers.keys()))
    special = modifier_select("Special Conditions", list(special_modifiers.keys()))

if st.button("Calculate To-Hit Modifier"):
    total = (
        pilot_skill_base[gunnery] +
        attacker_movement_modifiers[attacker_movement] +
        target_movement_modifiers[target_movement] +
        terrain_modifiers[terrain] +
        visibility_modifiers[visibility] +
        range_modifiers[range_val] +
        attacker_status_modifiers[attacker_status] +
        target_status_modifiers[target_status] +
        heat_modifiers[heat] +
        ew_modifiers[ew] +
        special_modifiers[special]
    )

    st.success(f"🎯 Total To-Hit Modifier: {total}")
    st.info(
        f"**Breakdown:**\n"
        f"- Pilot Skill: {pilot_skill_base[gunnery]}\n"
        f"- Attacker Move: {attacker_movement_modifiers[attacker_movement]}\n"
        f"- Target Move: {target_movement_modifiers[target_movement]}\n"
        f"- Terrain: {terrain_modifiers[terrain]}\n"
        f"- Visibility: {visibility_modifiers[visibility]}\n"
        f"- Range: {range_modifiers[range_val]}\n"
        f"- Attacker Status: {attacker_status_modifiers[attacker_status]}\n"
        f"- Target Status: {target_status_modifiers[target_status]}\n"
        f"- Heat: {heat_modifiers[heat]}\n"
        f"- EW: {ew_modifiers[ew]}\n"
        f"- Special: {special_modifiers[special]}"
    )
