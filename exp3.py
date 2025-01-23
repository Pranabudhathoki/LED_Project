import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import urllib.request
from io import BytesIO
from tkcalendar import Calendar
import re
from datetime import datetime

class HotelManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sunset Hotel Management System")
        self.root.geometry("1200x800")
        self.root.configure(bg='#ffffff')
        
        # Color scheme
        self.colors = {
            'primary': '#D4AF37',  # Gold
            'secondary': '#1E3D59',  # Dark blue
            'accent': '#E94F37',    # Red
            'bg': '#FFFFFF',        # White
            'text': '#333333'       # Dark gray
        }
        
        # Configure styles
        self.style = ttk.Style()
        self.style.configure('Custom.TButton',
            padding=10,
            background=self.colors['accent'],
            foreground='white',
            font=('Helvetica', 12)
        )
        
        # Load and cache images
        self.images = {
            'logo': self.load_and_resize_image(r"C:\\Users\\Dell\\OneDrive\Desktop\\Led_project\\1.png", (100, 50)),
            'landing': self.load_and_resize_image(r"C:\\Users\\Dell\\OneDrive\Desktop\\Led_project\\1.png", (1200, 800)),
            'login_bg': self.load_and_resize_image(r"C:\\Users\\Dell\\OneDrive\Desktop\\Led_project\\2.png", (600, 800)),
            'signup_bg': self.load_and_resize_image(r"C:\\Users\\Dell\\OneDrive\\Desktop\\Led_project\\3.png", (600, 800)),
            'dashboard_bg': self.load_and_resize_image(r"C:\\Users\\Dell\\OneDrive\\Desktop\\Led_project\\4.png", (1000, 800))
        }
        
        # Initialize user state
        self.current_user = None
        
        # Show landing page first
        self.show_landing_page()
        
    def load_and_resize_image(self, url, size):
        try:
            headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as u:
                raw_data = u.read()
            image = Image.open(BytesIO(raw_data))
            image = image.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image from {url}: {e}")
            # Create a blank image as fallback
            blank = Image.new('RGB', size, color='lightgray')
            return ImageTk.PhotoImage(blank)

    def show_landing_page(self):
        self.clear_window()
        
        # Background
        bg_label = tk.Label(self.root, image=self.images['landing'])
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Logo
        logo_label = tk.Label(self.root, image=self.images['logo'], bg='transparent')
        logo_label.place(x=20, y=20)
        
        # Tagline
        tagline = tk.Label(
            self.root,
            text="Where comfort meets elegance, and every stay feels like home.",
            font=('Helvetica', 24, 'bold'),
            fg='white',
            bg='transparent'
        )
        tagline.place(relx=0.5, rely=0.4, anchor='center')
        
        # Login button
        login_btn = ttk.Button(
            self.root,
            text="Login",
            style='Custom.TButton',
            command=self.show_login_page
        )
        login_btn.place(relx=0.9, rely=0.05, anchor='ne')

    def show_login_page(self):
        self.clear_window()
        
        # Create split view
        left_frame = tk.Frame(self.root, width=600)
        left_frame.pack(side='left', fill='both')
        
        right_frame = tk.Frame(self.root, width=600, bg='white')
        right_frame.pack(side='right', fill='both', expand=True)
        
        # Left side - Background image
        bg_label = tk.Label(left_frame, image=self.images['login_bg'])
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Right side - Login form
        login_container = tk.Frame(right_frame, bg='white')
        login_container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Logo
        logo_label = tk.Label(login_container, image=self.images['logo'], bg='white')
        logo_label.pack(pady=20)
        
        # Welcome text
        tk.Label(
            login_container,
            text="Welcome Back",
            font=('Helvetica', 32, 'bold'),
            fg=self.colors['accent'],
            bg='white'
        ).pack(pady=10)
        
        tk.Label(
            login_container,
            text="Enter your details to sign in",
            font=('Helvetica', 14),
            fg=self.colors['text'],
            bg='white'
        ).pack(pady=5)
        
        # Login form
        username_var = tk.StringVar()
        password_var = tk.StringVar()
        
        tk.Label(
            login_container,
            text="Username*",
            font=('Helvetica', 12),
            fg=self.colors['text'],
            bg='white'
        ).pack(anchor='w', pady=(20,5))
        
        ttk.Entry(
            login_container,
            textvariable=username_var,
            width=40
        ).pack(pady=5)
        
        tk.Label(
            login_container,
            text="Password*",
            font=('Helvetica', 12),
            fg=self.colors['text'],
            bg='white'
        ).pack(anchor='w', pady=(20,5))
        
        ttk.Entry(
            login_container,
            textvariable=password_var,
            show="•",
            width=40
        ).pack(pady=5)
        
        # Submit button
        ttk.Button(
            login_container,
            text="SUBMIT",
            style='Custom.TButton',
            command=lambda: self.handle_login(username_var.get(), password_var.get())
        ).pack(pady=30)
        
        # Links
        links_frame = tk.Frame(login_container, bg='white')
        links_frame.pack(pady=10)
        
        create_account = tk.Label(
            links_frame,
            text="Create account",
            font=('Helvetica', 12),
            fg=self.colors['primary'],
            cursor='hand2',
            bg='white'
        )
        create_account.pack(side='left', padx=10)
        create_account.bind('<Button-1>', lambda e: self.show_signup_page())
        
        forgot_password = tk.Label(
            links_frame,
            text="Forgot Password?",
            font=('Helvetica', 12),
            fg=self.colors['primary'],
            cursor='hand2',
            bg='white'
        )
        forgot_password.pack(side='left', padx=10)

    def show_signup_page(self):
        self.clear_window()
        
        # Create split view
        left_frame = tk.Frame(self.root, width=600)
        left_frame.pack(side='left', fill='both')
        
        right_frame = tk.Frame(self.root, width=600, bg='white')
        right_frame.pack(side='right', fill='both', expand=True)
        
        # Left side - Background image
        bg_label = tk.Label(left_frame, image=self.images['signup_bg'])
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Right side - Signup form
        signup_container = tk.Frame(right_frame, bg='white')
        signup_container.place(relx=0.5, rely=0.5, anchor='center')
        
        # Logo
        logo_label = tk.Label(signup_container, image=self.images['logo'], bg='white')
        logo_label.pack(pady=20)
        
        # Sign Up text
        tk.Label(
            signup_container,
            text="Sign Up",
            font=('Helvetica', 32, 'bold'),
            fg=self.colors['accent'],
            bg='white'
        ).pack(pady=10)
        
        tk.Label(
            signup_container,
            text="Enter your details to sign up",
            font=('Helvetica', 14),
            fg=self.colors['text'],
            bg='white'
        ).pack(pady=5)
        
        # Form fields
        fields = [
            ("Full name*", "name"),
            ("Email*", "email"),
            ("Date of birth", "dob"),
            ("Phone Number*", "phone"),
            ("Country*", "country")
        ]
        
        field_vars = {}
        
        for label, key in fields:
            tk.Label(
                signup_container,
                text=label,
                font=('Helvetica', 12),
                fg=self.colors['text'],
                bg='white'
            ).pack(anchor='w', pady=(20,5))
            
            field_vars[key] = tk.StringVar()
            ttk.Entry(
                signup_container,
                textvariable=field_vars[key],
                width=40
            ).pack(pady=5)
        
        # Submit button
        ttk.Button(
            signup_container,
            text="SIGN UP",
            style='Custom.TButton',
            command=lambda: self.handle_signup(field_vars)
        ).pack(pady=30)
        
        # Login link
        login_link = tk.Label(
            signup_container,
            text="Already have an account? Login",
            font=('Helvetica', 12),
            fg=self.colors['primary'],
            cursor='hand2',
            bg='white'
        )
        login_link.pack(pady=10)
        login_link.bind('<Button-1>', lambda e: self.show_login_page())

    def show_dashboard(self):
        self.clear_window()
        
        # Create sidebar
        sidebar = tk.Frame(self.root, width=200, bg=self.colors['secondary'])
        sidebar.pack(side='left', fill='y')
        sidebar.pack_propagate(False)
        
        # Logo in sidebar
        logo_label = tk.Label(sidebar, image=self.images['logo'], bg=self.colors['secondary'])
        logo_label.pack(pady=20)
        
        # Navigation buttons
        nav_items = [
            ("Menu", lambda: self.show_dashboard_page("menu")),
            ("Customer", lambda: self.show_dashboard_page("customer")),
            ("Booking", lambda: self.show_dashboard_page("booking")),
            ("Details", lambda: self.show_dashboard_page("details")),
            ("Report", lambda: self.show_dashboard_page("report")),
            ("Login Out", self.handle_logout)
        ]
        
        for text, command in nav_items:
            btn = tk.Button(
                sidebar,
                text=text,
                font=('Helvetica', 12),
                bg=self.colors['secondary'],
                fg='white',
                bd=0,
                pady=15,
                cursor='hand2',
                activebackground=self.colors['primary'],
                command=command
            )
            btn.pack(fill='x', pady=2)
        
        # Main content area
        main_content = tk.Frame(self.root, bg='white')
        main_content.pack(side='right', fill='both', expand=True)
        
        # Background image
        bg_label = tk.Label(main_content, image=self.images['dashboard_bg'])
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Welcome message
        tk.Label(
            main_content,
            text=f"Welcome, {self.current_user}!",
            font=('Helvetica', 24, 'bold'),
            fg=self.colors['secondary'],
            bg='white'
        ).pack(pady=20)

    def handle_login(self, username, password):
        # This is a mock login - in a real application, you would verify against a database
        if username and password:  # Simple validation
            self.current_user = username
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Please enter both username and password")

    def handle_signup(self, field_vars):
        # Validate fields
        required_fields = ['name', 'email', 'phone', 'country']
        for field in required_fields:
            if not field_vars[field].get():
                messagebox.showerror("Error", f"Please enter your {field}")
                return
        
        # Email validation
        email = field_vars['email'].get()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Please enter a valid email address")
            return
        
        # In a real application, you would save the user data to a database
        messagebox.showinfo("Success", "Account created successfully!")
        self.show_login_page()

    def handle_logout(self):
        self.current_user = None
        self.show_landing_page()

    def show_dashboard_page(self, page):
        # This would show different content based on the selected navigation item
        messagebox.showinfo("Navigation", f"Navigating to {page} page")

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HotelManagementSystem()
    app.run()