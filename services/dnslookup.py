import dns.resolver

def get_mx(domain):
    try:
        resolver = dns.resolver.Resolver()

        resolver.nameservers = [
            "8.8.8.8",
            "8.8.4.4",
            "1.1.1.1"
        ]

        answers = resolver.resolve(
            domain,
            "MX",
            lifetime=5
        )

        return sorted(
            [str(r.exchange) for r in answers]
        )

    except Exception as e:
        print(f"MX lookup failed: {e}")
        return []