import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def arc_to_cubic_beziers(center, radius, start_angle, end_angle):
    """Split arc into cubic Bézier segments"""
    segments = []
    total_angle = end_angle - start_angle
    num_segments = int(np.ceil(abs(total_angle) / (np.pi / 2)))  # ≤ 90° per segment
    delta = total_angle / num_segments

    for i in range(num_segments):
        θ0 = start_angle + i * delta
        θ1 = θ0 + delta

        # Points on circle
        p0 = center + radius * np.array([np.cos(θ0), np.sin(θ0)])
        p3 = center + radius * np.array([np.cos(θ1), np.sin(θ1)])

        # Tangent control point length (magic constant for circle)
        alpha = (4 / 3) * np.tan((θ1 - θ0) / 4)

        # Tangents at p0 and p3
        dir0 = np.array([-np.sin(θ0), np.cos(θ0)])
        dir1 = np.array([-np.sin(θ1), np.cos(θ1)])

        p1 = p0 + alpha * radius * dir0
        p2 = p3 - alpha * radius * dir1

        segments.append([p0, p1, p2, p3])
    return segments

def bezier_cubic(t, P0, P1, P2, P3):
    return (1 - t)**3 * P0 + 3 * (1 - t)**2 * t * P1 + 3 * (1 - t) * t**2 * P2 + t**3 * P3

# Parameters
center = np.array([0, 0])
radius = 1.0
start_angle = 0
end_angle = np.pi * 1.5  # 270 degrees

segments = arc_to_cubic_beziers(center, radius, start_angle, end_angle)

# Sample all segments
t_vals = np.linspace(0, 1, 50)
curve_points = []
for seg in segments:
    P0, P1, P2, P3 = seg
    curve_points.extend(bezier_cubic(t, P0, P1, P2, P3) for t in t_vals)
curve_points = np.array(curve_points)

# Animation
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Cubic Bézier Arc Approximation")

# Draw reference circle
circle = plt.Circle(center, radius, color='gray', linestyle='--', fill=False)
ax.add_artist(circle)

# Draw control polygons
for seg in segments:
    cps = np.array(seg)
    ax.plot(cps[:, 0], cps[:, 1], 'k--', alpha=0.3)
    ax.plot(cps[:, 0], cps[:, 1], 'ro', markersize=3)

# Initialize line
curve_line, = ax.plot([], [], 'b-', lw=2)

def init():
    curve_line.set_data([], [])
    return curve_line,

def update(i):
    x = curve_points[:i, 0]
    y = curve_points[:i, 1]
    curve_line.set_data(x, y)
    return curve_line,

ani = animation.FuncAnimation(fig, update, frames=len(curve_points),
                              init_func=init, blit=True, interval=15)

# Save to MP4
ani.save("cubic_arc_approximation.mp4", writer='ffmpeg', fps=30)
print("Saved to cubic_arc_approximation.mp4")
