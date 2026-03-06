from pyngrok import ngrok, conf
import subprocess, sys, time, os, threading

PORT = 5000

def run_flask():
    """Run the Flask app as a subprocess."""
    subprocess.Popen(
        [sys.executable, "app.py"],
        cwd=os.path.dirname(__file__)
    )

print("=" * 55)
print("  Heart Disease System - Public Host Launcher")
print("=" * 55)

# Start Flask in background thread (subprocess)
print("\n[1/3] Starting Flask server on port", PORT, "...")
run_flask()
time.sleep(3)  # Give Flask time to start

# Open ngrok tunnel
print("[2/3] Creating public ngrok tunnel...")
try:
    tunnel = ngrok.connect(PORT, "http")
    public_url = tunnel.public_url
    print("\n" + "=" * 55)
    print("  ✅  YOUR PUBLIC LINK IS READY!")
    print("=" * 55)
    print(f"\n  🌐  {public_url}")
    print(f"\n  Local:  http://localhost:{PORT}")
    print("\n  Share the link above with anyone!")
    print("  Press Ctrl+C to stop the server.\n")
    print("=" * 55)

    # Keep running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[3/3] Shutting down...")
        ngrok.kill()

except Exception as e:
    print(f"\n[ERROR] Could not create tunnel: {e}")
    print("\nTIP: You can still access locally at:")
    print(f"  http://localhost:{PORT}")
