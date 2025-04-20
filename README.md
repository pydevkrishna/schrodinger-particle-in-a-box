# 🧠 Schrödinger Equation: Particle in a 1D Box

This project solves the **time-independent Schrödinger equation (TISE)** for a **particle in a one-dimensional infinite potential well** using Python. It visualizes the wavefunctions and energy levels for the first few quantum states.

<br/>

## 🧪 Physics Background

The potential V(x) is defined as:

![Image](https://github.com/user-attachments/assets/78d8307c-fa7d-423b-bc3a-cc453632f3da)

A particle trapped inside a 1D box with infinitely high walls obeys the TISE:

![Image](https://github.com/user-attachments/assets/5179fe26-7466-4b2d-9d3c-61f28b871777)

For a box from \( x=0 \) to \(x=L \), the analytical solutions are:

- **Wavefunctions:**  
![Image](https://github.com/user-attachments/assets/4aa617d6-eeeb-464b-98e4-d34681e2f848)


- **Energy Levels:**  
 ![Image](https://github.com/user-attachments/assets/9288e933-8f4a-4aae-b30a-1a62766124ca)

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

2. Install dependencies:
   ```bash
   pip install numpy scipy matplotlib

3. Run the Script:
   ```bash
   python particle_in_box.py

<br>

## 📈 Output

You’ll see a plot showing the first few normalized wavefunctions (ψn(x)) inside the box, with corresponding quantized energy levels:
Each wavefunction has n−1 nodes and satisfies boundary conditions: 
 ψ(0)=ψ(L)=0
<br/>
## 🧠 Learn More
This is a great starting point if you're:

1. Learning quantum mechanics

2. Practicing numerical methods

3. Exploring scientific computing and visualization

<br/>

## 📄 License
This project is licensed under the MIT License. Feel free to use, modify, and share!
