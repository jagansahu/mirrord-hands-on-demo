from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class PaymentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/payment":
            amount = 100
            fee = 5
            total = amount + fee

            response = {
                "service": "payment-service",
                "amount": amount,
                "fee": fee,
                "total": total,
                "version": "local-v2"
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

            print(f"Payment calculated: ${total}")
        else:
            self.send_error(404)

HTTPServer(("0.0.0.0", 8080), PaymentHandler).serve_forever()
