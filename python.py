
import ipaddress
import requests


def get_ip_info(ip):
    # Validate the IP address
    try:
        ip_obj = ipaddress.ip_address(ip)
    except ValueError:
        print("Invalid IP address!")
        return

    # Check whether the IP is public
    if not ip_obj.is_global:
        print("Please enter a public IP address.")
        return

    url = f"https://ipwho.is/{ip}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data.get("success", False):
            print("Lookup failed:", data.get("message", "Unknown error"))
            return

        connection = data.get("connection") or {}
        timezone = data.get("timezone") or {}

        print("\n===== IP INFORMATION =====")
        print("IP Address :", data.get("ip", "N/A"))
        print("Country    :", data.get("country", "N/A"))
        print("Region     :", data.get("region", "N/A"))
        print("City       :", data.get("city", "N/A"))
        print("ISP        :", connection.get("isp", "N/A"))
        print("Organization:", connection.get("org", "N/A"))
        print("Timezone   :", timezone.get("id", "N/A"))
        print("==========================")

    except requests.RequestException as error:
        print("Network/API error:", error)

if __name__ == "__main__":
    user_ip = input("Enter a public IP address: ").strip()
    get_ip_info(user_ip)
