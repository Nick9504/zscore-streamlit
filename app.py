import streamlit as st

# ----------------------------
# CONFIG PAGINA
# ----------------------------

st.set_page_config(
    page_title="Z Score Calculator",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# CSS CUSTOM
# ----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ffffff, #e9d5ff);
}

.title {
    color: #5b21b6;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 30px;
}

.result-box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 80vh;
}

.result {
    font-size: 90px;
    font-weight: bold;
    color: #111;
}

.dot {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-top: 20px;
}

.small-text {
    margin-top: 15px;
    font-size: 20px;
    color: #444;
}

.block-container {
    padding-top: 2rem;
}

.stButton > button {
    width: 100%;
    background-color: #7c3aed;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 18px;
    border: none;
}

.stButton > button:hover {
    background-color: #5b21b6;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# SESSION STATE
# ----------------------------

if "z" not in st.session_state:
    st.session_state.z = 0

if "color" not in st.session_state:
    st.session_state.color = "gray"

if "status" not in st.session_state:
    st.session_state.status = "Inserisci i dati"

# ----------------------------
# LAYOUT
# ----------------------------

left, right = st.columns([1.2, 1])

# ----------------------------
# INPUT
# ----------------------------

with left:

    st.markdown(
        '<div class="title">Z Score Calculator</div>',
        unsafe_allow_html=True
    )

    wc = st.number_input(
        "Capitale Circolante",
        value=0.0
    )

    ta = st.number_input(
        "Totale Attivo",
        value=1.0
    )

    re = st.number_input(
        "Utili non distribuiti",
        value=0.0
    )

    ebit = st.number_input(
        "EBIT",
        value=0.0
    )

    mve = st.number_input(
        "Capitalizzazione",
        value=0.0
    )

    tl = st.number_input(
        "Totale Passivo",
        value=1.0
    )

    sales = st.number_input(
        "Ricavi",
        value=0.0
    )

    # ----------------------------
    # BOTTONE
    # ----------------------------

    calculate = st.button("Calcola Z Score")

    # ----------------------------
    # CALCOLO
    # ----------------------------

    if calculate:

        z = (
            1.2 * (wc / ta)
            + 1.4 * (re / ta)
            + 3.3 * (ebit / ta)
            + 0.6 * (mve / tl)
            + 1.0 * (sales / ta)
        )

        # LOGICA COLORI

        if z > 2.99:
            color = "green"
            status = "Azienda Solida"

        elif z >= 1.81:
            color = "gray"
            status = "Zona Intermedia"

        else:
            color = "red"
            status = "Rischio Elevato"

        # SALVATAGGIO

        st.session_state.z = z
        st.session_state.color = color
        st.session_state.status = status

# ----------------------------
# OUTPUT
# ----------------------------

with right:

    st.markdown("## Risultato Z Score")

    st.metric(label="Z Score", value=f"{st.session_state.z:.2f}")

    # pallino colore (vero componente Streamlit)
    if st.session_state.color == "green":
        st.success("🟢 Azienda Solida")

    elif st.session_state.color == "gray":
        st.warning("⚪ Zona Intermedia")

    else:
        st.error("🔴 Rischio Elevato")
