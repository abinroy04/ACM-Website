import os
from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory, session
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from dotenv import load_dotenv
from glob import glob
from functools import wraps

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

STATIC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

@app.route('/sitemap.xml')
def serve_sitemap():
    return send_from_directory('static', 'sitemap.xml')

@app.route('/robots.txt')
def serve_robots():
    return send_from_directory('static', 'robots.txt')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        try:
            # Email configuration
            msg = MIMEMultipart()
            msg['From'] = os.environ.get('EMAIL_ID')
            msg['To'] = os.environ.get('EMAIL_ID')  # or your desired email
            msg['Subject'] = f"Contact Form Message from {name}"
            
            body = f"""
            Name: {name}
            Email: {email}
            Subject: {subject}
            Message: {message}
            """
            msg.attach(MIMEText(body, 'plain'))
            
            # Send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(os.environ.get('EMAIL_ID'), os.environ.get('APP_PASSWORD'))
                server.send_message(msg)
            
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print(f"Error sending email: {e}")
            flash('Sorry, there was an error sending your message.', 'error')
            
        return redirect(url_for('contact'))
        
    return render_template('contact.html')



# Team Section
TEAM_DATA = {
    'faculty_sponsor': {
        'name': 'Er. Gayathri J L',
        'title': 'Faculty Sponsor',
        'department': 'Department of Computer Science and Engineering',
        'image': 'faculty-sponsor.jpg',
        'linkedin': 'gayathri.jl@saintgits.org',
        'description': 'Assistant Professor at Saintgits College of Engineering, Department of Computer Science and Engineering with expertise in Computer and Information Science.'
    },
    'executive_committee': [
        {
            'name': 'Diya Nair',
            'title': 'Chairperson',
            'department': 'CSE 2022-2026',
            'image': 'DiyaNair.jpg',
            'linkedin': 'https://www.linkedin.com/in/diya-nair-83a12a323/',
            'description': 'Leading the ACM Student Chapter with a focus on fostering technical growth and community engagement.'
        },
        {
            'name': 'Abin Roy',
            'title': 'Vice Chairperson',
            'department': 'CSE 2022-2026',
            'image': 'AbinR.jpg',
            'linkedin': 'https://www.linkedin.com/in/abin-roy-750783293/',
            'description': 'Enthusiastic about technology and creating communities. Using technical skills and strategic planning to support innovation and teamwork.'
        },
        {
            'name': 'Nandana A',
            'title': 'Treasurer',
            'department': 'CSE 2022-2026',
            'image': 'NandanaA.jpg',
            'linkedin': 'https://www.linkedin.com/in/nandana-a-481a18263/',
            'description': 'Dedicated to efficient resource management and encouraging innovation through impactful technical events.'
        }
    ],
    'core_team': [
        {
            'name': 'Adithya Arun',
            'title': 'Operations Head',
            'department': 'CSE 2022-2026',
            'image': 'AdithyaA.jpg',
            'linkedin': 'https://www.linkedin.com/in/adithya-arun-806704322/',
            'description': 'A strategic thinker with a passion for seamless execution. Committed to driving operational excellence and fostering a culture of and teamwork.'
        },
        {
            'name': 'Gayathri Sreekumar',
            'title': 'Marketing Head',
            'department': 'CSE 2022-2026',
            'image': 'GayathriSree.jpg',
            'linkedin': 'https://www.linkedin.com/in/gayathri-sreekumar-95525231b/',
            'description': 'A creative strategist with a flair for innovation and narrative crafting. Driven to bridge ideas and people through impactful campaigns.'
        },
        {
            'name': 'Jeevan Thomas',
            'title': 'Media Head',
            'department': 'CSE 2022-2026',
            'image': 'JeevanT.png',
            'linkedin': 'https://www.linkedin.com/in/jeevan-thomas-214aa531b/',
            'description': 'Passionate about technology and team building, photographer and videographer , mixer and editor . A technically profound personal.'
        }
    ]
}


@app.route('/team')
def team():
    return render_template('team.html', team_data=TEAM_DATA)



# Events Section

@app.route('/events')
def events():
    events_data = get_events_data()
    return render_template('events.html', events_data=events_data)


def get_events_data():
    return {
        'upcoming': [
            {
                'image': 'Workshop.jpg',
                'status': {'text': 'Upcoming', 'color': 'blue'},#Change to green for registration open
                'date': 'March 2025',
                'title': 'BootCamp with TCS',
                'description': 'Learn modern web development techniques with hands-on practice sessions.',
                'category': {'name': 'Workshop', 'color': 'blue'},
                'registration_enabled': 0,
                'registration_fee': 100,
                'event_id': 'bootcamp_tcs'
            },
            {
                'image': 'hackathon.png',
                'status': {'text': 'Upcoming', 'color': 'blue'}, #Change to green for registration open
                'date': 'March, 2025',
                'title': 'Lumino 25',
                'description': '30-hour coding challenge to solve real-world problems with innovative solutions.',
                'category': {'name': 'Hackathon', 'color': 'green'},
                'registration_enabled': 1,
                'registration_fee': 250,
                'event_id': 'lumino_25'
            }
        ],
        'past': [
            {
                'date': 'October 12, 2024',
                'title': 'Exploring Power BI',
                'description': 'Introduction to Power BI, fundamentals and best practices.',
                'category': {'name': 'Workshop', 'color': 'green'},
                'gallery_link': 'power-bi'
            },
            {
                'date': 'Oct 8, 2024',
                'title': 'Crack the Code: Strategies to Dominate a hackathon',
                'description': 'Equip students with strategies, insights, and real-world tips on how to approach hackathons, solve problems effectively, and showcase your skills like a pro!',
                'category': {'name': 'Webinar', 'color': 'blue'},
                'gallery_link': 'crack-the-code'
            },
            {
                'date': 'May 14, 2024',
                'title': 'Student Chapter Inauguration',
                'description': 'Inaguration of the student chapter at Saintgits College of Engineering by the Honourable District Collector of Kottayam Smt. V. Vigneshwari IAS',
                'category': {'name': 'Events', 'color': 'white'},
                'gallery_link': 'inauguration'
            }
        ]
    }



# Gallery Section

def get_event_images(event_id):
    """Get all images for a specific event from the gallery directory"""
    event_path = os.path.join(STATIC_DIR, 'images', 'gallery', event_id)
    
    if not os.path.exists(event_path):
        print(f"Directory does not exist: {event_path}")
        return []
    
    image_files = []
    for ext in ['jpg', 'jpeg', 'png', 'JPG', 'JPEG', 'PNG']:
        pattern = os.path.join(event_path, f'*.{ext}')
        image_files.extend(glob(pattern))
    
    # Simplified return without captions
    return [{'src': f"images/gallery/{event_id}/{os.path.basename(img)}"} 
            for img in set(image_files)]

GALLERY_DATA = {
    'power-bi': {
        'title': 'Exploring Power BI',
        'date': 'October 12, 2024',
        'description': 'Introduction to Power BI, fundamentals and best practices.',
    },
    'crack-the-code': {
        'title': 'Crack the Code: Strategies to Dominate a hackathon',
        'date': 'Oct 8, 2024',
        'description': 'Equip students with strategies, insights, and real-world tips on hackathons.',
    },
    'inauguration': {
        'title': 'Student Chapter Inauguration',
        'date': 'May 14, 2024',
        'description': 'Inauguration by District Collector of Kottayam',
    }
}

@app.route('/gallery')
def gallery():
    event_id = request.args.get('event')
    view = request.args.get('view')
    
    if event_id and event_id in GALLERY_DATA:
        event_data = GALLERY_DATA[event_id].copy()
        event_data['images'] = get_event_images(event_id)
        return render_template('gallery.html', gallery_data=GALLERY_DATA, event_data=event_data, view=view)
    
    if view == 'all':
        for event_id in GALLERY_DATA:
            GALLERY_DATA[event_id]['images'] = get_event_images(event_id)
    else:
        # For the gallery overview, get only the first image from each event
        for event_id in GALLERY_DATA:
            images = get_event_images(event_id)
            GALLERY_DATA[event_id]['images'] = images[:1] if images else []
            print(f"Overview images for {event_id}: {GALLERY_DATA[event_id]['images']}")  # Debug print
    
    return render_template('gallery.html', gallery_data=GALLERY_DATA, event_data=None, view=view)



# Registration Section 

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def send_registration_email(form_data, file_data):
    sender_email = os.getenv('EMAIL_ID')
    app_password = os.getenv('APP_PASSWORD')
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = sender_email  # Sending to yourself
    msg['Subject'] = f"New Event Registration: {form_data['event']}"
    
    # Email body
    body = f"""
    New Registration Details:
    
    Full Name: {form_data['full_name']}
    Phone: {form_data['phone']}
    Email: {form_data['email']}
    College: {form_data['college']}
    Event: {form_data['event']}
    """
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach payment proof if provided
    if file_data:
        # Create image attachment directly from the file data
        img = MIMEImage(file_data)
        img.add_header('Content-Disposition', 'attachment', filename='payment_proof.jpg')
        msg.attach(img)
    
    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/registration', methods=['GET', 'POST'])
def register():
    events_data = get_events_data()
    available_events = [event for event in events_data['upcoming'] 
                       if event['registration_enabled'] == 1]
    
    if request.method == 'POST':
        try:
            # Get form data
            form_data = {
                'full_name': request.form.get('full_name'),
                'phone': request.form.get('phone'),
                'email': request.form.get('email'),
                'college': request.form.get('college'),
                'event': request.form.get('event')
            }
            
            # Validate required fields
            if not all(form_data.values()):
                flash('Please fill in all required fields.', 'error')
                app.logger.warning('Form validation failed: missing required fields')
                return redirect(url_for('register'))
            
            # Handle file data
            file_data = None
            if 'payment_proof' in request.files:
                file = request.files['payment_proof']
                if file and file.filename and allowed_file(file.filename):
                    file_data = file.read()
                else:
                    flash('Please upload a valid image file (PNG, JPG, JPEG, or GIF).', 'error')
                    app.logger.warning('Invalid file upload attempt')
                    return redirect(url_for('register'))
            else:
                flash('Payment proof is required.', 'error')
                app.logger.warning('No file uploaded')
                return redirect(url_for('register'))
            
            # Send email
            email_sent = send_registration_email(form_data, file_data)
            if email_sent:
                app.logger.info(f'Registration successful for: {form_data["email"]}')
                flash(f'Registration successful, {form_data["full_name"]}!', 'success')
            else:
                app.logger.error(f'Email sending failed for: {form_data["email"]}')
                flash('Registration failed. Please try again.', 'error')
            
            return redirect(url_for('register'))
            
        except Exception as e:
            app.logger.error(f"Registration error: {str(e)}")
            flash('An unexpected error occurred. Please try again or reach out via mail.', 'error')
            return redirect(url_for('register'))
    
    return render_template('registration.html', available_events=available_events)

# Webmasters Section ! Do not touch

WEBMASTERS_DATA = [
    {
        'name': 'Abin Roy',
        'department': 'CSE 2022-2026',
        'image': 'AbinR.jpg'
    },
    {
        'name': 'Alen V A',
        'department': 'CSE 2022-2026',
        'image': 'AlenVA.jpg'
    },
    {
        'name': 'Jeevan Thomas',
        'department': 'CSE 2022-2026',
        'image': 'JeevanT.png'
    }
]

@app.route('/webmasters')
def webmasters():
    return render_template('webmasters.html', webmasters=WEBMASTERS_DATA)

if __name__ == '__main__':
    app.run(debug=False)
