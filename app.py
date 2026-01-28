import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Epidemiological Analysis Dashboard", layout="wide")

st.title(" Kerala Communicable Diseases Analysis (2025 - 2026)")
st.markdown("---")

# 1. Data Preparation
data = {
    'Disease': ['Fever', 'Dengue', 'Leptospirosis', 'Hepatitis-A', 'Malaria', 'ADD', 'Measles', 'Influenza', 'Nipah (NiV)'],
    'Total_Confirmed': [1523696, 7248, 1610, 7273, 614, 317683, 207, 3558, 9],
    'Total_Deaths': [39, 28, 95, 49, 2, 8, 14, 25, 5]
}
df = pd.DataFrame(data)

# Calculate Metrics
df['CFR (%)'] = (df['Total_Deaths'] / df['Total_Confirmed']) * 100
total_all_cases = df['Total_Confirmed'].sum()
df['Morbidity (%)'] = (df['Total_Confirmed'] / total_all_cases) * 100

# # --- Section 1: Dashboard Overview ---
# col_m1, col_m2, col_m3 = st.columns(3)
# col_m1.metric("Total Confirmed Cases", f"{total_all_cases:,}")
# col_m2.metric("Highest Mortality", "Leptospirosis (95)", delta="95 Deaths")
# col_m3.metric("Critical Threat", "Nipah (NiV)", delta="55.56% CFR")

# st.markdown("### 📋 Statistical Summary")
# st.dataframe(df.style.background_gradient(cmap='Reds', subset=['CFR (%)']), use_container_width=True)

# st.markdown("---")

# --- Section 2: Visual Analytics ---
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader(" Case Fatality Rate  (CFR%)")
    # تم تقليل figsize من (6, 4) إلى (5, 3) لتصغير الحجم
    fig1, ax1 = plt.subplots(figsize=(5, 3)) 
    df_cfr = df.sort_values('CFR (%)', ascending=False)
    sns.barplot(x='CFR (%)', y='Disease', data=df_cfr, palette='Reds_r', ax=ax1)
    ax1.tick_params(axis='both', which='major', labelsize=8) # تصغير حجم الخط
    st.pyplot(fig1, use_container_width=True)
    
    st.markdown("**Analysis:**")
    st.info("""
    Nipah Virus (NiV) exhibits the highest CFR at 55.56%. 
    Measles and Leptospirosis follow with significant rates.
    """)

with row1_col2:
    st.subheader(" Proportional Morbidity (%)")
    fig2, ax2 = plt.subplots(figsize=(5, 3)) 
    df_morb = df.sort_values('Morbidity (%)', ascending=False)
    sns.barplot(x='Morbidity (%)', y='Disease', data=df_morb, palette='viridis', ax=ax2)
    ax2.set_xscale('log') 
    ax2.tick_params(axis='both', which='major', labelsize=8)
    st.pyplot(fig2, use_container_width=True)
    
    st.markdown("**Analysis:**")
    st.info("""
    Fever have 81.99% Percent  for burden, 
    but it is not considered a high risk. Nipah represents a very small percentage (0.00048%).
    """)

st.markdown("---")

# --- Section 3: Comparative Mapping ---
st.subheader(" Comparative Analysis Mapping")
# جعل العمود الأيسر للمخطط أصغر والتحليل بجانبه
row2_col1, row2_col2 = st.columns([1.5, 1])

with row2_col1:
    # تم تحديد أبعاد أصغر للمخطط المبعثر
    fig3, ax3 = plt.subplots(figsize=(5, 3)) 
    scatter = ax3.scatter(df['Morbidity (%)'], df['CFR (%)'], 
                          s=df['CFR (%)']*30+50, c=df['CFR (%)'], 
                          cmap='Reds', alpha=0.6, edgecolors='black')
    
    for i, txt in enumerate(df['Disease']):
        ax3.annotate(txt, (df['Morbidity (%)'][i], df['CFR (%)'][i]), 
                     xytext=(3, 3), textcoords='offset points', fontsize=7)
    
    ax3.set_xscale('log')
    ax3.set_xlabel("Prevalence (Morbidity %)", fontsize=8)
    ax3.set_ylabel("Fatality Rate (CFR %)", fontsize=8)
    ax3.tick_params(labelsize=7)
    st.pyplot(fig3, use_container_width=False) # تم إيقاف التمدد التلقائي هنا

with row2_col2:
    st.markdown("###  Strategic Insights")
    st.info("""
    **The Epidemic Paradox:**
    The mapping reveals a clear inverse relationship. 
    1. **Nipah:** High individual risk.
    2. **Fever:** High logistical burden.
    3. **Leptospirosis:** Hybrid threat.
    """)
