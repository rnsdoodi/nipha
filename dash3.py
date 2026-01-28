import streamlit as st

# Set Page Config
st.set_page_config(page_title="Strategic Recommendations - NiV", layout="wide")

st.title(" Strategic Recommendations & Action Plan")
st.markdown("---")

# Introduction
st.markdown("""
Based on the **Descriptive Analysis** of the 2025 Kerala outbreak and WHO guidelines, 
the following actions are recommended to contain the spread of Nipah Virus (NiV).
""")

# Creating three columns for different categories
col1, col2 = st.columns(2)

with col1:
    st.subheader(" Public Prevention & Safety")
    st.write("Measures to be followed by the general public:")
    
    st.checkbox("Limit hospital visits to emergencies only (especially in Palakkad & Malappuram).")
    st.checkbox("Mandatory mask-wearing for healthcare workers, patients, and companions.")
    st.checkbox("Strict food hygiene: Boil date palm sap and wash/peel fruits thoroughly.")
    st.checkbox("Discard any fruits with visible signs of bat bites.")
    st.checkbox("Avoid unprotected physical contact with suspected or confirmed patients.")

with col2:
    st.subheader(" Clinical & Operational Response")
    st.write("Measures for healthcare facilities and authorities:")
    
    st.checkbox("Intensify field surveillance for active fever cases in affected clusters.")
    st.checkbox("Maintain high-level alerts in hospitals across neighboring districts.")
    st.checkbox("Enhance contact tracing using CCTV and mobile tower data mapping.")
    st.checkbox("Establish isolation wards with strict Droplet and Airborne precautions.")
    st.checkbox("Provide intensive supportive care for severe neurological/respiratory complications.")

st.divider()

# Strategic Long-term Recommendations
st.header(" Strategic Policy Advice")
st.info("""
1. **One Health Approach:** Increase coordination between veterinary and human health departments to monitor fruit bat (reservoir) activity.
2. **Early Detection Systems:** Strengthen laboratory capacities in at-risk states to reduce testing turnaround time.
3. **Public Awareness:** Launch risk-communication campaigns focused on the absence of a vaccine to promote behavioral changes.
4. **Surveillance Auditing:** Regularly audit Infection Prevention and Control (IPC) and waste management practices in all government and private hospitals.
""")

# Footer Note
st.markdown("---")
st.caption("Note: These recommendations are based on the protocols established by the Kerala Ministry of Health and WHO situational advice for 2025-2026.")
