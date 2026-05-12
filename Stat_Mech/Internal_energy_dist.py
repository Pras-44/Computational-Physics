import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import cm

# Personal Preference
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['mathtext.fontset'] = 'stix'

# 1. Define the 10x10 State Space Grid
x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)
X, Y = np.meshgrid(x, y)


# 2. Define the Energy Function based (T)
def calc_U(T):
    # Gaussian distribution representing the concentration of Internal Energy
    return 100 * np.exp(-((X - 2) ** 2 + (Y - 2) ** 2) / (2 * T ** 2))


# --- Setup the 3D Figure ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.25)  # Make room for the slider

# Aesthetics
fig.patch.set_facecolor('#ffffff')
ax.set_facecolor('#f4f4f4')

# Initial State: Cold & Rigid
T_init = 1.0
U_init = calc_U(T_init)

# Store the surface in a list so we can reference and delete it during updates
surf = [ax.plot_surface(X, Y, U_init, cmap=cm.inferno, linewidth=0, antialiased=True, alpha=0.9)]

ax.set_title("Relationship between internal energy and temperature", fontsize=14, weight='bold')
ax.set_xlabel("State Space ($N_x$)", fontsize=12)
ax.set_ylabel("State Space ($N_y$)", fontsize=12)
ax.set_zlabel("Internal Energy ($U$)", fontsize=12)

# Lock the Z-axis so the mountain actually "melts" instead of the camera auto-scaling
ax.set_zlim(0, 100)

#No rotation
ax.view_init(elev=30, azim=-45)
ax.disable_mouse_rotation()

#Interactive Temperature Slider
ax_T = plt.axes([0.2, 0.1, 0.6, 0.03], facecolor='lightgoldenrodyellow')
slider_T = Slider(ax_T, 'Temperature ($T$)', 0.5, 6.0, valinit=T_init)


def update(val):
    current_T = slider_T.val

    # 1. Remove the old mountain
    surf[0].remove()

    # 2. Calculate the new energy distribution
    new_U = calc_U(current_T)

    # 3. Draw the new mountain
    surf[0] = ax.plot_surface(X, Y, new_U, cmap=cm.inferno, linewidth=0, antialiased=True, alpha=0.9)

    fig.canvas.draw_idle()


# Attach the update function to the slider
slider_T.on_changed(update)

plt.show()

#PL
