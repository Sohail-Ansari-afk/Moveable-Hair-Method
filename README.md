# 📐 Moveable Hair Method — Surveying Calculator

A **Streamlit web app** that solves the classic **Moveable Hair Method** problem in transit theodolite surveying. Just plug in your field readings and instantly get distances, elevations, and a live diagram — no manual calculation needed!

---
<img width="1919" height="809" alt="image" src="https://github.com/user-attachments/assets/b9654b31-7eea-46a0-bd62-3d4322ca66f4" /> <img width="311" height="844" alt="image" src="https://github.com/user-attachments/assets/e61287ff-2f22-4fa0-bdf7-b1c94e64bc31" />
<img width="659" height="575" alt="image" src="https://github.com/user-attachments/assets/7d4ccca9-f9a9-4250-bdc2-8df9bde20d4c" />
<img width="1833" height="665" alt="image" src="https://github.com/user-attachments/assets/0837b999-e59a-4be1-b2de-8227b9206553" />




## 🤔 What Problem Does This Solve?

Imagine you're a surveyor standing at a point **O** with a theodolite (a precision angle-measuring instrument). You're looking at a staff (a tall measuring rod) held vertically at a distant point **A**.

Your job: **Find the exact elevation (RL) of point A** without walking over there.

### The trick 🎩
Instead of reading one crosshair, you use **two moveable hairs** in the eyepiece to sight **two different points** on the staff — one low, one high. The difference in their heights and the angles you measure mathematically give you the distance and elevation!

---

## 🧮 The Maths (In Plain English)

Think of it like this:

> You're at eye level looking at a flagpole far away.  
> You measure the angle to the **bottom flag** (θ₁) and the angle to the **top flag** (θ₂).  
> You know the distance between the two flags (S).  
> From that, you can figure out how far away the flagpole is — and how high or low it is compared to you!

### Step-by-step formulas:

| Step | What we find | Formula |
|------|-------------|---------|
| 1️⃣ | **Staff Intercept (S)** — gap between the two readings | `S = Upper staff reading − Lower staff reading` |
| 2️⃣ | **Horizontal Distance (D)** — how far away is the staff? | `D = S / (tan θ₁ + tan θ₂)` |
| 3️⃣ | **Vertical Component (V)** — height difference | `V = D × tan θ₂` |
| 4️⃣ | **RL of Staff Station A** — final answer | `RL of A = RL of Instrument Axis − V − h` |

> `h` = lower staff reading (the reading at the bottom target)

---

## 📖 Worked Example (from the textbook)

**Given:**
- Instrument at station **O**, staff at station **A**
- Lower target angle: **θ₁ = +4°30′**,  staff reading = **0.950 m**
- Upper target angle: **θ₂ = +6°30′**,  staff reading = **3.250 m**
- RL of instrument axis = **255.500 m**

**Solution walkthrough:**

```
Step 1 — Staff Intercept
   S = 3.250 − 0.950 = 2.300 m

Step 2 — Horizontal Distance
   D = 2.300 / (tan 4.5° + tan 6.5°)
   D = 2.300 / (0.07870 + 0.11394)
   D ≈ 11.940 m

Step 3 — Vertical Component
   V = 11.940 × tan 6.5°
   V ≈ 1.360 m

Step 4 — RL of Staff Station A
   RL of A = 255.500 − 1.360 − 0.950
   RL of A = 253.190 m  ✅
```

---

## 🖥️ App Features

| Feature | Description |
|---------|-------------|
| 📊 **Live Results** | S, D, V, and RL update instantly as you change inputs |
| 📈 **Surveying Diagram** | Visual diagram showing instrument, lines of sight, angles, and dimension arrows |
| 🔬 **Sensitivity Analysis** | See how D and RL change if you vary θ₂ — great for understanding the geometry |
| 🧮 **Step-by-Step Solution** | Each calculation step shown with working values |

---

## 🚀 How to Run

### Prerequisites
Make sure you have Python installed, then install the required libraries:

```bash
pip install streamlit matplotlib numpy
```

### Launch the app

```bash
cd "E:\Download\ADM\RL Assignment"
streamlit run moveable_hair_method.py
```

Then open your browser at 👉 **http://localhost:8501**

---

## 🎮 How to Use

1. **Open the sidebar** (left panel) — this has all your input fields
2. **Enter Lower Target values:**
   - Degrees and minutes of the lower vertical angle (θ₁)
   - The staff reading at the lower hair (in metres)
3. **Enter Upper Target values:**
   - Degrees and minutes of the upper vertical angle (θ₂)
   - The staff reading at the upper hair (in metres)
4. **Enter RL of the Instrument Axis** (from your field notes)
5. **Watch everything update live!** 🎉

> 💡 **Tip:** Try changing θ₂ slightly and watch the Sensitivity Analysis graph show how the computed distance D and RL of A shift.

---

## 📐 Understanding the Diagram

```
Instrument O (at RL 255.500 m)
     |
     |  ←—— instrument pillar
     •  ← theodolite here
    / \
   /   \  ← lines of sight (dashed)
  /θ₁ θ₂\
 /         \
•-----------•----[staff]----
O           A    ↑ upper target (θ₂ = 6°30′)
     D      ↑ lower target (θ₁ = 4°30′)
            ↑ ground (RL of A = 253.190 m)
```

- 🟡 **Orange dot** = Instrument position O
- 🔵 **Blue dot** = Lower hair target (θ₁)
- 🟣 **Purple dot** = Upper hair target (θ₂)
- 🟢 **Green dot** = Staff station A (ground level)
- 🔴 **Red arrow** = Vertical component V
- 🟢 **Green arrow** = Staff intercept S
- 🟡 **Orange arrow** = Horizontal distance D

---

## 📚 Background: Why "Moveable Hair"?

In a standard theodolite, crosshairs are **fixed**. In the moveable hair method, you can **adjust the hairs** to target any two points on the staff. This means:

- ✅ You can use an ordinary transit theodolite (no special stadia diaphragm needed)
- ✅ Flexible — you pick which two points on the staff to read
- ⚠️ Slower — you must make **two separate angle observations** per setup
- ⚠️ The theodolite may be disturbed between the two readings

---

## 🗂️ File Structure

```
RL Assignment/
├── moveable_hair_method.py   ← Main Streamlit app
└── README.md                 ← This file
```

---

## 📝 Notes

- Angles are entered as **degrees and minutes separately** (e.g., 4°30′ → Degrees: 4, Minutes: 30)
- All staff readings are in **metres**
- The app assumes **positive vertical angles** (angles of elevation above horizontal)
- The method is from **Fig. 11.14** of standard surveying textbooks (Moveable Hair / Tangential Method)
