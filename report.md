# Subnet Analysis Report

## 1. Which subnet has the most hosts?
The subnet `10.0.0.0/22` has the most usable hosts (1022 hosts).

## 2. Are there any overlapping subnets?
Yes, there is an overlap between `10.0.0.0/23` and `10.0.0.0/24`.

## 3. What is the smallest and largest subnet in terms of address space?
- Smallest: `192.168.1.0/24` (254 usable hosts)
- Largest: `10.0.0.0/22` (1022 usable hosts)

## 4. Suggested Subnetting Strategy
Use smaller subnets (e.g., /25 or /26) for networks with few devices to avoid wasting IPs. Group similar departments or services into VLSM-based subnets.
