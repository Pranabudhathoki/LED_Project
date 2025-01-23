import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
import re
from datetime import datetime
from tkcalendar import Calendar

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sunset Hotel Management System")
        self.root.geometry("1200x800")
        
        # Set color scheme
        self.colors = {
            'primary': '#D4AF37',  # Gold
            'secondary': '#1E3D59', # Dark blue
            'bg': '#F8F9FA',
            'text': '#333333',
            'white': '#FFFFFF'
        }
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure(
            "Custom.TButton",
            padding=10,
            font=("Helvetica", 12),
            background=self.colors['primary']
        )
        self.style.configure(
            "Title.TLabel",
            font=("Helvetica", 24, "bold"),
            foreground=self.colors['secondary']
        )
        
        # Create main container
        self.main_container = tk.Frame(root, bg=self.colors['bg'])
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        # Initialize navigation history
        self.nav_history = []
        
        # Show home page
        self.show_home_page()
    
    def show_home_page(self):
        self.clear_page()
        
        # Header
        header = self.create_header()
        
        # Main content
        content = tk.Frame(self.main_container, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Hero section
        hero = tk.Frame(content, bg=self.colors['bg'])
        hero.pack(fill=tk.X, pady=50)
        
        hero_title = tk.Label(
            hero,
            text="SUNSET HOTEL",
            font=("Helvetica", 48, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        hero_title.pack()
        
        hero_subtitle = tk.Label(
            hero,
            text="Where comfort meets elegance",
            font=("Helvetica", 24),
            fg=self.colors['text'],
            bg=self.colors['bg']
        )
        hero_subtitle.pack(pady=10)
        
        # Action buttons
        btn_frame = tk.Frame(content, bg=self.colors['bg'])
        btn_frame.pack(pady=30)
        
        book_btn = ttk.Button(
            btn_frame,
            text="Book Now",
            style="Custom.TButton",
            command=self.show_booking_page
        )
        book_btn.pack(side=tk.LEFT, padx=10)
        
        explore_btn = ttk.Button(
            btn_frame,
            text="Explore Rooms",
            style="Custom.TButton",
            command=self.show_rooms_page
        )
        explore_btn.pack(side=tk.LEFT, padx=10)
        
        # Features section
        features = tk.Frame(content, bg=self.colors['bg'])
        features.pack(fill=tk.X, pady=50)
        
        features_title = tk.Label(
            features,
            text="Our Features",
            font=("Helvetica", 32, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        features_title.pack(pady=20)
        
        feature_items = tk.Frame(features, bg=self.colors['bg'])
        feature_items.pack()
        
        self.create_feature(feature_items, "Luxury Rooms", "Experience ultimate comfort")
        self.create_feature(feature_items, "Fine Dining", "World-class cuisine")
        self.create_feature(feature_items, "Spa & Wellness", "Rejuvenate your senses")
    
    def show_login_page(self):
        self.clear_page()
        
        # Create centered container
        container = tk.Frame(self.main_container, bg=self.colors['white'])
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Logo
        logo = tk.Label(
            container,
            text="SUNSET",
            font=("Helvetica", 36, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['white']
        )
        logo.pack(pady=20)
        
        # Welcome text
        welcome = tk.Label(
            container,
            text="Welcome Back",
            font=("Helvetica", 24),
            fg=self.colors['text'],
            bg=self.colors['white']
        )
        welcome.pack(pady=10)
        
        # Login form
        form = tk.Frame(container, bg=self.colors['white'])
        form.pack(pady=20)
        
        # Username
        username_label = tk.Label(
            form,
            text="Username",
            font=("Helvetica", 12),
            fg=self.colors['text'],
            bg=self.colors['white']
        )
        username_label.pack(anchor="w")
        
        username_entry = ttk.Entry(form, width=40)
        username_entry.pack(pady=5)
        
        # Password
        password_label = tk.Label(
            form,
            text="Password",
            font=("Helvetica", 12),
            fg=self.colors['text'],
            bg=self.colors['white']
        )
        password_label.pack(anchor="w")
        
        password_entry = ttk.Entry(form, width=40, show="•")
        password_entry.pack(pady=5)
        
        # Login button
        login_btn = ttk.Button(
            form,
            text="Login",
            style="Custom.TButton",
            command=self.handle_login
        )
        login_btn.pack(pady=20)
        
        # Links
        links = tk.Frame(form, bg=self.colors['white'])
        links.pack()
        
        signup_link = tk.Label(
            links,
            text="Create Account",
            font=("Helvetica", 10),
            fg="blue",
            cursor="hand2",
            bg=self.colors['white']
        )
        signup_link.pack(side=tk.LEFT, padx=10)
        signup_link.bind("<Button-1>", lambda e: self.show_signup_page())
        
        forgot_link = tk.Label(
            links,
            text="Forgot Password?",
            font=("Helvetica", 10),
            fg="blue",
            cursor="hand2",
            bg=self.colors['white']
        )
        forgot_link.pack(side=tk.LEFT, padx=10)
        
        # Back button
        back_btn = ttk.Button(
            container,
            text="Back to Home",
            command=self.show_home_page
        )
        back_btn.pack(pady=20)
    
    def show_booking_page(self):
        self.clear_page()
        
        # Header
        header = self.create_header()
        
        # Main content
        content = tk.Frame(self.main_container, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Title
        title = tk.Label(
            content,
            text="Book Your Stay",
            font=("Helvetica", 32, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        title.pack(pady=20)
        
        # Booking form
        form = tk.Frame(content, bg=self.colors['white'], padx=40, pady=40)
        form.pack(fill=tk.X)
        
        # Dates
        dates_frame = tk.Frame(form, bg=self.colors['white'])
        dates_frame.pack(fill=tk.X, pady=10)
        
        # Check-in
        checkin_frame = tk.Frame(dates_frame, bg=self.colors['white'])
        checkin_frame.pack(side=tk.LEFT, padx=10)
        
        checkin_label = tk.Label(
            checkin_frame,
            text="Check-in Date",
            font=("Helvetica", 12),
            bg=self.colors['white']
        )
        checkin_label.pack(anchor="w")
        
        self.checkin_cal = Calendar(checkin_frame, selectmode='day')
        self.checkin_cal.pack()
        
        # Check-out
        checkout_frame = tk.Frame(dates_frame, bg=self.colors['white'])
        checkout_frame.pack(side=tk.LEFT, padx=10)
        
        checkout_label = tk.Label(
            checkout_frame,
            text="Check-out Date",
            font=("Helvetica", 12),
            bg=self.colors['white']
        )
        checkout_label.pack(anchor="w")
        
        self.checkout_cal = Calendar(checkout_frame, selectmode='day')
        self.checkout_cal.pack()
        
        # Guest details
        details_frame = tk.Frame(form, bg=self.colors['white'])
        details_frame.pack(fill=tk.X, pady=20)
        
        # Guests
        guests_label = tk.Label(
            details_frame,
            text="Number of Guests",
            font=("Helvetica", 12),
            bg=self.colors['white']
        )
        guests_label.pack(anchor="w")
        
        guests_frame = tk.Frame(details_frame, bg=self.colors['white'])
        guests_frame.pack(fill=tk.X)
        
        self.adults_var = tk.StringVar(value="2")
        self.children_var = tk.StringVar(value="0")
        
        adults_spin = ttk.Spinbox(
            guests_frame,
            from_=1,
            to=4,
            width=10,
            textvariable=self.adults_var
        )
        adults_spin.pack(side=tk.LEFT, padx=5)
        
        adults_label = tk.Label(
            guests_frame,
            text="Adults",
            bg=self.colors['white']
        )
        adults_label.pack(side=tk.LEFT, padx=5)
        
        children_spin = ttk.Spinbox(
            guests_frame,
            from_=0,
            to=4,
            width=10,
            textvariable=self.children_var
        )
        children_spin.pack(side=tk.LEFT, padx=5)
        
        children_label = tk.Label(
            guests_frame,
            text="Children",
            bg=self.colors['white']
        )
        children_label.pack(side=tk.LEFT, padx=5)
        
        # Room type
        room_label = tk.Label(
            details_frame,
            text="Room Type",
            font=("Helvetica", 12),
            bg=self.colors['white']
        )
        room_label.pack(anchor="w", pady=(20,5))
        
        self.room_var = tk.StringVar(value="Deluxe")
        room_types = ["Standard", "Deluxe", "Suite", "Presidential Suite"]
        
        for room in room_types:
            rb = ttk.Radiobutton(
                details_frame,
                text=room,
                value=room,
                variable=self.room_var
            )
            rb.pack(anchor="w")
        
        # Submit button
        submit_btn = ttk.Button(
            form,
            text="Proceed to Payment",
            style="Custom.TButton",
            command=self.handle_booking
        )
        submit_btn.pack(pady=20)
    
    def show_rooms_page(self):
        self.clear_page()
        
        # Header
        header = self.create_header()
        
        # Main content
        content = tk.Frame(self.main_container, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True, padx=40, pady=20)
        
        # Title
        title = tk.Label(
            content,
            text="Our Rooms",
            font=("Helvetica", 32, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['bg']
        )
        title.pack(pady=20)
        
        # Room cards
        rooms_frame = tk.Frame(content, bg=self.colors['bg'])
        rooms_frame.pack(fill=tk.X)
        
        self.create_room_card(
            rooms_frame,
            "Standard Room",
            "Perfect for solo travelers or couples",
            "From $99/night"
        )
        
        self.create_room_card(
            rooms_frame,
            "Deluxe Room",
            "Spacious room with city view",
            "From $149/night"
        )
        
        self.create_room_card(
            rooms_frame,
            "Suite",
            "Luxury suite with separate living area",
            "From $249/night"
        )
        
        self.create_room_card(
            rooms_frame,
            "Presidential Suite",
            "Ultimate luxury with panoramic views",
            "From $499/night"
        )
    
    def create_header(self):
        header = tk.Frame(self.main_container, bg=self.colors['white'])
        header.pack(fill=tk.X)
        
        # Logo
        logo = tk.Label(
            header,
            text="SUNSET",
            font=("Helvetica", 24, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['white']
        )
        logo.pack(side=tk.LEFT, padx=20, pady=10)
        
        # Navigation
        nav = tk.Frame(header, bg=self.colors['white'])
        nav.pack(side=tk.RIGHT, padx=20)
        
        nav_items = [
            ("Home", self.show_home_page),
            ("Rooms", self.show_rooms_page),
            ("Book", self.show_booking_page),
            ("Login", self.show_login_page)
        ]
        
        for text, command in nav_items:
            btn = ttk.Button(
                nav,
                text=text,
                command=command,
                style="Custom.TButton"
            )
            btn.pack(side=tk.LEFT, padx=5)
        
        return header
    
    def create_feature(self, parent, title, description):
        feature = tk.Frame(parent, bg=self.colors['white'], padx=20, pady=20)
        feature.pack(side=tk.LEFT, padx=10)
        
        title_label = tk.Label(
            feature,
            text=title,
            font=("Helvetica", 16, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['white']
        )
        title_label.pack()
        
        desc_label = tk.Label(
            feature,
            text=description,
            fg=self.colors['text'],
            bg=self.colors['white']
        )
        desc_label.pack()
    
    def create_room_card(self, parent, title, description, price):
        card = tk.Frame(
            parent,
            bg=self.colors['white'],
            padx=20,
            pady=20,
            relief="raised",
            bd=1
        )
        card.pack(fill=tk.X, pady=10)
        
        title_label = tk.Label(
            card,
            text=title,
            font=("Helvetica", 18, "bold"),
            fg=self.colors['secondary'],
            bg=self.colors['white']
        )
        title_label.pack(anchor="w")
        
        desc_label = tk.Label(
            card,
            text=description,
            fg=self.colors['text'],
            bg=self.colors['white']
        )
        desc_label.pack(anchor="w", pady=5)
        
        price_label = tk.Label(
            card,
            text=price,
            font=("Helvetica", 14, "bold"),
            fg=self.colors['primary'],
            bg=self.colors['white']
        )
        price_label.pack(anchor="w")
        
        book_btn = ttk.Button(
            card,
            text="Book Now",
            style="Custom.TButton",
            command=self.show_booking_page
        )
        book_btn.pack(anchor="e")
    
    def clear_page(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()
    
    def handle_login(self):
        messagebox.showinfo("Login", "Login functionality to be implemented")
    
    def handle_booking(self):
        checkin = self.checkin_cal.get_date()
        checkout = self.checkout_cal.get_date()
        adults = self.adults_var.get()
        children = self.children_var.get()
        room_type = self.room_var.get()
        
        booking_details = f"""
        Booking Details:
        Check-in: {checkin}
        Check-out: {checkout}
        Adults: {adults}
        Children: {children}
        Room Type: {room_type}
        """
        
        messagebox.showinfo("Booking Confirmation", booking_details)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()