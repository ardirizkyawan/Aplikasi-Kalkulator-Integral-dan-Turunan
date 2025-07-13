import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi simbol x
x = sp.Symbol('x')

st.title("🧮 Kalkulator Integral dan Turunan")
st.write("Aplikasi ini menghitung turunan atau integral dari fungsi matematika aljabar.")

# Contoh fungsi bawaan
contoh_fungsi = {
    "x**2": "x**2",
    "sin(x)": "sin(x)",
    "e**x": "exp(x)",
    "1/x": "1/x"
}

# Input fungsi
fungsi_input = st.text_input("Masukkan fungsi f(x):", value="x**2")

# Pilihan contoh
st.markdown("Atau pilih contoh fungsi:")
contoh_dipilih = st.selectbox("Contoh Fungsi:", list(contoh_fungsi.keys()))
if contoh_dipilih:
    fungsi_input = contoh_fungsi[contoh_dipilih]

# Pilih operasi
operasi = st.radio("Pilih Operasi:", ("Turunan", "Integral Tak Tentu", "Integral Tentu"))

# Hitung turunan/integral
try:
    fungsi = sp.sympify(fungsi_input)
    
    if operasi == "Turunan":
        hasil = sp.diff(fungsi, x)
        st.latex(f"f'(x) = {sp.latex(hasil)}")

    elif operasi == "Integral Tak Tentu":
        hasil = sp.integrate(fungsi, x)
        st.latex(f"\\int f(x)\\,dx = {sp.latex(hasil)} + C")

    elif operasi == "Integral Tentu":
        a = st.number_input("Batas bawah (a):", value=0.0)
        b = st.number_input("Batas atas (b):", value=1.0)
        hasil = sp.integrate(fungsi, (x, a, b))
        st.latex(f"\\int_{{{a}}}^{{{b}}} f(x)\\,dx = {sp.latex(hasil)}")

    # Tampilkan grafik
    st.subheader("📈 Grafik Fungsi")
    f_np = sp.lambdify(x, fungsi, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_np(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"f(x) = {fungsi_input}")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.legend()
    st.pyplot(f
