import numpy_financial as npf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


"""
tvm calc1
console log output: cash flow growth overtime.

NumPy Financial:

Author: NumPy Developers
Date: Dec 15 2023
Title: NumPy Financial
Version: stable
Type: Computer Program/Software
URL: https://numpy.org/numpy-financial/

"""

# Given values for future value calculation, negative for outflow (cash going into investment)
cash_flows = [
    -1200,
    -2400,
    -4800,
    -9600,
    -19200,
]  # Cash flows over 5 periods, client doubles investment every year
interest_rate = 0.3  # Annual interest rate

# Calculate future value using npf.fv function
future_value_tvm1 = npf.fv(
    rate=interest_rate, nper=len(cash_flows), pmt=300, pv=cash_flows[0]
)

print(f"Future Value: {future_value_tvm1:.2f}")

"""
tvm calc2
plot futrevalues overtime with different leverage amounts.

Matplotlib:

Author: Matplotlib Development Team
Date: Dec 15 2023
Title: Matplotlib: Visualization with Python
Version: stale
Type: Computer Program/Software
URL: https://matplotlib.org/stable/

NumPy Financial:

Author: NumPy Developers
Date: Dec 15 2023
Title: NumPy Financial
Version: stable
Type: Computer Program/Software
URL: https://numpy.org/numpy-financial/



"""

import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
import numpy as np

# Given values for present value calculation
present_value = 1000
interest_rate = 0.12  # 12% interest rate
periods = np.arange(1, 5) * 2  # Array of periods (1 to 5 years) scaled by 2

# Calculate future values
future_value_tvm2 = present_value * (1 + interest_rate) ** periods

# Different investments
investment0 = future_value_tvm2  # no leverage
investment1 = future_value_tvm2 * 2  # 2x leverage
investment2 = future_value_tvm2 * 3  # 3x leverage


# Function to update the plot
def investmentfunc(label):
    if label == "Show All":
        line0.set_ydata(investment0)
        line1.set_ydata(investment1)
        line2.set_ydata(investment2)
        line0.set_visible(True)
        line1.set_visible(True)
        line2.set_visible(True)
    else:
        investmentdict = {
            "No Leverage": investment0,
            "2x Leverage": investment1,
            "3x Leverage": investment2,
        }
        ydata = investmentdict[label]
        line0.set_ydata(ydata)
        line1.set_ydata(ydata)
        line2.set_ydata(ydata)
        line0.set_visible(label == "No Leverage")
        line1.set_visible(label == "2x Leverage")
        line2.set_visible(label == "3x Leverage")

    ax.relim()
    ax.autoscale_view()
    plt.draw()


# Create a line plot using Matplotlib
fig, ax = plt.subplots()
(line0,) = ax.plot(periods, investment0, lw=2, color="red", visible=False)
(line1,) = ax.plot(periods, investment1, lw=2, color="blue", visible=False)
(line2,) = ax.plot(periods, investment2, lw=2, color="green", visible=False)

# Define the position of the radio buttons
# Coordinates are in the form [left, bottom, width, height]
radio_ax = plt.axes([0.8, 0.78, 0.15, 0.15])
radio_labels = ("No Leverage", "2x Leverage", "3x Leverage", "Show All")
radio = RadioButtons(radio_ax, radio_labels)

# Set up the radio button event handler
radio.on_clicked(investmentfunc)

# Set y-axis limits to increase by 500
ax.set_ylim(0, max(investment2) + 500)

# Display the plot
plt.grid(True)
plt.show()
