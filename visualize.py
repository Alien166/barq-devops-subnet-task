import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("/home/toba/Barq-System/subnet_report.json")

df["Subnet"] = df["Network Address"] + "/" + df["CIDR"].astype(str)

plt.figure(figsize=(12,6))
plt.bar(df["Subnet"], df["Usable Hosts"], color='skyblue')
plt.xlabel("Subnet")
plt.ylabel("Usable IP Addresses per Subnet")
plt.title("Usable Hosts per Subnet")
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("/home/toba/Barq-System/network_plot1.png")
plt.show()


labels = df["Subnet"]
sizes = df["Usable Hosts"]

plt.figure(figsize=(16, 16))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140
)

plt.title("Usable IPs per Subnet" , fontsize=20 )
plt.tight_layout()

plt.savefig("/home/toba/Barq-System/network_pie_chart1.png")

plt.show()