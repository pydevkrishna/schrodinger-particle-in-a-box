# 🧠 Schrödinger Equation: Particle in a 1D Box

This project solves the **time-independent Schrödinger equation (TISE)** for a **particle in a one-dimensional infinite potential well** using Python. It visualizes the wavefunctions and energy levels for the first few quantum states.

<br/>

## 🧪 Physics Background

A particle trapped inside a 1D box with infinitely high walls obeys the TISE:

![Image](https://github.com/user-attachments/assets/5179fe26-7466-4b2d-9d3c-61f28b871777)

For a box from \( x=0 \) to \(x=L \), the analytical solutions are:

- **Wavefunctions:**  
  \[
  \psi_n(x) = \sqrt{\frac{2}{L}} \sin\left( \frac{n \pi x}{L} \right)
  \]
- **Energy Levels:**  
  \[
  E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2}
  \]

In this project, we solve the equation **numerically** using the **finite difference method**.

<br/>

## 🧰 Tools Used

- Python 3
- `numpy` – for numerical computation
- `scipy.linalg` – for solving the eigenvalue problem
- `matplotlib` – for plotting wavefunctions

<br/>

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/schrodinger-particle-in-a-box.git
   cd schrodinger-particle-in-a-box
