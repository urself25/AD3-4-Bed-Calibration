import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

def main():
    st.title("3D Printer Bed Calibration Assistant")
    st.write("Enter your 9-point calibration Z-height values below:")
    
    cols = ["A", "B", "C"]
    rows = ["1", "2", "3"]
    input_values = []
    
    for row in rows:
        row_values = []
        cols_input = st.columns(3)
        for i, col in enumerate(cols):
            value = cols_input[i].number_input(f"{col}{row}", value=0.0, step=0.01, format="%.2f")
            row_values.append(value)
        input_values.append(row_values)
    
    values_flat = [val for sublist in input_values for val in sublist]
    
    if st.button("Analyze Calibration"):
        outliers = detect_outliers(values_flat)
        adjustments = suggest_adjustments(values_flat)
        
        # Display outlier detection results
        st.subheader("Outlier Detection")
        for i, (val, is_outlier) in enumerate(zip(values_flat, outliers)):
            if is_outlier:
                st.warning(f"Point {cols[i%3]}{rows[i//3]} ({val:.2f}) is an outlier.")
        
        # Display adjustment suggestions
        st.subheader("Suggested Adjustments")
        adj_matrix = np.array(adjustments).reshape(3, 3)
        st.write("Values indicate how much to adjust each point to even the bed:")
        st.table(adj_matrix)
        
        # Generate heatmap
        st.subheader("Calibration Heatmap")
        fig, ax = plt.subplots()
        sns.heatmap(np.array(input_values), annot=True, fmt=".2f", cmap="coolwarm", center=np.mean(values_flat), linewidths=0.5, linecolor="black", ax=ax)
        ax.set_xticklabels(cols)
        ax.set_yticklabels(rows, rotation=0)
        st.pyplot(fig)

if __name__ == "__main__":
    main()