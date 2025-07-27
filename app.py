import streamlit as st

st.title("📈 Value % ➜ Kelly-panossuositus (vig poistettu)")

st.markdown("Syötä bookkerin kerroin, arvioitu value-% (Surebet.com) ja kassasi koko. Laskuri poistaa automaattisesti 2.5 % vig:in ja laskee panoksen Kelly 0.25x -mallilla (max 1 % kassasta).")

# 🔢 Syötteet
odds = st.number_input("📌 Oma kerroin", min_value=1.01, value=2.00, step=0.01)
value_pct = st.number_input("🎯 Arvioitu value-prosentti (%)", value=4.0, step=0.1)
bankroll = st.number_input("💰 Kassasi (€)", min_value=1.0, value=1000.0, step=10.0)

# ⚙️ Asetukset
vig_margin = 0.025  # 2.5 % vig
real_value_pct = value_pct - (vig_margin * 100)

# Laskenta
edge = real_value_pct / 100
if odds <= 1 or edge <= 0:
    stake = 0
    full_kelly = 0
    scaled_kelly = 0
else:
    full_kelly = (edge / (odds - 1)) * bankroll
    scaled_kelly = full_kelly * 0.25
    max_stake = bankroll * 0.01
    stake = min(scaled_kelly, max_stake)

# 📊 Tulokset
st.subheader("📊 Tulokset")
st.write(f"**Vig-poistettu value-%:** {real_value_pct:.2f} %")
st.write(f"**Edge:** {edge * 100:.2f} %")
st.write(f"**Täysi Kelly-panossuositus:** {full_kelly:.2f} €")
st.write(f"**Kelly 0.25x:** {scaled_kelly:.2f} €")
st.write(f"**Max panos (1 % kassasta):** {bankroll * 0.01:.2f} €")

if stake > 0:
    st.success(f"💰 **Suositeltu panos:** {stake:.2f} €")
else:
    st.warning("⚠️ Reaalinen value on liian pieni – ei suositeltua panosta.")
