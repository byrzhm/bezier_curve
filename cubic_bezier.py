import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 4 control points for cubic Bézier curve
P0 = np.array([0, 0])
P1 = np.array([1, 2])
P2 = np.array([3, -1])
P3 = np.array([4, 0])

def bezier_cubic(t, P0, P1, P2, P3):
    """Compute a point on a cubic Bézier curve"""
    return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-2, 3)
ax.set_aspect('equal')
ax.set_title("Cubic Bézier Curve Animation")

# Plot control points and lines
control_points = np.array([P0, P1, P2, P3])
ax.plot(control_points[:, 0], control_points[:, 1], 'k--', alpha=0.5)
ax.plot(control_points[:, 0], control_points[:, 1], 'ro')

# Line that will be updated
curve_line, = ax.plot([], [], 'b-', linewidth=2)

# Prepare data for animation
t_vals = np.linspace(0, 1, 200)
curve_points = np.array([bezier_cubic(t, P0, P1, P2, P3) for t in t_vals])

def init():
    curve_line.set_data([], [])
    return curve_line,

def update(frame):
    x = curve_points[:frame, 0]
    y = curve_points[:frame, 1]
    curve_line.set_data(x, y)
    return curve_line,

ani = animation.FuncAnimation(fig, update, frames=len(t_vals),
                              init_func=init, blit=True, interval=20)

# Show the animation
# plt.show()

# Save to mp4
ani.save("cubic_bezier.mp4", writer='ffmpeg', fps=30)
print("Saved to cubic_bezier.mp4")
