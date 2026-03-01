import pyshark
import sys

def extract_dns_queries(pcap_file):
    try:
        capture = pyshark.FileCapture(
            pcap_file,
            display_filter='dns.flags.response == 0'
        )

        seen = set()
        dns_server_ip = None
        results = []

        for packet in capture:
            try:
                if 'DNS' in packet:

                    domain = packet.dns.qry_name

                    # IPv4
                    if 'IP' in packet:
                        src_ip = packet.ip.src
                        dst_ip = packet.ip.dst

                    # IPv6
                    elif 'IPV6' in packet:
                        src_ip = packet.ipv6.src
                        dst_ip = packet.ipv6.dst
                    else:
                        continue

                    # Store DNS server IP (first destination found)
                    if dns_server_ip is None:
                        dns_server_ip = dst_ip

                    entry = (src_ip, domain)

                    if entry not in seen:
                        seen.add(entry)
                        results.append(entry)

            except AttributeError:
                continue

        capture.close()

        # ====== OUTPUT FORMAT ======
        print("\nPyShark DNS Query Extractor")
        print("=" * 40)

        if dns_server_ip:
            print(f"DNS IP Address: {dns_server_ip}\n")

        print("{:<20} {}".format("Source IP", "Domain Name"))
        print("-" * 50)

        for src_ip, domain in results:
            print("{:<20} {}".format(src_ip, domain))

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 dnsExtract.py <file.pcap or file.pcapng>")
        sys.exit(1)

    extract_dns_queries(sys.argv[1])
