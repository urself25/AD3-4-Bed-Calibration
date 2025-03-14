import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def detect_outliers(values, threshold=1.5):
    mean_value = np.mean(values)
    std_dev = np.std(values)
    lower_threshold = mean_value - (threshold * std_dev)
    upper_threshold = mean_value + (threshold * std_dev)
    return [(val < lower_threshold or val > upper_threshold) for val in values]

def round_adjustment(value, increment):
    return round(value / increment) * increment

def suggest_adjustments(values):
    center_value = values[4]  # The center point (B2) is always the reference
    adjustments = []
    for i, v in enumerate(values):
        diff = center_value - v  # Calculate difference from center
        if i == 4:  # Center point
            adjustments.append(round_adjustment(diff, 0.02))
        else:
            if abs(diff) >= 0.5:
                adjustments.append(round_adjustment(diff, 0.5))
            elif abs(diff) >= 0.1:
                adjustments.append(round_adjustment(diff, 0.1))
            else:
                adjustments.append(round_adjustment(diff, 0.05))
    return adjustments

def generate_heatmap(values):
    values_matrix = np.array(values).reshape(3, 3)
    fig, ax = plt.subplots()
    sns.heatmap(values_matrix, annot=True, fmt=".2f", cmap="coolwarm", center=np.mean(values), linewidths=0.5, linecolor="black", ax=ax)
    ax.set_xticklabels(['A', 'B', 'C'])
    ax.set_yticklabels(['1', '2', '3'], rotation=0)

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    encoded = base64.b64encode(buf.read()).decode("utf-8")
    plt.close(fig)
    return encoded  # Return the heatmap image as a base64 string
