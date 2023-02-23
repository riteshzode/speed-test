# Import speedtest library
import speedtest

# Create a Speedtest object
st = speedtest.Speedtest()

st.get_best_server()

# Get download and upload speeds
download = st.download()
upload = st.upload()

# Convert bytes to megabits per second
download_mbps = download / (1024**2)
upload_mbps = upload / (1024**2)

# Print the results
print(f"Download speed: {download_mbps:.2f} Mbps")
print(f"Upload speed: {upload_mbps:.2f} Mbps")

