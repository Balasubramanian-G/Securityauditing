from socket import socket, AF_INET, SOCK_STREAM, gethostbyname
import requests

target = input("Enter the IP address or domain: ")
ip = gethostbyname(target)
startingport = int(input("Enter starting port number: "))
endingport = int(input("Enter ending port number: "))
portstoscan = range(startingport, endingport + 1)


def scan_ports(ip, ports):
    open_ports = []
    print(f"\nScanning ports {startingport} to {endingport} on {ip}...\n")
    for i in ports:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, i))
            if result == 0:
                print(f"Port {i} is open")
                open_ports.append(i)
            else:
                print(f"Port {i} is closed")
            sock.close()
        except Exception as e:
            print(f"Error scanning port {i}: {e}")
    return open_ports


def grab_banner(ip, port):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip, port))
        try_recv = s.recv(1024)
        s.close()
        if try_recv:
            return try_recv.decode(errors='ignore').strip()
        else:
            return "no banner"
    except TimeoutError:
        return "timed out"
    except Exception as e:
        return f"Error: {e}"
        


def check_http_headers(url):
    headers_report = {}
    
    try:
        response = requests.get(url, timeout=3)
        headers = response.headers
        for header in ["Content-Security-Policy","Strict-Transport-Security","X-Content-Type-Options","X-Frame-Options","X-XSS-Protection"]:
            if header in headers:
                headers_report[header] = "Present"
            else:
                headers_report[header] = "Missing"
                
    except requests.exceptions.RequestException as e:
        headers_report["HTTP Header Check"] = f"Failed to retrieve headers: {e}"
        
    return headers_report
    

def generate_report(ip, open_ports, banners, http_headers):
    report_lines = []
    report_lines.append("--- Security Audit Report ---")
    report_lines.append(f"Target: {ip}\n")

    report_lines.append("Open Ports:")
    if open_ports:
        for port in open_ports:
            report_lines.append(f" - Port {port} is OPEN")
    else:
        report_lines.append("No open ports found.")
    report_lines.append("")

    report_lines.append("Service Banners:")
    for port, banner in banners.items():
        report_lines.append(f" - Port {port}: {banner}")
    report_lines.append("")

    report_lines.append("HTTP Security Headers:")
    if http_headers:
        for header, status in http_headers.items():
            report_lines.append(f" - {header}: {status}")
    else:
        report_lines.append("No HTTP services found.")

    return "\n".join(report_lines)

open_ports = scan_ports(ip, portstoscan)
banners = {}
for i in open_ports:
    banner = grab_banner(ip,i)
    banners[i] = banner

custom_http_port = input("Enter port for HTTP header check (or press enter to skip):")
if custom_http_port:
    url = f"http://{target}:{custom_http_port}"
    http_headers = check_http_headers(url)
else:
    http_headers = {}
    
report = generate_report(ip,open_ports,banners,http_headers)

with open("security_audit_report.txt", "w") as f:
    f.write(report)
print("\nSecurity audit complete.Report saved to 'security_audit_report.txt'")
