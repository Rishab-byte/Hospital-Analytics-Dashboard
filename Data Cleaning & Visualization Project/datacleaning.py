import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('hospital_analytics_raw_dataset.csv')
data = data.drop_duplicates()
print(data.duplicated().sum())

data['disease'] = data['disease'].fillna(data['disease'].mode()[0])
data['age'] = data['age'].fillna(data['age'].median())
data['hospital'] = data['hospital'].fillna(data['hospital'].mode()[0])
data['treatment_cost'] = data['treatment_cost'].fillna(
    data['treatment_cost'].median())
data['recovery_days'] = pd.to_numeric(data['recovery_days'])
data['recovery_days'] = data['recovery_days'].fillna(
    data['recovery_days'].median())

data.to_csv('hospital_cleaned_data.csv', index=False)

data = pd.read_csv('hospital_cleaned_data.csv')
avg_cost = data.groupby("hospital")["treatment_cost"].mean()
plt.style.use("dark_background")

plt.rcParams.update({
    "figure.facecolor": "#1e293b",
    "axes.facecolor": "#1e293b",
    "axes.edgecolor": "#334155",
    "axes.labelcolor": "white",
    "xtick.color": "#94a3b8",
    "ytick.color": "#94a3b8",
    "text.color": "white",
    "grid.color": "#334155",
    "grid.alpha": 0.4,
    "font.size": 11
})
plt.barh(avg_cost.index, avg_cost.values, color="#38bdf8",
         edgecolor="#2563eb",
         linewidth=1.5)
plt.title("Average Treatment Cost by Hospital")
plt.xlabel("Average Treatment Cost (₹)")
plt.ylabel("Hospital")
plt.grid(axis='x', linestyle='--')
plt.savefig("cost_hospital.png", dpi=300, bbox_inches="tight")
plt.tight_layout()
plt.show()


plt.hist(data['age'], color="#93c5fd", bins=15,
         edgecolor="#38bdf8",
         alpha=0.85)
plt.title("Age Distribution of Patients", fontsize=14)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("age_distribution.png", dpi=300, bbox_inches="tight")
plt.show()


disease_count = data['disease'].value_counts()
plt.barh(disease_count.index, disease_count.values, color="#2563eb",
         edgecolor="#2563eb")
plt.title("Disease Occurrence Among Patients", fontsize=14)
plt.xlabel("Number of Patients")
plt.ylabel("Disease")
plt.legend()
plt.xticks(rotation=45)
plt.grid(axis='x', linestyle='--')
plt.tight_layout()
plt.savefig("disease_frequency.png", dpi=300, bbox_inches="tight")
plt.show()


gender_count = data['gender'].value_counts()
plt.pie(gender_count.values, labels=gender_count.index, colors=[
    "#38bdf8",
    "#2563eb",
    "#60a5fa",
    "#93c5fd"
])
plt.title("Gender Distribution of Patients", fontsize=14)
plt.tight_layout()
plt.savefig("gender_distribution.png", dpi=300, bbox_inches="tight")
plt.show()
