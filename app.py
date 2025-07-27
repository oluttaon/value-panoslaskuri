import streamlit as st

st.title("📈 Value ➜ Panossuositus -laskuri")

st.markdown("Syötä pehmeän bookkerin kerroin, arvioitu value-prosentti ja kassasi koko. Laskuri laskee fair probabilityn ja antaa panossuosituksen Kellyn mukaan (0.25x, max 1 % kassasta).")

# 🔢 Syötteet
own_odds = st.number_input("📌 Oma kerroin (pehmeä)", min_value=1.01, value=2.00, step=0.01)
value_pct = st.number_input("🎯 Arvioitu value-prosentti (%)", value=4.0, step=0.1)
bankroll = st.number_input("💰 Kassasi koko (€)", min_value=1.0, value=1000.0, step=10.0)

# 🔍 Laskenta
fair_prob = 1 / (own_odds * (1 + value_pct / 100))
edge = (own_odds * fair_prob) - 1
kelly_fraction = 0.25
kelly_stake = (edge / (own_odds - 1)) * bankroll * kelly_fraction
max_stake = bankroll * 0.01
recommended_stake = max(min(kelly_stake, max_stake), 0)

# 📊 Tulokset
st.subheader("📊 Tulokset")
st.write(f"**Fair probability:** {fair_prob:.4f} ({fair_prob * 100:.2f} %)")
st.write(f"**Kelly-panossuositus (0.25x):** {kelly_stake:.2f} €")
st.write(f"**Max panos (1 % kassasta):** {max_stake:.2f} €")
st.success(f"💰 **Suositeltu panos:** {recommended_stake:.2f} €")
