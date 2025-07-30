import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the 3 control points
P0 = np.array([0, 0])
P1 = np.array([2, 3])
P2 = np.array([4, 0])

def bezier_quadratic(t, P0, P1, P2):
    """Evaluate quadratic Bézier curve at parameter t"""
    return (1 - t)**2 * P0 + 2 * (1 - t) * t * P1 + t**2 * P2

# Set up figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)
ax.set_aspect('equal')
ax.set_title("Quadratic Bézier Curve Animation")

# Plot control polygon and points
control_points = np.array([P0, P1, P2])
ax.plot(control_points[:, 0], control_points[:, 1], 'k--', alpha=0.5)
ax.plot(control_points[:, 0], control_points[:, 1], 'ro')

# Initialize curve line
curve_line, = ax.plot([], [], 'b-', linewidth=2)

# Sample points along the curve
t_vals = np.linspace(0, 1, 200)
curve_points = np.array([bezier_quadratic(t, P0, P1, P2) for t in t_vals])

def init():
    curve_line.set_data([], [])
    return curve_line,

def update(frame):
    x = curve_points[:frame, 0]
    y = curve_points[:frame, 1]
    curve_line.set_data(x, y)
    return curve_line,

# Animate
ani = animation.FuncAnimation(fig, update, frames=len(t_vals),
                              init_func=init, blit=True, interval=20)

# Save to MP4
ani.save("quadratic_bezier.mp4", writer='ffmpeg', fps=30)
print("Saved to quadratic_bezier.mp4")
