import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))

ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9 = axs.flat

x_line = list((1, 2, 3, 4, 5, 6))
y_line = list((2, 4, 3, 7, 6, 9))
ax1.plot(x_line, y_line, color='blue', marker='o', linewidth=2, label='Тренд')
ax1.set_title('1. Лінійний графік (Line plot)')
ax1.set_xlabel('Час')
ax1.set_ylabel('Значення')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend()

np.random.seed(10)
x_scat = np.random.rand(30) * 10
y_scat = x_scat + np.random.randn(30) * 1.5
ax2.scatter(x_scat, y_scat, color='crimson', alpha=0.8, edgecolors='black')
ax2.set_title('2. Діаграма розсіювання (Scatter)')
ax2.set_xlabel('Параметр X')
ax2.set_ylabel('Параметр Y')
ax2.grid(True, linestyle=':', alpha=0.5)

categories = list(('ІТ', 'Економіка', 'Право', 'Дизайн'))
students = list((120, 85, 60, 95))
ax3.bar(categories, students, color='skyblue', edgecolor='black', width=0.5)
ax3.set_title('3. Стовпчаста діаграма (Bar chart)')
ax3.set_xlabel('Спеціальність')
ax3.set_ylabel('Кількість студентів')
ax3.grid(axis='y', linestyle='--', alpha=0.5)

grades = np.random.normal(loc=75, scale=12, size=200)
ax4.hist(grades, bins=12, color='mediumseagreen', edgecolor='black', alpha=0.8)
ax4.set_title('4. Гістограма (Histogram)')
ax4.set_xlabel('Оцінка за тест')
ax4.set_ylabel('Частота')
ax4.grid(axis='y', linestyle='--', alpha=0.5)

labels_pie = list(('Навчання', 'Сон', 'Відпочинок', 'Спорт'))
sizes_pie = list((35, 30, 25, 10))
colors_pie = list(('#ff9999', '#66b3ff', '#99ff99', '#ffcc99'))
ax5.pie(sizes_pie, labels=labels_pie, colors=colors_pie, autopct='%1.0f%%', startangle=90)
ax5.set_title('5. Секторна діаграма (Pie chart)')

x_stem = np.linspace(0, 10, 15)
y_stem = np.sin(x_stem)
ax6.stem(x_stem, y_stem, linefmt='purple', markerfmt='ro', basefmt='black')
ax6.set_title('6. Стеблова діаграма (Stem plot)')
ax6.set_xlabel('Відліки')
ax6.set_ylabel('Амплітуда')
ax6.grid(True, linestyle=':', alpha=0.5)

x_c = np.linspace(-3, 3, 50)
y_c = np.linspace(-3, 3, 50)
X_c, Y_c = np.meshgrid(x_c, y_c)
Z_c = np.sin(X_c) * np.cos(Y_c)
contour = ax7.contourf(X_c, Y_c, Z_c, levels=12, cmap='coolwarm')
ax7.contour(X_c, Y_c, Z_c, levels=12, colors='black', linewidths=0.4)
fig.colorbar(contour, ax=ax7)
ax7.set_title('7. Контурний графік (Contour)')
ax7.set_xlabel('X')
ax7.set_ylabel('Y')

x_q = np.linspace(-2, 2, 10)
y_q = np.linspace(-2, 2, 10)
X_q, Y_q = np.meshgrid(x_q, y_q)
Z_q = X_q**2 + Y_q**2
U, V = np.gradient(Z_q)
ax8.quiver(X_q, Y_q, U, V, color='darkblue')
ax8.set_title('8. Поле градієнтів (Quiver)')
ax8.set_xlabel('X')
ax8.set_ylabel('Y')
ax8.grid(True, linestyle=':', alpha=0.5)

fs = 500
t = np.linspace(0, 4, 4 * fs)
signal = np.sin(2 * np.pi * (20 + 30 * t) * t) + 0.3 * np.random.randn(len(t))
Pxx, freqs, bins, im = ax9.specgram(signal, NFFT=128, noverlap=64, Fs=fs, cmap='viridis')
fig.colorbar(im, ax=ax9)
ax9.set_title('9. Спектрограма (Spectrogram)')
ax9.set_xlabel('Час (с)')
ax9.set_ylabel('Частота (Гц)')

plt.tight_layout()
plt.show()