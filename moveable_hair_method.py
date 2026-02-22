import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Moveable Hair Method – Surveying Calculator",
    page_icon="📐",
    layout="wide",
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .main { background: #0f172a; }
    .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); }

    .hero-title {
        font-size: 2.4rem; font-weight: 700;
        background: linear-gradient(90deg, #38bdf8, #818cf8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .hero-subtitle { color: #94a3b8; font-size: 1rem; margin-top: 0.2rem; margin-bottom: 1.5rem; }

    .formula-card {
        background: #1e293b; border: 1px solid #334155; border-radius: 12px;
        padding: 1.2rem 1.5rem; margin-bottom: 1rem;
    }
    .formula-card h4 { color: #38bdf8; margin-bottom: 0.5rem; font-size: 0.95rem;
        letter-spacing: 0.05em; text-transform: uppercase; }
    .formula-card p { color: #e2e8f0; font-family: 'Courier New', monospace;
        font-size: 0.95rem; margin: 0.2rem 0; }

    .result-card {
        background: linear-gradient(135deg, #1e3a5f, #1e293b);
        border: 1px solid #38bdf8; border-radius: 12px;
        padding: 1rem 1.5rem; text-align: center; margin-bottom: 1rem;
    }
    .result-card .label { color: #94a3b8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em; }
    .result-card .value { color: #38bdf8; font-size: 2rem; font-weight: 700; }
    .result-card .unit  { color: #64748b; font-size: 0.85rem; }

    .step-card {
        background: #1e293b; border-left: 3px solid #818cf8;
        border-radius: 0 8px 8px 0; padding: 0.8rem 1.2rem; margin-bottom: 0.6rem;
    }
    .step-card .step-title { color: #818cf8; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; }
    .step-card .step-eq   { color: #e2e8f0; font-family: monospace; font-size: 0.95rem; }
    .step-card .step-val  { color: #34d399; font-size: 1.05rem; font-weight: 600; }

    section[data-testid="stSidebar"] { background: #1e293b; border-right: 1px solid #334155; }
    section[data-testid="stSidebar"] label { color: #e2e8f0 !important; }
    hr { border-color: #334155; }
</style>
""", unsafe_allow_html=True)

# ─── Helper ───────────────────────────────────────────────────────────────────
def dms_to_decimal(degrees, minutes, seconds=0):
    return degrees + minutes / 60 + seconds / 3600

# ─── Sidebar – Inputs ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Input Parameters")
    st.markdown("---")

    st.markdown("#### 📍 Lower Target (θ₁)")
    theta1_deg = st.number_input("Degrees (θ₁)", min_value=0, max_value=89, value=4, step=1)
    theta1_min = st.number_input("Minutes (θ₁)", min_value=0, max_value=59, value=30, step=1)
    s1 = st.number_input("Lower Staff Reading (h) [m]", min_value=0.001, value=0.950, step=0.001, format="%.3f")

    st.markdown("#### 📍 Upper Target (θ₂)")
    theta2_deg = st.number_input("Degrees (θ₂)", min_value=0, max_value=89, value=6, step=1)
    theta2_min = st.number_input("Minutes (θ₂)", min_value=0, max_value=59, value=30, step=1)
    s2 = st.number_input("Upper Staff Reading [m]", min_value=0.001, value=3.250, step=0.001, format="%.3f")

    st.markdown("#### 🏛️ Instrument")
    rl_instrument = st.number_input("RL of Instrument Axis [m]", value=255.500, step=0.001, format="%.3f")

    st.markdown("---")
    st.markdown(
        "<small style='color:#64748b'>Moveable Hair Method – Transit Theodolite<br>"
        "Angles are elevation (+ve above horizontal)</small>",
        unsafe_allow_html=True,
    )

# ─── Calculations ─────────────────────────────────────────────────────────────
theta1 = dms_to_decimal(theta1_deg, theta1_min)
theta2 = dms_to_decimal(theta2_deg, theta2_min)

t1_rad = math.radians(theta1)
t2_rad = math.radians(theta2)

S    = s2 - s1
D    = S / (math.tan(t1_rad) + math.tan(t2_rad))
V    = D * math.tan(t2_rad)
h    = s1
RL_A = rl_instrument - V - h

# ─── Main Layout ──────────────────────────────────────────────────────────────
st.markdown('<p class="hero-title">📐 Moveable Hair Method</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="hero-subtitle">Transit Theodolite Surveying Calculator — Reduced Level of Staff Station</p>',
    unsafe_allow_html=True,
)

left_col, right_col = st.columns([1.1, 1.9], gap="large")

# ── LEFT: Formulas + Step-by-step ─────────────────────────────────────────────
with left_col:
    st.markdown("### 📖 Key Formulas")
    st.markdown(f"""
    <div class="formula-card"><h4>Staff Intercept</h4><p>S = Upper reading − Lower reading</p></div>
    <div class="formula-card"><h4>Horizontal Distance</h4><p>D = S / (tan θ₁ + tan θ₂)</p></div>
    <div class="formula-card"><h4>Vertical Component</h4><p>V = D · tan θ₂ = S·tan θ₂ / (tan θ₁ + tan θ₂)</p></div>
    <div class="formula-card">
        <h4>Reduced Level of Staff Station A</h4>
        <p>RL of A = RL of Instrument Axis − V − h</p>
        <p style='color:#64748b; font-size:0.82rem;'>where h = lower staff reading</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🧮 Step-by-Step Solution")
    st.markdown(f"""
    <div class="step-card">
        <div class="step-title">Step 1 — Input Angles</div>
        <div class="step-eq">θ₁ = {theta1_deg}°{theta1_min}′ = {theta1:.4f}°</div>
        <div class="step-eq">θ₂ = {theta2_deg}°{theta2_min}′ = {theta2:.4f}°</div>
    </div>
    <div class="step-card">
        <div class="step-title">Step 2 — Staff Intercept</div>
        <div class="step-eq">S = {s2:.3f} − {s1:.3f}</div>
        <div class="step-val">S = {S:.3f} m</div>
    </div>
    <div class="step-card">
        <div class="step-title">Step 3 — Horizontal Distance</div>
        <div class="step-eq">D = {S:.3f} / (tan {theta1:.4f}° + tan {theta2:.4f}°)</div>
        <div class="step-eq">D = {S:.3f} / ({math.tan(t1_rad):.5f} + {math.tan(t2_rad):.5f})</div>
        <div class="step-val">D = {D:.3f} m</div>
    </div>
    <div class="step-card">
        <div class="step-title">Step 4 — Vertical Component</div>
        <div class="step-eq">V = {D:.3f} × tan {theta2:.4f}°</div>
        <div class="step-val">V = {V:.3f} m</div>
    </div>
    <div class="step-card">
        <div class="step-title">Step 5 — RL of Staff Station A</div>
        <div class="step-eq">RL = {rl_instrument:.3f} − {V:.3f} − {h:.3f}</div>
        <div class="step-val">RL of A = {RL_A:.3f} m</div>
    </div>
    """, unsafe_allow_html=True)

# ── RIGHT: Results + Graph ─────────────────────────────────────────────────────
with right_col:
    st.markdown("### 📊 Results")

    r1, r2, r3, r4 = st.columns(4)
    with r1:
        st.markdown(f"""<div class="result-card">
            <div class="label">Intercept S</div>
            <div class="value">{S:.3f}</div><div class="unit">metres</div></div>""",
            unsafe_allow_html=True)
    with r2:
        st.markdown(f"""<div class="result-card">
            <div class="label">Distance D</div>
            <div class="value">{D:.3f}</div><div class="unit">metres</div></div>""",
            unsafe_allow_html=True)
    with r3:
        st.markdown(f"""<div class="result-card">
            <div class="label">Vertical V</div>
            <div class="value">{V:.3f}</div><div class="unit">metres</div></div>""",
            unsafe_allow_html=True)
    with r4:
        st.markdown(f"""<div class="result-card">
            <div class="label">RL of A</div>
            <div class="value">{RL_A:.3f}</div><div class="unit">metres</div></div>""",
            unsafe_allow_html=True)

    st.markdown("### 📈 Surveying Diagram")

    # ── Key points ────────────────────────────────────────────────────────────
    O        = np.array([0.0, rl_instrument])
    A_ground = np.array([D,   RL_A])
    A_lower  = np.array([D,   RL_A + h])
    A_upper  = np.array([D,   RL_A + h + S])

    # ── Elevation range for axis limits ───────────────────────────────────────
    elev_range = abs(rl_instrument - RL_A)
    pad_y      = max(elev_range * 0.45, 0.8)
    y_lo = RL_A - pad_y * 2.0
    y_hi = rl_instrument + pad_y * 2.0
    x_lo = -D * 0.10
    x_hi = D  *  1.10

    fig, ax = plt.subplots(figsize=(11, 7))
    fig.patch.set_facecolor("#0f172a")
    ax.set_facecolor("#1e293b")
    for sp in ax.spines.values():
        sp.set_edgecolor("#334155")
    ax.tick_params(colors="#94a3b8")
    ax.xaxis.label.set_color("#94a3b8")
    ax.yaxis.label.set_color("#94a3b8")
    ax.title.set_color("#e2e8f0")
    ax.grid(True, color="#334155", linewidth=0.5, alpha=0.6)

    # Set limits first so transform is valid when we compute arc points
    ax.set_xlim(x_lo, x_hi)
    ax.set_ylim(y_lo, y_hi)

    # Ground line
    ax.plot([x_lo, x_hi], [RL_A, RL_A], color="#374151", linewidth=1.5,
            linestyle="--", zorder=1, label="_nolegend_")

    # Instrument pillar
    ax.plot([0, 0], [RL_A, O[1]], color="#64748b", linewidth=5, zorder=2)
    ax.scatter(*O, color="#f59e0b", s=130, zorder=5, label="Instrument O")
    ax.annotate(f"  Instrument O\n  RL = {rl_instrument:.3f} m",
                O, color="#f59e0b", fontsize=8.5, va="center")

    # Staff pole
    staff_top_y = A_upper[1] + 0.25
    ax.plot([D, D], [RL_A, staff_top_y], color="#94a3b8", linewidth=4, zorder=2)

    # Staff station points
    ax.scatter(*A_lower, color="#38bdf8", s=90, zorder=5,
               label=f"Lower target (θ₁ = {theta1_deg}°{theta1_min}′)")
    ax.scatter(*A_upper, color="#818cf8", s=90, zorder=5,
               label=f"Upper target (θ₂ = {theta2_deg}°{theta2_min}′)")
    ax.scatter(*A_ground, color="#34d399", s=90, zorder=5,
               label=f"Staff station A  RL = {RL_A:.3f} m")

    # Staff reading labels — placed to the LEFT of the staff (no right-side clipping)
    lbl_x = D - D * 0.025
    ax.annotate(f"s₁ = {s1:.3f} m", A_lower, xytext=(lbl_x, A_lower[1]),
                color="#38bdf8", fontsize=8, va="center", ha="right",
                arrowprops=dict(arrowstyle="-", color="#38bdf8", lw=0.8))
    ax.annotate(f"s₂ = {s2:.3f} m", A_upper, xytext=(lbl_x, A_upper[1]),
                color="#818cf8", fontsize=8, va="center", ha="right",
                arrowprops=dict(arrowstyle="-", color="#818cf8", lw=0.8))
    ax.annotate(f"RL_A = {RL_A:.3f} m", A_ground,
                xytext=(lbl_x, A_ground[1] - pad_y * 0.4),
                color="#34d399", fontsize=8, va="top", ha="right",
                arrowprops=dict(arrowstyle="-", color="#34d399", lw=0.8))

    # Lines of sight
    ax.plot([O[0], A_lower[0]], [O[1], A_lower[1]],
            color="#38bdf8", linewidth=1.5, linestyle="--", alpha=0.85, zorder=3)
    ax.plot([O[0], A_upper[0]], [O[1], A_upper[1]],
            color="#818cf8", linewidth=1.5, linestyle="--", alpha=0.85, zorder=3)

    # ── Angle arcs drawn in DISPLAY (pixel) space – no distortion ─────────────
    # We sample points along the arc at fixed pixel radius, then convert back to data coords.
    theta1_data_angle = math.degrees(math.atan2(A_lower[1] - O[1], A_lower[0] - O[0]))
    theta2_data_angle = math.degrees(math.atan2(A_upper[1] - O[1], A_upper[0] - O[0]))

    fig.canvas.draw()  # needed to make the transform valid
    disp_O = ax.transData.transform(O)

    for end_ang_deg, r_px, color in [
        (theta1_data_angle, 55, "#38bdf8"),
        (theta2_data_angle, 80, "#818cf8"),
    ]:
        angs   = np.linspace(0, math.radians(end_ang_deg), 80)
        px_pts = disp_O + r_px * np.column_stack([np.cos(angs), np.sin(angs)])
        dat_pts = ax.transData.inverted().transform(px_pts)
        ax.plot(dat_pts[:, 0], dat_pts[:, 1], color=color, linewidth=1.8, zorder=4)

    # Arc labels at the midpoint of each arc
    for end_ang_deg, r_px, color, lbl in [
        (theta1_data_angle, 55, "#38bdf8", f"θ₁={theta1_deg}°{theta1_min}′"),
        (theta2_data_angle, 80, "#818cf8", f"θ₂={theta2_deg}°{theta2_min}′"),
    ]:
        mid_ang  = math.radians(end_ang_deg / 2)
        lbl_disp = disp_O + (r_px + 14) * np.array([math.cos(mid_ang), math.sin(mid_ang)])
        lbl_dat  = ax.transData.inverted().transform(lbl_disp)
        ax.text(lbl_dat[0], lbl_dat[1], lbl, color=color, fontsize=8.5,
                ha="left", va="bottom", zorder=6,
                bbox=dict(boxstyle="round,pad=0.15", fc="#1e293b", ec="none", alpha=0.7))

    # ── Dimension arrows ──────────────────────────────────────────────────────
    # Horizontal distance D — below ground
    arrow_y = RL_A - pad_y * 0.55
    ax.annotate("", xy=(D, arrow_y), xytext=(0, arrow_y),
                arrowprops=dict(arrowstyle="<->", color="#f59e0b", lw=1.8))
    ax.text(D / 2, arrow_y - pad_y * 0.18, f"D = {D:.3f} m",
            ha="center", color="#f59e0b", fontsize=9)

    # V — vertical component (instrument level ↔ lower hair level), drawn at 60% of D
    v_x = D * 0.60
    ax.annotate("", xy=(v_x, A_lower[1]), xytext=(v_x, O[1]),
                arrowprops=dict(arrowstyle="<->", color="#fb7185", lw=1.8))
    ax.text(v_x - D * 0.02, (A_lower[1] + O[1]) / 2, f"V = {V:.3f} m",
            color="#fb7185", fontsize=8.5, va="center", ha="right")

    # S — staff intercept (lower hair ↔ upper hair), drawn at 85% of D
    s_x = D * 0.85
    ax.annotate("", xy=(s_x, A_upper[1]), xytext=(s_x, A_lower[1]),
                arrowprops=dict(arrowstyle="<->", color="#a3e635", lw=1.8))
    ax.text(s_x - D * 0.02, (A_upper[1] + A_lower[1]) / 2, f"S = {S:.3f} m",
            color="#a3e635", fontsize=8.5, va="center", ha="right")

    ax.set_xlabel("Horizontal Distance (m)", fontsize=9)
    ax.set_ylabel("Elevation (m)", fontsize=9)
    ax.set_title("Moveable Hair Method – Surveying Diagram", fontsize=11, pad=12)
    ax.legend(loc="upper left", fontsize=8,
              facecolor="#1e293b", edgecolor="#334155", labelcolor="#e2e8f0")

    fig.tight_layout(pad=1.8)
    st.pyplot(fig, use_container_width=True)

# ─── Sensitivity Analysis ─────────────────────────────────────────────────────
st.markdown("---")
st.markdown("### 🔬 Sensitivity Analysis — How D & RL change with θ₂")

theta2_range = np.linspace(max(0.5, theta1 + 0.1), 45, 300)
D_range, RL_range = [], []
for t2 in theta2_range:
    t2r = math.radians(t2)
    d   = S / (math.tan(t1_rad) + math.tan(t2r))
    v   = d * math.tan(t2r)
    D_range.append(d)
    RL_range.append(rl_instrument - v - h)

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.8))
for a in (ax1, ax2):
    a.set_facecolor("#1e293b")
    for sp in a.spines.values():
        sp.set_edgecolor("#334155")
    a.tick_params(colors="#94a3b8")
    a.xaxis.label.set_color("#94a3b8")
    a.yaxis.label.set_color("#94a3b8")
    a.title.set_color("#e2e8f0")
    a.grid(True, color="#334155", linewidth=0.5, alpha=0.5)
fig2.patch.set_facecolor("#0f172a")

ax1.plot(theta2_range, D_range, color="#38bdf8", linewidth=2)
ax1.axvline(theta2, color="#f59e0b", linestyle="--", linewidth=1.5, label=f"Current θ₂ = {theta2:.2f}°")
ax1.axhline(D,      color="#f59e0b", linestyle=":",  linewidth=1)
ax1.scatter([theta2], [D], color="#f59e0b", s=80, zorder=5)
ax1.set_xlabel("θ₂ (degrees)")
ax1.set_ylabel("D – Horizontal Distance (m)")
ax1.set_title("D vs θ₂")
ax1.legend(fontsize=8, facecolor="#1e293b", edgecolor="#334155", labelcolor="#e2e8f0")

ax2.plot(theta2_range, RL_range, color="#818cf8", linewidth=2)
ax2.axvline(theta2, color="#f59e0b", linestyle="--", linewidth=1.5, label=f"Current θ₂ = {theta2:.2f}°")
ax2.axhline(RL_A,   color="#f59e0b", linestyle=":",  linewidth=1)
ax2.scatter([theta2], [RL_A], color="#f59e0b", s=80, zorder=5)
ax2.set_xlabel("θ₂ (degrees)")
ax2.set_ylabel("RL of Staff Station A (m)")
ax2.set_title("RL of A vs θ₂")
ax2.legend(fontsize=8, facecolor="#1e293b", edgecolor="#334155", labelcolor="#e2e8f0")

fig2.tight_layout()
st.pyplot(fig2, use_container_width=True)

st.markdown("""
<div style='background:#1e293b; border:1px solid #334155; border-radius:10px;
            padding:1rem 1.5rem; margin-top:1rem;'>
<b style='color:#38bdf8'>ℹ️ About this method</b><br>
<span style='color:#94a3b8; font-size:0.92rem;'>
The <b style='color:#e2e8f0'>Moveable Hair Method</b> uses two vertical angles (θ₁ to the lower
target, θ₂ to the upper target) and the corresponding staff readings to compute horizontal
distance and RL without a stadia diaphragm. All sidebar inputs update the diagram and
sensitivity plots in real-time.
</span></div>
""", unsafe_allow_html=True)
