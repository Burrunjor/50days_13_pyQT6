from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox
import sys



class AveSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()
        self.metric_selector = QComboBox()
        self.metric_selector.addItems(['Imperial (miles)', 'Metric (Kms)'])
        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()
        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)
        self.output_label = QLabel("")

        # Add Widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.metric_selector, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.output_label, 3, 0, 1, 3)
        self.setLayout(grid)

    def calculate(self):
        speed = float(self.distance_line_edit.text()) / float(self.time_line_edit.text())
        if self.metric_selector .currentText() == 'Imperial (miles)':
            self.output_label.setText(f'Average Speed: {round(speed, 2)} mph')
        if self.metric_selector .currentText() == 'Metric (Kms)':
            self.output_label.setText(f'Average Speed: {round(speed, 2)} kmph')


app = QApplication(sys.argv)
ave_speed_calculator = AveSpeedCalculator()
ave_speed_calculator.show()
sys.exit(app.exec())