import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Setup awal
st.set_page_config(page_title="Kalkulator Integral dan Turunan", layout="centered")

st.title("🧮 Kalkulator Integral dan Turunan")
st.write("Aplikasi ini menghitung turunan dan integral dari fungsi aljabar menggunakan Python + Streamlit.")

# Input fungsi
user_input = st.text_input("Masukkan fungsi aljabar (gunakan x sebagai variabel):", "x**2 + 3*x + 2")

# Simbol
x = sp.symbols('x')
try:
    fungsi = sp.sympify(user_input)

    # Hitung turunan dan integral
    turunan = sp.diff(fungsi, x)
    integral = sp.integrate(fungsi, x)

    # Tampilkan hasil simbolik
    st.subheader("📘 Hasil Simbolik")
    st.latex(f"f(x) = {sp.latex(fungsi)}")
    st.latex(f"f'(x) = {sp.latex(turunan)}")
    st.latex(f"\\int f(x) dx = {sp.latex(integral)} + C")

    # Evaluasi numerik pada titik tertentu
    st.subheader("🔢 Evaluasi Numerik")
    eval_point = st.number_input("Masukkan nilai x untuk evaluasi:", value=1.0)
    f_val = fungsi.evalf(subs={x: eval_point})
    f_prime_val = turunan.evalf(subs={x: eval_point})
    st.write(f"f({eval_point}) = {f_val}")
    st.write(f"f'({eval_point}) = {f_prime_val}")

    # Grafik fungsi dan turunannya
    st.subheader("📈 Grafik Fungsi dan Turunannya")
    x_vals = np.linspace(float(eval_point) - 10, float(eval_point) + 10, 400)
    f_lambd = sp.lambdify(x, fungsi, modules=['numpy'])
    f_prime_lambd = sp.lambdify(x, turunan, modules=['numpy'])

    y_vals = f_lambd(x_vals)
    y_prime_vals = f_prime_lambd(x_vals)

    plt.figure(figsize=(8, 4))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    plt.plot(x_vals, y_prime_vals, label="f'(x)", color='red', linestyle='--')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.title("Grafik Fungsi dan Turunannya")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    st.pyplot(plt)

except Exception as e:
    st.error(f"Terjadi kesalahan dalam pemrosesan fungsi: {e}")
