import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre
import matplotlib.animation as animation
from matplotlib.widgets import Slider

#Task 1

x = np.linspace(-1, 1, 400)
plt.figure(figsize=(10,6))

for n in range(1, 8):
    y = legendre(n)(x)
    #plt.plot(x, y, label=f'n = {n}')

# Реализация выносок (с помощью аннотаций)
for n, xpos in enumerate(np.linspace(-0.9, 0.9, 7), start=1):
    ymax = legendre(n)(xpos)
    plt.annotate(f'n = {n}', xy=(xpos, ymax), xytext=(xpos+0.1, ymax + 0.2),
                 arrowprops=dict(facecolor='black', shrink=0.05), fontsize=9)

plt.title('Полиномы Лежандра')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('P(x)')
plt.show()

#Task 2
ratios = [(3,2), (3,4), (5,4), (5,6)]
t = np.linspace(0, 2*np.pi, 1000)

fig, axes = plt.subplots(2, 2, figsize=(10, 7))
axes = axes.flatten()

for ax, ratio in zip(axes, ratios):
    x = np.sin(ratio[0]*t)
    y = np.sin(ratio[1]*t)
    ax.plot(x, y)
    ax.set_title(f"{ratio[0]} : {ratio[1]}")
    ax.axis('equal')
    ax.grid(True)

plt.tight_layout()
plt.show()

#Task 3

fig, ax = plt.subplots()
t = np.linspace(0, 2*np.pi, 1000)

line, = ax.plot([], [], lw=2)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.grid(True)
ax.set_title('Animation Lissague')

def animate(i):
    freq = i / 100  # параметр изменяется от 0 до 1
    x = np.sin(t)
    y = np.sin(freq * t)
    line.set_data(x, y)
    return line,

ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)
plt.show()

#Task 4
x = np.linspace(0, 4*np.pi, 500)

fig, axs = plt.subplots(3, 1, figsize=(9, 8))
plt.subplots_adjust(left=0.1, bottom=0.35)

# Исходные настройки волн
ampl1, freq1 = 1, 1
ampl2, freq2 = 1, 2

wave1, = axs[0].plot(x, ampl1*np.sin(freq1*x), color='blue', label='Wave 1')
wave2, = axs[1].plot(x, ampl2*np.sin(freq2*x), color='green', label='Wave 2')
result_wave, = axs[2].plot(x, ampl1*np.sin(freq1*x) + ampl2*np.sin(freq2*x), color='red', label='Result')

# Слайдеры
axfreq1 = plt.axes([0.25, 0.25, 0.65, 0.03])
sfreq1 = Slider(axfreq1, 'Freq 1', 0.1, 10.0, valinit=freq1)

axampl1 = plt.axes([0.25, 0.2, 0.65, 0.03])
sampl1 = Slider(axampl1, 'Ampl 1', 0.1, 5.0, valinit=ampl1)

axfreq2 = plt.axes([0.25, 0.1, 0.65, 0.03])
sfreq2 = Slider(axfreq2, 'Freq 2', 0.1, 10.0, valinit=freq2)

axampl2 = plt.axes([0.25, 0.05, 0.65, 0.03])
sampl2 = Slider(axampl2, 'Ampl 2', 0.1, 5.0, valinit=ampl2)

def update(val):
    f1, a1, f2, a2 = sfreq1.val, sampl1.val, sfreq2.val, sampl2.val
    wave1.set_ydata(a1*np.sin(f1*x))
    wave2.set_ydata(a2*np.sin(f2*x))
    result_wave.set_ydata(a1*np.sin(f1*x) + a2*np.sin(f2*x))
    fig.canvas.draw_idle()

sfreq1.on_changed(update)
sampl1.on_changed(update)
sfreq2.on_changed(update)
sampl2.on_changed(update)

axs[0].set_title('Wave 1')
axs[1].set_title('Wave 2')
axs[2].set_title('Wave 1 + Wave 2')

plt.tight_layout()
plt.show()

#Task 5

# Данные
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Среднеквадратичная ошибка MSE - пример функции
Z = (X - 2)**2 + (Y - 3)**2

fig = plt.figure(figsize=(12, 6))

# Обычный масштаб
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE обычный масштаб')

# Логарифмический масштаб по z
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_zscale('log')
ax2.set_title('MSE логарифмический масштаб по z')

plt.tight_layout()
plt.show()