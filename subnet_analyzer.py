import pandas as pd
import ipaddress
import matplotlib.pyplot as plt

file_path = "/home/toba/Barq-System/ip_data.xlsx"

df = pd.read_excel(file_path)

print("Data from Excel:")
print(df.head(26))
print("-" * 50)

df["CIDR"] = df["Subnet Mask"].apply(
    lambda mask: ipaddress.IPv4Network(f"0.0.0.0/{mask}", strict=False).prefixlen
)

print("Data with CIDR:")
print(df.head(26))
print("-" * 50)

def calc_network_info(row):
    ip = row["IP Address"]
    cidr = row["CIDR"]
    network = ipaddress.IPv4Network(f"{ip}/{cidr}", strict=False)
    return pd.Series({
        "Network Address": str(network.network_address),
        "Broadcast Address": str(network.broadcast_address),
        "Usable Hosts": network.num_addresses - 2
    })

df[["Network Address", "Broadcast Address", "Usable Hosts"]] = df.apply(calc_network_info, axis=1)

print("Data with Network Information:")
print(df.head(26))
print("-" * 50)

grouped = df.groupby(["Network Address", "CIDR"]).size().reset_index(name='Count of IPs')

print("Grouped Data:")
print(grouped)
print("-" * 50)

output_json_path = "/home/toba/Barq-System/subnet_report1.json"
df.to_json(output_json_path, orient="records", indent=4)

print(f"Subnet report saved to {output_json_path}")
print("-" * 50)


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